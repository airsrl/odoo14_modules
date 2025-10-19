from odoo import models, fields, api

class WarehouseValuationLineDetail(models.Model):
    _name = 'warehouse.valuation.line.detail'
    _order = 'date asc'

    line_id = fields.Many2one('warehouse.valuation.line')
    product_id = fields.Many2one('product.product', related='line_id.product_id')
    date = fields.Datetime()
    move = fields.Char()
    type = fields.Char()
    qt = fields.Float()
    price_unit = fields.Float()
    value_unit = fields.Float()
    cost = fields.Float()
    qt_initial = fields.Float()
    qt_final = fields.Float()
    amount_value = fields.Float()

    def open(self):
        return