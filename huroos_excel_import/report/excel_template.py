from odoo.models import AbstractModel


class PartnerXlsx(AbstractModel):
    _name = 'report.huroos_excel_import.excel_template'
    _inherit = "report.report_xlsx.abstract"

    def generate_xlsx_report(self, workbook, data, periods):
        sheet = workbook.add_worksheet('Excel Template')
        bold = workbook.add_format({'bold': True})
        bold.set_border()
        unique = workbook.add_format({'bold': True, 'bg_color': '#00ff00'})
        unique.set_border()
        index = 0
        column_names = periods.get_column_names()
        for field in column_names['required_columns']:
            sheet.write(0, index, field, unique)
            index += 1
        for field in column_names['columns']:
            sheet.write(0, index, field, bold)
            index += 1
