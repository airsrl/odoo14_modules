# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).
import base64
import os
import shutil
import zipfile
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'fatturapa.attachment.import.zip'

    journal_id = fields.Many2one('account.journal')
    use_sequence = fields.Boolean()

    # def action_import(self):
    #     r = super(AccountMove, self.with_context({'force_journal_id': self.journal_id, 'force_use_sequence': self.use_sequence})).action_import()
    #     return r

    def action_import(self):
        self.ensure_one()
        #Aggiunta valori per forzare registro e sequenza da xml
        self = self.with_context({'force_journal_id': self.journal_id, 'force_use_sequence': self.use_sequence})

        tmp_dir_name = "/tmp/{}_{}".format(
            self.env.cr.dbname, datetime.now().timestamp()
        )
        if os.path.isdir(tmp_dir_name):
            shutil.rmtree(tmp_dir_name)
        os.mkdir(tmp_dir_name)
        zip_data = base64.b64decode(self.datas)
        zip_file_path = "%s/e_bills_to_import.zip" % tmp_dir_name
        with open(zip_file_path, "wb") as writer:
            writer.write(zip_data)
        tmp_dir_name_xml = tmp_dir_name + "/XML"
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(tmp_dir_name_xml)
        for xml_filename in os.listdir(tmp_dir_name_xml):
            with open("{}/{}".format(tmp_dir_name_xml, xml_filename), "rb") as reader:
                content = reader.read()
            attach_vals = {
                "name": xml_filename,
                "datas": base64.encodebytes(content),
            }
            att_in = self.env["fatturapa.attachment.in"].create(attach_vals)

            #Controlla se importare xml in fatture attive o passive
            journal_type = 'purchase'
            if self.journal_id.type == 'sale':
                journal_type = 'sale'

            if att_in.xml_supplier_id.id == self.env.company.partner_id.id or journal_type == 'sale':
                #FATTURA ATTIVA XML
                att_in.unlink()
                # message_follower_ids added by ['fatturapa.attachment.in'].create
                # if attach_vals["message_follower_ids"]:
                #     del attach_vals["message_follower_ids"]
                attach_vals["state"] = "validated"
                att_out = self.env["fatturapa.attachment.out"].create(attach_vals)
                att_out._import_e_invoice_out()
                att_out.attachment_import_zip_id = self.id
            else:
                #FATTURA PASSIVA XML
                in_invoice_registration_date = (
                    self.env.company.in_invoice_registration_date
                )
                # we don't have the received date
                self.env.company.in_invoice_registration_date = "inv_date"
                att_in.attachment_import_zip_id = self.id
                wizard = (
                    self.env["wizard.import.fatturapa"]
                    .with_context(
                        active_ids=[att_in.id], active_model="fatturapa.attachment.in"
                    )
                    .create({})
                )
                wizard.importFatturaPA()
                att_in.attachment_import_zip_id = self.id
                self.env.company.in_invoice_registration_date = (
                    in_invoice_registration_date
                )
        if os.path.isdir(tmp_dir_name):
            shutil.rmtree(tmp_dir_name)
        self.state = "done"


class FatturaPAAttachmentOut(models.Model):
    _inherit = "fatturapa.attachment.out"

    def invoiceCreate(self, fatt, fatturapa_attachment, FatturaBody, partner_id):
        # invoice_id = super(FatturaPAAttachmentOut, self).invoiceCreate(fatt, fatturapa_attachment, FatturaBody, partner_id)
        context = self.env.context

        if context.get('force_journal_id', False):
            partner_model = self.env["res.partner"]
            invoice_model = self.env["account.move"]
            currency_model = self.env["res.currency"]
            ftpa_doctype_model = self.env["fiscal.document.type"]
            wizard_import = self.env["wizard.import.fatturapa"]
            rel_docs_model = self.env["fatturapa.related_document_type"]
            partner = partner_model.browse(partner_id)
            company = self.env.company
            currency = currency_model.search(
                [("name", "=", FatturaBody.DatiGenerali.DatiGeneraliDocumento.Divisa)]
            )
            if not currency:
                raise UserError(
                    _(
                        "No currency found with code %s."
                        % FatturaBody.DatiGenerali.DatiGeneraliDocumento.Divisa
                    )
                )
            sale_journal = context.get('force_journal_id')
            debit_account_id = sale_journal.default_account_id.id
            comment = ""
            docType_id = False
            invtype = "out_invoice"
            docType = FatturaBody.DatiGenerali.DatiGeneraliDocumento.TipoDocumento
            if docType:
                docType_record = ftpa_doctype_model.search([("code", "=", docType)])
                if docType_record:
                    docType_id = docType_record[0].id
                else:
                    raise UserError(_("Document type %s not handled.") % docType)
                if docType == "TD04":
                    invtype = "out_refund"

            causLst = FatturaBody.DatiGenerali.DatiGeneraliDocumento.Causale
            if causLst:
                for caus in causLst:
                    comment += caus + "\n"
            e_invoice_date = datetime.strptime(
                FatturaBody.DatiGenerali.DatiGeneraliDocumento.Data, "%Y-%m-%d"
            ).date()
            invoice_data = {
                "invoice_date": e_invoice_date,
                "name": FatturaBody.DatiGenerali.DatiGeneraliDocumento.Numero,
                "fiscal_document_type_id": docType_id,
                "sender": fatt.FatturaElettronicaHeader.SoggettoEmittente or False,
                "move_type": invtype,
                "partner_id": partner_id,
                "currency_id": currency[0].id,
                "journal_id": sale_journal.id,
                "fiscal_position_id": (partner.property_account_position_id.id or False),
                "invoice_payment_term_id": partner.property_supplier_payment_term_id.id,
                "company_id": company.id,
                "fatturapa_attachment_out_id": fatturapa_attachment.id,
                "narration": comment,
            }
            wizard_import.set_efatt_rounding(FatturaBody, invoice_data)
            wizard_import.set_art73(FatturaBody, invoice_data)

            Withholdings = FatturaBody.DatiGenerali.DatiGeneraliDocumento.DatiRitenuta
            if Withholdings:
                wizard_import.log_inconsistency(
                    _("Invoice %s: DatiRitenuta not handled")
                    % FatturaBody.DatiGenerali.DatiGeneraliDocumento.Numero
                )
            wizard_import.set_e_invoice_lines(FatturaBody, invoice_data)
            invoice = invoice_model.create(invoice_data)
            self.set_invoice_line_ids(FatturaBody, debit_account_id, partner, invoice)
            invoice._recompute_dynamic_lines()
            invoice.write(invoice._convert_to_write(invoice._cache))

            rel_docs_dict = {
                "order": FatturaBody.DatiGenerali.DatiOrdineAcquisto,
                "contract": FatturaBody.DatiGenerali.DatiContratto,
                "agreement": FatturaBody.DatiGenerali.DatiConvenzione,
                "reception": FatturaBody.DatiGenerali.DatiRicezione,
                "invoice": FatturaBody.DatiGenerali.DatiFattureCollegate,
            }

            for rel_doc_key, rel_doc_data in rel_docs_dict.items():
                if not rel_doc_data:
                    continue
                for rel_doc in rel_doc_data:
                    doc_datas = wizard_import._prepareRelDocsLine(
                        invoice.id, rel_doc, rel_doc_key
                    )
                    for doc_data in doc_datas:
                        # Note for v12: must take advantage of batch creation
                        rel_docs_model.create(doc_data)

            wizard_import.set_activity_progress(FatturaBody, invoice)
            wizard_import.set_ddt_data(FatturaBody, invoice)
            wizard_import.set_delivery_data(FatturaBody, invoice)
            wizard_import.set_summary_data(FatturaBody, invoice)
            wizard_import.set_vehicles_data(FatturaBody, invoice)

            due_dates = wizard_import._get_last_due_date(FatturaBody.DatiPagamento)
            if due_dates:
                invoice.invoice_date_due = due_dates[-1]
            invoice.with_context(
                check_move_validity=False
            )._move_autocomplete_invoice_lines_values()

            wizard_import.set_attachments_data(FatturaBody, invoice)
            invoice.process_negative_lines()
            # invoice_id.journal_id = context.get('force_journal_id').id
        else:
            invoice = super(FatturaPAAttachmentOut, self).invoiceCreate(fatt, fatturapa_attachment, FatturaBody,
                                                                           partner_id)
        if context.get('force_use_sequence', False):
            invoice.name = FatturaBody.DatiGenerali.DatiGeneraliDocumento.Numero

        return invoice

