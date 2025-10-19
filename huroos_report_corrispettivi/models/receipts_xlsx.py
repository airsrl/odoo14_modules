# -*- coding: utf-8 -*-
# Copyright 2018 addOons Srl (<http://www.addoons.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import datetime
import logging


from odoo import models
from odoo.tools import float_round


class ReportCorrispettiviByDay(models.AbstractModel):
    """
    REPORT RICEVUTE/FATTURE RAGGRUPPATE PER GIORNO
    """
    _name = 'report.report_corrispettivi_by_day'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, receipts):


        sheet = workbook.add_worksheet('Documenti Fiscali')
        header = workbook.add_format({'bold': True, 'text_wrap': True, 'border': True, 'border_color': 'black'})
        domain = [('name', '!=', False), ('invoice_date', '>=', data['form']['from_date']), ('invoice_date', '<=', data['form']['to_date'])]
        if len(data['form']['journal_ids']) > 0:
            domain.append(('journal_id', 'in', data['form']['journal_ids']))

        docs = self.env['account.move'].search(domain, order="invoice_date asc")
        tax_groups = self.env['account.tax.group'].search([('include_report_corrispettivi', '=', True)])


        receipts = sorted(docs, key=lambda i: i['invoice_date'])

        columns = ['Data']

        payment_method_columns = []
        rows = {}
        for obj in receipts:

            if data['form']['type'] == 'day':
                # creo dizionario per giorno
                if str(obj.invoice_date) not in rows:
                    rows[str(obj.invoice_date)] = {}
                    for tax_group in tax_groups:
                        if tax_group.id not in rows[str(obj.invoice_date)].keys():
                            rows[str(obj.invoice_date)][tax_group.id] = {
                                'imponibile': 0,
                                'tasse': 0
                            }
                # prendo ammontare tasse per gruppo tassa
                tax_groups_amounts = obj.amount_by_group
                for tax_group_amount in tax_groups_amounts:
                    if tax_group_amount[6] in rows[str(obj.invoice_date)].keys():
                        rows[str(obj.invoice_date)][tax_group_amount[6]]['imponibile'] += tax_group_amount[2]
                        rows[str(obj.invoice_date)][tax_group_amount[6]]['tasse'] += tax_group_amount[1]
            else:
                if obj.name not in rows:
                    rows[obj.name] = {
                        'data': str(obj.invoice_date),
                        'cliente': obj.partner_id.name,
                        'vat': obj.partner_id.vat if obj.partner_id.vat else "",
                        'fiscalcode': obj.partner_id.fiscalcode if obj.partner_id.fiscalcode else "",
                        'amount_total': obj.amount_total,
                        'amount_untaxed': obj.amount_untaxed,
                        'amount_tax': obj.amount_tax,
                    }
                    for tax_group in tax_groups:
                        if tax_group.id not in rows[obj.name].keys():
                            rows[obj.name][tax_group.id] = {
                                'imponibile': 0,
                                'tasse': 0
                            }
                # prendo ammontare tasse per gruppo tassa
                tax_groups_amounts = obj.amount_by_group
                for tax_group_amount in tax_groups_amounts:
                    if tax_group_amount[6] in rows[obj.name].keys():
                        rows[obj.name][tax_group_amount[6]]['imponibile'] += tax_group_amount[2]
                        rows[obj.name][tax_group_amount[6]]['tasse'] += tax_group_amount[1]

        if data['form']['type'] == 'list':
            columns = ['Data', 'N° fattura', 'Cliente', 'P.IVA', 'Codice Fiscale', 'Imponibile totale', 'Tasse totali', 'Totale Fattura']
        for tax_group in tax_groups:
            columns.append(tax_group.label_report_corrispettivi_imponibile or 'Imponibile ' + tax_group.name)
            columns.append(tax_group.label_report_corrispettivi_tassa or tax_group.name)

        c = 0

        for l in columns:
            sheet.set_column(0, c, 30)
            sheet.write(0, c, l, header)
            c += 1

        row = 1
        for data_corrispettivi in rows.keys():
            c = 0
            if data['form']['type'] == 'list':
                sheet.write(row, c, rows[data_corrispettivi]['data'], header)
                sheet.write(row, c+1, data_corrispettivi, header)
                sheet.write(row, c+2, rows[data_corrispettivi]['cliente'], header)
                sheet.write(row, c+3, rows[data_corrispettivi]['vat'], header)
                sheet.write(row, c+4, rows[data_corrispettivi]['fiscalcode'], header)
                sheet.write(row, c + 5, rows[data_corrispettivi]['amount_untaxed'], header)
                sheet.write(row, c + 6, rows[data_corrispettivi]['amount_tax'], header)
                sheet.write(row, c + 7, rows[data_corrispettivi]['amount_total'], header)
                c += 7
            else:
                sheet.write(row, c, data_corrispettivi, header)

            for tax_group in tax_groups:
                c += 1
                sheet.write(row, c, rows[data_corrispettivi][tax_group.id]['imponibile'], header)
                c += 1
                sheet.write(row, c, rows[data_corrispettivi][tax_group.id]['tasse'], header)

            row += 1

