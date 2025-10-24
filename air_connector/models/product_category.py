from odoo import models, fields


class ProductCategory(models.Model):
    _inherit = 'product.category'

    wp_avoid_sync = fields.Boolean(string='WP Avoid Sync', default=False)
