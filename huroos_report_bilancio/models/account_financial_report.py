# -*- coding: utf-8 -*-
# Powered by Karanveer Singh.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

from odoo import models, fields, api, _
from odoo.tools import float_is_zero


class AccountFinancialReport(models.Model):
    _inherit = "account.financial.html.report"

    '''
    
    ATTIVARE QUESTO PEZZO DI CODICE PER ATTIVARE FILTRO DATA PER DATA FATTURA 
    (ATTIVARE ANCHE LA VISTA 'search_template_view.xml' NEL MANIFEST)
    
    filter_invoice_date = True

    @api.model
    def _get_options_date_domain(self, options):
        """Inherit per inserire possibilità di filtrare per data fattura e non solo data contabile."""

        date_option = options.get('date')

        if not date_option:
            return []

        date_option['strict_range'] = True

        if options.get('invoice_date', False):
            options['date']['date_field'] = "invoice_date"

        return super(AccountFinancialReport, self)._get_options_date_domain(options)
    '''

    def is_bilancio(self):
        if self.id == self.env.ref('huroos_report_bilancio.stato_patrimoniale_cee').id:
            return 'stato_patrimoniale'
        elif self.id == self.env.ref('huroos_report_bilancio.conto_economico_cee').id:
            return 'conto_economico'
        if self.id == self.env.ref('huroos_report_bilancio.report_bilancio_cee').id:
            return 'report_bilancio'
        else:
            return 'no_bilancio'

    def _build_lines_hierarchy(self, options_list, financial_lines, solver, groupby_keys):
        lines = super(AccountFinancialReport, self)._build_lines_hierarchy(options_list, financial_lines, solver, groupby_keys)
        lines_to_remove = []

        for line in lines:
            if ('caret_options' in line and line['caret_options'] == 'account.account' and len(line['columns']) > 0 and
                    line['columns'][0]['no_format'] == 0):
                lines_to_remove.append(line)
        lines = [line for line in lines if line not in lines_to_remove]
        return lines

    def dividi_righe_stato_patrimoniale(self, lines, is_bilancio_completo=False):
        """
        is_bilancio_completo: indica se stiamo considerando il report bilancio stato pratrimoniale e conto economico uniti
        sezione 1: in alto a sinistra
        sezione 2: in alto a destra
        sezione 3: dopo le due colonne indica i conti d'ordini che hanno larghezza completa
        sezione 4: in basso a sinistra, indiza i totali dell'attivo
        sezione 5 in basso a destra, indica i totali del passivo
        """

        passivita = 'liability'
        attivita = 'asset'

        if not is_bilancio_completo:
            sezione_passivo = self.env.ref('huroos_report_bilancio.sp_passivo').id
            sezione_conti_ordine = self.env.ref('huroos_report_bilancio.sp_conti_ordine').id
            sezione_totale_attivita = self.env.ref('huroos_report_bilancio.totale_attivo').id
            sezione_totale_passivita = self.env.ref('huroos_report_bilancio.totale_passivo_sp').id
            sezione_totale_utile = self.env.ref('huroos_report_bilancio.totale_utile_sp').id
            sezione_pareggio = self.env.ref('huroos_report_bilancio.totale_pareggio_sp').id
        else:
            sezione_passivo = self.env.ref('huroos_report_bilancio.sp_passivo_bilancio').id
            sezione_conti_ordine = self.env.ref('huroos_report_bilancio.sp_conti_ordine_bilancio').id
            sezione_totale_attivita = self.env.ref('huroos_report_bilancio.totale_attivo_bilancio').id
            sezione_totale_passivita = self.env.ref('huroos_report_bilancio.totale_passivo_sp_bilancio').id
            sezione_totale_utile = self.env.ref('huroos_report_bilancio.totale_utile_sp_bilancio').id
            sezione_pareggio = self.env.ref('huroos_report_bilancio.totale_pareggio_sp_bilancio').id
        righe = {
            'sezione_1': [],
            'sezione_2': [],
            'sezione_3': [],
            'sezione_4': [],
            'sezione_5': [],
        }
        for line in lines:
            if ('caret_options' in line and line['caret_options'] == 'account.account' and len(line['columns']) > 0 and
                    line['columns'][0]['no_format'] == 0):
                continue

            sezione = 0

            conti = self.env['account.account'].search(['|', ('code', '=', line['name'].split(' - ')[0]),
                                                        ('name', '=', line['name']),
                                                        ('area', '=', 'stato_patrimoniale'),
                                                        ('deprecated', '=', False)])

            if not conti:
                conti = self.env['account.account'].search(['|', ('code', '=', line['name'].split(' ')[0]),
                                                            ('name', '=', line['name']),
                                                            ('area', '=', 'stato_patrimoniale'),
                                                            ('deprecated', '=', False)])

            # Quando è attiva la funzionalitá totals_below_sections
            if not conti:
                code = line['name'].split(' ')
                if len(code) > 1:
                    conti = self.env['account.account'].search(['|', ('code', '=', code[1]),
                                                                ('name', '=', line['name']),
                                                                ('area', '=', 'stato_patrimoniale'),
                                                                ('deprecated', '=', False)])

            if len(conti) > 1:
                conto = conti[0]
                # se si trovano piu conti relativi ad una riga cioè esistono righe con lo stesso nome
                # si controlla se la riga del report finanziario è in attivo o in passivo e di conseguenza
                # si selezione il conto corretto di tipo attività o passività
                riga = self.env['account.financial.html.report.line'].browse(line['id'])
                tabella_riga = self.env['account.financial.html.report.line'].browse(int(riga.parent_path.split('/')[0]))
                if tabella_riga.code == "SP_AT":
                    for c in conti:
                        if c.user_type_id.internal_group == attivita:
                            conto = c
                elif tabella_riga.code == "SP_PASS":
                    for c in conti:
                        if c.user_type_id.internal_group == passivita:
                            conto = c
            else:
                conto = conti
            # si controlla il macroaggregato
            if conto.macroaggregate_id:
                conto = conto.macroaggregate_id

            # passività finisce nella sezione 2 a destra
            code = line['id'].split('_')[1] if 'total_' in str(line['id']) else line['id']
            if conto.user_type_id.internal_group == passivita or str(code) == str(sezione_passivo):
                righe['sezione_2'].append(line)
                sezione = 2

            # sezione conto ordine
            if line['id'] == sezione_conti_ordine:
                righe['sezione_3'].append(line)
                sezione = 3

            # sezione totale attivita
            if line['id'] == sezione_totale_attivita:
                righe['sezione_4'].append(line)
                sezione = 4

            # sezione totale passivita , utile d'esercizio, pareggio
            if line['id'] in [sezione_totale_passivita, sezione_totale_utile, sezione_pareggio]:
                righe['sezione_5'].append(line)
                sezione = 5

            # cerco se è un conto d'ordine
            if sezione == 0:
                conto = self.env['account.account'].search(['|', ('code', '=', line['name'].split(' - ')[0]),
                                                            ('name', '=', line['name']),
                                                            ('area', '=', 'conti_ordine'), ('deprecated', '=', False)],
                                                           limit=1)
                if not conto:
                    conto = self.env['account.account'].search(['|', ('code', '=', line['name'].split(' ')[0]),
                                                                ('name', '=', line['name']),
                                                                ('area', '=', 'conti_ordine'),
                                                                ('deprecated', '=', False)],
                                                               limit=1)
                if conto.macroaggregate_id:
                    conto = conto.macroaggregate_id
                if conto.id:
                    righe['sezione_3'].append(line)
                    sezione = 3

            # se non è nessuna delle altre è un attività
            if sezione == 0:
                righe['sezione_1'].append(line)
                sezione = 1

        return righe

    def dividi_righe_conto_economico(self, lines, is_bilancio_completo=False):
        """
        is_bilancio_completo: indica se stiamo considerando il report bilancio stato pratrimoniale e conto economico uniti
        sezione 1: in alto a sinistra
        sezione 2: in alto a destra
        sezione 3: dopo le due colonne indica i conti d'ordini che hanno larghezza completa
        sezione 4: in basso a sinistra, indiza i totali dell'attivo
        sezione 5 in basso a destra, indica i totali del passivo
        """

        passivita = 'expense'
        attivita = 'income'
        if not is_bilancio_completo:
            sezione_passivo = self.env.ref('huroos_report_bilancio.ce_passivo').id
            sezione_totale_attivita = self.env.ref('huroos_report_bilancio.totale_ricavi').id
            sezione_totale_passivita = self.env.ref('huroos_report_bilancio.totale_costi_ce').id
            sezione_totale_utile = self.env.ref('huroos_report_bilancio.totale_utile_ce').id
            sezione_pareggio = self.env.ref('huroos_report_bilancio.totale_pareggio_ce').id
        else:
            sezione_passivo = self.env.ref('huroos_report_bilancio.ce_passivo_bilancio').id
            sezione_totale_attivita = self.env.ref('huroos_report_bilancio.totale_ricavi_bilancio').id
            sezione_totale_passivita = self.env.ref('huroos_report_bilancio.totale_costi_ce_bilancio').id
            sezione_totale_utile = self.env.ref('huroos_report_bilancio.totale_utile_ce_bilancio').id
            sezione_pareggio = self.env.ref('huroos_report_bilancio.totale_pareggio_ce_bilancio').id
        righe = {
            'sezione_1': [],
            'sezione_2': [],
            'sezione_3': [],
            'sezione_4': [],
            'sezione_5': [],
        }
        for line in lines:
            if ('caret_options' in line and line['caret_options'] == 'account.account' and len(line['columns']) > 0 and
                    line['columns'][0]['no_format'] == 0):
                continue

            sezione = 0

            conti = self.env['account.account'].search(['|', ('code', '=', line['name'].split(' - ')[0]),
                                                        '&', ('name', '=', line['name']),
                                                        '&', ('area', '=', 'conto_economico'),
                                                             ('deprecated', '=', False)])

            if not conti:
                conti = self.env['account.account'].search(['|', ('code', '=', line['name'].split(' ')[0]),
                                                            '&', ('name', '=', line['name']),
                                                            '&', ('area', '=', 'conto_economico'),
                                                                 ('deprecated', '=', False)])

            # Quando è attiva la funzionalitá totals_below_sections
            if not conti:
                code = line['name'].split(' ')
                if len(code) > 1:
                    conti = self.env['account.account'].search(['|', ('code', '=', code[1]),
                                                                ('name', '=', line['name']),
                                                                ('area', '=', 'conto_economico'),
                                                                ('deprecated', '=', False)])

            if len(conti) > 1:
                conto = conti[0]
                # se si trovano piu conti relativi ad una riga cioè esistono righe con lo stesso nome
                # si controlla se la riga del report finanziario è in attivo o in passivo e di conseguenza
                # si selezione il conto corretto di tipo attività o passività
                riga = self.env['account.financial.html.report.line'].browse(line['id'])
                tabella_riga = self.env['account.financial.html.report.line'].browse(riga.parent_path.split('/')[0])
                if tabella_riga.code == "CE_AT":
                    for c in conti:
                        if c.user_type_id.internal_group == attivita:
                            conto = c
                elif tabella_riga.code == "CE_PASS":
                    for c in conti:
                        if c.user_type_id.internal_group == passivita:
                            conto = c
            else:
                conto = conti
            # si controlla il macroaggregato
            if conto.macroaggregate_id:
                conto = conto.macroaggregate_id

            # passività finisce nella sezione 2 a destra
            code = line['id'].split('_')[1] if 'total_' in str(line['id']) else line['id']
            if conto.user_type_id.internal_group == passivita or str(code) == str(sezione_passivo):
                righe['sezione_1'].append(line)
                sezione = 2

            # sezione totale attivita
            if line['id'] == sezione_totale_attivita:
                righe['sezione_5'].append(line)
                sezione = 4

            # sezione totale passivita , utile d'esercizio, pareggio
            if line['id'] in [sezione_totale_passivita, sezione_totale_utile, sezione_pareggio]:
                righe['sezione_4'].append(line)
                sezione = 5

            # se non è nessuna delle altre è un attività
            if sezione == 0:
                righe['sezione_2'].append(line)
                sezione = 1

        return righe

    def dividi_righe_report_bilancio(self, lines):
        """
        funzione chiamata dal report per dividere le righe del report in stato patrimoniale e conto economico
        :param lines:
        :return:
        """

        sp_attivo = self.env.ref('huroos_report_bilancio.sp_attivo_bilancio').id
        sp_passivo = self.env.ref('huroos_report_bilancio.sp_passivo_bilancio').id
        id_co = self.env.ref('huroos_report_bilancio.sp_conti_ordine_bilancio').id
        totale_attivo = self.env.ref('huroos_report_bilancio.totale_attivo_bilancio').id
        totale_passivo_sp = self.env.ref('huroos_report_bilancio.totale_passivo_sp_bilancio').id
        totale_utile_sp = self.env.ref('huroos_report_bilancio.totale_utile_sp_bilancio').id
        totale_pareggio_sp = self.env.ref('huroos_report_bilancio.totale_pareggio_sp_bilancio').id

        html_report_lines = self.env['account.financial.html.report.line'].search_read(["|", "|", "|", ('parent_path', '=ilike', str(sp_attivo) + '/%'),
                                              ('parent_path', '=ilike', str(sp_passivo) + '/%'),('parent_path', '=ilike', str(id_co) + '/%'),
                                            ('id', 'in', [totale_attivo, totale_passivo_sp, totale_utile_sp, totale_pareggio_sp])], fields=['name'])
        sp_ids = []
        for riga in html_report_lines:
            sp_ids.append(riga['id'])

        righe_stato_parimoniale = []
        righe_conto_economico = []

        # divido le righe tra stato patrimoniale e conto economico
        for line in lines:
            if line['id'] in sp_ids or ('parent_id' in line.keys() and line['parent_id'] in sp_ids):
                righe_stato_parimoniale.append(line)
            else:
                righe_conto_economico.append(line)

        sezioni_sp = self.dividi_righe_stato_patrimoniale(righe_stato_parimoniale, is_bilancio_completo=True)
        sezioni_ce = self.dividi_righe_conto_economico(righe_conto_economico, is_bilancio_completo=True)

        return {
            'sp': sezioni_sp,
            'ce': sezioni_ce
        }

class AccountReports(models.AbstractModel):
    _inherit = "account.report"

    def is_bilancio(self):
        return 'no_bilancio'