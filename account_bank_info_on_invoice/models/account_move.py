from odoo import fields, models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    bank_name = fields.Many2one(
        comodel_name="res.bank",
        related="partner_bank_id.bank_id",
        string="Nome e SWIFT",
        store=True
    )
