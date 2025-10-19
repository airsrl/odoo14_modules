# Copyright 2022 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

from odoo import models, fields


class huroos_shippypro_connector_authentication(models.Model):
    _inherit = 'res.company'

    authentication_code = fields.Char(
        string="Auth code"
    )
    APIOrdersID = fields.Char(
        string="API orders ID",
        help="SHIPPYPRO: You need to add an APIOrders marketplace in order to use this request. "
             "You can retrieve your own APIOrdersID by clicking on Edit button inside the marketplace page")
    image_url_path = fields.Char(
        string="Good image URL",
        help='Good image on ShippyPRO'
    )
    shipping_auto_confirm = fields.Boolean(
        string="Shipping auto confirm",
        help="When checked the shipping is auto confirmed and a shipping label is created with the selected carrier.")
    carrier_id = fields.Many2one(
        comodel_name="delivery.carrier",
        string="Default delivery carrier"
    )
    delivery_package_type_id = fields.Many2one(
        comodel_name="product.packaging",
        string="Default delivery package type"
    )
    shippy_pro_carrier_id = fields.Many2one(
        related="carrier_id.shippy_pro_carrier_id",
        readonly=True
    )
