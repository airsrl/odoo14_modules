from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    cbi_id = fields.Char()

class AccountMove(models.Model):
    _inherit = 'account.move'

    multi_due = fields.Char()
    multi_date_due = fields.Char()