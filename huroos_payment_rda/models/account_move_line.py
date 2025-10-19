from odoo import fields, models, api


class AccountMoveLIne(models.Model):
    _inherit = 'account.move.line'

    amount_residual_rda = fields.Monetary(
        string='Importo residuo',
        store=False,
        compute='_compute_amount_residual_rda'
    )

    @api.depends('amount_residual', 'move_id.withholding_tax_amount')
    def _compute_amount_residual_rda(self):
        for rec in self:
            if rec.amount_residual:
                rec.amount_residual_rda = rec.amount_residual - rec.move_id.withholding_tax_amount
            else:
                rec.amount_residual_rda = 0

    def reconcile(self):
        # Tolgo la riga di ritenuta se sto riconciliando con Nota di Credito
        results = super(AccountMoveLIne, self).reconcile()

        if not results:
            return results

        if "in_refund" in self.move_id.mapped("move_type"):
            for invoice in self.move_id:
                invoice.write({'withholding_tax_line_ids': [(5, )]})

        return results
