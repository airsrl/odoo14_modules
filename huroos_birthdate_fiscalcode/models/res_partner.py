from odoo import fields, models, api
from codicefiscale import codicefiscale

class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthdate_fiscalcode=fields.Date(string='Data di nascita',compute='_compute_birthday_fiscalcode',inverse="set_birthdate_fiscalcode",store=True)
    birthmonth_fiscalcode=fields.Char(string='Mese di nascita',compute='_compute_birthday_fiscalcode',inverse="set_birthdate_fiscalcode",store=True)

    @api.depends('fiscalcode')
    def _compute_birthday_fiscalcode(self):
        for partner in self:
            if partner.fiscalcode:
                try:
                    cf = codicefiscale.decode(partner.fiscalcode)
                    birthdate = cf['birthdate']
                    partner.birthdate_fiscalcode=birthdate.date()
                    partner.birthmonth_fiscalcode=birthdate.strftime("%B").capitalize()
                except:
                    partner.birthdate_fiscalcode = False
                    partner.birthmonth_fiscalcode = ""

    def set_birthdate_fiscalcode(self):
        pass