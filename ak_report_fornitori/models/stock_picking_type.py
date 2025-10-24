from odoo import models, fields


class StockPickingType(models.Model):
    _inherit = 'stock.picking.type'

    is_sellout_picking_type = fields.Boolean(string="Is a sellout picking type", help="Used for report fornitori")
    is_scrap_picking_type = fields.Boolean(string="Is a scrap picking type", help="Used for report fornitori")
    is_new_coming_picking_type = fields.Boolean(string="Is a new coming picking type", help="Used for report fornitori")
