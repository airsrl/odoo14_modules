from odoo import api, fields, models


class setup_margini(models.Model):
    _name = "ak_connettore.setup_margini"
    _description = "Setup margine"

    da = fields.Float(string="Da")
    a = fields.Float(string="A")
    ricarico = fields.Float(string="Ricarico")
    arrotondamento = fields.Float(string="Arrotondamento")

