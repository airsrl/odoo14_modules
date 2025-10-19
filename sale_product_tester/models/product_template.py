from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    allowed_tester = fields.Boolean('Tester')
    tester_description=fields.Char('Suffisso tester',default="")
    tester_price=fields.Monetary('Tester price')



