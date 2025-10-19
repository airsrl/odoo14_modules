from odoo import api,fields,models
# -*- coding: utf-8 -*-
# Powered by Karanveer Singh.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

class WizardReportCorrispettivi(models.TransientModel):
    _name = "wizard.report.corrispettivi"

    date_start = fields.Date(string="Data inizio")
    date_end = fields.Date(string="Data fine")
    journal_ids = fields.Many2many('account.journal')

    document_type = fields.Selection([('day', 'Diviso per giorni'),
                                      ('list', 'Elenco - Documenti Fiscali')])

    def download_xls(self):

        datas = {
            'model': 'account.invoice',
            'form': {'from_date': self.date_start,
                     'type': self.document_type,
                     'to_date': self.date_end,
                     'journal_ids': self.journal_ids.ids if self.journal_ids else []},
        }


        return self.env.ref('huroos_report_corrispettivi.corrispettivi_grouped_by_day_xlsx').report_action(self, data=datas)

