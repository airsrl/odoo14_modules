from odoo import models, fields, api

class WarehouseValuationLine(models.Model):
    _name = 'warehouse.valuation.line'

    valuation_id = fields.Many2one('warehouse.valuation')
    product_id = fields.Many2one('product.product')
    final_qty = fields.Float()
    cost = fields.Float()
    product_type = fields.Selection([('purchase', 'Acquisto'), ('production', 'Produzione')])
    detail_lines = fields.One2many('warehouse.valuation.line.detail', 'line_id', delete='cascade')

    #CMP
    cmp_price_unit = fields.Float()
    cmp_total_value = fields.Float()

    #FIFO
    fifo_price_unit = fields.Float()
    fifo_total_value = fields.Float()

    #LIFO
    lifo_price_unit = fields.Float()
    lifo_total_value = fields.Float()



