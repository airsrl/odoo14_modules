from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
import pandas as pd
import base64
import logging

_logger = logging.getLogger(__name__)


class ExcelImport(models.TransientModel):
    _name = "excel.import"
    _description = "Import data from a xlsx file"

    file = fields.Binary(
        string="Excel file"
    )
    file_name = fields.Char(help="This field is only used to check if the file uploaded has xlsx extension.")
    model_id = fields.Many2one(
        comodel_name="ir.model",
        string="Model to import records"
    )
    record_limit = fields.Integer(
        string="Record limit",
        required=True,
        default=100,
        help="After the creation of this number of records the script will "
             "commit to the database, saving all records created until now "
             "(It's suggested a number between 100 and 500)."
    )
    line_ids = fields.One2many(
        comodel_name="field.line",
        inverse_name="file_id",
        string="File columns"
    )
    is_fast_import = fields.Boolean(
        string="Direct import",
        help="Flag this if your Excel file already has columns with Odoo field names."
    )
    can_update = fields.Boolean(
        string="Update records if already exist",
        default=True
    )
    template_with_technical_names = fields.Boolean(
        string="with techincal names",
        help="Flag this if you want to download a xlsx template with technical names, ready for 'Direct import'.",
        default=True
    )

    @api.onchange('file')
    def update_line_ids(self):
        if not self.file:
            self.line_ids = None
        else:
            # Check file's extension
            extension = self.file_name.split('.')[-1]
            if extension != 'xlsx':
                raise ValidationError(_("The file must be a xlsx file."))
            file = base64.decodebytes(self.file)
            dataframe = pd.read_excel(file)
            column_names = list(dataframe.columns)
            for column in column_names:
                self.env['field.line'].create(
                    {
                        'file_id': self.id,
                        'name': column
                    }
                )

    @api.constrains('record_limit')
    def check_record_limit(self):
        if self.record_limit <= 0:
            raise ValidationError(_("The record limit can't less or equal to zero. "
                                    "It's suggested a number between 100 and 500."))

    @api.constrains('line_ids')
    def check_field_id_unique(self):
        field_list = list()
        for record in self.line_ids:
            if not record.field_id:
                continue
            else:
                field_list.append(record.field_id.name)
        if len(field_list) != len(set(field_list)):
            raise ValidationError(_("You can't choose a field multiple times."))

    def get_column_names(self):
        columns = list()
        required_columns = list()
        for field in self.model_id.field_id:
            if not self.template_with_technical_names:
                local_translation = self.env['ir.translation'].with_context(lang=self.env.user.lang).get_field_string(self.model_id.model)
                if field.required:
                    required_columns.append(local_translation[field.name])
                else:
                    columns.append(local_translation[field.name])
            else:
                if field.required:
                    required_columns.append(field.name)
                else:
                    columns.append(field.name)
        return {
            'required_columns': required_columns,
            'columns': columns
        }

    def dowmload_xlsx_template(self):
        return self.env.ref('huroos_excel_import.action_report_excel_template').report_action(self)

    def button_import_data(self):
        file = base64.decodebytes(self.file)
        dataframe = pd.read_excel(file, dtype=str)
        records = dataframe.to_dict(orient='records')
        # excel_constrains is a list of all column names to check for duplicates in the Excel file
        excel_constraints = list()
        # while odoo_constrains is a list of all field names to check for duplicates in the database
        odoo_constraints = list()
        raw_search_fields = dict()
        if not self.is_fast_import:
            column_relation = dict()
            for line in self.line_ids:
                # Associate column names to fields
                if not line.field_id:
                    continue
                else:
                    column_relation.update({line.name: line.field_id.name})
                if line.is_unique:
                    odoo_constraints.append(line.field_id.name)
                if line.is_raw_search:
                    raw_search_fields.update({line.name: line.raw_search_field.name})
        else:
            column_relation = dict(zip(dataframe.columns.values.tolist(), dataframe.columns.values.tolist()))
        # If no row is selected as unique field, all rows will be used as filter to search for duplicates
        if len(odoo_constraints) == 0:
            for line in self.line_ids:
                if not line.field_id:
                    continue
                else:
                    odoo_constraints.append(line.field_id.name)
                    excel_constraints.append(line.name)
        # Delete duplicate records based on is_unique field
        if len(excel_constraints) > 0:
            duplicated_records = dataframe.duplicated(excel_constraints)
            duplicated_records = dataframe[duplicated_records].to_dict(orient='records')
            for element in duplicated_records:
                records.remove(element)
        # Converting records in Odoo language, so that Odoo can understand them
        created_records = 0
        for element in records:
            data = dict()
            for key in element:
                if key not in column_relation:
                    continue
                if str(element[key]) == 'nan':
                    data.update({column_relation[key]: None})
                    continue
                # Search the field to check its type
                field = self.env['ir.model.fields'].search(
                    [
                        ('model_id.model', '=', self.model_id.model),
                        ('name', '=', column_relation[key])
                    ]
                )
                if field.ttype in ['many2one', 'many2many']:
                    value_of_field = element[key]
                    if key in raw_search_fields:
                        if field.ttype not in ['many2one', 'many2many']:
                            raise ValidationError(_(f"The {key} column is not a many2one or many2many field. "
                                                    "You can't use it as raw search field."))
                        else:
                            try:
                                relation = self.env[field.relation].search([(raw_search_fields[key], '=', value_of_field)], limit=1)
                                if not relation:
                                    relation = self.env[field.relation].create({raw_search_fields[key]: value_of_field, 'name': value_of_field})
                            except ValueError:
                                raise ValidationError(_(f"Field {raw_search_fields[key]} doesn't exist in model {field.relation}."))
                            except Exception as ex:
                                raise ValidationError(_(ex))
                    else:
                        relation = self.env[field.relation].search([('name', '=', value_of_field)], limit=1)
                        if not relation:
                            relation = self.env[field.relation].create({'name': value_of_field})
                    if field.ttype == 'many2many':
                        relation_id = [(4, relation.id)]
                        if field.name in odoo_constraints:
                            odoo_constraints.remove(field.name)
                    else:
                        relation_id = relation.id
                    data.update({column_relation[key]: relation_id})
                elif field.ttype == 'boolean':
                    if element[key] in ['0', 'false', 'False']:
                        data.update({column_relation[key]: False})
                    elif element[key] in ['1', 'true', 'True']:
                        data.update({column_relation[key]: True})
                    else:
                        raise ValidationError(_(f"Wrong value for column {key}.\n"
                                                f"It must be one of this values: 0, false, False, 1, true, True"))
                elif field.ttype == 'float':
                    try:
                        data.update({column_relation[key]: float(str(element[key]).replace(',', '.'))})
                    except Exception as ex:
                        raise ValidationError(ex)
                elif field.ttype == 'integer':
                    try:
                        data.update({column_relation[key]: int(element[key])})
                    except Exception as ex:
                        raise ValidationError(ex)
                else:
                    data.update({column_relation[key]: element[key]})
            if len(odoo_constraints) > 0:
                # Search in the db with a query, if record doesn't exist I create it
                sql_model_name = "_".join(self.model_id.model.split('.'))
                query = f"SELECT id FROM {sql_model_name} WHERE "
                values = list()
                for field in odoo_constraints:
                    if field != odoo_constraints[-1]:
                        query += field + " = %s AND "
                    else:
                        query += field + " = %s"
                    values.append(data[field])
                # Check if the record exists in the database
                self.env.cr.execute(query, tuple(values))
                exist = self.env.cr.fetchall()
            else:
                exist = []
            if not exist:
                self.env[self.model_id.model].create(data)
                created_records += 1
                _logger.info(f"--- {created_records} RECORDS CREATED ---")
                if created_records == self.record_limit:
                    _logger.info(f"--- COMMITTED {created_records} RECORDS ---")
                    created_records = 0
                    self.env.cr.commit()
            else:
                if self.can_update:
                    self.env[self.model_id.model].browse(exist[0]).write(data)
                    _logger.info(f"--- RECORD WITH ID {exist[0]} UPDATED ---")
                else:
                    _logger.info(f"--- RECORD WITH ID {exist[0]} EXISTS ON THE DATABASE ---")


class FieldLine(models.TransientModel):
    _name = "field.line"
    _description = "Field line of Excel file"

    file_id = fields.Many2one(
        comodel_name="excel.import",
        string="File ID"
    )
    name = fields.Char(
        string="Column name",
        readonly=True
    )
    field_id = fields.Many2one(
        comodel_name="ir.model.fields",
        string="Field"
    )
    relation_model = fields.Char(
        related="field_id.relation"
    )
    # Rows set to is_unique = True are used as filter to search in the database for duplicates
    # If no row is selected as unique field, all rows will be used as filter to search for duplicates
    is_unique = fields.Boolean(
        string="Field is unique"
    )
    # raw_search is basically used to search a relation with a field different from 'name'
    is_raw_search = fields.Boolean(
        string="Raw search",
        help="Flag this field to search in the database directly "
             "from another field, rather than the field 'name' (only for many2one and many2many fields)."
    )
    model_id = fields.Many2one(
        comodel_name="ir.model",
        related="file_id.model_id"
    )
    raw_search_field = fields.Many2one(
        comodel_name="ir.model.fields",
        string="Raw search field",
        domain="[('model_id.model', '=', relation_model)]"
    )

    @api.constrains('raw_search_field')
    def _check_raw_search_field(self):
        for line in self:
            if line.relation_model is not False and line.is_raw_search and not line.raw_search_field:
                raise ValidationError(_("Raw search field is mandatory if you select 'Raw search'"))
