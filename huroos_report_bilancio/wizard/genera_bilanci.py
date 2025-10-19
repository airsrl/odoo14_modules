# -*- coding: utf-8 -*-
# Powered by Karanveer Singh.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).


from odoo import fields, api, models,_

class GeneraStatoPatrimoniale(models.TransientModel):

    _name = "genera.stato.patrimoniale"

    nascondi_zeri = fields.Boolean(default=False)
    escludi_move_line = fields.Boolean()


    # def bilancio_corrente(self):
    #     chiusura_anno_ids = self.env['year.closing'].search([])
    #     for chiusura in chiusura_anno_ids:
    #         for operazioni in chiusura.move_year_ids:
    #             for line in operazioni.line_ids:
    #                 line.write({'escludi_report_bilancio': False})
    #                 print("ESCLUDI FALSE")
    #
    # def bilancio_anno_precente(self):
    #     chiusura_anno_ids = self.env['year.closing'].search([])
    #     for chiusura in chiusura_anno_ids:
    #         for operazioni in chiusura.move_year_ids:
    #             #ESCLUDI SOLO QUELLE DI CHIUSURA
    #             if operazioni.date.day == 31:
    #                 for line in operazioni.line_ids:
    #                     line.write({'escludi_report_bilancio': True})
    #                     print("ESCLUDI TRUE")
    #             else:
    #                 for line in operazioni.line_ids:
    #                     line.write({'escludi_report_bilancio': False})
    #                     print("ESCLUDI FALSE")


    def crea_gerarchia(self, area):
        """
        funzione che collega i conti agli aggregati
        :param area:
        :return:
        """
        aggregati = self.env['account.account'].search(
            [('deprecated', '=', False), ('hierarchy_type', '=', 'aggregate'), ('area', '=', area)])
        conti = self.env['account.account'].search([('deprecated', '=', False), ('hierarchy_type', '=', False)])
        for aggregato in aggregati:
            for conto in conti:
                if conto.code.startswith(aggregato.code):
                    conto.macroaggregate_id = aggregato.macroaggregate_id.id
                    conto.aggregate_id = aggregato.id
                    conto.area = area
        self.env.cr.commit()


    def genera_sp(self):
        """
        funzione che genera le righe per il report dello stato patrimoniale
        """
        self.crea_gerarchia('stato_patrimoniale')
        self.genera_bilancio('stato_patrimoniale', 'SP_', 'asset', 'liability',
                             'huroos_report_bilancio.sp_attivo', 'huroos_report_bilancio.sp_passivo', '+sum', '+sum')
        self.genera_bilancio('stato_patrimoniale', 'RB_SP_', 'asset', 'liability',
                             'huroos_report_bilancio.sp_attivo_bilancio', 'huroos_report_bilancio.sp_passivo_bilancio',
                             '+sum','+sum')
        # self.genera_bilancio('conti_ordine', 'CO_', 'account.data_account_type_current_assets', 'account.data_account_type_current_liabilities',
        #                      'huroos_report_bilancio.sp_conti_ordine', 'huroos_report_bilancio.sp_conti_ordine')

    def genera_ce(self):
        """
        funzione che genera le righe per il report del conto economico
        """
        self.crea_gerarchia('conto_economico')
        self.genera_bilancio('conto_economico', 'CE_', 'income', 'expense',
                             'huroos_report_bilancio.ce_attivo', 'huroos_report_bilancio.ce_passivo', '+sum', '+sum')
        self.genera_bilancio('conto_economico', 'RB_CE_', 'income', 'expense',
                             'huroos_report_bilancio.ce_attivo_bilancio', 'huroos_report_bilancio.ce_passivo_bilancio', '+sum', '+sum')

    def genera_bilancio(self, area, prefisso, tipo_attivita, tipo_passivita, attivo, passivo, sum_string_att, sum_string_pass):
        """
        funzione che genera le righe per i report di bilancio: stato patrimoniale e conto economico
        la loro struttura è sempre uguale (a 3 livelli) differisce solo per alcuni parametri.

        :param area: l'area di appartenenza dei macroaggregati del report (stato patrimoniale, conto_economico, ecc)
        :param prefisso: prefisso con cui nominare le le righe di report per utilizzare le formule
        :param tipo_attivita: tipologia macroaggregato attivo, cambia in base all'area. stato patrimoniale--->attivita', passivita'.
                                conto economico--->costi, ricavi
        :param tipo_passivita: tipologia macroaggregato passivo, cambia in base all'area. stato patrimoniale--->attivita', passivita'.
                                conto economico--->costi, ricavi
        :param attivo: riferimento del blocco del report che contiene i macroaggregati di tipo attivo
        :param passivo: riferimento del blocco del report che contiene i macroaggregati di tipo passivo
        :return:
        """

        macroaggregati = self.env['account.account'].search([('deprecated', '=', False), ('hierarchy_type', '=', 'macroaggragate'), ('area', '=', area)])
        aggregati = self.env['account.account'].search([('deprecated', '=', False), ('hierarchy_type', '=', 'aggregate'), ('area', '=', area)])
        aggregati_liv_3 = self.env['account.account'].search([('deprecated', '=', False), ('hierarchy_type', '=', 'sottoconto_terzo_livello'), ('area', '=', area)])
        aggregati_liv_4 = self.env['account.account'].search([('deprecated', '=', False), ('hierarchy_type', '=', 'sottoconto_quarto_livello'), ('area', '=', area)])
        aggregati_liv_5 = self.env['account.account'].search([('deprecated', '=', False), ('hierarchy_type', '=', 'sottoconto_quinto_livello'), ('area', '=', area)])
        aggregati_liv_6 = self.env['account.account'].search([('deprecated', '=', False), ('hierarchy_type', '=', 'sottoconto_sesto_livello'), ('area', '=', area)])
        attivo = self.env.ref(attivo)
        passivo = self.env.ref(passivo)
        macroaggregati_counter = 0
        if not self.escludi_move_line :
            domain_escludi_scritture = ""
        else:
            domain_escludi_scritture = ", ('escludi_report_bilancio', '=', False)"

        formula_attivo = ""
        formula_passivo = ""
        for macroaggregato in macroaggregati:
            macroaggregati_counter += 1
            aggregati_counter = 0

            # i codici riga dei report finanziari devono avere un codice univoco
            codice_riga_macroaggregato = prefisso + str(macroaggregati_counter).zfill(3) + "_" + str(aggregati_counter).zfill(3)
            if macroaggregato.code:
                nome_macro = macroaggregato.code + " - " + macroaggregato.name
            else:
                nome_macro = macroaggregato.name

            # serve per decidere se il macro è di tipo attività o passività
            attivo_passivo = attivo.id
            sum_string = sum_string_att
            if macroaggregato.user_type_id.internal_group == tipo_passivita:
                attivo_passivo = passivo.id
                sum_string = sum_string_pass
            if macroaggregato.user_type_id.internal_group == tipo_attivita:
                attivo_passivo = attivo.id

            # creazione macro
            data_macro = {
                'name': nome_macro,
                'code': codice_riga_macroaggregato,
                'parent_id': attivo_passivo,
                'sequence': macroaggregati_counter,
                'level': 1,
            }
            new_macroaggregato = self.env['account.financial.html.report.line'].create(data_macro)
            self.env.cr.commit()

            formula_macroaggregato = ""
            for aggregato in list(filter(lambda s: s.macroaggregate_id.id == macroaggregato.id, aggregati)):
                aggregati_counter += 1
                livello_3_counter = 0
                codice_riga_aggregato = prefisso + str(macroaggregati_counter).zfill(3) + "_" + str(aggregati_counter).zfill(3) + "_" + str(livello_3_counter).zfill(3)
                data_aggregato = {
                    'name': aggregato.code + " - " + aggregato.name,
                    'code': codice_riga_aggregato,
                    'parent_id': new_macroaggregato.id,
                    'domain': """[('account_id.macroaggregate_id', '=', %s),
                                ('account_id.aggregate_id', '=', %s),
                                ('account_id.sottoconto_terzo_livello', '=', False),
                                ('account_id.sottoconto_quarto_livello', '=', False),
                                ('account_id.sottoconto_quinto_livello', '=', False),
                                ('account_id.sottoconto_sesto_livello', '=', False),
                                ('account_id.hierarchy_type', '=', False) %s]""" % (macroaggregato.id, aggregato.id, domain_escludi_scritture),
                    'groupby': "account_id",
                    'sequence': aggregati_counter,
                    'level': 2,
                    'hide_if_zero': self.nascondi_zeri
                }
                new_aggregato = self.env['account.financial.html.report.line'].create(data_aggregato)
                self.env.cr.commit()
                formula_aggregato = ""
                for livello_3 in list(filter(lambda s: s.macroaggregate_id.id == macroaggregato.id and s.aggregate_id.id == aggregato.id, aggregati_liv_3)):
                    livello_3_counter += 1
                    livello_4_counter = 0
                    codice_riga_liv_3 = prefisso + str(macroaggregati_counter).zfill(3) + "_" + str(aggregati_counter).zfill(3) \
                                        + "_" + str(livello_3_counter).zfill(3) + "_" + str(livello_4_counter).zfill(3)

                    data_liv_3 = {
                        'name': livello_3.code + " - " + livello_3.name,
                        'code': codice_riga_liv_3,
                        'parent_id': new_aggregato.id,
                        'domain': """[('account_id.macroaggregate_id', '=', %s),
                                    ('account_id.aggregate_id', '=', %s),
                                    ('account_id.sottoconto_terzo_livello', '=', %s),
                                    ('account_id.sottoconto_quarto_livello', '=',False),
                                    ('account_id.sottoconto_quinto_livello', '=', False),
                                    ('account_id.sottoconto_sesto_livello', '=', False),
                                    ('account_id.hierarchy_type', '=', False) %s]""" % (
                        macroaggregato.id, aggregato.id, livello_3.id, domain_escludi_scritture),
                        'groupby': "account_id",
                        'sequence': livello_3_counter,
                        'level': 3
                    }
                    new_livello_3 = self.env['account.financial.html.report.line'].create(data_liv_3)
                    self.env.cr.commit()
                    formula_livello_3 = ""

                    for livello_4 in list(filter(lambda s: s.macroaggregate_id.id == macroaggregato.id and s.aggregate_id.id == aggregato.id
                            and s.sottoconto_terzo_livello.id == livello_3.id,aggregati_liv_4)):
                        livello_4_counter += 1
                        livello_5_counter = 0
                        codice_riga_liv_4 = prefisso + str(macroaggregati_counter).zfill(3) + "_" + str(aggregati_counter).zfill(3) \
                                            + "_" + str(livello_3_counter).zfill(3) + "_" + str(livello_4_counter).zfill(3)

                        data_liv_4 = {
                            'name': livello_4.code + " - " + livello_4.name,
                            'code': codice_riga_liv_4,
                            'parent_id': new_livello_3.id,
                            'domain': """[('account_id.macroaggregate_id', '=', %s), 
                                        ('account_id.aggregate_id', '=', %s),
                                        ('account_id.sottoconto_terzo_livello', '=', %s),
                                        ('account_id.sottoconto_quarto_livello', '=', %s),
                                        ('account_id.sottoconto_quinto_livello', '=', False),
                                        ('account_id.sottoconto_sesto_livello', '=', False),
                                        ('account_id.hierarchy_type', '=', False) %s]""" % (macroaggregato.id, aggregato.id, livello_3.id, livello_4.id, domain_escludi_scritture),
                            'groupby': "account_id",
                            'sequence': livello_4_counter,
                            'level': 4
                        }
                        new_livello_4 = self.env['account.financial.html.report.line'].create(data_liv_4)
                        self.env.cr.commit()

                        formula_livello_4 = ""
                        for livello_5 in list(filter(lambda s: s.macroaggregate_id.id == macroaggregato.id and s.aggregate_id.id == aggregato.id
                                                 and s.sottoconto_terzo_livello.id == livello_3.id
                                                 and s.sottoconto_quarto_livello.id == livello_4.id, aggregati_liv_5)):
                            livello_5_counter += 1
                            livello_6_counter = 0
                            codice_riga_liv_5 = prefisso + str(macroaggregati_counter).zfill(3) + "_" + str(aggregati_counter).zfill(3) \
                                                + "_" + str(livello_3_counter).zfill(3) + "_" + str(livello_4_counter).zfill(3) \
                                                + "_" + str(livello_5_counter).zfill(3)

                            data_liv_5 = {
                                'name': livello_5.code + " - " + livello_5.name,
                                'code': codice_riga_liv_5,
                                'parent_id': new_livello_4.id,
                                'domain': """[('account_id.macroaggregate_id', '=', %s), 
                                            ('account_id.aggregate_id', '=', %s),
                                            ('account_id.sottoconto_terzo_livello', '=', %s),
                                            ('account_id.sottoconto_quarto_livello', '=', %s),
                                            ('account_id.sottoconto_quinto_livello', '=', %s),
                                            ('account_id.sottoconto_sesto_livello', '=', False),
                                            ('account_id.hierarchy_type', '=', False) %s]""" % (
                                macroaggregato.id, aggregato.id, livello_3.id, livello_4.id, livello_5.id, domain_escludi_scritture),
                                'groupby': "account_id",
                                'sequence': livello_5_counter,
                                'level': 4
                            }
                            new_livello_5 =self.env['account.financial.html.report.line'].create(data_liv_5)
                            self.env.cr.commit()

                            formula_livello_5 = ""
                            for livello_6 in list(filter(lambda s: s.macroaggregate_id.id == macroaggregato.id and s.aggregate_id.id == aggregato.id
                                                        and s.sottoconto_terzo_livello.id == livello_3.id
                                                        and s.sottoconto_quarto_livello.id == livello_4.id
                                                        and s.sottoconto_quinto_livello.id == livello_5.id,aggregati_liv_6)):
                                livello_6_counter += 1
                                codice_riga_liv_6 = prefisso + str(macroaggregati_counter).zfill(3) + "_" + str(aggregati_counter).zfill(3) \
                                                    + "_" + str(livello_3_counter).zfill(3) + "_" + str(livello_4_counter).zfill(3) \
                                                    + "_" + str(livello_5_counter).zfill(3) + "_" + str(livello_6_counter).zfill(3)

                                data_liv_6 = {
                                    'name': livello_6.code + " - " + livello_6.name,
                                    'code': codice_riga_liv_6,
                                    'parent_id': new_livello_5.id,
                                    'domain': """[('account_id.macroaggregate_id', '=', %s), 
                                                ('account_id.aggregate_id', '=', %s),
                                                ('account_id.sottoconto_terzo_livello', '=', %s),
                                                ('account_id.sottoconto_quarto_livello', '=', %s),
                                                ('account_id.sottoconto_quinto_livello', '=', %s),
                                                ('account_id.sottoconto_sesto_livello', '=', %s),
                                                ('account_id.hierarchy_type', '=', False) %s]""" % (
                                        macroaggregato.id, aggregato.id, livello_3.id, livello_4.id, livello_5.id, livello_6.id, domain_escludi_scritture),
                                    'groupby': "account_id",
                                    'formulas': sum_string,
                                    'sequence': livello_6_counter,
                                    'level': 4
                                }
                                self.env['account.financial.html.report.line'].create(data_liv_6)
                                self.env.cr.commit()
                                formula_livello_5 += codice_riga_liv_6 + " + "
                            new_livello_5.write({'formulas': self.check_formula(formula_livello_5) + sum_string})
                            formula_livello_4 += codice_riga_liv_5 + " + "
                        new_livello_4.write({'formulas': self.check_formula(formula_livello_4) + sum_string})
                        formula_livello_3 += codice_riga_liv_4 + " + "
                    new_livello_3.write({'formulas': self.check_formula(formula_livello_3) + sum_string})
                    formula_aggregato += codice_riga_liv_3 + " + "
                new_aggregato.write({'formulas': self.check_formula(formula_aggregato) + sum_string})
                formula_macroaggregato += codice_riga_aggregato + " + "
            new_macroaggregato.write({'formulas': self.check_formula(formula_macroaggregato)})

            if attivo_passivo == attivo.id:
                formula_attivo += codice_riga_macroaggregato + " + "
            if attivo_passivo == passivo.id:
                formula_passivo += codice_riga_macroaggregato + " + "
        attivo.write({'formulas': self.check_formula(formula_attivo)})
        passivo.write({'formulas': self.check_formula(formula_passivo)})

    def check_formula(self, formula):

        formula = formula[:-3]
        if formula == '' or formula == ' ':
            formula = '0'
        return formula

    def cancella_righe_report(self):
        """
        Svuota le righe di stato patrimoniale e conto economico.
        utile nel caso cambi la struttura di macroaggregati e aggregati
        """
        self.env.cr.execute("DELETE FROM account_financial_html_report_line WHERE code LIKE 'SP\____\____' AND code != 'SP_TOT_ATT'")
        self.env.cr.execute("DELETE FROM account_financial_html_report_line WHERE code LIKE 'CE\____\____' AND code != 'CE_TOT_ATT'")
        self.env.cr.execute("DELETE FROM account_financial_html_report_line WHERE code LIKE 'CO\____\____'")
        self.env.cr.execute("DELETE FROM account_financial_html_report_line WHERE code LIKE 'RB_SP\____\____' AND code != 'SP_TOT_ATT_BILANCIO'")
        self.env.cr.execute("DELETE FROM account_financial_html_report_line WHERE code LIKE 'RB_CE\____\____' AND code != 'CE_TOT_ATT_BILANCIO'")
        self.env.cr.execute("UPDATE account_financial_html_report_line set formulas = null where code = 'CE_PASS' "
                            "or code = 'CE_AT' or code = 'SP_PASS' or code = 'SP_AT' or code = 'SP_CONTI_ORDINE' or code = 'CE_PASS_BILANCIO' "
                            "or code = 'CE_AT_BILANCIO' or code = 'SP_PASS_BILANCIO' or code = 'SP_AT_BILANCIO' or code = 'SP_CONTI_ORDINE_BILANCIO'")
        self.env.cr.commit()