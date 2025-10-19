from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    product_excel_columns = fields.Char(
        string="Colonne Excel per import prodotti",
        config_parameter="huroos_excel_import_for_users.product_excel_columns"
    )
    sale_order_excel_columns = fields.Char(
        string="Colonne Excel per import ordini di vendita",
        config_parameter="huroos_excel_import_for_users.sale_order_excel_columns"
    )
