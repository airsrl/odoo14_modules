from odoo import models, fields, api

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    batch_stock_move_ids = fields.Many2many('stock.move')
