from odoo import fields, models, api


class WizardImportFatturapa(models.TransientModel):
    _inherit = "wizard.import.fatturapa"


    def invoiceCreate(self, fatt, fatturapa_attachment, FatturaBody, partner_id):
        invoice=super(WizardImportFatturapa,self).invoiceCreate(fatt, fatturapa_attachment, FatturaBody, partner_id)
        invoice._onchange_invoice_date()
        return invoice