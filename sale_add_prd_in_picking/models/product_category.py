# Copyright 2022 - Huroos srl - www.huroos.comMany2many
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api


class product_category(models.Model):
    """ Adding category infos """
    _inherit = ['product.category']

    additional_products_in_picking = fields.Many2many(
        comodel_name="product.product",
        string="Additional products",
    )


