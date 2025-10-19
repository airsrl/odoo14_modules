from odoo import fields, models

class PartnerPrivateInvoice(models.Model):
    _inherit = 'res.partner'

    private_foreign = fields.Boolean(
        string="Privato estero",
        help="Indica che il contatto viene trattato come un Privato estero,"
             "quindi in assenza di CF e VAT, il suo codice generico seguirà lo standard ISO +11 volte 9"
    )
