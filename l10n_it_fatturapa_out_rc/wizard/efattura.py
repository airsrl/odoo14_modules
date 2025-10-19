# Copyright 2021 Alex Comba - Agile Business Group
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

# from odoo.addons.l10n_it_fatturapa_out.wizard.efattura import (
#     EFatturaOut as _EFatturaOut,
# )
# Aggiunta di Marco Frascerra (part of https://www.huroos.com)
# Convertirò la classe EFatturaOut in una classe figlia di TransientModel dell'orm di Odoo
from odoo import models


# extend the EFatturaOut class to add a new helper function
class EFatturaOut(models.TransientModel):
    _inherit = "efattura.out"

    def get_template_values(self):
        get_sign = self.env["wizard.export.fatturapa"].getSign
        template_values = super(EFatturaOut, self).get_template_values()
        template_values.update({"get_sign": get_sign})
        return template_values
