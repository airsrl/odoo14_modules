from odoo import fields, models, api


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    code_msi=fields.Char('Codice Mag. MSI')

