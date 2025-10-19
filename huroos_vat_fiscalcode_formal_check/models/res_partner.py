from odoo import api, models
from odoo.exceptions import ValidationError
import re

CODICE_REGEXP = "^[0-9A-Z]{16}$"
IVA_REGEXP = "^[0-9]{11}$"
SETDISP = [1, 0, 5, 7, 9, 13, 15, 17, 19, 21, 2, 4, 18,
           20, 11, 3, 6, 8, 12, 14, 16, 10, 22, 25, 24, 23]
ORD_ZERO = ord('0')
ORD_A = ord('A')


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.constrains('fiscalcode')
    def check_fiscalcode(self):
        for partner in self:
            if not partner.fiscalcode:
                # Because it is not mandatory
                continue
            elif partner.company_type == "person":
                # Person case
                if partner.company_name:
                    # In E-commerce, if there is company_name,
                    # the user might insert VAT in fiscalcode field.
                    # Perform the same check as Company case
                    continue
                if len(partner.fiscalcode) != 16:
                    raise ValidationError("The fiscal code lenght is incorrect: "
                                          "it should be exactly 16 characters long.")
                fiscalcode = partner.fiscalcode.upper()
                match = re.match(CODICE_REGEXP, fiscalcode)
                if not match:
                    raise ValidationError("The fiscal code contains invalid characters: "
                                          "the only valid characters are letters and numbers.")
                s = 0
                for i in range(1, 14, 2):
                    character = fiscalcode[i]
                    if character.isdigit():
                        s += ord(character) - ORD_ZERO
                    else:
                        s += ord(character) - ORD_A
                for i in range(0, 15, 2):
                    character = fiscalcode[i]
                    if character.isdigit():
                        character = ord(character) - ORD_ZERO
                    else:
                        character = ord(character) - ORD_A
                    s += SETDISP[character]
                if s % 26 + ORD_A != ord(fiscalcode[15]):
                    raise ValidationError("The fiscal code is incorrect: "
                                          "the control code does not match.")
        return True

    @api.constrains('vat')
    def check_vat_validation(self):
        for partner in self:
            if not partner.vat:
                # Because it's not mandatory
                continue
            else:
                if len(partner.vat) == 13:
                    vat_country_code = partner.vat[:2]
                    vat = partner.vat[2:]
                    if vat_country_code != partner.country_id.code:
                        raise ValidationError("The VAT country code does not match: "
                                              "it should be the same as the country set in Contacts.")
                else:
                    vat = partner.vat
                if len(vat) != 11:
                    raise ValidationError("The VAT lenght is incorrect: "
                                          "it should be exactly 11 characters long "
                                          "(country code excluded, if present).")
                match = re.match(IVA_REGEXP, vat)
                if not match:
                    raise ValidationError("The VAT number contains invalid characters: "
                                          "it should contain only digits.")
                s = 0
                for i in range(0, 10, 2):
                    s += ord(vat[i]) - ORD_ZERO
                for i in range(1, 10, 2):
                    digit = 2 * (ord(vat[i]) - ORD_ZERO)
                    if digit > 9:
                        digit -= 9
                    s += digit
                if (10 - s % 10) % 10 != ord(vat[10]) - ORD_ZERO:
                    raise ValidationError("The VAT number is incorrect: "
                                          "the control code does not match.")
        return True
