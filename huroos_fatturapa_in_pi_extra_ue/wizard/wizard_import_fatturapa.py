import logging
import re

from odoo import models
from odoo.exceptions import UserError
from odoo.tools.translate import _
from textwrap import wrap
import warnings

_logger = logging.getLogger(__name__)

class WizardImportFatturapa(models.TransientModel):
    _inherit = "wizard.import.fatturapa"

    def getPartnerBase(self, DatiAnagrafici):  # noqa: C901
        if not DatiAnagrafici:
            return False
        partner_model = self.env["res.partner"]
        cf = DatiAnagrafici.CodiceFiscale or False
        vat = False
        if DatiAnagrafici.IdFiscaleIVA:
            # Format Italian VAT ID to always have 11 char
            # to avoid validation error when creating the given partner
            if DatiAnagrafici.IdFiscaleIVA.IdPaese.upper() == "IT":
                vat = "{}{}".format(
                    DatiAnagrafici.IdFiscaleIVA.IdPaese.upper(),
                    DatiAnagrafici.IdFiscaleIVA.IdCodice.rjust(11, "0")[:11],
                )
            else:
                vat = "{}{}".format(
                    DatiAnagrafici.IdFiscaleIVA.IdPaese.upper(),
                    re.sub(r"\W+", "", DatiAnagrafici.IdFiscaleIVA.IdCodice).upper(),
                )
                #check if the PI is from Swiss it generate error
                if DatiAnagrafici.IdFiscaleIVA.IdPaese.upper() == "CH" and len(vat) == 12:
                    wrap_vat = wrap(vat, 3)
                    vat = "{}{}{}{}{}{}{}".format(
                        wrap_vat[0],
                        '-',
                        wrap_vat[1],
                        '.',
                        wrap_vat[2],
                        '.',
                        wrap_vat[3],
                    )

        partners = partner_model
        res_partner_rule = (
            self.env["ir.model.data"]
            .sudo()
            .xmlid_to_object("base.res_partner_rule", raise_if_not_found=False)
        )
        if vat:
            domain = [("vat", "ilike", vat)]
            if (
                    self.env.context.get("from_attachment")
                    and res_partner_rule
                    and res_partner_rule.active
            ):
                att = self.env.context.get("from_attachment")
                domain.extend(
                    [
                        "|",
                        ("company_id", "child_of", att.company_id.id),
                        ("company_id", "=", False),
                    ]
                )
            partners = partner_model.search(domain)
            # air fix cerca il contatto per partita iva e controlla che ci sia
            # l'etichetta Fornitore
            if len(partners) > 1:
                _logger.info('air fix cerca il contatto per partita iva e fornitore')
                category_id_model = self.env["res.partner.category"]
                category_fornitore_id = category_id_model.search([('name', 'like', 'Fornitor')], limit=1)
                # _logger.info(f'category_fornitore_id: {category_fornitore_id.id}')
                if category_fornitore_id:
                    domain = [("vat", "=", vat), ("category_id", "in", [category_fornitore_id.id])]
                    partners = partner_model.search(domain)
        if not partners and cf:
            domain = [("fiscalcode", "=", cf)]
            if (
                    self.env.context.get("from_attachment")
                    and res_partner_rule
                    and res_partner_rule.active
            ):
                att = self.env.context.get("from_attachment")
                domain.extend(
                    [
                        "|",
                        ("company_id", "child_of", att.company_id.id),
                        ("company_id", "=", False),
                    ]
                )
            partners = partner_model.search(domain)
        commercial_partner_id = False
        if len(partners) > 1:
            for partner in partners:
                if (
                        commercial_partner_id
                        and partner.commercial_partner_id.id != commercial_partner_id
                ):
                    if "99999999999" in vat:
                        warnings.warn("Two distinct partners with "
                                      "extra UE VAT number 99999999999"
                                      "already present in database.", DeprecationWarning)
                    else:
                        raise UserError(
                            _(
                                "Two distinct partners with "
                                "VAT number %s or Fiscal Code %s already "
                                "present in db." % (vat, cf)
                            )
                        )
                commercial_partner_id = partner.commercial_partner_id.id
        if partners:
            if not commercial_partner_id:
                commercial_partner_id = partners[0].commercial_partner_id.id
            self.check_partner_base_data(commercial_partner_id, DatiAnagrafici)
            return commercial_partner_id
        else:
            # partner to be created
            country_id = False
            if DatiAnagrafici.IdFiscaleIVA:
                CountryCode = DatiAnagrafici.IdFiscaleIVA.IdPaese
                countries = self.CountryByCode(CountryCode)
                if countries:
                    country_id = countries[0].id
                    if countries[0].code == 'CH':
                        return
                else:
                    raise UserError(
                        _("Country Code %s not found in system.") % CountryCode
                    )
            vals = {
                "vat": vat,
                "fiscalcode": cf,
                "is_company": (
                        DatiAnagrafici.Anagrafica.Denominazione and True or False
                ),
                "eori_code": DatiAnagrafici.Anagrafica.CodEORI or "",
                "country_id": country_id,
            }
            if DatiAnagrafici.Anagrafica.Nome:
                vals["firstname"] = DatiAnagrafici.Anagrafica.Nome
            if DatiAnagrafici.Anagrafica.Cognome:
                vals["lastname"] = DatiAnagrafici.Anagrafica.Cognome
            if DatiAnagrafici.Anagrafica.Denominazione:
                vals["name"] = DatiAnagrafici.Anagrafica.Denominazione

            return partner_model.create(vals).id
