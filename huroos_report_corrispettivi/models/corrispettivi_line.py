from odoo import models, fields, api

class CorrispettiviLine(models.Model):
    _name = 'corrispettivi.line'

    import_corr_id = fields.Many2one('import.corrispettivi')
    day_name = fields.Char()
    day = fields.Integer()
    date = fields.Date()
    currency_id = fields.Many2one(related='import_corr_id.currency_id')
    amount = fields.Monetary(currency_field="currency_id")