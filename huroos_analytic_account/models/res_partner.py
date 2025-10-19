from odoo import fields,models


class ResPartner(models.Model):
    _inherit = "res.partner"

    analytic_account_id = fields.Many2one('account.analytic.account', string="Conto analitico", help="Conto analitico di default")
    analytic_tag_ids = fields.Many2many('account.analytic.tag', string="Etichette analitiche", help="Conto analitico di default")