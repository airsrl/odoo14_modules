from odoo import models, api


class WizardImportFatturapa(models.TransientModel):
    _inherit = "wizard.import.fatturapa"

    @api.model
    def invoiceCreate(self, fatt, fatturapa_attachment, FatturaBody, partner_id):
        res = super(WizardImportFatturapa,self).invoiceCreate(fatt, fatturapa_attachment, FatturaBody, partner_id)

        partner = res.partner_id
        invoice_line_ids = res.invoice_line_ids
        for line in invoice_line_ids:
            if partner.income_account_id and res.move_type in ('out_invoice', 'out_refund', 'out_receipt'):
                line.write({'account_id':partner.income_account_id.id})
            if partner.expence_account_id and res.move_type in ('in_invoice', 'in_refund', 'in_receipt'):
                line.write({'account_id':partner.expence_account_id.id})

        for line in res.line_ids:
            tax = self.env['account.tax'].search([('name','=',line.name)], limit=1)
            if tax and line.account_id not in tax.invoice_repartition_line_ids.mapped('account_id'):
                if partner.income_account_id and res.move_type in ('out_invoice', 'out_refund', 'out_receipt'):
                    line.write({'account_id':partner.income_account_id.id})
                if partner.expence_account_id and res.move_type in ('in_invoice', 'in_refund', 'in_receipt'):
                    line.write({'account_id':partner.expence_account_id.id})
        
        return res
