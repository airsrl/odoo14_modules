from odoo import models, fields,api,_



class HuroosMonth(models.Model):
    _name = 'huroos.month'

    code=fields.Integer('Codice')
    name=fields.Char('Nome')