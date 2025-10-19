from odoo import fields,models


class AccountAccount(models.Model):
    _inherit = "account.account"

    analytic_account_id = fields.Many2one('account.analytic.account', string="Conto analitico", help="Conto analitico di default")