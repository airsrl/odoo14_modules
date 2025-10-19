from odoo import fields, models, api


class WizardDeleteInvoice(models.TransientModel):
    _name = 'wizard.delete.invoice'

    name = fields.Char()
    date_start = fields.Date('Data inizio')
    date_end = fields.Date('Data fine')
    journal_ids = fields.Many2many('account.journal',
                                   string='Registri'
                                   )

    def invoice_to_delete(self):
        invoices = self.env['account.move'].search(
            [
                ('date', '>=', self.date_start),
                ('date', '<=', self.date_end),
                ('journal_id', 'in', self.journal_ids.ids),
                ('ref', 'not like', 'RdA')
            ]
        )

        witholding_tax_ids = self.env['withholding.tax.move'].search([ ('date', '>=', self.date_start),('date', '<=', self.date_end),])
        for wt in witholding_tax_ids:
            wt.write({'state': 'due'})
            if wt.full_reconcile_id:
                wt.full_reconcile_id.reconciled_line_ids.remove_move_reconcile()
                self.env.cr.commit()
            print("Aggiornato stato ritenuta")

        invoices.with_context(force_delete=True).force_delete_invoice_and_related_payment()
        return