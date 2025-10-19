from odoo import fields, models, api

class ProductPackaging(models.Model):
    _inherit = 'product.template'

    product_packaging = fields.Boolean('Prodotto imballaggio')

    qty_contained=fields.Float('Qtà contenuta')

    box_standard_id=fields.Many2one('product.product',
                                     string='BOX',
                                     domain="[('product_packaging','=',True)]"
                                     )
    box_tester_id = fields.Many2one('product.product',
                                      string='BOX',
                                      domain = "[('product_packaging','=',True)]"
                                     )
    hide_in_doc=fields.Boolean('Nascondi in Doc.')
