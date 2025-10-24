from odoo import fields, models, api


class product_template_custom(models.Model):
    _inherit = "product.template"
    #_description = "Campi aggiuntivi modulo product.template"

    default_code_import = fields.Char(string="Riferimento interno padre")

class product_product_custom(models.Model):
    _inherit = "product.product"

    default_code_import = fields.Char(related='product_tmpl_id.default_code_import')