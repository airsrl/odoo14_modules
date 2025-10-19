# -*- coding: utf-8 -*-
import logging

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from lxml import etree
from io import BytesIO
import PyPDF2
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject, NumberObject, createStringObject

from odoo.modules import get_module_resource


class ComunicazioneLiquidazione(models.Model):
    _inherit = "comunicazione.liquidazione"

    natura_giuridica = fields.Char(string="Natura Giuridica")
    declarant_firstname = fields.Char(string="Nome")
    declarant_lastname = fields.Char(string="Cognome")
    declarant_city = fields.Char(string="Città Nascita")
    declarant_date = fields.Date(string="Data Nascita")
    codice_ateco_id = fields.Many2one("ateco.category", string="Codice Ateco")
    def set_need_appearances_writer(self, writer):
        """
        Funzione usata dalla get_export_pdf per generare il report
        precompilato dell'AdE liquidazione periodica IVA
        """
        try:
            catalog = writer._root_object
            # get the AcroForm tree
            if "/AcroForm" not in catalog:
                writer._root_object.update({
                    NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})

            need_appearances = NameObject("/NeedAppearances")
            writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
            return writer

        except Exception as e:
            print('set_need_appearances_writer() catch : ', repr(e))
            return writer

    def get_export_iva_annuale_pdf(self):
        """
        Funzione che compila il modulo standard della comunicazione periodica
        IVA dell'AdE, il modulo è presente nella cartella data/moduli_pdf
        """
        pdf_module_path = get_module_resource('l10n_it_account_lipe', 'data', 'moduli_pdf', 'IVA_2023_mod.pdf')
        input_stream = open(pdf_module_path, "rb")

        pdf_reader = PyPDF2.PdfFileReader(input_stream, strict=False)

        if "/AcroForm" in pdf_reader.trailer["/Root"]:
            pdf_reader.trailer["/Root"]["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        pdf_writer = PyPDF2.PdfFileWriter()

        self.set_need_appearances_writer(pdf_writer)
        if "/AcroForm" in pdf_writer._root_object:
            # Acro form is form field, set needs appearances to fix printing issues
            pdf_writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})

        data_dict_pag1 = {
            'CODICE FISCALE1': self.taxpayer_vat,
            'partita_iva_2': self.taxpayer_vat,
            'denominazione_ragione_sociale': self.company_id.name,
            'codice_fiscale_sottoscrittore': self.declarant_fiscalcode,
            'codice_carica': self.codice_carica_id.code,
            'natura_giuridica': self.natura_giuridica,
            'firma1': 'X',
            'cognome': self.declarant_lastname,
            'nome': self.declarant_firstname,
            'data_nascita_day': self.declarant_date.day if self.declarant_date else False,
            'data_nascita_month': self.declarant_date.month if self.declarant_date else False,
            'data_nascita_year': self.declarant_date.year if self.declarant_date else False,
            'comune_nascita': self.declarant_city,
            'codice_fiscale_incaricato': self.delegate_fiscalcode,
            'firma2': 'X',
            'data_impegno': f'{str(self.date_commitment).split("-")[2]}     {str(self.date_commitment).split("-")[1]}     {str(self.date_commitment).split("-")[0]}',
        }

        data_dict_pag2 = {
            'CODICE FISCALE2': self.taxpayer_vat,
            'codice_ateco': self.codice_ateco_id.code.replace(".","") if self.codice_ateco_id.code else False,
        }

        if len(self.quadri_vp_ids) == 0:
            raise ValidationError(_('Nessun Quadro VP aggiunto.'))

        lipe_annuale = self.quadri_vp_ids[0].liquidazioni_ids[0]

        def get_imponibile_imposta_with_type(tag):
            #Differenzia tra Beni e Servizi
            tax_ids = self.env['account.tax'].search([('dichiarazione_annuale_quadro', '=', tag)])
            imponibile_beni = 0
            imposte_beni = 0
            imponibile_servizi = 0
            imposte_servizi = 0
            for tax in tax_ids:
                #Righe Imponibile
                account_move_line_imponibile = self.env['account.move.line'].search(['&', '&', ('tax_ids', '=', tax.id), ('date', '>=', lipe_annuale.date_range_ids[0].date_start), ('date', '<=', lipe_annuale.date_range_ids[0].date_end)])
                #Righe Imposta
                account_move_line_imposta = self.env['account.move.line'].search(['&', '&', ('tax_line_id', '=', tax.id), ('date', '>=', lipe_annuale.date_range_ids[0].date_start), ('date', '<=', lipe_annuale.date_range_ids[0].date_end)])





                debit_beni = 0
                credit_beni = 0
                debit_servizi = 0
                credit_servizi = 0
                for line in account_move_line_imponibile:

                    if tag == 'VJ16':
                        #Gestione ITA
                            debit_servizi += line.debit
                            credit_servizi += line.credit
                    else:
                        #Gestione INTA/EXTRA
                        #Servizi
                        if line.invoice_id.fiscal_document_type_id.code == 'TD01' or line.invoice_id.fiscal_document_type_id.code == 'TD09' or (tag == 'VJ3' and  line.invoice_id.fiscal_document_type_id.code == 'TD11'):
                            debit_servizi += line.debit
                            credit_servizi += line.credit
                        #Beni
                        if line.invoice_id.fiscal_document_type_id.code == 'TD10':
                            debit_beni += line.debit
                            credit_beni += line.credit



                imponibile_beni += (debit_beni - credit_beni)
                imponibile_servizi += (debit_servizi - credit_servizi)

                debit_beni = 0
                credit_beni = 0
                debit_servizi = 0
                credit_servizi = 0
                for line in account_move_line_imposta:
                    if tag == 'VJ16':
                        # Gestione ITA
                        debit_servizi += line.debit
                        credit_servizi += line.credit
                    else:
                        # Gestione INTA/EXTRA
                        # Servizi
                        if line.invoice_id.fiscal_document_type_id.code == 'TD01' or line.invoice_id.fiscal_document_type_id.code == 'TD09' or (tag == 'VJ3' and  line.invoice_id.fiscal_document_type_id.code == 'TD11'):
                            debit_servizi += line.debit
                            credit_servizi += line.credit
                        # Beni
                        if line.invoice_id.fiscal_document_type_id.code == 'TD10':
                            debit_beni += line.debit
                            credit_beni += line.credit

                imposte_beni += (debit_beni - credit_beni)
                imposte_servizi += (debit_servizi - credit_servizi)


            return {
                'imponibile_beni': imponibile_beni,
                'imposte_beni': imposte_beni,
                'imponibile_servizi': imponibile_servizi,
                'imposte_servizi': imposte_servizi
            }


        def get_imponibile_imposta_from_tag(tag):
            """
            Restituisce la somma imponibile e imposta delle aliquote
            con il tag passato
            """
            if tag == 'VF19':
                print("OK")
            imponibile = 0
            imposta = 0
            #Verifica TAG righe di Debito
            for tax in lipe_annuale.debit_vat_account_line_ids:
                tax_ids = [tax.tax_id]
                is_gruppo = False
                if tax.tax_id.amount_type == 'group':
                    is_gruppo = True
                    #Imposta di gruppo
                    for child_tax in tax.tax_id.children_tax_ids:
                        tax_ids.append(child_tax)

                for tax in tax_ids:
                    for quadro in tax.dichiarazione_annuale_quadro:
                        if quadro.name == tag:
                            tax_datas = tax._compute_totals_tax({
                                'from_date': lipe_annuale.date_range_ids[0].date_start,
                                'to_date': lipe_annuale.date_range_ids[0].date_end,
                                'registry_type': 'customer'
                            })
                            imponibile += tax_datas[1]
                            imposta += tax_datas[2]

                            # Se la tassa è un gruppo prendo l'imposta dal figlio e l'imponibile dal padre
                            if is_gruppo:
                                tax_datas = tax_ids[0]._compute_totals_tax({
                                    'from_date': lipe_annuale.date_range_ids[0].date_start,
                                    'to_date': lipe_annuale.date_range_ids[0].date_end,
                                    'registry_type': 'customer'
                                })
                                imponibile += tax_datas[1]

            #Verifica TAG righe di Credito
            for tax in lipe_annuale.credit_vat_account_line_ids:
                tax_ids = [tax.tax_id]
                is_gruppo = False
                if tax.tax_id.amount_type == 'group':
                    # Imposta di gruppo
                    is_gruppo = True
                    for child_tax in tax.tax_id.children_tax_ids:
                        tax_ids.append(child_tax)

                for tax in tax_ids:
                    for quadro in tax.dichiarazione_annuale_quadro:
                        if quadro.name == tag:
                            tax_datas = tax._compute_totals_tax({
                                'from_date': lipe_annuale.date_range_ids[0].date_start,
                                'to_date': lipe_annuale.date_range_ids[0].date_end,
                                'registry_type': 'supplier'
                            })
                            imponibile += tax_datas[1]
                            imposta += tax_datas[2]

                            #Se la tassa è un gruppo prendo l'imposta dal figlio e l'imponibile dal padre
                            if is_gruppo:
                                tax_datas = tax_ids[0]._compute_totals_tax({
                                    'from_date': lipe_annuale.date_range_ids[0].date_start,
                                    'to_date': lipe_annuale.date_range_ids[0].date_end,
                                    'registry_type': 'supplier'
                                })
                                imponibile_imposta_principale = tax_datas[1]
                                imposta_totale = 0
                                for children in tax_ids[0].children_tax_ids:
                                    imposta_totale += children.amount

                                peso_imposta = tax.amount / imposta_totale
                                imponibile += imponibile_imposta_principale * peso_imposta


            return {'imponibile': round(imponibile, 2), 'imposta': round(imposta,2) }


        def get_sum_imponibile_imposta_from_tags(tags):
            """
            Restituisce la somma imponibile e la somma imposta
            di tutte le aliquote che hanno i tag passati
            """
            imponibile = 0
            imposta = 0
            for tag in tags:
                datas = get_imponibile_imposta_from_tag(tag)
                imponibile += datas['imponibile']
                imposta += datas['imposta']
            return {'imponibile': round(imponibile, 2) , 'imposta': round(imposta, 2) }


        #TOTALI
        VE24_IMPONIBILE = get_sum_imponibile_imposta_from_tags(['VE1','VE2','VE3','VE4','VE5','VE6','VE7','VE8','VE9','VE10','VE11','VE12','VE20','VE21','VE22','VE23'])['imponibile']
        VE24_IMPOSTA = get_sum_imponibile_imposta_from_tags(['VE1', 'VE2', 'VE3', 'VE4', 'VE5', 'VE6', 'VE7', 'VE8', 'VE9', 'VE10', 'VE11', 'VE12', 'VE20', 'VE21','VE22', 'VE23'])['imposta']
        VE30_VE38_IMPONIBILE = get_sum_imponibile_imposta_from_tags(['VE30','VE31','VE32','VE33','VE34','VE35','VE36','VE37','VE38'])['imponibile']
        VE39_IMPONIBILE = get_imponibile_imposta_from_tag('VE39')['imponibile']


        data_dict_pag3 = {
            'CODICE FISCALE3': self.taxpayer_vat,
        }

        data_dict_pag4 = {
            'CODICE FISCALE4': self.taxpayer_vat,
        }

        VE40_IMPONIBILE = 0
        # BLOCCO VE40
        account_move_line = self.env['account.move.line'].search(['&', '&', ('account_id.asset_type', '=', 'beni_ammortizzabili'),
                                                                  ('date', '>=',lipe_annuale.date_range_ids[0].date_start),
                                                                  ('date', '<=', lipe_annuale.date_range_ids[0].date_end)])
        VE40_CREDIT = 0
        VE40_DEBIT = 0
        for line in account_move_line:
            calcola = False
            for tax in line.tax_ids:
                if tax.type_tax_use == 'sale':
                    calcola = True
            if calcola:
                VE40_DEBIT += line.debit
                VE40_CREDIT += line.credit

        VE40_IMPONIBILE = VE40_CREDIT - VE40_DEBIT
        VE50_IMPONIBILE = VE24_IMPONIBILE + VE30_VE38_IMPONIBILE - VE39_IMPONIBILE - VE40_IMPONIBILE




        data_dict_pag5 = {
            'CODICE FISCALE5': self.taxpayer_vat,
            'VE20': str(get_imponibile_imposta_from_tag('VE20')['imponibile']).replace('.', ','),
            'VE20_IMP': str(get_imponibile_imposta_from_tag('VE20')['imposta']).replace('.', ','),
            'VE21': str(get_imponibile_imposta_from_tag('VE21')['imponibile']).replace('.', ','),
            'VE21_IMP': str(get_imponibile_imposta_from_tag('VE21')['imposta']).replace('.', ','),
            'VE22': str(get_imponibile_imposta_from_tag('VE22')['imponibile']).replace('.', ','),
            'VE22_IMP': str(get_imponibile_imposta_from_tag('VE22')['imposta']).replace('.', ','),
            'VE23': str(get_imponibile_imposta_from_tag('VE23')['imponibile']).replace('.', ','),
            'VE23_IMP': str(get_imponibile_imposta_from_tag('VE23')['imposta']).replace('.', ','),
            'VE24': str(VE24_IMPONIBILE).replace('.', ','),
            'VE24_IMP': str(VE24_IMPOSTA).replace('.', ','),
            'VE26': str(VE24_IMPOSTA).replace('.', ','),
            'VE30/1': str(get_imponibile_imposta_from_tag('VE30/1')['imponibile']).replace('.', ','),
            'VE30/2': str(get_imponibile_imposta_from_tag('VE30/2')['imponibile']).replace('.', ','),
            'VE30/3': str(get_imponibile_imposta_from_tag('VE30/3')['imponibile']).replace('.', ','),
            'VE30/4': str(get_imponibile_imposta_from_tag('VE30/4')['imponibile']).replace('.', ','),
            'VE30/5': str(get_imponibile_imposta_from_tag('VE30/5')['imponibile']).replace('.', ','),
            'VE31': str(get_imponibile_imposta_from_tag('VE31')['imponibile']).replace('.', ','),
            'VE32': str(get_imponibile_imposta_from_tag('VE32')['imponibile']).replace('.', ','),
            'VE33': str(get_imponibile_imposta_from_tag('VE33')['imponibile']).replace('.', ','),
            'VE34': str(get_imponibile_imposta_from_tag('VE34')['imponibile']).replace('.', ','),
            'VE40': str(VE40_IMPONIBILE).replace('.', ','),
            'VE50': str(VE50_IMPONIBILE).replace('.', ','),
        }

        # TOTALI
        VE23_IMPONIBILE = get_sum_imponibile_imposta_from_tags(['VF1', 'VF2', 'VF3', 'VF4', 'VF5', 'VF6', 'VF7', 'VF8', 'VF9', 'VF10', 'VF11', 'VF12', 'VF13', 'VF17', 'VF18/1', 'VF18/2','VF19/1', 'VF20', 'VF21', 'VF22', 'VF23/1', 'VF22'])['imponibile']
        VE23_IMPOSTA = get_sum_imponibile_imposta_from_tags( ['VF1', 'VF2', 'VF3', 'VF4', 'VF5', 'VF6', 'VF7', 'VF8', 'VF9', 'VF10', 'VF11', 'VF12', 'VF13'])['imposta']
        VF25_IMPOSTA = VE23_IMPOSTA

        #BLOCCO VF27
        account_move_line = self.env['account.move.line'].search(['&', '&', '&', '&', ('move_id.ref', 'not ilike', 'BILANCIO'), ('move_id.ref', '!=', 'FATTURE DA RICEVERE'), ('account_id.asset_type', '!=', False),
                                                                  ('date', '>=', lipe_annuale.date_range_ids[0].date_start),
                                                                  ('date', '<=', lipe_annuale.date_range_ids[0].date_end)])
        VF27_1_CREDIT = 0
        VF27_1_DEBIT = 0
        VF27_2_CREDIT = 0
        VF27_2_DEBIT = 0
        VF27_3_CREDIT = 0
        VF27_3_DEBIT = 0
        for line in account_move_line:
            if line.account_id.asset_type == 'beni_ammortizzabili':
                VF27_1_CREDIT += line.credit
                VF27_1_DEBIT += line.debit
            if line.account_id.asset_type == 'beni_strumentali':
                VF27_2_CREDIT += line.credit
                VF27_2_DEBIT += line.debit
            if line.account_id.asset_type == 'beni_rivendita_produzione':
                VF27_3_CREDIT += line.credit
                VF27_3_DEBIT += line.debit


        VF27_1_IMPONIBILE = VF27_1_DEBIT - VF27_1_CREDIT
        VF27_2_IMPONIBILE = VF27_2_DEBIT - VF27_2_CREDIT
        VF27_3_IMPONIBILE = VF27_3_DEBIT - VF27_3_CREDIT



        data_dict_pag6 = {
            'CODICE FISCALE6': self.taxpayer_vat,
            'VF1': str(get_imponibile_imposta_from_tag('VF1')['imponibile']).replace('.', ','),
            'VF1_IMP': str(get_imponibile_imposta_from_tag('VF1')['imposta']).replace('.', ','),
            'VF2': str(get_imponibile_imposta_from_tag('VF2')['imponibile']).replace('.', ','),
            'VF2_IMP': str(get_imponibile_imposta_from_tag('VF2')['imposta']).replace('.', ','),
            'VF3': str(get_imponibile_imposta_from_tag('VF3')['imponibile']).replace('.', ','),
            'VF3_IMP': str(get_imponibile_imposta_from_tag('VF3')['imposta']).replace('.', ','),
            'VF4': str(get_imponibile_imposta_from_tag('VF4')['imponibile']).replace('.', ','),
            'VF4_IMP': str(get_imponibile_imposta_from_tag('VF4')['imposta']).replace('.', ','),
            'VF5': str(get_imponibile_imposta_from_tag('VF5')['imponibile']).replace('.', ','),
            'VF5_IMP': str(get_imponibile_imposta_from_tag('VF5')['imposta']).replace('.', ','),
            'VF6': str(get_imponibile_imposta_from_tag('VF6')['imponibile']).replace('.', ','),
            'VF6_IMP': str(get_imponibile_imposta_from_tag('VF6')['imposta']).replace('.', ','),
            'VF7': str(get_imponibile_imposta_from_tag('VF7')['imponibile']).replace('.', ','),
            'VF7_IMP': str(get_imponibile_imposta_from_tag('VF7')['imposta']).replace('.', ','),
            'VF8': str(get_imponibile_imposta_from_tag('VF8')['imponibile']).replace('.', ','),
            'VF8_IMP': str(get_imponibile_imposta_from_tag('VF8')['imposta']).replace('.', ','),
            'VF9': str(get_imponibile_imposta_from_tag('VF9')['imponibile']).replace('.', ','),
            'VF9_IMP': str(get_imponibile_imposta_from_tag('VF9')['imposta']).replace('.', ','),
            'VF10': str(get_imponibile_imposta_from_tag('VF10')['imponibile']).replace('.', ','),
            'VF10_IMP': str(get_imponibile_imposta_from_tag('VF10')['imposta']).replace('.', ','),
            'VF11': str(get_imponibile_imposta_from_tag('VF11')['imponibile']).replace('.', ','),
            'VF11_IMP': str(get_imponibile_imposta_from_tag('VF11')['imposta']).replace('.', ','),
            'VF12': str(get_imponibile_imposta_from_tag('VF12')['imponibile']).replace('.', ','),
            'VF12_IMP': str(get_imponibile_imposta_from_tag('VF12')['imposta']).replace('.', ','),
            'VF13': str(get_imponibile_imposta_from_tag('VF13')['imponibile']).replace('.', ','),
            'VF13_IMP': str(get_imponibile_imposta_from_tag('VF13')['imposta']).replace('.', ','),
            # 'VF14': str(get_imponibile_imposta_from_tag('VF14')['imponibile']).replace('.', ','),
            # 'VF14_IMP': str(get_imponibile_imposta_from_tag('VF14')['imposta']).replace('.', ','),
            'VF17': str(get_imponibile_imposta_from_tag('VF17')['imponibile']).replace('.', ','),
            'VF18/1': str(get_imponibile_imposta_from_tag('VF18/1')['imponibile']).replace('.', ','),
            'VF18/2': str(get_imponibile_imposta_from_tag('VF18/2')['imponibile']).replace('.', ','),
            'VF19/1': str(get_imponibile_imposta_from_tag('VF19/1')['imponibile']).replace('.', ','),
            'VF19/2': str(get_imponibile_imposta_from_tag('VF19/2')['imponibile']).replace('.', ','),
            'VF20': str(get_imponibile_imposta_from_tag('VF20')['imponibile']).replace('.', ','),
            'VF21': str(get_imponibile_imposta_from_tag('VF21')['imponibile']).replace('.', ','),
            'VF22': str(get_imponibile_imposta_from_tag('VF22')['imponibile']).replace('.', ','),
            'VF23/1': str(get_imponibile_imposta_from_tag('VF23/1')['imponibile']).replace('.', ','),
            'VF23/2': str(get_imponibile_imposta_from_tag('VF23/2')['imponibile']).replace('.', ','),
            'VF24': str(get_imponibile_imposta_from_tag('VF24')['imponibile']).replace('.', ','),
            'VF25': str(VE23_IMPONIBILE).replace('.', ','),
            'VF25_IMP': str(VE23_IMPOSTA).replace('.', ','),
            'VF27': str(VF25_IMPOSTA).replace('.', ','),
            'VF28/1': str(get_imponibile_imposta_from_tag('VF28/1')['imponibile']).replace('.', ','),
            'VF28/2': str(get_imponibile_imposta_from_tag('VF28/1')['imposta']).replace('.', ','),
            'VF28/3': str(get_imponibile_imposta_from_tag('VF28/3')['imponibile']).replace('.', ','),
            'VF28/4': str(get_imponibile_imposta_from_tag('VF28/3')['imposta']).replace('.', ','),
            'VF28/5': str(get_imponibile_imposta_from_tag('VF28/5')['imponibile']).replace('.', ','),
            'VF28/6': str(get_imponibile_imposta_from_tag('VF28/5')['imposta']).replace('.', ','),
            'VF29/1': str(VF27_1_IMPONIBILE).replace('.', ','),
            'VF29/2': str(VF27_2_IMPONIBILE).replace('.', ','),
            'VF29/3': str(VF27_3_IMPONIBILE).replace('.', ','),
            'VF29/4': str(VE23_IMPONIBILE - VF27_1_IMPONIBILE - VF27_2_IMPONIBILE - VF27_3_IMPONIBILE).replace('.', ','),
        }


        data_dict_pag7 = {
            'CODICE FISCALE7': self.taxpayer_vat,
            'VF71': str(VF25_IMPOSTA).replace('.', ','),
        }

        # SOLAMENTE ALIQUOTA VJ3 COLLEGATA A FATTURE DI TIPO BENI
        VJ3 = get_imponibile_imposta_with_type('VJ3')
        VJ3_IMPONIBILE = VJ3['imponibile_servizi']
        VJ3_IMPOSTA = VJ3['imposte_servizi']

        #SOLAMENTE ALIQUOTA VJ9 COLLEGATA A FATTURE DI TIPO BENI
        VJ9 = get_imponibile_imposta_with_type('VJ9')
        VJ9_IMPONIBILE = VJ9['imponibile_beni']
        VJ9_IMPOSTA = VJ9['imposte_beni']

        #SOLAMENTE ALIQUOTA VJ9 COLLEGATA A FATTURE DI TIPO SERVIZI
        VJ16 = get_imponibile_imposta_with_type('VJ16')
        VJ16_IMPONIBILE = VJ16['imponibile_servizi']
        VJ16_IMPOSTA = VJ16['imposte_servizi']

        # TOTALI
        # VE19_IMPOSTA = get_sum_imponibile_imposta_from_tags(
        #     ['VJ1', 'VJ2', 'VJ4', 'VJ5', 'VJ6', 'VJ7', 'VJ8', 'VJ9', 'VJ10', 'VJ11', 'VJ12', 'VJ13', 'VJ14',
        #      'VJ15', 'VJ16', 'VJ17', 'VJ18'])['imposta']
        VJ19_IMPOSTA = get_sum_imponibile_imposta_from_tags(
            ['VJ1', 'VJ2', 'VJ4', 'VJ5', 'VJ6', 'VJ7', 'VJ8', 'VJ10', 'VJ11', 'VJ12', 'VJ13', 'VJ14', 'VJ15',
             'VJ17', 'VJ18'])['imposta']
        VJ19_IMPOSTA += VJ3_IMPOSTA + VJ9_IMPOSTA + VJ16_IMPOSTA

        data_dict_pag8 = {
            'CODICE FISCALE8': self.taxpayer_vat,
            'VJ1': str(get_imponibile_imposta_from_tag('VJ1')['imponibile']).replace('.', ','),
            'VJ1_IMP': str(get_imponibile_imposta_from_tag('VJ1')['imposta']).replace('.', ','),
            'VJ2': str(get_imponibile_imposta_from_tag('VJ2')['imponibile']).replace('.', ','),
            'VJ2_IMP': str(get_imponibile_imposta_from_tag('VJ2')['imposta']).replace('.', ','),
            'VJ3': str(VJ3_IMPONIBILE).replace('.', ','),
            'VJ3_IMP': str(VJ3_IMPOSTA).replace('.', ','),
            'VJ4': str(get_imponibile_imposta_from_tag('VJ4')['imponibile']).replace('.', ','),
            'VJ4_IMP': str(get_imponibile_imposta_from_tag('VJ4')['imposta']).replace('.', ','),
            'VJ5': str(get_imponibile_imposta_from_tag('VJ5')['imponibile']).replace('.', ','),
            'VJ5_IMP': str(get_imponibile_imposta_from_tag('VJ5')['imposta']).replace('.', ','),
            'VJ6': str(get_imponibile_imposta_from_tag('VJ6')['imponibile']).replace('.', ','),
            'VJ6_IMP': str(get_imponibile_imposta_from_tag('VJ6')['imposta']).replace('.', ','),
            'VJ7': str(get_imponibile_imposta_from_tag('VJ7')['imponibile']).replace('.', ','),
            'VJ7_IMP': str(get_imponibile_imposta_from_tag('VJ7')['imposta']).replace('.', ','),
            'VJ8': str(get_imponibile_imposta_from_tag('VJ8')['imponibile']).replace('.', ','),
            'VJ8_IMP': str(get_imponibile_imposta_from_tag('VJ8')['imposta']).replace('.', ','),
            'VJ9': str(VJ9_IMPONIBILE).replace('.', ','),
            'VJ9_IMP': str(VJ9_IMPOSTA).replace('.', ','),
            'VJ10': str(get_imponibile_imposta_from_tag('VJ10')['imponibile']).replace('.', ','),
            'VJ10_IMP': str(get_imponibile_imposta_from_tag('VJ10')['imposta']).replace('.', ','),
            'VJ11': str(get_imponibile_imposta_from_tag('VJ11')['imponibile']).replace('.', ','),
            'VJ11_IMP': str(get_imponibile_imposta_from_tag('VJ11')['imposta']).replace('.', ','),
            'VJ12': str(get_imponibile_imposta_from_tag('VJ12')['imponibile']).replace('.', ','),
            'VJ12_IMP': str(get_imponibile_imposta_from_tag('VJ12')['imposta']).replace('.', ','),
            'VJ13': str(get_imponibile_imposta_from_tag('VJ13')['imponibile']).replace('.', ','),
            'VJ13_IMP': str(get_imponibile_imposta_from_tag('VJ13')['imposta']).replace('.', ','),
            'VJ14': str(get_imponibile_imposta_from_tag('VJ14')['imponibile']).replace('.', ','),
            'VJ14_IMP': str(get_imponibile_imposta_from_tag('VJ14')['imposta']).replace('.', ','),
            'VJ15': str(get_imponibile_imposta_from_tag('VJ15')['imponibile']).replace('.', ','),
            'VJ15_IMP': str(get_imponibile_imposta_from_tag('VJ15')['imposta']).replace('.', ','),
            'VJ16': str(VJ16_IMPONIBILE).replace('.', ','),
            'VJ16_IMP': str(VJ16_IMPOSTA).replace('.', ','),
            'VJ17': str(get_imponibile_imposta_from_tag('VJ17')['imponibile']).replace('.', ','),
            'VJ17_IMP': str(get_imponibile_imposta_from_tag('VJ17')['imposta']).replace('.', ','),
            'VJ18': str(get_imponibile_imposta_from_tag('VJ18')['imponibile']).replace('.', ','),
            'VJ18_IMP': str(get_imponibile_imposta_from_tag('VJ18')['imposta']).replace('.', ','),
            'VJ19': str(VJ19_IMPOSTA).replace('.', ','),
        }

        from_date = str(self.year) + '-01-01'
        to_date = str(self.year) + '-12-31'
        liquidazioni_anno = self.env['account.vat.period.end.statement'].sudo().search([('date', '>=', from_date), ('date', '<=', to_date), ('state', '!=', 'draft')])

        data_dict_pag9 = {
            'CODICE FISCALE9': self.taxpayer_vat,
            'VH1C':0,
            'VH1D': 0,
            'VH2C': 0,
            'VH2D': 0,
            'VH3C': 0,
            'VH3D': 0,
            'VH4C': 0,
            'VH4D': 0,
            'VH5C': 0,
            'VH5D': 0,
            'VH6C': 0,
            'VH6D': 0,
            'VH7C':0,
            'VH7D': 0,
            'VH8C': 0,
            'VH8D': 0,
            'VH9C': 0,
            'VH9D': 0,
            'VH10C': 0,
            'VH10D': 0,
            'VH11C': 0,
            'VH11D': 0,
            'VH12C': 0,
            'VH12D': 0,
            'VH13C': 0,
            'VH13D': 0,
            'VH14C': 0,
            'VH14D': 0,
            'VH15C': 0,
            'VH15D': 0,
            'VH16C': 0,
            'VH16D': 0,
            'VH17': 0,
            'VH17_M': 1,
        }

        VL8 = 0

        for liquidazione in liquidazioni_anno:
            #debit = self.env['report.l10n_it_account.vat_statement'].sudo()._get_account_vat_amounts('debit', liquidazione.debit_vat_account_line_ids)
            #credit = self.env['report.l10n_it_account.vat_statement'].sudo()._get_account_vat_amounts('credit',liquidazione.credit_vat_account_line_ids)
            #debit_amount = 0
            #credit_amount = 0
            #for account in debit:
             #   debit_amount = debit[account]['amount']
            #for account in credit:
             #   credit_amount = credit[account]['amount']

            if liquidazione.date.month == 1:
                #Gennaio
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH1C'] = abs(somma)
                else:
                    data_dict_pag9['VH1D'] = abs(somma)

                #VL8, VERIFICA SE CI SONO CREDITI ANNO PRECEDENTE
                VL8 = liquidazione.previous_credit_vat_amount

            if liquidazione.date.month == 2:
                #Febbraio
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH2C'] = abs(somma)
                else:
                    data_dict_pag9['VH2D'] = abs(somma)
            if liquidazione.date.month == 3:
                #Marzo
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH3C'] = abs(somma)
                else:
                    data_dict_pag9['VH3D'] = abs(somma)
            if liquidazione.date.month == 4:
                #Aprile
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH5C'] = abs(somma)
                else:
                    data_dict_pag9['VH5D'] = abs(somma)
            if liquidazione.date.month == 5:
                #Maggio
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH6C'] = abs(somma)
                else:
                    data_dict_pag9['VH6D'] = abs(somma)
            if liquidazione.date.month == 6:
                #Giugno
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH7C'] = abs(somma)
                else:
                    data_dict_pag9['VH7D'] = abs(somma)
            if liquidazione.date.month == 7:
                #Luglio
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH9C'] = abs(somma)
                else:
                    data_dict_pag9['VH9D'] = abs(somma)
            if liquidazione.date.month == 8:
                #Agosto
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH10C'] = abs(somma)
                else:
                    data_dict_pag9['VH10D'] = abs(somma)
            if liquidazione.date.month == 9:
                #Settembre
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH11C'] = abs(somma)
                else:
                    data_dict_pag9['VH11D'] = abs(somma)
            if liquidazione.date.month == 10:
                #Ottobre
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH13C'] = abs(somma)
                else:
                    data_dict_pag9['VH13D'] = abs(somma)
            if liquidazione.date.month == 11:
                #Novembre
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH14C'] = abs(somma)
                else:
                    data_dict_pag9['VH14D'] = abs(somma)
            if liquidazione.date.month == 12:
                #Dicembre
                somma = liquidazione.authority_vat_amount
                if somma < 0:
                    data_dict_pag9['VH15C'] = abs(somma)
                else:
                    data_dict_pag9['VH15D'] = abs(somma)

                #VERIFICA ACCONTI PER TAG VH17
                for line in liquidazione.generic_vat_account_line_ids:
                    data_dict_pag9['VH17'] = str(abs(line.amount)).replace(".",  ",")

        #Trimestri, questo blocco solo per i trimestrali
        #aggiugere un flag in LIPE IVA
        #data_dict_pag9['VH4C'] = data_dict_pag9['VH1C'] + data_dict_pag9['VH2C'] + data_dict_pag9['VH3C']
        #data_dict_pag9['VH4D'] = data_dict_pag9['VH1D'] + data_dict_pag9['VH2D'] + data_dict_pag9['VH3D']
        #data_dict_pag9['VH8C'] = data_dict_pag9['VH5C'] + data_dict_pag9['VH6C'] + data_dict_pag9['VH7C']
        #data_dict_pag9['VH8D'] = data_dict_pag9['VH5D'] + data_dict_pag9['VH6D'] + data_dict_pag9['VH7D']
        #data_dict_pag9['VH12C'] = data_dict_pag9['VH9C'] + data_dict_pag9['VH10C'] + data_dict_pag9['VH11C']
        #data_dict_pag9['VH12D'] = data_dict_pag9['VH9D'] + data_dict_pag9['VH10D'] + data_dict_pag9['VH11D']
        #data_dict_pag9['VH16C'] = data_dict_pag9['VH13C'] + data_dict_pag9['VH14C'] + data_dict_pag9['VH15C']
        #data_dict_pag9['VH16D'] = data_dict_pag9['VH13D'] + data_dict_pag9['VH14D'] + data_dict_pag9['VH15D']


        VL3 = (VJ19_IMPOSTA + VE24_IMPOSTA) - VF25_IMPOSTA
        VL4 = abs(VF25_IMPOSTA - (VJ19_IMPOSTA + VE24_IMPOSTA))
        if VL3 > 0:
            VL4 = 0

        data_dict_pag10 = {
            'CODICE FISCALE10': self.taxpayer_vat,
        }

        data_dict_pag11 = {
            'CODICE FISCALE11': self.taxpayer_vat,
            'VL1': str(VJ19_IMPOSTA + VE24_IMPOSTA).replace('.', ','),
            'VL2': str(VF25_IMPOSTA).replace('.', ','),
            'VL3': str(VL3).replace('.', ','),
            'VL4': str(VL4).replace('.', ','),
            'VL8': str(VL8).replace('.', ','),
            'VL30/2': str(VL3).replace('.', ','),
        }

        quadro_vp_id = self.quadri_vp_ids[0]

        data_dict_pag12 = {
            # 'CODICE FISCALE12': self.taxpayer_vat,
            # 'CODICE_FISCALE_LIPE': self.taxpayer_fiscalcode,
            # 'MODULO_N': 1,
            # 'MESE_LIPE': str(quadro_vp_id.month).zfill(2) if quadro_vp_id.period_type == 'month' else '',
            # 'TRIMESTRE': str(quadro_vp_id.quarter).zfill(2) if quadro_vp_id.period_type == 'quarter' else '',
            # 'SUBFORNITURE': quadro_vp_id.subcontracting,
            # 'EVENTI_ECCEZIONALI': quadro_vp_id.exceptional_events,
            # 'OPERAZIONI_STRAORDINARIE': '',
            # 'ACCONTO_DOVUTO': str(quadro_vp_id.metodo_acconto_dovuto),
            # 'VP2': str(quadro_vp_id.imponibile_operazioni_attive).replace('.', ' '),
            # 'VP3': str(quadro_vp_id.imponibile_operazioni_passive).replace('.', ' '),
            # 'VP4': str(quadro_vp_id.iva_esigibile).replace('.', ' '),
            # 'VP5': str(quadro_vp_id.iva_detratta).replace('.', ' '),
            # 'VP6/1': str(quadro_vp_id.iva_dovuta_debito).replace('.', ' '),
            # 'VP6/2': str(quadro_vp_id.iva_dovuta_credito).replace('.', ' '),
            # 'VP7': str(quadro_vp_id.debito_periodo_precedente).replace('.', ' '),
            # 'VP8': str(quadro_vp_id.credito_periodo_precedente).replace('.', ' '),
            # 'VP9': str(quadro_vp_id.credito_anno_precedente).replace('.', ' '),
            # 'VP10': str(quadro_vp_id.versamento_auto_UE).replace('.', ' '),
            # 'VP11': str(quadro_vp_id.crediti_imposta).replace('.', ' '),
            # 'VP12': str(quadro_vp_id.interessi_dovuti).replace('.', ' '),
            # 'VP13': str(quadro_vp_id.accounto_dovuto).replace('.', ' '),
            # 'VP14/1': str(quadro_vp_id.iva_da_versare).replace('.', ' '),
            # 'VP14/2': str(quadro_vp_id.iva_a_credito).replace('.', ' '),
        }

        VT1_1 = 0
        VT1_2 = 0
        VT1_3 = 0
        VT1_4 = 0
        VT1_5 = 0
        VT1_6 = 0



        for tax in lipe_annuale.debit_vat_account_line_ids:
            if tax.tax_id.iva_corr or tax.tax_id.iva_fatt:
                #somma imponibile vendite e imposta vendite
                tax_datas = tax.tax_id._compute_totals_tax({
                    'from_date': lipe_annuale.date_range_ids[0].date_start,
                    'to_date': lipe_annuale.date_range_ids[0].date_end,
                    'registry_type': 'customer'
                })
                VT1_1 += tax_datas[1]
                VT1_2 += tax_datas[2]

        for tax in lipe_annuale.debit_vat_account_line_ids:
            if tax.tax_id.iva_corr:
                #Imposta vs. soggetti privati
                tax_datas = tax.tax_id._compute_totals_tax({
                    'from_date': lipe_annuale.date_range_ids[0].date_start,
                    'to_date': lipe_annuale.date_range_ids[0].date_end,
                    'registry_type': 'customer'
                })
                VT1_3 += tax_datas[1]
                VT1_4 += tax_datas[2]
            if tax.tax_id.iva_fatt:
                #Imposta vs. soggetti privati
                tax_datas = tax.tax_id._compute_totals_tax({
                    'from_date': lipe_annuale.date_range_ids[0].date_start,
                    'to_date': lipe_annuale.date_range_ids[0].date_end,
                    'registry_type': 'customer'
                })
                VT1_5 += tax_datas[1]
                VT1_6 += tax_datas[2]

            #Calcolo l'iva di Fatture che hanno però intestatario privato.
            #Rimuovo tale importo dale VT1_5 e VT1_6 e lo sommo al 3 e 4.
            # Righe Imponibile
            if tax.tax_id.iva_fatt:
                account_move_line_imponibile = self.env['account.move.line'].search(
                    ['&', '&', ('tax_ids', '=', tax.tax_id.id), ('date', '>=', lipe_annuale.date_range_ids[0].date_start),
                     ('date', '<=', lipe_annuale.date_range_ids[0].date_end)])
                # Righe Imposta
                account_move_line_imposta = self.env['account.move.line'].search(
                    ['&', '&', ('tax_line_id', '=', tax.tax_id.id), ('date', '>=', lipe_annuale.date_range_ids[0].date_start),
                     ('date', '<=', lipe_annuale.date_range_ids[0].date_end)])

                tot_imponibile_privati_debiti = 0
                tot_imponibile_privati_crediti = 0
                tot_imposta_privati_debiti = 0
                tot_imposta_privati_crediti = 0
                for line in account_move_line_imposta:
                    if not line.invoice_id.partner_id.vat:
                        print("TROVATO")
                        #Se la fattura e' ad un privato
                        tot_imposta_privati_debiti += line.debit
                        tot_imposta_privati_crediti += line.credit

                for line in account_move_line_imponibile:
                    if not line.invoice_id.partner_id.vat:
                        print("TROVATO2")
                        #Se la fattura e' ad un privato
                        tot_imponibile_privati_debiti += line.debit
                        tot_imponibile_privati_crediti += line.credit

                #Rimuovo dai soggetti IVA
                VT1_5 -= round(tot_imponibile_privati_crediti - tot_imponibile_privati_debiti, 2)
                VT1_6 -= round(tot_imposta_privati_crediti - tot_imposta_privati_debiti, 2)
                #Sposto sotto soggetti Privati
                VT1_3 += round(tot_imponibile_privati_crediti - tot_imponibile_privati_debiti, 2)
                VT1_4 += round(tot_imposta_privati_crediti - tot_imposta_privati_debiti, 2)


        region_private_operation = {
            'Abruzzo': {'imponibile': 0, 'imposta': 0},
            'Basilicata': {'imponibile': 0, 'imposta': 0},
            'Trento': {'imponibile': 0, 'imposta': 0},
            'Bolzano': {'imponibile': 0, 'imposta': 0},
            'Calabria': {'imponibile': 0, 'imposta': 0},
            'Campania': {'imponibile': 0, 'imposta': 0},
            'Emilia Romagna': {'imponibile': 0, 'imposta': 0},
            'Friuli Venezia Giulia': {'imponibile': 0, 'imposta': 0},
            'Lazio': {'imponibile': 0, 'imposta': 0},
            'Liguria': {'imponibile': 0, 'imposta': 0},
            'Lombardia': {'imponibile': 0, 'imposta': 0},
            'Marche': {'imponibile': 0, 'imposta': 0},
            'Molise': {'imponibile': 0, 'imposta': 0},
            'Piemonte': {'imponibile': 0, 'imposta': 0},
            'Puglia': {'imponibile': 0, 'imposta': 0},
            'Sardegna': {'imponibile': 0, 'imposta': 0},
            'Sicilia': {'imponibile': 0, 'imposta': 0},
            'Toscana': {'imponibile': 0, 'imposta': 0},
            'Umbria': {'imponibile': 0, 'imposta': 0},
            "Valle d'Aosta": {'imponibile': 0, 'imposta': 0},
            'Veneto': {'imponibile': 0, 'imposta': 0},
        }



        for tax in lipe_annuale.debit_vat_account_line_ids:
            if tax.tax_id.iva_corr or tax.tax_id.iva_fatt:
                # Imposta vs. soggetti privati
                # 1.Operazioni Imponibili
                account_move_line = self.env['account.move.line'].sudo().search(['&','&',('date', '>=', lipe_annuale.date_range_ids[0].date_start),
                                                                                 ('date', '<=', lipe_annuale.date_range_ids[0].date_end),
                                                                                 ('tax_ids', '=', tax.tax_id.id )])
                for line in account_move_line:
                    imponibile = line.debit - line.credit
                    #Verifica che si tratti o di corrispettivo o di fattura  a privato
                    if tax.tax_id.iva_corr or not line.invoice_id.partner_id.vat:

                        if not line.partner_id or not line.invoice_id.session_id.config_id.analytic_account_id.region_id:
                            #Se il cliente non e' impostato oppure non e' presente la regione imposta in quella di Default
                            region_private_operation['Lombardia']['imponibile'] += imponibile
                        elif line.invoice_id.session_id.config_id.analytic_account_id.region_id:
                            region_private_operation[line.invoice_id.session_id.config_id.analytic_account_id.region_id.name]['imponibile'] += imponibile
                        else:
                            # Se il cliente non e' impostato oppure non e' presente la regione imposta in quella di Default
                            region_private_operation['Lombardia']['imponibile'] += imponibile





                # # 1.Operazioni Imposta
                account_move_line = self.env['account.move.line'].sudo().search(['&', '&', ('date', '>=', lipe_annuale.date_range_ids[0].date_start),
                                                                                 ('date', '<=', lipe_annuale.date_range_ids[0].date_end),
                                                                                 ('tax_line_id', '=', tax.tax_id.id)])
                for line in account_move_line:
                    imposta = line.debit - line.credit
                    # Verifica che si tratti o di corrispettivo o di fattura  a privato
                    if tax.tax_id.iva_corr or not line.invoice_id.partner_id.vat:
                        if not line.partner_id or not line.invoice_id.session_id.config_id.analytic_account_id.region_id:
                            #Se il cliente non e' impostato oppure non e' presente la regione imposta in quella di Default
                            region_private_operation['Lombardia']['imposta'] += imposta

                        elif line.invoice_id.session_id.config_id.analytic_account_id.region_id:
                            region_private_operation[line.invoice_id.session_id.config_id.analytic_account_id.region_id.name]['imposta'] += imposta
                        else:
                            # Se il cliente non e' impostato oppure non e' presente la regione imposta in quella di Default
                            region_private_operation['Lombardia']['imposta'] += imposta


        data_dict_pag13 = {
            'CODICE FISCALE13': self.taxpayer_vat,
            'VT1/2':  round(VT1_2,2),
            'VT1/1':  round(VT1_1,2),
            'VT1/5':  round(VT1_5,2),
            'VT1/6':  round(VT1_6,2),
            'VT1/3':  round(VT1_3,2),
            'VT1/4':  round(VT1_4,2),
            'VT2/1': round(abs(region_private_operation['Abruzzo']['imponibile']), 2),
            'VT2/2': round(abs(region_private_operation['Abruzzo']['imposta']), 2),
            'VT3/1': round(abs(region_private_operation['Basilicata']['imponibile']), 2),
            'VT3/2': round(abs(region_private_operation['Basilicata']['imposta']), 2),
            'VT4/1': round(abs(region_private_operation['Bolzano']['imponibile']), 2),
            'VT4/2': round(abs(region_private_operation['Bolzano']['imposta']), 2),
            'VT5/1': round(abs(region_private_operation['Calabria']['imponibile']), 2),
            'VT5/2': round(abs(region_private_operation['Calabria']['imposta']), 2),
            'VT6/1': round(abs(region_private_operation['Campania']['imponibile']), 2),
            'VT6/2': round(abs(region_private_operation['Campania']['imposta']), 2),
            'VT7/1': round(abs(region_private_operation['Emilia Romagna']['imponibile']), 2),
            'VT7/2': round(abs(region_private_operation['Emilia Romagna']['imposta']), 2),
            'VT8/1': round(abs(region_private_operation['Friuli Venezia Giulia']['imponibile']), 2),
            'VT8/2': round(abs(region_private_operation['Friuli Venezia Giulia']['imposta']), 2),
            'VT9/1': round(abs(region_private_operation['Lazio']['imponibile']), 2),
            'VT9/2': round(abs(region_private_operation['Lazio']['imposta']), 2),
            'VT10/1': round(abs(region_private_operation['Liguria']['imponibile']), 2),
            'VT10/2': round(abs(region_private_operation['Liguria']['imposta']), 2),
            'VT11/1': round(abs(region_private_operation['Lombardia']['imponibile']), 2),
            'VT11/2': round(abs(region_private_operation['Lombardia']['imposta']), 2),
            'VT12/1': round(abs(region_private_operation['Marche']['imponibile']), 2),
            'VT12/2': round(abs(region_private_operation['Marche']['imposta']), 2),
            'VT13/1': round(abs(region_private_operation['Molise']['imponibile']), 2),
            'VT13/2': round(abs(region_private_operation['Molise']['imposta']), 2),
            'VT14/1': round(abs(region_private_operation['Piemonte']['imponibile']), 2),
            'VT14/2': round(abs(region_private_operation['Piemonte']['imposta']), 2),
            'VT15/1': round(abs(region_private_operation['Puglia']['imponibile']), 2),
            'VT15/2': round(abs(region_private_operation['Puglia']['imposta']), 2),
            'VT16/1': round(abs(region_private_operation['Sardegna']['imponibile']), 2),
            'VT16/2': round(abs(region_private_operation['Sardegna']['imposta']), 2),
            'VT17/1': round(abs(region_private_operation['Sicilia']['imponibile']), 2),
            'VT17/2': round(abs(region_private_operation['Sicilia']['imposta']), 2),
            'VT18/1': round(abs(region_private_operation['Toscana']['imponibile']), 2),
            'VT18/2': round(abs(region_private_operation['Toscana']['imposta']), 2),
            'VT19/1': round(abs(region_private_operation['Trento']['imponibile']), 2),
            'VT19/2': round(abs(region_private_operation['Trento']['imposta']), 2),
            'VT20/1': round(abs(region_private_operation['Umbria']['imponibile']), 2),
            'VT20/2': round(abs(region_private_operation['Umbria']['imposta']), 2),
            'VT21/1': round(abs(region_private_operation["Valle d'Aosta"]['imponibile']), 2),
            'VT21/2': round(abs(region_private_operation["Valle d'Aosta"]['imposta']), 2),
            'VT22/1': round(abs(region_private_operation['Veneto']['imponibile']), 2),
            'VT22/2': round(abs(region_private_operation['Veneto']['imposta']), 2)
        }


        data_dict_pag14 = {
            'CODICE FISCALE14': self.taxpayer_vat,
            'VX1': str(VL3).replace('.', ','),
            'VX2/1': str(VL4).replace('.', ','),
            'VX2/2': str('').replace('.', ','),
            'VX3': str('').replace('.', ','),
        }

        data_dict_pag15 = {
            'CODICE FISCALE15': self.taxpayer_vat,
        }
        data_dict_pag16 = {
            'CODICE FISCALE16': self.taxpayer_vat,
        }
        data_dict_pag17 = {
            'CODICE FISCALE17': self.taxpayer_vat,
        }
        data_dict_pag18 = {
            'CODICE FISCALE18': self.taxpayer_vat,
        }
        data_dict_pag19 = {
            'CODICE FISCALE19': self.taxpayer_vat,
        }
        data_dict_pag20 = {
            'CODICE FISCALE20': self.taxpayer_vat,
        }
        data_dict_pag21 = {
            'CODICE FISCALE21': self.taxpayer_vat,
        }
        data_dict_pag22 = {
            'CODICE FISCALE22': self.taxpayer_vat,
        }






        pdf_writer.addPage(pdf_reader.getPage(0))
        pdf_writer.addPage(pdf_reader.getPage(1))
        pdf_writer.addPage(pdf_reader.getPage(2))
        pdf_writer.addPage(pdf_reader.getPage(3))
        pdf_writer.addPage(pdf_reader.getPage(4))
        pdf_writer.addPage(pdf_reader.getPage(5))
        pdf_writer.addPage(pdf_reader.getPage(6))
        pdf_writer.addPage(pdf_reader.getPage(7))
        pdf_writer.addPage(pdf_reader.getPage(8))
        pdf_writer.addPage(pdf_reader.getPage(9))
        pdf_writer.addPage(pdf_reader.getPage(10))
        pdf_writer.addPage(pdf_reader.getPage(11))
        pdf_writer.addPage(pdf_reader.getPage(12))
        pdf_writer.addPage(pdf_reader.getPage(13))
        pdf_writer.addPage(pdf_reader.getPage(14))
        pdf_writer.addPage(pdf_reader.getPage(15))
        pdf_writer.addPage(pdf_reader.getPage(16))
        pdf_writer.addPage(pdf_reader.getPage(17))
        pdf_writer.addPage(pdf_reader.getPage(18))
        pdf_writer.addPage(pdf_reader.getPage(19))
        pdf_writer.addPage(pdf_reader.getPage(20))
        pdf_writer.addPage(pdf_reader.getPage(21))
        page = pdf_writer.getPage(1)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag1)
        page = pdf_writer.getPage(2)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag2)
        page = pdf_writer.getPage(3)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag3)
        page = pdf_writer.getPage(4)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag4)
        page = pdf_writer.getPage(5)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag5)
        page = pdf_writer.getPage(6)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag6)
        page = pdf_writer.getPage(7)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag7)
        page = pdf_writer.getPage(8)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag8)
        page = pdf_writer.getPage(9)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag9)
        page = pdf_writer.getPage(10)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag10)
        page = pdf_writer.getPage(11)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag11)
        page = pdf_writer.getPage(12)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag12)
        page = pdf_writer.getPage(13)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag13)
        page = pdf_writer.getPage(14)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag14)
        page = pdf_writer.getPage(15)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag15)
        page = pdf_writer.getPage(16)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag16)
        page = pdf_writer.getPage(17)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag17)
        page = pdf_writer.getPage(18)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag18)
        page = pdf_writer.getPage(19)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag19)
        page = pdf_writer.getPage(20)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag20)
        page = pdf_writer.getPage(21)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag21)


        output_stream = BytesIO()
        pdf_writer.write(output_stream)
        return output_stream.getvalue()

    def get_export_iva_periodico_pdf(self):
        data_dict_pag1 = {
            'CODICE FISCALE1': self.taxpayer_vat,
            'partita_iva_2': self.taxpayer_vat,
            'anno_imposta': str(self.year),
            'Codice': str(self.codice_carica_id.code),
            'impegno_prestazione': str(self.delegate_commitment),
            'denominazione_ragione_sociale': self.company_id.name,
            'codice_fiscale_sottoscrittore': self.declarant_fiscalcode,
            'codice_carica': self.codice_carica_id.code,
            'natura_giuridica': self.natura_giuridica,
            'firma1': 'X',
            'cognome': self.declarant_lastname,
            'nome': self.declarant_firstname,
            'data_nascita_day': self.declarant_date.day if self.declarant_date else False,
            'data_nascita_month': self.declarant_date.month if self.declarant_date else False,
            'data_nascita_year': self.declarant_date.year if self.declarant_date else False,
            'comune_nascita': self.declarant_city,
            'codice_fiscale_incaricato': self.delegate_fiscalcode,
            'firma2': 'X',
            'data_impegno': f'{str(self.date_commitment).split("-")[2]}{str(self.date_commitment).split("-")[1]}{str(self.date_commitment).split("-")[0]}',
        }
        # Reader
        pdf_module_path = get_module_resource('l10n_it_account_lipe', 'data', 'moduli_pdf', 'header_IVA_periodica_2023.pdf')
        input_stream = open(pdf_module_path, "rb")
        pdf_reader = PyPDF2.PdfFileReader(input_stream, strict=False)
        # Writer
        pdf_writer = PyPDF2.PdfFileWriter()
        self.set_need_appearances_writer(pdf_writer)
        if "/AcroForm" in pdf_writer._root_object:
            # Acro form is form field, set needs appearances to fix printing issues
            pdf_writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})
        # Add pages
        pdf_writer.addPage(pdf_reader.getPage(0))
        pdf_writer.addPage(pdf_reader.getPage(1))
        # Write pages
        page = pdf_writer.getPage(1)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag1)

        output_stream = BytesIO()
        pdf_writer.write(output_stream)
        return output_stream.getvalue()

    def get_export_iva_periodico_pdf(self):


        data_dict_pag1 = {
            'CODICE FISCALE1': self.taxpayer_vat,
            'anno_imposta': str(self.year),
            'partita_iva_2': self.taxpayer_vat,
            'denominazione_ragione_sociale': self.company_id.name,
            'codice_fiscale_sottoscrittore': self.declarant_fiscalcode,
            'Codice': str(self.codice_carica_id.code),
            'natura_giuridica': self.natura_giuridica,
            'firma1': 'X',
            'cognome': self.declarant_lastname,
            'nome': self.declarant_firstname,
            'data_nascita_day': self.declarant_date.day if self.declarant_date else False,
            'data_nascita_month': self.declarant_date.month if self.declarant_date else False,
            'data_nascita_year': self.declarant_date.year if self.declarant_date else False,
            'comune_nascita': self.declarant_city,
            'codice_fiscale_incaricato': self.delegate_fiscalcode,
            'impegno_prestazione': str(self.delegate_commitment),
            'firma2': 'X',
            'data_impegno': f'{str(self.date_commitment).split("-")[2]}{str(self.date_commitment).split("-")[1]}{str(self.date_commitment).split("-")[0]}',
        }

        # Reader
        pdf_module_path = get_module_resource('l10n_it_account_lipe', 'data', 'moduli_pdf', 'header_IVA_periodica_2023.pdf')
        input_stream = open(pdf_module_path, "rb")
        pdf_reader = PyPDF2.PdfFileReader(input_stream, strict=False)
        # Writer
        pdf_writer = PyPDF2.PdfFileWriter()
        self.set_need_appearances_writer(pdf_writer)
        if "/AcroForm" in pdf_writer._root_object:
            # Acro form is form field, set needs appearances to fix printing issues
            pdf_writer._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})
        # Add pages
        pdf_writer.addPage(pdf_reader.getPage(0))
        pdf_writer.addPage(pdf_reader.getPage(1))
        # Write pages
        page = pdf_writer.getPage(1)
        pdf_writer.updatePageFormFieldValues(page, data_dict_pag1)

        # Reader
        pdf_module_path = get_module_resource('l10n_it_account_lipe', 'data', 'moduli_pdf', 'body_IVA_periodica_2023.pdf')
        input_stream = open(pdf_module_path, "rb")
        pdf_reader = PyPDF2.PdfFileReader(input_stream, strict=False)
        page_n = 2
        i = 1
        for quadro_vp_id in self.quadri_vp_ids:
            data_dict_pag12 = {
                f'CODICE FISCALE12_{i}': self.taxpayer_vat,
                f'CODICE_FISCALE_LIPE_{i}': self.taxpayer_fiscalcode,
                f'MODULO_N_{i}': 1,
                f'MESE_LIPE_{i}': str(quadro_vp_id.month).zfill(2) if quadro_vp_id.period_type == 'month' else '',
                f'TRIMESTRE_{i}': str(quadro_vp_id.quarter).zfill(2) if quadro_vp_id.period_type == 'quarter' else '',
                f'SUBFORNITURE_{i}': quadro_vp_id.subcontracting,
                f'EVENTI_ECCEZIONALI_{i}': quadro_vp_id.exceptional_events,
                f'OPERAZIONI_STRAORDINARIE_{i}': '',
                # 'ACCONTO_DOVUTO': str(quadro_vp_id.metodo_acconto_dovuto),
                f'VP2_{i}':
                    "{:.2f}".format(quadro_vp_id.imponibile_operazioni_attive).replace('.', '*').replace(',',
                                                                                                         '.').replace(
                        '*', ',').split(',')[0].replace(',', ''),
                f'VP2_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.imponibile_operazioni_attive).replace('.', '*').replace(',',
                                                                                                         '.').replace(
                        '*', ',').split(',')[1].replace(',', ''),
                f'VP3_{i}':
                    "{:.2f}".format(quadro_vp_id.imponibile_operazioni_passive).replace('.', '*').replace(',',
                                                                                                          '.').replace(
                        '*', ',').split(',')[0].replace(',', ''),
                f'VP3_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.imponibile_operazioni_passive).replace('.', '*').replace(',',
                                                                                                          '.').replace(
                        '*', ',').split(',')[1].replace(',', ''),
                f'VP4_{i}':
                    "{:.2f}".format(quadro_vp_id.iva_esigibile).replace('.', '*').replace(',', '.').replace('*',
                                                                                                            ',').split(
                        ',')[0].replace(',', ''),
                f'VP4_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.iva_esigibile).replace('.', '*').replace(',', '.').replace('*',
                                                                                                            ',').split(
                        ',')[1].replace(',', ''),
                f'VP5_{i}':
                    "{:.2f}".format(quadro_vp_id.iva_detratta).replace('.', '*').replace(',', '.').replace('*',
                                                                                                           ',').split(
                        ',')[0].replace(',', ''),
                f'VP5_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.iva_detratta).replace('.', '*').replace(',', '.').replace('*',
                                                                                                           ',').split(
                        ',')[1].replace(',', ''),
                f'VP6/1_{i}':
                    "{:.2f}".format(quadro_vp_id.iva_dovuta_debito).replace('.', '*').replace(',', '.').replace('*',
                                                                                                                ',').split(
                        ',')[0].replace(',', ''),
                f'VP6/1_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.iva_dovuta_debito).replace('.', '*').replace(',', '.').replace('*',
                                                                                                                ',').split(
                        ',')[1].replace(',', ''),
                f'VP6/2_{i}':
                    "{:.2f}".format(quadro_vp_id.iva_dovuta_credito).replace('.', '*').replace(',', '.').replace('*',
                                                                                                                 ',').split(
                        ',')[0].replace(',', ''),
                f'VP6/2_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.iva_dovuta_credito).replace('.', '*').replace(',', '.').replace('*',
                                                                                                                 ',').split(
                        ',')[1].replace(',', ''),
                f'VP7_{i}':
                    "{:.2f}".format(quadro_vp_id.debito_periodo_precedente).replace('.', '*').replace(',', '.').replace(
                        '*',
                        ',').split(
                        ',')[0].replace(',', ''),
                f'VP7_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.debito_periodo_precedente).replace('.', '*').replace(',', '.').replace(
                        '*',
                        ',').split(
                        ',')[1].replace(',', ''),
                f'VP8_{i}': "{:.2f}".format(quadro_vp_id.credito_periodo_precedente).replace('.', '*').replace(',',
                                                                                                          '.').replace(
                    '*', ',').split(',')[0].replace(',', ''),
                f'VP8_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.credito_periodo_precedente).replace('.', '*').replace(',',
                                                                                                       '.').replace(
                        '*', ',').split(',')[1].replace(',', ''),
                f'VP9_{i}':
                    "{:.2f}".format(quadro_vp_id.credito_anno_precedente).replace('.', '*').replace(',', '.').replace(
                        '*',
                        ',').split(
                        ',')[0].replace(',', ''),
                f'VP9_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.credito_anno_precedente).replace('.', '*').replace(',', '.').replace(
                        '*',
                        ',').split(
                        ',')[1].replace(',', ''),
                f'VP10_{i}':
                    "{:.2f}".format(quadro_vp_id.versamento_auto_UE).replace('.', '*').replace(',', '.').replace('*',
                                                                                                                 ',').split(
                        ',')[0].replace(',', ''),
                f'VP10_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.versamento_auto_UE).replace('.', '*').replace(',', '.').replace('*',
                                                                                                                 ',').split(
                        ',')[1].replace(',', ''),
                f'VP11_{i}': "{:.2f}".format(quadro_vp_id.crediti_imposta).replace('.', '*').replace(',', '.').replace('*',
                                                                                                                  ',').split(
                    ',')[0].replace(',', ''),
                f'VP11_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.crediti_imposta).replace('.', '*').replace(',', '.').replace('*',
                                                                                                              ',').split(
                        ',')[1].replace(',', ''),
                f'VP12_{i}': "{:.2f}".format(quadro_vp_id.interessi_dovuti).replace('.', '*').replace(',', '.').replace('*',
                                                                                                                   ',').split(
                    ',')[0].replace(',', ''),
                f'VP12_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.interessi_dovuti).replace('.', '*').replace(',', '.').replace('*',
                                                                                                               ',').split(
                        ',')[1].replace(',', ''),
                f'VP13_{i}': "{:.2f}".format(quadro_vp_id.accounto_dovuto).replace('.', '*').replace(',', '.').replace('*',
                                                                                                                  ',').split(
                    ',')[0].replace(',', ''),
                f'VP13_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.accounto_dovuto).replace('.', '*').replace(',', '.').replace('*',
                                                                                                              ',').split(
                        ',')[1].replace(',', ''),
                f'VP14/1_{i}': "{:.2f}".format(quadro_vp_id.iva_da_versare).replace('.', '*').replace(',', '.').replace('*',
                                                                                                                   ',').split(
                    ',')[0].replace(',', ''),
                f'VP14/1_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.iva_da_versare).replace('.', '*').replace(',', '.').replace('*',
                                                                                                             ',').split(
                        ',')[1].replace(',', ''),
                f'VP14/2_{i}':
                    "{:.2f}".format(quadro_vp_id.iva_a_credito).replace('.', '*').replace(',', '.').replace('*',
                                                                                                            ',').split(
                        ',')[0].replace(',', ''),
                f'VP14/2_dec_{i}':
                    "{:.2f}".format(quadro_vp_id.iva_a_credito).replace('.', '*').replace(',', '.').replace('*',
                                                                                                            ',').split(
                        ',')[1].replace(',', ''),
            }
            # Add pages
            pdf_writer.addPage(pdf_reader.getPage(i-1))
            # Write pages
            page = pdf_writer.getPage(page_n)
            pdf_writer.updatePageFormFieldValues(page, data_dict_pag12)
            page_n += 1
            i += 1

        output_stream = BytesIO()
        pdf_writer.write(output_stream)
        return output_stream.getvalue()

