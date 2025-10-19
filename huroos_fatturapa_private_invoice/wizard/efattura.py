# from odoo.addons.l10n_it_fatturapa_out.wizard.efattura import EFatturaOut
import logging

from odoo.addons.l10n_it_fatturapa_out.wizard.efattura import (
    EFatturaOut as _EFatturaOut,
)
_logger = logging.getLogger(__name__)


class EFatturaOut(_EFatturaOut):
    # Devo estendere get_id_fiscale_iva() con il controllo su private_foreign e aggiungere il codice iso 99999999999, ma
    # dato che get_id_fiscale_iva() è dentro la funzione get_template_values() e non posso estendere una funzione
    # incapsulata dentro un'altra funzione, devo ricopiare l'intera funziona get_id_fiscale_iva()

    def get_template_values(self):  # noqa: C901
        """Prepare values and helper functions for the template"""

        def get_id_fiscale_iva(partner, prefer_fiscalcode=False):
            id_paese = partner.country_id.code
            if partner.vat:
                if id_paese == "IT" and partner.vat.startswith("IT"):
                    id_codice = partner.vat[2:]
                else:
                    id_codice = partner.vat
            elif partner.fiscalcode or id_paese == "IT":
                id_codice = False
            else:
                id_codice = "99999999999"

            if prefer_fiscalcode and partner.fiscalcode:
                id_codice = partner.fiscalcode

            # INFO-1: Controllo aggiunto in questo modulo
            if partner.private_foreign and not partner.vat and not partner.fiscalcode:
                id_codice = "99999999999"

            return {
                "id_paese": id_paese,
                "id_codice": id_codice,
            }

        template_values = super().get_template_values()
        template_values["get_id_fiscale_iva"] = get_id_fiscale_iva

        return template_values
