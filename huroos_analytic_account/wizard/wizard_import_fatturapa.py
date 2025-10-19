from odoo import models, api


class WizardImportFatturapa(models.TransientModel):
    _inherit = "wizard.import.fatturapa"

    @api.model
    def invoiceCreate(self, fatt, fatturapa_attachment, FatturaBody, partner_id):
        res = super(WizardImportFatturapa,self).invoiceCreate(fatt, fatturapa_attachment, FatturaBody, partner_id)

        partner = res.partner_id
        invoice_line_ids = res.invoice_line_ids
        for line in invoice_line_ids:
            if partner.analytic_account_id:
                line.write({'analytic_account_id':partner.analytic_account_id.id})
            if partner.analytic_tag_ids:
                line.write({'analytic_tag_ids':[(6,0,partner.analytic_tag_ids.ids)]})
        
        return res