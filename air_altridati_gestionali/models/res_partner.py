from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    dati_gestionali_ids = fields.Many2many('air.dati.gestionali')
