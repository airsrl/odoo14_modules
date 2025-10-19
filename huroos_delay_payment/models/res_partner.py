from odoo import models, fields, api
from odoo.exceptions import UserError



class ResPartner(models.Model):
    _inherit = 'res.partner'

    due_date_delay = fields.Integer()
    months_due_date_delay = fields.Many2many('huroos.month',string="Mesi")
