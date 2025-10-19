from odoo import api, fields, models
from odoo.exceptions import ValidationError


class AssetAsset(models.Model):
    _inherit = "asset.asset"

    already_partially_depr = fields.Boolean(
        string="Già parzialmente ammortizzato",
        help="Seleziona se il bene è stato precedentemente ammortizzato su un altro sistema."
    )
    partially_depr_times = fields.Integer(
        string="Ammortizzazioni subite in precedenza",
        help="Inserire il numero di volte in cui il bene è stato ammortizzato negli altri sistemi."
    )
    can_edit_partial_depr = fields.Boolean(
        compute="_compute_can_edit_partial_depr",
        help="Campo tecnico per rendere readonly i campi di ammortamento parziale, una volta avvenuto "
             "il primo ammortamento sul sistema Odoo."
    )

    @api.constrains('already_partially_depr', 'partially_depr_times')
    def _check_partially_depr_vals(self):
        if self.already_partially_depr and (self.partially_depr_times <= 0):
            raise ValidationError(
                "I campi 'Ammortizzazioni subite in precedenza' e 'Valore già ammortizzato' non possono essere minori "
                "o uguali a zero, se il campo 'Già parzialmente ammortizzato' è selezionato."
            )

    @api.depends('depreciation_ids', 'depreciation_ids.line_ids')
    def _compute_can_edit_partial_depr(self):
        for asset in self:
            asset.can_edit_partial_depr = True
            if asset.depreciation_ids and asset.depreciation_ids.line_ids:
                asset.can_edit_partial_depr = False

    @api.onchange('already_partially_depr')
    def _onchange_already_partially_depr(self):
        """Azzero valori storico ammortamenti in caso di spunta tolta"""
        if self.already_partially_depr:
            self.partially_depr_times = 0

    def update_depreciation_lines(self):
        depr_date = fields.date(self.purchase_date.year, 12, 31)

        for i in range(self.partially_depr_times):

            for depr in self.depreciation_ids:
                depr.generate_depreciation_lines(depr_date)

            depr_date = fields.date(depr_date.year + 1, 12, 31)
