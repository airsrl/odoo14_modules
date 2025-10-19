# -*- coding: utf-8 -*-
# Copyright 2019 Federico Ranieri (<http://www.huroos.it>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import models, api


class UpdateNotifyAruba(models.TransientModel):
    _name = 'update.notify.aruba'
    _description = "Wizard to send multiple e-invoice ARUBA"

    def recalculate(self):
        if self.env.context.get('active_ids'):
            einvoice_ids = self.env['account.move'].browse(self.env.context.get('active_ids'))
            for x in einvoice_ids:
                x.button_draft()
                x._compute_amount()
                x._recompute_tax_lines(recompute_tax_base_amount=True)
                x._recompute_dynamic_lines(recompute_tax_base_amount=True)
                for line in x.invoice_line_ids:
                    line._compute_tax_line_id()
                x.action_post()

    def update_notify(self):
        if self.env.context.get('active_ids'):
            einvoice_ids = self.env['account.move'].browse(self.env.context.get('active_ids'))
            for x in einvoice_ids:
                if x.fatturapa_attachment_out_id:
                    x.fatturapa_attachment_out_id.get_single_sdi_notification()
