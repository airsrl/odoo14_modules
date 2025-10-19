from odoo import fields, models, api

class SecuroVehicleType(models.Model):
    _name="securo.vehicle.type"
    name = fields.Char()
class FleetVehicleModle(models.Model):
    _inherit = 'fleet.vehicle.model'


    vehicle_type = fields.Many2one('securo.vehicle.type',string="Tipo generale")
