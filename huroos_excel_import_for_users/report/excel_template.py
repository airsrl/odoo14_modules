from odoo.models import AbstractModel
from odoo.exceptions import ValidationError


COLUMN_WIDTHS_PRD = [25, 70, 20, 16, 15, 10, 20, 15, 15, 15, 50, 25, 16, 18]
COLUMN_WIDTHS_ORD = [25, 35, 11, 15, 24, 25, 25, 25, 65, 8, 8, 12, 22, 8, 8]

# product_column_template = {
#     'main': {
#         'default_code': 'Codice Rif. Interno',
#         'name': 'Nome',
#         'categ_id': 'Categoria',
#         'list_price': 'Prezzo al pubblico',
#         'uom_id': 'Unità di misura',
#         'taxes_id': 'Imposte',
#         'description': 'Note interne',
#     },
#     'one2many_fields': {
#         'attribute_line_ids': {
#             'attribute_id': 'Attributo',
#             'value_ids': 'Valori'
#         },
#         'customer_ids': {
#             'name': 'Cliente',
#             'product_name': 'Descrizione cliente',
#             'product_code': 'Codice Rif. Cliente'
#         }
#     },
#     'models': {
#         'product.pricelist.item': {
#             'date_start': 'Data inizio validità',
#             'fixed_price': 'Prezzo listino cliente'
#         }
#     }
# }

# order_column_template = {
#     'main': {
#         'partner_id': 'Contatto cliente',
#         'client_order_ref': 'Riferimento cliente/Riferimento ordine',
#         'revision_seq': 'N° Revisione',
#         'date_order': 'Data ordine',
#         'data_consegna': "Data di consegna dell'ordine",
#         'payment_term_id': 'Termini di pagamento'
#     },
#     'variants': 'Varianti',
#     'one2many_fields': {
#         'order_line': {
#             'product_id': 'Riferimento interno prodotto',
#             'name': 'Descrizione (se lasciata bianca metterà in automatico il nome del prodotto)',
#             'product_uom_qty': 'Quantità',
#             'product_uom': 'UDM',
#             'price_unit': 'Prezzo unitario',
#             'commitment_date': 'Data di consegna prodotto',
#             'tax_id': 'Imposte',
#             'discount': 'Sconto %'
#         }
#     }
# }


def get_column_names(data):
    column_names = list()
    for obj in data:
        if obj == 'main':
            for column in data[obj].values():
                column_names.append(column)
        elif obj in ['one2many_fields', 'models']:
            for key, value in data[obj].items():
                for column in value.values():
                    column_names.append(column)
        elif obj == 'variants':
            column_names.append(data[obj])
    return column_names


def set_column_widths(sheet, model):
    index = 0
    if model == 'product.template':
        column_widths = COLUMN_WIDTHS_PRD
    elif model == 'sale.order':
        column_widths = COLUMN_WIDTHS_ORD
    for width in column_widths:
        sheet.set_column(index, index, width)
        index += 1


class PartnerXlsx(AbstractModel):
    _name = 'report.huroos_excel_import_for_users.excel_template'
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, periods):
        sheet = workbook.add_worksheet('Excel Template')
        bold = workbook.add_format({'bold': True, 'bg_color': '#d9d9d9'})
        bold.set_border()
        index = 0
        model = periods.model
        if not model:
            raise ValidationError("Qualcosa è andato storto. Non sono riuscito a ricevere il modello per il template.")
        if model == 'product.template':
            column_template = self.env['ir.config_parameter'].sudo().get_param('huroos_excel_import_for_users.product_excel_columns')
            column_template = eval(str(column_template))
        elif model == 'sale.order':
            column_template = self.env['ir.config_parameter'].sudo().get_param('huroos_excel_import_for_users.sale_order_excel_columns')
            column_template = eval(str(column_template))
        column_names = get_column_names(column_template)
        set_column_widths(sheet, model)
        for column in column_names:
            sheet.write(0, index, column, bold)
            index += 1
