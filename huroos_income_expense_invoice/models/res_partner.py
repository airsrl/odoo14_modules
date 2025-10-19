from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    expence_account_id = fields.Many2one(
        comodel_name="account.account",
        string="Conto di Costo",
        domain="[('internal_group', '=', 'expense')]"
    )
    income_account_id = fields.Many2one(
        comodel_name="account.account",
        string="Conto di Ricavo",
        domain="[('internal_group', '=', 'income')]"
    )
