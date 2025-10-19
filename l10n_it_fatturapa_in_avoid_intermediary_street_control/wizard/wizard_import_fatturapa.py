from odoo import models, _
from odoo.exceptions import UserError


class WizardImportFatturapa(models.TransientModel):
    _inherit = "wizard.import.fatturapa"

    def importFatturaPA(self):
        self.ensure_one()
        fatturapa_attachment_obj = self.env["fatturapa.attachment.in"]
        fatturapa_attachment_ids = self.env.context.get("active_ids", False)

        (
            price_precision,
            different_price_precisions,
            original_price_precision,
        ) = self._set_decimal_precision("Product Price", "price_decimal_digits")
        (
            qty_precision,
            different_qty_precisions,
            original_qty_precision,
        ) = self._set_decimal_precision(
            "Product Unit of Measure", "quantity_decimal_digits"
        )
        (
            discount_precision,
            different_discount_precisions,
            original_discount_precision,
        ) = self._set_decimal_precision("Discount", "discount_decimal_digits")

        new_invoices = []
        # convert to dict in order to be able to modify context
        self.env.context = dict(self.env.context)
        for fatturapa_attachment_id in fatturapa_attachment_ids:
            self.env.context.update(inconsistencies="")
            fatturapa_attachment = fatturapa_attachment_obj.browse(
                fatturapa_attachment_id
            )
            if fatturapa_attachment.in_invoice_ids:
                raise UserError(_("File is linked to bills yet."))

            fatt = self.get_invoice_obj(fatturapa_attachment)
            cedentePrestatore = fatt.FatturaElettronicaHeader.CedentePrestatore
            # 1.2
            partner_id = self.getCedPrest(cedentePrestatore)
            # 1.3
            TaxRappresentative = fatt.FatturaElettronicaHeader.RappresentanteFiscale
            # 1.5
            Intermediary = (
                fatt.FatturaElettronicaHeader.TerzoIntermediarioOSoggettoEmittente
            )

            generic_inconsistencies = ""
            if self.env.context.get("inconsistencies"):
                generic_inconsistencies = self.env.context["inconsistencies"] + "\n\n"

            xmlproblems = getattr(fatt, "_xmldoctor", None)
            if xmlproblems:  # None or []
                generic_inconsistencies += "\n".join(xmlproblems) + "\n\n"

            # 2
            for fattura in fatt.FatturaElettronicaBody:

                # reset inconsistencies
                self.env.context.update(inconsistencies="")

                invoice = self.invoiceCreate(
                    fatt, fatturapa_attachment, fattura, partner_id
                )

                self.set_StabileOrganizzazione(cedentePrestatore, invoice)
                if TaxRappresentative:
                    tax_partner_id = self.getPartnerBase(
                        TaxRappresentative.DatiAnagrafici
                    )
                    invoice.write({"tax_representative_id": tax_partner_id})
                if Intermediary:
                    # This tyr was made to avoid the street control,
                    # if there is no street it continues to work.
                    try:
                        Intermediary_id = self.getPartnerBase(Intermediary.DatiAnagrafici)
                    except:
                        Intermediary_id = self.getPartnerBase(Intermediary.DatiAnagrafici)
                    invoice.write({"intermediary": Intermediary_id})
                new_invoices.append(invoice.id)
                self.check_invoice_amount(invoice, fattura)

                invoice.set_einvoice_data(fattura)

                if self.env.context.get("inconsistencies"):
                    invoice_inconsistencies = self.env.context["inconsistencies"]
                else:
                    invoice_inconsistencies = ""
                invoice.inconsistencies = (
                    generic_inconsistencies + invoice_inconsistencies
                )

        if price_precision and different_price_precisions:
            self._restore_original_precision(price_precision, original_price_precision)
        if qty_precision and different_qty_precisions:
            self._restore_original_precision(qty_precision, original_qty_precision)
        if discount_precision and different_discount_precisions:
            self._restore_original_precision(
                discount_precision, original_discount_precision
            )

        return {
            "view_type": "form",
            "name": "Electronic Bills",
            "view_mode": "tree,form",
            "res_model": "account.move",
            "type": "ir.actions.act_window",
            "domain": [("id", "in", new_invoices)],
        }