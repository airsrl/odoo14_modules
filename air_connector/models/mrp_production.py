from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    tag_ids = fields.Many2many('mrp.production.tag', string='Tags')


class MrpProductionTag(models.Model):
    _name = 'mrp.production.tag'

    name = fields.Char(string="Nome")
    color = fields.Integer(string="Colore")
