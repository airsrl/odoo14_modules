from odoo import models, fields, api

class AccountJournal(models.Model):
    _inherit = 'account.journal'

    huroos_id = fields.Char()

class AccountTax(models.Model):
    _inherit = 'account.tax'

    huroos_id = fields.Char()

class AccountRcType(models.Model):
    _inherit = 'account.rc.type'

    huroos_id = fields.Char()

class FiscalPosition(models.Model):
    _inherit = 'account.fiscal.position'

    huroos_id = fields.Char()