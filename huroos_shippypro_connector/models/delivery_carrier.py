# Copyright 2022 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

from odoo import models, fields
from ..code import shippypro_utils as su


class delivery_carrier_custom(models.Model):
    _inherit = 'delivery.carrier'

    shippy_pro_carrier_id = fields.Many2one(
        "shippypro.carrier",
        string="ShippyPRO carrier"
    )


class shippypro_carriers(models.Model):
    _name = "shippypro.carrier"
    _description = "ShippyPRO carrier"

    def _update_carriers_from_shippypro(self):
        shippypro_carriers_list = su.get_carriers(self.env)
        if not shippypro_carriers_list:
            return
        existing_carrier_ids = self.search([]).mapped("carrier_id")
        for carrier in shippypro_carriers_list:
            if carrier[0] not in existing_carrier_ids:
                self.create(
                    {
                        "carrier_id": carrier[0],
                        "carrier_type": carrier[1],
                        "carrier_label": carrier[2],
                        "carrier_service": carrier[3],

                    }
                )

    carrier_id = fields.Char(
        string="Carrier ID"
    )
    carrier_type = fields.Char(
        string="Carrier type"
    )
    carrier_label = fields.Char(
        string="Label"
    )
    carrier_service = fields.Char(
        string="Carrier service"
    )

    def name_get(self):
        res = []
        for record in self:
            name = f"{record.carrier_type} - {record.carrier_label} - {record.carrier_service}"
            res.append((record.id, name))

        return res
