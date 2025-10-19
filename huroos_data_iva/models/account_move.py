from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'

    date_iva = fields.Date()

    def action_post(self):
        """
        Assegna la competenza IVA
        """
        res = super().action_post()
        competence_iva = self.env['ir.config_parameter'].sudo().get_param('huroos_data_iva.account_competence_iva')
        for inv in self:
            for move_line in inv.line_ids:
                date_iva = inv.date_iva
                if not date_iva:
                    date_iva = move_line.date
                # Configurazione Competenza IVA
                if competence_iva:
                    if move_line.tax_ids or move_line.tax_line_id:
                        move_line.write({'date_iva': date_iva})
        return res


    def rc_inv_vals(self, partner, rc_type, lines, currency):
        """
        Ereditato per integrazione data iva su autofattura in reverse charge
        """
        r = super(AccountMove, self).rc_inv_vals(partner, rc_type, lines, currency)
        if self.date_iva:
            r['date_iva'] = self.date_iva
        return r


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    date_iva = fields.Date()


