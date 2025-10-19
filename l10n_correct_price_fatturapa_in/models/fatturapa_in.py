from odoo import fields, models, api

class AccountMove(models.Model):
    _inherit = "account.move"

    def write(self,vals):
        res=super(AccountMove, self).write(vals)
        return res
class FatturaPAAttachmentIn(models.Model):
    _inherit = "fatturapa.attachment.in"


    automatic_correction = fields.Boolean(string='Correggi automaticamente',help="Allinea automaticamente il valore delle imposte identiche alla fattura xml",default=True)