from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.onchange('partner_id', 'fiscal_position_id')
    def onchange_partner_id_corrispettivi(self):
        if (
            self.partner_id.use_corrispettivi or
            self.fiscal_position_id.corrispettivi
        ):
            self.set_corr_journal()
        else:
            if not self.journal_id:
                self.journal_id = self._get_default_journal()