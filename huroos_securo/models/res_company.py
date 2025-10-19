from odoo import fields, models, api


class ResCompany(models.Model):
    _inherit = 'res.company'


    securo_incaricato = fields.Char('Nome incaricato alla consegna dpi')
    securo_luogo = fields.Char('Luogo consegna dpi')
    securo_signature = fields.Binary('Firma incaricato',attachment=True)
    securo_ceo =  fields.Binary('Firma datore di lavoro',attachment=True)
