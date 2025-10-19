from odoo import models


class AccountTax(models.Model):
    _inherit = "account.tax"

    def _get_tax_name(self):
        """
        Override della funzione per fix problema (copia) nel nome delle
        imposte che compaiono del report Liquidazione IVA
        """

        self.ensure_one()
        name = self.with_context({'lang': self.env.user.lang}).name
        if self.parent_tax_ids and len(self.parent_tax_ids) == 1:
            name = self.parent_tax_ids[0].name
        return name
