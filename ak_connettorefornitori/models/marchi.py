from odoo import fields, models, api


class categoria(models.Model):
    _name = "ak_connettore.marchio"
    _description = "Marchio"

    distributore_id = fields.Many2one('ak_connettore.distributore', string="Distributore")
    name = fields.Char(string="Marchio", required=True)
    marchio_mappata = fields.Char(string="Marchio mappato")
    note = fields.Text(string="Note")
