import re
from datetime import datetime

import logging
from odoo import api, fields, models, registry
from odoo.exceptions import UserError
from odoo.tools import float_is_zero
from odoo.tools.translate import _
from odoo.tools.misc import formatLang
from odoo.addons.base_iban.models.res_partner_bank import pretty_iban



_logger = logging.getLogger(__name__)


WT_CODES_MAPPING = {
    "RT01": "ritenuta",
    "RT02": "ritenuta",
    "RT03": "inps",
    "RT04": "enasarco",
    "RT05": "enpam",
    "RT06": "other",
}


class WizardImportFatturapa(models.TransientModel):
    _inherit = "wizard.import.fatturapa"

    def amount_tax_summary(self, FatturaBody, invoice):
        amount_summary=0
        Summary_datas = FatturaBody.DatiBeniServizi.DatiRiepilogo
        if Summary_datas:
            for summary in Summary_datas:
                amount_summary += float(summary.Imposta or 0.0)
        return amount_summary

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
                self.amount_summary_correct(invoice,fattura,partner_id)
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

    def amount_summary_correct(self,invoice, FatturaBody, partner_id):
        val=[]
        amount_summary=self.amount_tax_summary(FatturaBody, invoice)
        lang_env = invoice.with_context(lang=invoice.partner_id.lang).env
        if invoice.amount_by_group:
            imposte=invoice.amount_by_group[0]
            imposte_list=list(imposte)
            imposte_list[1]=amount_summary
            amount_string =list(formatLang(lang_env, amount_summary, currency_obj=invoice.currency_id))
            str_a=''
            imposte_list[3] = str_a.join(amount_string)

            imposte_tuple = tuple(imposte_list)
            val.append(imposte_tuple)
        invoice.sudo().write({'amount_by_group':val})

    def importFatturaOdA(self):
        warningmess = None
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
                    Intermediary_id = self.getPartnerBase(Intermediary.DatiAnagrafici)
                    invoice.write({"intermediary": Intermediary_id})
                new_invoices.append(invoice.id)
                self.check_invoice_amount(invoice, fattura)

                invoice.set_einvoice_data(fattura)
                vals ={'partner_id':invoice.partner_id.id,'invoice_ids':[(4,invoice.id)]}
                purchase_order = self.env['purchase.order'].create(vals)



                if self.env.context.get("inconsistencies"):
                    invoice_inconsistencies = self.env.context["inconsistencies"]
                else:
                    invoice_inconsistencies = ""
                invoice.inconsistencies = (
                    generic_inconsistencies + invoice_inconsistencies
                )
                self.amount_summary_correct(invoice,fattura,partner_id)
                for invoice_line in invoice.invoice_line_ids:
                    if invoice_line.product_id:
                        dt = datetime.combine(invoice_line.date, datetime.min.time())
                        vals_righe={ 'sequence': 10, 'name':invoice_line.name,'product_id':invoice_line.product_id.id,
                                     'order_id':purchase_order.id,'product_qty':invoice_line.quantity,
                                     'price_unit':invoice_line.price_unit,'taxes_id':[(6,0,invoice_line.tax_ids.ids)],
                                     'date_planned':dt,'analytic_tag_ids': [[6, False, []]],
                                     'qty_received_manual': 0, 'product_uom': 1,'display_type': False,'move_dest_ids': [],
                                     'account_analytic_id': False,}

                        purchase_line =self.env['purchase.order.line'].create(vals_righe)
                        invoice_line.purchase_line_id = purchase_line.id
                        #tolto la conferma automatica
                # purchase_order.button_confirm()
                # try:
                #  # In order to validate stock movement
                #     action_view= purchase_order.action_view_picking()
                #     picking = self.env[action_view['res_model']].browse(int(action_view['res_id']))
                #     confirm = picking.action_confirm()
                    # if confirm:
                    #
                    #     action_assign = picking.action_assign()
                    #
                    #     if action_assign:
                    #
                    #         validate = picking.button_validate()
                    #
                    #         if validate:
                    #             if validate['res_model'] == 'stock.immediate.transfer':
                    #                 wiz = self.env[validate['res_model']].with_context(validate['context']).sudo().create({
                    #
                    #                 })
                    #                 res = wiz.sudo().process()
                    #
                    #                 # If the quantity sent is more than the one requested procede.
                    #
                    #         elif validate['res_model'] == 'stock.overprocessed.transfer':
                    #             wiz = self.env[res['res_model']].with_context(validate['context']).sudo().create({
                    #
                    #             })
                    #             res = wiz.sudo().action_confirm()
                    #
                    #
                    #         elif validate['res_model'] == 'stock.backorder.confirmation':
                    #             wiz = self.env[res['res_model']].with_context(validate['context']).sudo().create({
                    #
                    #             })
                    #
                    #             wiz.sudo().process_cancel_backorder()
                # except:
                #         warningmess = {
                # 'title': ('Richiesta controllo manuale'),
                # 'message' : _('Impossibile confermare il movimento di magazzino automaticamente!'),
                #         }



        if price_precision and different_price_precisions:
            self._restore_original_precision(price_precision, original_price_precision)
        if qty_precision and different_qty_precisions:
            self._restore_original_precision(qty_precision, original_qty_precision)
        if discount_precision and different_discount_precisions:
            self._restore_original_precision(
                discount_precision, original_discount_precision
            )
        if not warningmess:
            return {
                "view_type": "form",
                "name": "Electronic Bills",
                "view_mode": "tree,form",
                "res_model": "account.move",
                "type": "ir.actions.act_window",
                "domain": [("id", "in", new_invoices)],
            }
        else:
            return {'warning': warningmess}

    def  get_line_product(self, line, partner):
        product=super(WizardImportFatturapa, self).get_line_product(line, partner)
        if not product:

            if line.CodiceArticolo:
                if len(line.CodiceArticolo) > 1:
                    CodiceArticolo = line.CodiceArticolo[0]
                else:
                    CodiceArticolo = line.CodiceArticolo[0]
                ean =  CodiceArticolo
                vals_product={'default_code':ean['CodiceValore'],
                          'name':line['Descrizione'] if 'Descrizione' in line else '','type':'product'}
                product =self.env['product.product'].search(['|',('barcode','=',ean['CodiceValore']),('default_code','=',ean['CodiceValore'])],limit=1)
                if not product:
                    product=self.env['product.product'].create(vals_product)
        return product
