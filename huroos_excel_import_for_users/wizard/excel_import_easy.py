from odoo import fields, models
from odoo.exceptions import ValidationError
import pandas as pd
import base64
import logging

_logger = logging.getLogger(__name__)


def clear_data_dict(data):
    for row in data:
        for key in row:
            if str(row[key]) == 'nan':
                row[key] = False
    return data


class ExcelImportEasy(models.TransientModel):
    _name = "excel.import.easy"
    _description = "Importa record da un file Excel."

    file = fields.Binary(
        string="File Excel"
    )
    model = fields.Selection(
        [
            ('product.template', 'Prodotti'),
            ('sale.order', 'Ordini di vendita')
        ],
        help="Modello sul quale importare i dati.",
        required=True
    )

    def print_xlsx_template(self):
        return self.env.ref('huroos_excel_import_for_users.action_report_excel_template').report_action(self)

    def get_many2one_field(self, field_value, field_relation, create=True, alternative_search=False, operator='='):
        if not alternative_search:
            value_id = self.env[field_relation].search([('name', operator, field_value)], limit=1)
        else:
            value_id = self.env[field_relation].search([(alternative_search, operator, field_value)], limit=1)
        if not value_id and create:
            value_id = self.env[field_relation].create({'name': field_value})
        elif not value_id and not create:
            raise ValidationError(f"Non sono riuscito a trovare il valore {field_value} nella tabella {field_relation}"
                                  f" e non sono autorizzato a creare un nuovo record.")
        return value_id

    def get_many2many_field(self, field_value_list, field_relation, **kwargs):
        field_value_list = field_value_list.split(',')
        field_ids = list()
        for value in field_value_list:
            # Excel vede le percentuali come float, di base
            if value.replace('.', '').isdigit() and field_relation == 'account.tax':
                value = f"{int(float(value) * 100)}%"
            value_id = self.env[field_relation].search([('name', '=', value)])
            if not value_id:
                value_vals = {'name': value}
                # Se ci sono field necessari alla creazione del campo li inserisco nel dizionario kwargs
                for key, val in kwargs.items():
                    value_vals.update({key: val})
                value_id = self.env[field_relation].create(value_vals)
            field_ids.append((4, value_id.id))
        return field_ids

    def get_one2many_field(self, field_relation, value, row, create=True, **kwargs):
        model_to_append_vals = dict()
        for column in value:
            field_value = row[value[column]]
            if not field_value:
                continue
            field = self.env['ir.model.fields'].search(
                [
                    ('model_id.model', '=', field_relation),
                    ('name', '=', column)
                ]
            )
            if field.ttype == 'many2one':
                # Posso passare una serie di key:value per cercare in un modello con un campo alternativo
                # key = campo (many2one) di relazione col modello
                # value = campo alternativo
                # Esempio: mi serve il product_id ma non voglio cercarlo in product.template tramite 'name'
                # ma tramite 'default_code' ---> alla funzione get_one2many_field
                # passo l'argomento product_id='default_code'
                if field.name in kwargs:
                    alternative_search = kwargs[field.name]
                else:
                    alternative_search = False
                value_id = self.get_many2one_field(field_value, field.relation, create=create, alternative_search=alternative_search)
                model_to_append_vals.update({column: value_id.id})

            elif field.ttype == 'many2many':
                if field.name == 'value_ids':
                    field_ids = self.get_many2many_field(str(field_value), field.relation, attribute_id=value_id.id)
                else:
                    field_ids = self.get_many2many_field(str(field_value), field.relation)
                model_to_append_vals.update({column: field_ids})
            elif field.ttype == 'one2many':
                raise ValidationError("Non è ancora possibile gestire campi one2many all'interno di un campo one2many")
            else:
                model_to_append_vals.update({column: field_value})
        return model_to_append_vals

    def get_variant(self, default_code, variants_to_check):
        product_tmpl = self.env['product.template'].search([('default_code', '=', default_code)], limit=1)
        # Rimuovo gli spazi
        variants_to_check = variants_to_check.replace(" ", "")
        variants_to_check = variants_to_check.split(',')
        for variant in product_tmpl.product_variant_ids:
            variant_list = list()
            for variant_value in variant.product_template_attribute_value_ids:
                variant_list.append(variant_value.display_name.replace(" ", ""))
            if set(variants_to_check) == set(variant_list):
                return variant
        else:
            raise ValidationError(f"Non sono riuscito a trovare la variante {variants_to_check} "
                                  f"tra le varianti del prodotto {product_tmpl.display_name}")

    def get_data(self):
        try:
            file = base64.decodebytes(self.file)
            dataframe = pd.read_excel(file, dtype=str)
            data = dataframe.to_dict(orient='records')
        except ValueError:
            raise ValidationError("ERRORE: il file non è stato riconosciuto come un file Excel. "
                                  "Per favore inserisci un file con estensione xlsx.")
        except Exception as ex:
            raise ValidationError(ex)
        return clear_data_dict(data)

    def import_products(self):
        column_template = self.env['ir.config_parameter'].sudo().get_param('huroos_excel_import_for_users.product_excel_columns')
        column_template = eval(str(column_template))
        data = self.get_data()
        product_obj = self.env['product.template']
        product = False
        # data è una lista di dizionari che hanno come chiavi i nomi delle colonne
        for row in data:
            if not product or row['Codice Rif. Interno'] is not False and row['Nome'] is not False:
                # CREAZIONE PRODOTTO
                product_data = dict()
                for column in column_template['main']:
                    if column in ['name', 'categ_id', 'default_code', 'uom_id'] and not row[column_template['main'][column]]:
                        if not product:
                            raise ValidationError(f"La colonna {column_template['main'][column]} non può "
                                                  f"essere vuota (almeno nella prima riga).")
                        else:
                            continue
                    field = self.env['ir.model.fields'].search(
                        [
                            ('model_id.model', '=', self.model),
                            ('name', '=', column)
                        ]
                    )
                    if not field:
                        continue

                    if field.ttype == 'many2one':
                        field_value = row[column_template['main'][column]]
                        if not field_value:
                            continue
                        value_id = self.get_many2one_field(field_value, field.relation)
                        product_data.update({column: value_id.id})

                    elif field.ttype == 'one2many':
                        raise ValidationError("ERRORE: un field one2many è presente nella chiave 'main'. "
                                              "I field di tipo one2many devono essere nella chiave 'one2many_fields'.")

                    elif field.ttype == 'many2many':
                        field_value_list = str(row[column_template['main'][column]])
                        if not field_value_list:
                            continue
                        field_ids = self.get_many2many_field(field_value_list, field.relation)
                        product_data.update({column: field_ids})

                    else:
                        field_value = row[column_template['main'][column]]
                        if not field_value:
                            continue
                        product_data.update({column: field_value})

                if not product_data.get('default_code', False) and not product_data.get('name', False):
                    continue
                if product_data.get('uom_id', False) is not False:
                    product_data.update({'uom_po_id': product_data['uom_id']})

                product = product_obj.search(
                    [
                        ('default_code', '=', product_data['default_code']),
                        ('name', '=', product_data['name'])
                    ]
                )
                if not product:
                    product = product_obj.create(product_data)
                    _logger.info(f"Il prodotto con ID {product.id} è stato CREATO")
                else:
                    product.write(product_data)
                    _logger.info(f"Il prodotto con ID {product.id} è stato AGGIORNATO")

            # ASSOCIO I FIELD ONE2MANY AL PRODOTTO
            for key, value in column_template['one2many_fields'].items():
                relation_field = self.env['ir.model.fields'].search(
                        [
                            ('model_id.model', '=', self.model),
                            ('name', '=', key)
                        ]
                    )
                if relation_field.ttype != 'one2many':
                    raise ValidationError(f"ERRORE: il campo {relation_field.name} è posizionato "
                                          f"nella chiave dedicata ai campi one2many, pur essendo un campo "
                                          f"di tipo {relation_field.ttype}. Per favore cambiare la sua posizione.")

                model_to_append_data = self.get_one2many_field(relation_field.relation, value, row)
                if not model_to_append_data:
                    continue

                # Gestione delle varianti prodotto
                if key == 'attribute_line_ids':
                    existing = False
                    for attribute_line in product.attribute_line_ids:
                        if attribute_line.attribute_id.id == model_to_append_data['attribute_id']:
                            existing = True
                            for k, ID in model_to_append_data['value_ids']:
                                if ID not in attribute_line.value_ids.ids:
                                    attribute_line.write({'value_ids': [(k, ID)]})
                                    _logger.info(f"Prodotto ID {product.id} -- Attributo {attribute_line.attribute_id.name} -- Aggiunta variante con ID {ID}")
                    if not existing:
                        product.write({key: [(0, 0, model_to_append_data)]})
                        _logger.info(f"Prodotto ID {product.id} -- Aggiunto attributo con ID {model_to_append_data['attribute_id']} -- ID varianti {model_to_append_data['value_ids']}")

                # Gestione dei codici cliente
                if key == 'customer_ids':
                    existing = False
                    for customer_line in product.customer_ids:
                        if customer_line.name.id == model_to_append_data['name']:
                            existing = True
                            if model_to_append_data.get('product_code', False):
                                product.write({'customer_ids': [(1, customer_line.id, model_to_append_data)]})
                                _logger.info(f"Prodotto ID {product.id} -- Aggiornato codice cliente {customer_line.name.name}")

                    if not existing and model_to_append_data.get('product_code', False):
                        product.write({key: [(0, 0, model_to_append_data)]})
                        _logger.info(f"Prodotto ID {product.id} -- Creato nuovo codice cliente")
                    # Mi salvo l'oggetto del cliente per poterlo usare poi nella creazione del listino
                    partner_id = self.env['res.partner'].search([('id', '=', model_to_append_data['name'])])
                    if not partner_id:
                        # Non dovrebbe mai succedere, ma se succede...
                        raise ValidationError("Qualcosa è andato storto. Non sono riuscito a trovare "
                                              "il contatto del cliente per associare il listino.")
                    pricelist_id = partner_id.property_product_pricelist
                    if not pricelist_id:
                        raise ValidationError(f"Qualcosa è andato storto. Non sono riuscito a trovare "
                                              f"alcun listino associato al cliente {partner_id.name}.")

            # CREO I RECORD PER I MODELLI ASSOCIATI
            for key, value in column_template['models'].items():
                if key == 'product.pricelist.item':
                    riga_listino_vals = dict()
                    for column in value:
                        field_value = row[column_template['models'][key][column]]
                        if not field_value:
                            break
                        riga_listino_vals.update({column: field_value})
                    if not riga_listino_vals:
                        continue
                    riga_listino_vals.update(
                        {
                            'applied_on': '1_product',
                            'compute_price': 'fixed',
                            'pricelist_id': pricelist_id.id,
                            'product_tmpl_id': product.id
                        }
                    )
                    domain = [
                        ('pricelist_id', '=', riga_listino_vals['pricelist_id']),
                        ('product_tmpl_id', '=', riga_listino_vals['product_tmpl_id']),
                        ('date_start', '=', riga_listino_vals['date_start']),
                        ('fixed_price', '=', riga_listino_vals['fixed_price'])
                    ]
                    existing = self.env['product.pricelist.item'].search(domain)
                    if not existing:
                        self.env['product.pricelist.item'].create(riga_listino_vals)
                        _logger.info(f"Prodotto con ID {product.id} inserito nel listino {pricelist_id.name} "
                                     f"-- Data inizio validità: {riga_listino_vals['date_start']} -- Prezzo: {riga_listino_vals['fixed_price']}")
                    else:
                        _logger.info(f"Prodotto con ID {product.id} già presente nel listino {pricelist_id.name} "
                                     f"con data inizio validità {riga_listino_vals['date_start']} e prezzo {riga_listino_vals['fixed_price']}")

    def import_orders(self):
        column_template = self.env['ir.config_parameter'].sudo().get_param('huroos_excel_import_for_users.sale_order_excel_columns')
        column_template = eval(str(column_template))
        data = self.get_data()
        order_obj = self.env['sale.order']
        order = False
        # data è una lista di dizionari che hanno come chiavi i nomi delle colonne
        for row in data:
            if not order and not row[column_template['main']['client_order_ref']]:
                raise ValidationError(f"La colonna {column_template['main']['client_order_ref']} non può "
                                      f"essere vuota (almeno nella prima riga).")
            elif not order or row[column_template['main']['client_order_ref']] is not False:
                order = order_obj.search([('name', '=', row[column_template['main']['client_order_ref']])], limit=1)
                if not order:
                    order = order_obj.search([('client_order_ref', '=', row[column_template['main']['client_order_ref']])], limit=1)
                if not order:
                    # CREAZIONE ORDINE
                    order_data = dict()
                    for column in column_template['main']:
                        field = self.env['ir.model.fields'].search(
                            [
                                ('model_id.model', '=', self.model),
                                ('name', '=', column)
                            ]
                        )
                        if not field:
                            continue

                        if field.ttype == 'many2one':
                            field_value = row[column_template['main'][column]]
                            if not field_value:
                                continue
                            value_id = self.get_many2one_field(field_value, field.relation, create=False)
                            order_data.update({column: value_id.id})

                        elif field.ttype == 'one2many':
                            raise ValidationError("ERRORE: un field one2many è presente nella chiave 'main'. "
                                                  "I field di tipo one2many devono essere nella chiave 'one2many_fields'.")

                        elif field.ttype == 'many2many':
                            field_value_list = str(row[column_template['main'][column]])
                            if not field_value_list:
                                continue
                            field_ids = self.get_many2many_field(field_value_list, field.relation)
                            order_data.update({column: field_ids})

                        else:
                            field_value = row[column_template['main'][column]]
                            if not field_value:
                                continue
                            order_data.update({column: field_value})

                    order = order_obj.create(order_data)
                    _logger.info(f"Ordine di vendita {order.id} CREATO")
            else:
                _logger.info(f"Ordine {order.id} ESISTENTE")

            # ASSOCIO LE RIGHE ALL'ORDINE
            for key, value in column_template['one2many_fields'].items():
                relation_field = self.env['ir.model.fields'].search(
                    [
                        ('model_id.model', '=', self.model),
                        ('name', '=', key)
                    ]
                )
                if relation_field.ttype != 'one2many':
                    raise ValidationError(f"ERRORE: il campo {relation_field.name} è posizionato "
                                          f"nella chiave dedicata ai campi one2many, pur essendo un campo "
                                          f"di tipo {relation_field.ttype}. Per favore cambiare la sua posizione.")

                line_to_append_data = self.get_one2many_field(relation_field.relation, value, row, create=False, product_id='default_code')
                if not line_to_append_data:
                    continue
                if row['Varianti'] is not False:
                    product_id = self.get_variant(row[value['product_id']], row['Varianti'])
                    line_to_append_data.update({'product_id': product_id.id})
                existing = order.order_line.search([('order_id', '=', order.id), ('product_id', '=', line_to_append_data['product_id'])], limit=1)
                if not existing:
                    order.write({key: [(0, 0, line_to_append_data)]})
                    _logger.info(f"Ordine {order.id} AGGIORNATO -- {line_to_append_data.values()}")
                else:
                    order.write({'order_line': [(1, existing.id, line_to_append_data)]})
                    _logger.info(f"Ordine {order.id} -- RIGA {existing.id} AGGIORNATA -- {line_to_append_data.values()}")

    def import_data(self):
        if not self.file:
            raise ValidationError("Per favore inserire un file per procedere "
                                  "all'importazione, oppure cliccare su Annulla")
        if self.model == 'product.template':
            self.import_products()

        elif self.model == 'sale.order':
            self.import_orders()

