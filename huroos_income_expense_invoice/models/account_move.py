from odoo import api, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.model
    def default_get(self, default_fields):
        values = super(AccountMoveLine, self).default_get(default_fields)

        if values.get('account_id') and values.get('partner_id'):
            partner = self.env['res.partner'].browse(values.get('partner_id'))
            move_type = self._context.get('default_move_type')

            if partner.income_account_id and move_type in ('out_invoice', 'out_refund', 'out_receipt'):
                values['account_id'] = partner.income_account_id.id

            if partner.expence_account_id and move_type in ('in_invoice', 'in_refund', 'in_receipt'):
                values['account_id'] = partner.expence_account_id.id

        return values

    def _get_computed_account(self):
        """Impedisco il cambio di conto se il partner ha il conto di costo/ricavo settato"""

        self.ensure_one()

        if not self.move_id.partner_id.income_account_id or not self.move_id.partner_id.expence_account_id:
            return super(AccountMoveLine, self)._get_computed_account()

        else:
            return self.account_id
