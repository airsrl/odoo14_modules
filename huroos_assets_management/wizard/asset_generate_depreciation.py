from odoo import api, fields, models


class WizardAssetsGenerateDepreciations(models.TransientModel):
    _inherit = "wizard.asset.generate.depreciation"

    skip_invoice_generation = fields.Boolean(string="Non generare registrazioni")

    def do_generate(self):
        if self.skip_invoice_generation:
            return super(WizardAssetsGenerateDepreciations, self.with_context(skip_invoice_generation=True)).do_generate()
        else:
            return super(WizardAssetsGenerateDepreciations, self).do_generate()
