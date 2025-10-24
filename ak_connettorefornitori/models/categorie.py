from odoo import fields, models, api


class categoria(models.Model):
    _name = "ak_connettore.categoria"
    _description = "Categoria"

    distributore_id = fields.Many2one('ak_connettore.distributore', string="Distributore")
    name = fields.Char(string="Categoria", required=True)
    categoria_mappata = fields.Many2one('product.category', string="Categoria mappata")
    note = fields.Text(string="Note")



