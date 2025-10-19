from odoo import models, api


class FatturaPAAttachmentOut(models.Model):
    _inherit = "fatturapa.attachment.out"

    @api.model
    def invoiceCreate(self, fatt, fatturapa_attachment, FatturaBody, partner_id):
        res = super(FatturaPAAttachmentOut,self).invoiceCreate(fatt, fatturapa_attachment, FatturaBody, partner_id)

        partner = res.partner_id
        invoice_line_ids = res.invoice_line_ids
        for line in invoice_line_ids:
            if partner.income_account_id and res.move_type in ('out_invoice', 'out_refund', 'out_receipt'):
                line.write({'account_id':partner.income_account_id.id})
            if partner.expence_account_id and res.move_type in ('in_invoice', 'in_refund', 'in_receipt'):
                line.write({'account_id':partner.expence_account_id.id})
        
        return res