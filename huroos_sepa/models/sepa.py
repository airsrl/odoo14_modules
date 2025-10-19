import base64
import random

from lxml import etree
from pyxb.utils import domutils
from pyxb.binding.datatypes import decimal as pyxb_decimal, ValidationError
import time

try:
    from base64 import encodebytes
except ImportError:  # 3+
    from base64 import encodestring as encodebytes

from odoo import models, fields, api,_
from odoo.addons.account_sepa import sanitize_communication
from odoo.exceptions import UserError
from odoo.tools import float_repr
from odoo.tools import float_round
from ..bindings.binding import (
    CBIPaymentRequest,
    CBIGroupHeader,
    CBIPaymentInstructionInformation,
    CBICreditTransferTransactionInformation,
    CBIPartyIdentification1,
    CBIOrganisationIdentification1,
    CBIGenericIdentification1,
    CBIIdType1,
    CBIPaymentTypeInformation1, CBIPaymentTypeInformation2, CBIServiceLevel1, CBIPartyIdentification4,
    CBIPostalAddress6, CBIIdType2,
    CBIOrganisationIdentification3, CBICashAccount1, CBIAccountIdentification1,
    CBIBranchAndFinancialInstitutionIdentification2, CBIFinancialInstitutionIdentification3,
    CBIClearingSystemMemberIdentification1, PaymentIdentification1, CBIAmountType1, CBIPartyIdentification3,
    ActiveOrHistoricCurrencyAndAmount,
    CBICashAccount2, RemittanceInformation5,
    CategoryPurpose1Choice)


from ..bindings.binding401 import (
    CBIPaymentRequest as CBIPaymentRequest01,
    CBIGroupHeader as CBIGroupHeader01,
    CBIPaymentInstructionInformation as CBIPaymentInstructionInformation01,
    CBICreditTransferTransactionInformation as CBICreditTransferTransactionInformation01,
    CBIPartyIdentification1 as CBIPartyIdentification101,
    CBIOrganisationIdentification1 as CBIOrganisationIdentification101,
    CBIGenericIdentification1 as CBIGenericIdentification101,
    CBIIdType1 as CBIIdType101,
    CBIPaymentTypeInformation1 as CBIPaymentTypeInformation101,
    CBIPaymentTypeInformation2 as CBIPaymentTypeInformation201,
    CBIServiceLevel1 as CBIServiceLevel101,
    CBIPartyIdentification4 as CBIPartyIdentification401,
    CBIIdType2 as CBIIdType201,
    CBIOrganisationIdentification3 as CBIOrganisationIdentification301,
    CBICashAccount1 as CBICashAccount101,
    CBIAccountIdentification1 as CBIAccountIdentification101,
    CBIBranchAndFinancialInstitutionIdentification2 as CBIBranchAndFinancialInstitutionIdentification201,
    CBIFinancialInstitutionIdentification3 as CBIFinancialInstitutionIdentification301,
    CBIClearingSystemMemberIdentification1 as CBIClearingSystemMemberIdentification101,
    PaymentIdentification1 as PaymentIdentification101,
    CBIAmountType1 as CBIAmountType101,
    CBIPartyIdentification3 as CBIPartyIdentification301,
    ActiveOrHistoricCurrencyAndAmount as ActiveOrHistoricCurrencyAndAmount01,
    CBICashAccount2 as CBICashAccount201,
    CategoryPurpose1Choice as CategoryPurpose1Choice01,
    DateAndDateTime2Choice as DateAndDateTime2Choice01,
    CBIPostalAddress24 as CBIPostalAddress2401,
    RemittanceInformation16 as RemittanceInformation1601,
    CBICashAccount3 as CBICashAccount301)


class AccountBatchPayment(models.Model):
    _inherit = 'account.batch.payment'

    iso_type = fields.Selection([('00.04.00', 'CBI PaymentRequest 00.04.00'),
                                 ('00.04.01', 'CBI PaymentRequest 00.04.01'),
                                 ('001.001.03', 'Pain.001.001.03'),
                                 ('001.003.03', 'Pain.001.003.03'),
                                 ('001.003.03.ch', 'Pain.001.001.03.ch.02')], default='00.04.00')



    def _generate_export_file(self):
        """
        Funzione che viene chiamata per generare il file XML del pagamento raggruppato
        Verifica il tipo ISO da esportare
        """
        if self.payment_method_code == 'sepa_ct':
            payments = self.payment_ids.sorted(key=lambda r: r.id)

            if self.iso_type == '001.003.03.ch':
                xml_doc = self._create_pain_001_001_03_ch_document(payments)
            elif self.iso_type == '001.003.03':
                xml_doc = self._create_pain_001_003_03_document(payments)
            elif self.iso_type == '001.001.03':
                xml_doc = self._create_pain_001_001_03_document(payments)
            elif self.iso_type == '00.04.00':
                xml_doc = self._create_00_04_00_document(payments)
            elif self.iso_type == '00.04.01':
                xml_doc = self._create_00_04_01_document(payments)

            return {
                'file': encodebytes(xml_doc),
                'filename': "SCT-" + self.journal_id.code + "-" + str(fields.Date.today()) + ".xml",
                # 'warning': self.sct_warning,
            }

        return super(AccountBatchPayment, self)._generate_export_file()



    def _create_00_04_01_document(self, doc_payments):
        """
        Crea il Documento di Tipo ISO 00_04_01
        """
        sepa_payment = CBIPaymentRequest01()
        company = self.journal_id.company_id
        name_length = self.sct_generic and 35 or 70
        val_MsgId = str(int(time.time() * 100))[-10:]
        val_MsgId = sanitize_communication(self.journal_id.company_id.name[-15:]) + val_MsgId
        val_MsgId = str(random.random()) + val_MsgId
        val_MsgId = val_MsgId[-30:]

        val_NbOfTxs = str(len(doc_payments))
        if len(val_NbOfTxs) > 15:
            raise ValidationError(_("Too many transactions for a single file."))
        if not self.journal_id.bank_account_id.bank_bic:
            raise UserError(_("There is no Bank Identifier Code recorded for bank account '%s' of journal '%s'") % (
                self.journal_id.bank_account_id.acc_number, self.journal_id.name))

        #HEADER
        sepa_payment.GrpHdr = CBIGroupHeader01(
            MsgId=val_MsgId,
            CreDtTm=time.strftime("%Y-%m-%dT%H:%M:%S"),
            NbOfTxs=val_NbOfTxs,
            CtrlSum=self.journal_id._get_CtrlSum(doc_payments),
        )

        sepa_payment.GrpHdr.InitgPty = CBIPartyIdentification101(
            Nm=sanitize_communication(company.sepa_initiating_party_name[:name_length]),
            Id=CBIIdType101()
        )
        sepa_payment.GrpHdr.InitgPty.Id.OrgId = CBIOrganisationIdentification101()
        #'0799996F'
        cbi_id = company.cbi_id
        if not cbi_id:
            raise UserError("Devi impostare l'ID CBI sull'azienda. ")
        sepa_payment.GrpHdr.InitgPty.Id.OrgId.append(
            CBIGenericIdentification101(
                Id=cbi_id,
                Issr='CBI'
            )
        )

        #PAYMENT
        sepa_payment.PmtInf = CBIPaymentInstructionInformation01(
            PmtInfId=(val_MsgId + str(self.journal_id.id))[-30:],
            BtchBookg=True,
            #Richiesta esito: TRA con esito, TRF senza esito
            PmtMtd='TRA',
            #Piorità Pagamento: NORM = Normale, HIGH = Urgente
            PmtTpInf=CBIPaymentTypeInformation101(
                InstrPrty='NORM',
                SvcLvl=CBIServiceLevel101(
                    Cd='SEPA'
                )
            ),
            #fields.Date.to_string(self.date)
            ReqdExctnDt=DateAndDateTime2Choice01(
                Dt=fields.Date.to_string(self.date)
            ),
            # Nome e indirizzo banca Debitore
            Dbtr=CBIPartyIdentification401(
                Nm=sanitize_communication(company.sepa_initiating_party_name[:name_length]),
                PstlAdr=CBIPostalAddress2401(
                    TwnNm=company.partner_id.city or "NOT_PROVIDED",
                    Ctry=company.partner_id.country_id.code,
                ),
                Id=CBIIdType201(
                    OrgId=CBIOrganisationIdentification301(
                        Othr=CBIGenericIdentification101(
                            Id=company.vat,
                            Issr='ADE'
                        )
                    )
                )
            ),
            # IBAN Banca Debitore
            DbtrAcct=CBICashAccount201(
                Id=CBIAccountIdentification101(
                    IBAN=self.journal_id.bank_account_id.sanitized_acc_number
                )
            ),
            # Abi Banca Debitore
            DbtrAgt=CBIBranchAndFinancialInstitutionIdentification201(
                FinInstnId=CBIFinancialInstitutionIdentification301(
                    ClrSysMmbId=CBIClearingSystemMemberIdentification101(
                        MmbId=self.journal_id.bank_account_id.bank_id.abi
                    )
                )
            ),
            ChrgBr='SLEV',
            CdtTrfTxInf=[]
        )

        if not self.journal_id.bank_account_id.bank_id.abi:
            raise UserError("Devi inserire il codice ABI sulla banca " + self.journal_id.bank_account_id.bank_id.name)

        #Abi Banca Debitore
        # sepa_payment.PmtInf.DbtrAgt = CBIBranchAndFinancialInstitutionIdentification201(
        #     FinInstnId=CBIFinancialInstitutionIdentification301(
        #         ClrSysMmbId=CBIClearingSystemMemberIdentification101(
        #             MmbId=self.journal_id.bank_account_id.bank_id.abi
        #         )
        #     )
        # )


        for payment in doc_payments:

            if not payment.partner_id.city:
                raise UserError("Manca la citta' per il Partner " + payment.partner_id.name)
            if not payment.partner_id.country_id:
                raise UserError("Manca la nazione per il Partner " + payment.partner_id.name)

            sepa_payment.PmtInf.CdtTrfTxInf.append(
                CBICreditTransferTransactionInformation01(
                    PmtId=PaymentIdentification101(
                        InstrId=sanitize_communication(payment.name),
                        EndToEndId=((val_MsgId + str(self.journal_id.id))[-30:] + str(payment.id))[-30:]
                    ),
                    PmtTpInf=CBIPaymentTypeInformation201(
                        #Causale bancaria
                        #Utilizzare “SUPP” per bonifici generici, “SALA” per stipendi, “INTC” per giroconti/girofondi;
                        CtgyPurp=CategoryPurpose1Choice01(
                            Cd='SUPP'
                        )
                    ),
                    Amt=CBIAmountType101(
                        InstdAmt=ActiveOrHistoricCurrencyAndAmount01(
                            float_repr(float_round(payment.amount, 2), 2),
                            Ccy=payment.currency_id and payment.currency_id.name or payment.journal_id.company_id.currency_id.name,
                        )
                    ),
                    Cdtr=CBIPartyIdentification301(
                        Nm=sanitize_communication((payment.invoice_partner_display_name or payment.partner_id.name)[:70]),
                        PstlAdr=CBIPostalAddress2401(
                            Ctry=payment.partner_id.country_id.code or "NOT_PROVIDED",
                            TwnNm=payment.partner_id.city
                        ),
                        CtryOfRes=payment.partner_id.country_id.code
                    ),
                    CdtrAcct=CBICashAccount301(
                        Id=CBIAccountIdentification101(
                            IBAN=sanitize_communication(payment.partner_bank_id.acc_number.replace(' ', ''))
                        )
                    ),
                    RmtInf=RemittanceInformation1601(
                        Ustrd=[sanitize_communication(str(payment.ref))]
                    )
                )
            )




        attach_str = sepa_payment.toxml(
            encoding="UTF-8",
        )

        return attach_str



    def _create_00_04_00_document(self, doc_payments):
        """
        Crea il Documento di Tipo ISO 00_04_00
        """
        sepa_payment = CBIPaymentRequest()
        company = self.journal_id.company_id
        name_length = self.sct_generic and 35 or 70
        val_MsgId = str(int(time.time() * 100))[-10:]
        val_MsgId = sanitize_communication(self.journal_id.company_id.name[-15:]) + val_MsgId
        val_MsgId = str(random.random()) + val_MsgId
        val_MsgId = val_MsgId[-30:]

        val_NbOfTxs = str(len(doc_payments))
        if len(val_NbOfTxs) > 15:
            raise ValidationError(_("Too many transactions for a single file."))
        if not self.journal_id.bank_account_id.bank_bic:
            raise UserError(_("There is no Bank Identifier Code recorded for bank account '%s' of journal '%s'") % (
                self.journal_id.bank_account_id.acc_number, self.journal_id.name))

        #HEADER
        sepa_payment.GrpHdr = CBIGroupHeader(
            MsgId=val_MsgId,
            CreDtTm=time.strftime("%Y-%m-%dT%H:%M:%S"),
            NbOfTxs=val_NbOfTxs,
            CtrlSum=self.journal_id._get_CtrlSum(doc_payments),
        )

        sepa_payment.GrpHdr.InitgPty = CBIPartyIdentification1(
            Nm=sanitize_communication(company.sepa_initiating_party_name[:name_length]),
            Id=CBIIdType1()
        )
        sepa_payment.GrpHdr.InitgPty.Id.OrgId = CBIOrganisationIdentification1()
        #'0799996F'
        cbi_id = company.cbi_id
        if not cbi_id:
            raise UserError("Devi impostare l'ID CBI sull'azienda. ")
        sepa_payment.GrpHdr.InitgPty.Id.OrgId.append(
            CBIGenericIdentification1(
                Id=cbi_id,
                Issr='CBI'
            )
        )

        #PAYMENT
        sepa_payment.PmtInf = CBIPaymentInstructionInformation(
            PmtInfId=(val_MsgId + str(self.journal_id.id))[-30:],
            #Richiesta esito: TRA con esito, TRF senza esito
            PmtMtd='TRA',
            #Piorità Pagamento: NORM = Normale, HIGH = Urgente
            PmtTpInf=CBIPaymentTypeInformation1(
                InstrPrty='NORM',
                SvcLvl=CBIServiceLevel1(
                    Cd='SEPA'
                )
            ),
            ReqdExctnDt=fields.Date.to_string(self.date),
            Dbtr=CBIPartyIdentification4(),
            DbtrAcct=CBICashAccount1(),
            DbtrAgt=CBIBranchAndFinancialInstitutionIdentification2(),
            ChrgBr='SLEV',
            CdtTrfTxInf=[]
        )

        #Nome e indirizzo banca Debitore
        sepa_payment.PmtInf.Dbtr = CBIPartyIdentification4(
            Nm=sanitize_communication(company.sepa_initiating_party_name[:name_length]),
            PstlAdr=CBIPostalAddress6(
                Ctry=company.partner_id.country_id.code,
            ),
            Id=CBIIdType2(
                OrgId=CBIOrganisationIdentification3(
                    Othr=CBIGenericIdentification1(
                        Id=company.vat,
                        Issr='ADE'
                    )
                )
            )
        )

        #IBAN Banca Debitore
        sepa_payment.PmtInf.DbtrAcct.Id = CBIAccountIdentification1(
            IBAN=self.journal_id.bank_account_id.sanitized_acc_number
        )

        if not self.journal_id.bank_account_id.bank_id.abi:
            raise UserError("Devi inserire il codice ABI sulla banca " + self.journal_id.bank_account_id.bank_id.name)

        #Abi Banca Debitore
        sepa_payment.PmtInf.DbtrAgt = CBIBranchAndFinancialInstitutionIdentification2(
            FinInstnId=CBIFinancialInstitutionIdentification3(
                ClrSysMmbId=CBIClearingSystemMemberIdentification1(
                    MmbId=self.journal_id.bank_account_id.bank_id.abi
                )
            )
        )


        for payment in doc_payments:

            if not payment.partner_id.city:
                raise UserError("Manca la citta' per il Partner " + payment.partner_id.name)
            if not payment.partner_id.country_id:
                raise UserError("Manca la nazione per il Partner " + payment.partner_id.name)

            sepa_payment.PmtInf.CdtTrfTxInf.append(
                CBICreditTransferTransactionInformation(
                    PmtId=PaymentIdentification1(
                        InstrId=sanitize_communication(payment.name),
                        EndToEndId=((val_MsgId + str(self.journal_id.id))[-30:] + str(payment.id))[-30:]
                    ),
                    PmtTpInf=CBIPaymentTypeInformation2(
                        #Causale bancaria
                        #Utilizzare “SUPP” per bonifici generici, “SALA” per stipendi, “INTC” per giroconti/girofondi;
                        CtgyPurp=CategoryPurpose1Choice(
                            Cd='SUPP'
                        )
                    ),
                    Amt=CBIAmountType1(
                        InstdAmt=ActiveOrHistoricCurrencyAndAmount(
                            float_repr(float_round(payment.amount, 2), 2),
                            Ccy=payment.currency_id and payment.currency_id.name or payment.journal_id.company_id.currency_id.name,
                        )
                    ),
                    Cdtr=CBIPartyIdentification3(
                        Nm=sanitize_communication((payment.invoice_partner_display_name or payment.partner_id.name)[:70]),
                        PstlAdr=CBIPostalAddress6(
                            Ctry=payment.partner_id.country_id.code,
                            TwnNm=payment.partner_id.city
                        ),
                        CtryOfRes=payment.partner_id.country_id.code
                    ),
                    CdtrAcct=CBICashAccount2(
                        Id=CBIAccountIdentification1(
                            IBAN=sanitize_communication(payment.partner_bank_id.acc_number.replace(' ', ''))
                        )
                    ),
                    RmtInf=RemittanceInformation5(
                        Ustrd=[sanitize_communication(str(payment.ref))]
                    )
                )
            )




        attach_str = sepa_payment.toxml(
            encoding="UTF-8",
        )

        return attach_str



