from odoo import _, models, fields
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"

    po_integration_invoice_id = fields.Many2one('account.move')