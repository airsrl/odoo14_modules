from odoo import models
from odoo.exceptions import UserError


class WizardExportFatturapa(models.TransientModel):
    _inherit = "wizard.export.fatturapa"

    def exportFatturaPA(self):
        try:
            return super(WizardExportFatturapa, self).exportFatturaPA()
        except Exception:
            # Search the invoice that produced the error
            invoices_with_error = []
            invoices_by_partner = self.group_invoices_by_partner()
            for partner in invoices_by_partner:
                context_partner = self.env.context.copy()
                context_partner.update({"lang": partner.lang})
                for invoice_ids in invoices_by_partner[partner]:
                    fatturapa, progressivo_invio = self.exportInvoiceXML(
                        partner, invoice_ids, context=context_partner
                    )
                    try:
                        self.saveAttachment(fatturapa, progressivo_invio)
                    except Exception:
                        for invoice in fatturapa.invoices:
                            invoices_with_error.append(invoice.name)

            raise UserError('Le seguenti fatture producono errori e devono essere controllate: ' + ', '.join(invoices_with_error))