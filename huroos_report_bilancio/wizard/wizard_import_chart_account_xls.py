# -*- coding: utf-8 -*-
# Powered by Karanveer Singh.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

import logging
from base64 import b64decode

import xlrd

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class WizardImportChartAccountXls(models.TransientModel):
    _name = 'wizard.import.chart.account.xls'

    name = fields.Char(default="Importa Piano dei Conti")
    file_xls_chart_import = fields.Binary()
    filename_file_xls_chart_import = fields.Char()

    def load_chart_from_xls(self):
        """
        La funzione importa il piano dei conti tramite il seguente tracciato excel:
        codice conto, nome conto, area, tipologia, macroaggregato, aggregato

        Un conto DEVE avere un nome e una tipologia, altrimenti non può essere creato.
        """
        if self.file_xls_chart_import:
            if not (self.filename_file_xls_chart_import.endswith('.xlsx') or self.filename_file_xls_chart_import.endswith('.xls')):
                raise UserError("Formato errato. Inserire un file XLS o XLSX.")
            wb = xlrd.open_workbook(file_contents=b64decode(self.file_xls_chart_import))
            sheet = wb.sheet_by_index(0)
            sheet.cell_value(0, 0)
            macroaggregato = 'macroaggragate'
            aggregato = 'aggregate'
            third_level = 'sottoconto_terzo_livello'
            fourth_level = 'sottoconto_quarto_livello'
            fifth_level = 'sottoconto_quinto_livello'
            sixthlevel = 'sottoconto_sesto_livello'
            credito = self.env.ref('account.data_account_type_receivable').id
            debito = self.env.ref('account.data_account_type_payable').id
            banca_cassa = self.env.ref('account.data_account_type_liquidity').id
            carta_di_credito = self.env.ref('account.data_account_type_credit_card').id
            attivita_correnti = self.env.ref('account.data_account_type_current_assets').id
            attivita_non_correnti = self.env.ref('account.data_account_type_non_current_assets').id
            risconti_attivi = self.env.ref('account.data_account_type_prepayments').id
            immobilizzazioni = self.env.ref('account.data_account_type_fixed_assets').id
            passivita_correnti = self.env.ref('account.data_account_type_current_liabilities').id
            passivita_non_correnti = self.env.ref('account.data_account_type_non_current_liabilities').id
            patrimonio_netto = self.env.ref('account.data_account_type_equity').id
            utili_di_esercizio = self.env.ref('account.data_unaffected_earnings').id
            ricavi = self.env.ref('account.data_account_type_revenue').id
            altri_ricavi = self.env.ref('account.data_account_type_other_income').id
            costi = self.env.ref('account.data_account_type_expenses').id
            ammortamenti = self.env.ref('account.data_account_type_depreciation').id
            costo_del_venduto = self.env.ref('account.data_account_type_direct_costs').id
            fuori_bilancio = self.env.ref('account.data_account_off_sheet').id
            conti_ordine = self.env.ref('huroos_report_bilancio.account_type_ordine').id

            record_non_importati = []
            for row in range(1, sheet.nrows):
                account = {}
                conto_effettivo = False
                for column in range(0, sheet.ncols):
                    cell = sheet.cell(row, column)
                    if column == 0:
                        # Prima Colonna, contiene il codice conto
                        if isinstance(cell.value, str):
                            account['code'] = cell.value
                        elif isinstance(cell.value, float) or isinstance(cell.value, int):
                            account['code'] = str(int(cell.value))

                    if 'code' in account:
                        if column == 1:
                            # Seconda Colonna, contiene il nome del conto
                            if isinstance(cell.value, str):
                                account['name'] = cell.value
                            elif isinstance(cell.value, float) or isinstance(cell.value, int):
                                account['name'] = str(int(cell.value))
                        if column == 2:
                            # Terza Colonna, area di ambito: Conto Economico, Stato Patrimoniale
                            if cell.value and cell.value.lower() == 'conto economico':
                                account['area'] = 'conto_economico'
                                account['user_type_id'] = ricavi
                                account['reconcile'] = False
                            if cell.value and cell.value.lower() == 'stato patrimoniale':
                                account['area'] = 'stato_patrimoniale'
                                account['reconcile'] = True
                                account['user_type_id'] = attivita_correnti
                            if cell.value and cell.value.lower() == "conti ordine":
                                account['area'] = 'conti_ordine'
                                account['user_type_id'] = conti_ordine
                                account['reconcile'] = False
                        if column == 3:
                            # Tipo di Conto
                            if 'area' in account and cell.value:
                                if cell.value:
                                    if cell.value.lower() == 'attività correnti':
                                        account['user_type_id'] = attivita_correnti
                                    if cell.value.lower() == 'passività correnti':
                                        account['user_type_id'] = passivita_correnti
                                    if cell.value.lower() == 'credito':
                                        account['user_type_id'] = credito
                                    if cell.value.lower() == 'debito':
                                        account['user_type_id'] = debito
                                    if cell.value.lower() == 'costi':
                                        account['user_type_id'] = costi
                                    if cell.value.lower() == 'ricavi':
                                        account['user_type_id'] = ricavi
                                    if cell.value.lower() == "conti ordine":
                                        account['user_type_id'] = conti_ordine
                                    if cell.value.lower() == "banca e cassa":
                                        account['user_type_id'] = banca_cassa
                                    if cell.value.lower() == "carta di credito":
                                        account['user_type_id'] = carta_di_credito
                                    if cell.value.lower() == "attività non correnti":
                                        account['user_type_id'] = attivita_non_correnti
                                    if cell.value.lower() == "risconti attivi":
                                        account['user_type_id'] = risconti_attivi
                                    if cell.value.lower() == "immobilizzazioni":
                                        account['user_type_id'] = immobilizzazioni
                                    if cell.value.lower() == "passività non correnti":
                                        account['user_type_id'] = passivita_non_correnti
                                    if cell.value.lower() == "patrimonio netto":
                                        account['user_type_id'] = patrimonio_netto
                                    if cell.value.lower() == "utili di esercizio":
                                        account['user_type_id'] = utili_di_esercizio
                                    if cell.value.lower() == "altri ricavi":
                                        account['user_type_id'] = altri_ricavi
                                    if cell.value.lower() == "ammortamenti":
                                        account['user_type_id'] = ammortamenti
                                    if cell.value.lower() == "costo del venduto":
                                        account['user_type_id'] = costo_del_venduto
                                    if cell.value.lower() == "fuori bilancio":
                                        account['user_type_id'] = fuori_bilancio

                        if column == 4:
                            # Legame al macroaggregato
                            if cell.value:
                                if isinstance(cell.value, float):
                                    cell.value = int(cell.value)
                                macroaggregato_obj = self.env['account.account'].search([
                                    ('hierarchy_type', '=', macroaggregato),('code', '=', str(cell.value))],limit=1)
                                if macroaggregato_obj:
                                    account['macroaggregate_id'] = macroaggregato_obj.id
                        if column == 5:
                            # Legame all'aggregato
                            if cell.value:
                                if isinstance(cell.value, float):
                                    cell.value = int(cell.value)
                                aggregato_obj = self.env['account.account'].search([
                                    ('hierarchy_type', '=', aggregato),('code', '=', str(cell.value))],limit=1)
                                if aggregato_obj:
                                    account['aggregate_id'] = aggregato_obj.id
                        if column == 6:
                            # Legame al terzo livello
                            if cell.value:
                                if isinstance(cell.value, float):
                                    cell.value = int(cell.value)
                                third_level_obj = self.env['account.account'].search([
                                    ('hierarchy_type', '=', third_level),('code', '=', str(cell.value))],limit=1)
                                if third_level_obj:
                                    account['sottoconto_terzo_livello'] = third_level_obj.id
                        if column == 7:
                            # Legame al quarto livello
                            if cell.value:
                                if isinstance(cell.value, float):
                                    cell.value = int(cell.value)
                                fourth_level_obj = self.env['account.account'].search([
                                    ('hierarchy_type', '=', fourth_level),('code', '=', str(cell.value))],limit=1)
                                if fourth_level_obj:
                                    account['sottoconto_quarto_livello'] = fourth_level_obj.id
                        if column == 8:
                            # Legame al quinto livello
                            if cell.value:
                                if isinstance(cell.value, float):
                                    cell.value = int(cell.value)
                                fifth_level_obj = self.env['account.account'].search([
                                    ('hierarchy_type', '=', fifth_level),('code', '=', str(cell.value))],limit=1)
                                if fifth_level_obj:
                                    account['sottoconto_quinto_livello'] = fifth_level_obj.id
                        if column == 9:
                            # Legame al sesto livello
                            if cell.value:
                                if isinstance(cell.value, float):
                                    cell.value = int(cell.value)
                                sixth_level_obj = self.env['account.account'].search([
                                    ('hierarchy_type', '=', sixthlevel),('code', '=', str(cell.value))],limit=1)
                                if sixth_level_obj:
                                    account['sottoconto_sesto_livello'] = sixth_level_obj.id
                        if column == 10:
                            if cell.value and cell.value > 0:
                                conto_effettivo = True
                if account != {}:
                    if 'macroaggregate_id' not in account.keys() and 'aggregate_id' not in account.keys():
                        # il conto è un macroaggregato
                        account['hierarchy_type'] = macroaggregato
                    if 'macroaggregate_id' in account.keys() and 'aggregate_id' not in account.keys():
                        # il conto è un aggregato
                        account['hierarchy_type'] = aggregato
                    if 'macroaggregate_id' in account.keys() and 'aggregate_id' in account.keys() and not conto_effettivo:
                        # terzo livello
                        if not 'sottoconto_terzo_livello' in account.keys():
                            account['hierarchy_type'] = third_level
                        elif not 'sottoconto_quarto_livello' in account.keys():
                            account['hierarchy_type'] = fourth_level
                        elif not 'sottoconto_quinto_livello' in account.keys():
                            account['hierarchy_type'] = fifth_level
                        elif not 'sottoconto_sesto_livello' in account.keys():
                            account['hierarchy_type'] = sixthlevel
                    try:
                        if len(account['name']) > 0:
                            existing_account = self.env['account.account'].search([('code', '=', account['code'])])
                            if not existing_account:
                                self.env['account.account'].create(account)
                                logging.info("Creato: " + account['code'])
                            else:
                                existing_account.write(account)
                                logging.info("Aggiornato: " + account['code'])
                    except ValidationError as e:
                        logging.info("SCARTATO " + account['name'] + ": " + e.args[0])
                        record_non_importati.append(account['name'])
                        continue
                    except TypeError as e:
                        logging.info("SCARTATO " + account['name'] + ": " + e.args[0])
                        record_non_importati.append(account['name'])
                        continue
                    except Exception as e:
                        logging.info("SCARTATO " + account['name'] + ": " + e.args[0])
                        record_non_importati.append(account['name'])
                        continue
            self.flush()
            logging.info("-----------FINE IMPORT------------")
            logging.info("SCARTATI " + str(len(record_non_importati)) + " record nelle seguenti righe: " + str(
                record_non_importati))
        else:
            raise UserError("Inserire un file XLS o XLSX da cui importare i dati")

    def download_xls_piano_dei_conti(self):
        """
        Scarica un tracciato da compilare. Per inserire nuovi tracciati scaricabili inserirli in static/src/download
        """
        return {
            'type': 'ir.actions.act_url',
            'url': '/huroos_report_bilancio/static/src/download/tracciato_piano_dei_conti.xlsx',
            'target': 'new',
        }