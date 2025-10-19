
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class PosConfig(models.Model):
    _inherit = 'pos.config'

    printer_ip = fields.Char(
        'Printer IP Address',
        help='The hostname or IP address of the fiscal printer',
        size=45
    )
    use_https = fields.Boolean(
        string='Use https',
        default=False,
    )
    show_receipt_when_printing = fields.Boolean(
        string='Show receipt on screen when printing', default=True)
    fiscal_printer_serial = fields.Char(string='Fiscal Printer Serial')

    fiscal_cashdrawer = fields.Boolean(string='Fiscal Printer Open CashDrawer')

    # decimal_rounding = fields.Integer(string='Product Price Decimal Rounding',
    #                                   default='2',
    #                                   help="Insert the numbers of decimal precison (from 0 to 2) for a product price to be rounded eg.: enter 1 to round 1,42 to 1,40")


    # @api.constrains('decimal_rounding')
    # def _check_value(self):
    #     if self.decimal_rounding > 2 or self.decimal_rounding < 0:
    #         raise ValidationError(_('Enter Value Between 0-2.'))
