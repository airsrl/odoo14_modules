from odoo import models

from .efattura import EFatturaOut


class WizardExportFatturapa(models.TransientModel):
    _inherit = "wizard.export.fatturapa"

    def _get_efattura_class(self):
        # return EFatturaOut
        return DeprecationWarning("Questa funzione è deprecata, aggiornare i moduli l10n_it_fatturapa_out,"
                                  "l10n_it_fatturapa_out_rc e l10n_it_fatturapa_out_wt.")
