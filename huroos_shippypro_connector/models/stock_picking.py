# Copyright 2022 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

from odoo import models, fields
from odoo.exceptions import UserError
from ..code import shippypro_utils as su


class huroos_shippypro_connector_shippypro(models.Model):
    _inherit = 'stock.picking'

    shippy_pro_sent_date = fields.Datetime(
        string="Date ShippyPro",
        readonly=True,
        copy=False
    )
    shippy_pro_estimated_arrival_date = fields.Datetime(
        string="Estimated arrival",
        readonly=True,
        copy=False
    )
    label_url = fields.Char(
        string="Shipping label link",
        readonly=True,
        copy=False,
        force_save=True
    )
    shippy_pro_order_number = fields.Char(
        string="Shippy pro order number",
        readonly=True,
        copy=False
    )
    shippy_pro_tracking_external_link = fields.Char(
        string="Tracking external link",
        readonly=True,
        copy=False
    )
    shippy_pro_tracking_number = fields.Char(
        string="Tracking number",
        readonly=True,
        copy=False
    )
    is_customer_location_usage = fields.Boolean(
        string="Customer location usage",
        compute="compute_is_customer_location",
        copy=False,
        readonly=True
    )
    is_shipping_auto_confirm = fields.Boolean(
        string="Is shipping auto confirm",
        compute="compute_is_shipping_auto_confirm",
        copy=False,
        readonly=True
    )
    carrier = fields.Many2one(
        related="carrier_id.shippy_pro_carrier_id"
    )

    def compute_is_customer_location(self):
        self.is_customer_location_usage = self.location_dest_id.usage == 'customer'

    def compute_is_shipping_auto_confirm(self):
        self.is_shipping_auto_confirm = self.env.company.shipping_auto_confirm

    def start_shippypro_routine(self):
        """ Creates order and shipping to ShippyPRO """
        shipping_auto_confirm = self.env.company.shipping_auto_confirm

        # Defaulting carrier_id (if empty) with company default carrier
        self.carrier_id = self.carrier_id or self.env.company.carrier_id

        # Defaulting packaging type (if empty) with company default delivery package type
        if self.has_packages:
            packages = self.package_ids
            for package in packages:
                if not package.packaging_id and self.env.company.delivery_package_type_id:
                    package.packaging_id = self.env.company.delivery_package_type_id.id

        # Checking is a legit picking movement
        if self.picking_type_id.code not in ["outgoing", "incoming"]:
            raise UserError(f"Picking type {self.picking_type_id.code} is not suitable for ShippyPRO")

        # Checking quantity done for outgoing movements
        if self.picking_type_id.code == "outgoing":
            items_count = 0
            for move in self.move_lines:
                items_count += int(move.quantity_done)
            if items_count == 0:
                raise UserError("No quantity done for outgoing shipping.")

        # Creates shipping
        is_shippypro_order_created = self.shippy_pro_put_order()
        if shipping_auto_confirm and is_shippypro_order_created:
            # Confirm shipping
            self.shippy_pro_ship_order()

    def task_exec_get_tracking_numbers(self):
        res = su.task_exec_get_tracking_numbers(self)
        return res

    def shippy_pro_put_order(self):
        # Create shipping on ShippyPRO
        res = su.shippy_pro_put_order(self)
        return res

    def shippy_pro_ship_order(self):
        # Confirm shipping
        res = su.shippy_pro_ship_order(self)
        return res
