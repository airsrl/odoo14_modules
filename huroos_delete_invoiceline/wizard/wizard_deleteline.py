from odoo import fields, models, api


class WizardDeleteline(models.TransientModel):
    _name = 'wizard.deleteline'

    name=fields.Char()
    account_line_ids = fields.Many2many('account.move.line')
    move_id = fields.Many2one('account.move')
