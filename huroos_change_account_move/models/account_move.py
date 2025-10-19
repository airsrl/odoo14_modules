from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class AccountMove(models.Model):
    _inherit = 'account.move'




class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'




