from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    warehouse_valuation = fields.Float(compute='get_warehouse_valuation')

    def get_warehouse_valuation(self):
        for p in self:
            #L'ultima riga contiene il valore progressivo finale
            line_id = self.env['warehouse.valuation.line.detail'].search([('product_id', '=', p.product_variant_id.id)], order='date desc', limit=1)
            if line_id:
                p.warehouse_valuation = line_id.amount_value
            else:
                p.warehouse_valuation = 0


    def open_warehouse_valuation(self):
        action = self.env["ir.actions.actions"]._for_xml_id("huroos_warehouse_valuation.huroos_warehouse_valuation_detail_action")
        action['domain'] = [('product_id', '=', self.product_variant_id.id)]
        return action