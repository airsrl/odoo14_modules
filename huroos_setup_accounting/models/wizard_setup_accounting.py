from odoo import models, fields, api
from odoo.exceptions import UserError
from base64 import b64decode
import calendar
import xlrd
import os


MONTHS = ["GENNAIO", "FEBBRAIO", "MARZO", "APRILE", "MAGGIO", "GIUGNO", "LUGLIO", "AGOSTO", "SETTEMBRE", "OTTOBRE", "NOVEMBRE", "DICEMBRE"]


def _get_absolute_path(relative_path):
    """Esempio relative_path: data/account_tax_import.xlsx"""

    working_dir = os.path.dirname(__file__)
    path = "../" + relative_path
    return os.path.join(working_dir, path)


class WizardSetupAccounting(models.TransientModel):
    _name = 'wizard.setup.accounting'

    ####################################################
    #             MULTI STEP WIZARD ENGINE             #
    ####################################################

    state = fields.Selection(
        selection=[
            ('step_1', "Funzionalità Contabili"),
            ('step_2', "Piano Dei Conti"),
            ('step_3', "Imposte"),
            ('step_4', "Registri"),
            ('step_5', "Assegna Conti"),
            ('step_6', "Import Saldi"),
            ('step_7', "Reverse Charge"),
            ('step_8', "Termini di Pagamento"),
            ('step_9', "Ritenute d'acconto"),
            ('step_10', "Data Range")
        ],
        help="Lo stato deve sempre terminare con un intero e deve essere univoco."
    )
    # Campo usato solo nella view per nascondere il bottone 'Successivo' in caso ci trovassimo nell'ultima pagina
    is_last_step = fields.Boolean(compute="_compute_is_last_step")

    @api.depends('state')
    def _compute_is_last_step(self):
        last_step = self.env['wizard.setup.accounting']._fields['state'].selection[-1][0]
        if self.state == last_step:
            self.is_last_step = True
        else:
            self.is_last_step = False

    def button_init(self):
        self._init_setup_tax()
        self._init_setup_journal()
        self._init_setup_payment_term()
        self._init_withholding_tax()

        self.state = 'step_1'
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.setup.accounting",
            "target": "new",
            "res_id": self.id
        }

    def button_next(self):
        last_step = self.env['wizard.setup.accounting']._fields['state'].selection[-1][0]
        state_number = int(self.state[-1]) + 1
        if state_number <= int(last_step.split('_')[-1]):
            self.state = f"step_{state_number}"
            self._onchange_state()
            return {
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "res_model": "wizard.setup.accounting",
                "target": "new",
                "res_id": self.id
            }

    def button_previous(self):
        state_number = int(self.state.split('_')[-1]) - 1
        if state_number >= 1:
            self.state = f"step_{state_number}"
            self._onchange_state()
            return {
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "res_model": "wizard.setup.accounting",
                "target": "new",
                "res_id": self.id
            }

    def button_exit(self):
        return True

    ####################################################
    #         END OF MULTI STEP WIZARD ENGINE          #
    ####################################################

    # Funzionalità
    module_e_invoice_in = fields.Boolean()
    module_e_invoice_out = fields.Boolean()
    module_reverse_charge = fields.Boolean()
    module_corrispettivi = fields.Boolean()
    module_ddt = fields.Boolean()
    module_intrastat = fields.Boolean()
    module_riba = fields.Boolean()
    module_vat_registries = fields.Boolean()
    module_vat_statement = fields.Boolean()
    module_lipe = fields.Boolean()
    module_withholding_tax = fields.Boolean()
    module_declaration_intent = fields.Boolean()
    module_split_payment = fields.Boolean()
    module_aruba = fields.Boolean()
    module_competenza_iva = fields.Boolean()
    module_massive_operations = fields.Boolean()
    module_template_registrazioni = fields.Boolean()

    # Piano Dei Conti
    pdc_file_import = fields.Binary()

    # Imposte
    account_tax_ids = fields.One2many(comodel_name='setup.account.tax', inverse_name='wizard_id')

    # Registri
    account_journal_ids = fields.One2many(comodel_name='setup.account.journal', inverse_name='wizard_id')

    # Conti Default
    a_partner_credit = fields.Many2one('account.account')
    a_partner_debit = fields.Many2one('account.account')
    a_product_income = fields.Many2one('account.account')
    a_product_expense = fields.Many2one('account.account')
    a_suspense = fields.Many2one('account.account')
    a_utili = fields.Many2one('account.account')
    a_perdite = fields.Many2one('account.account')
    a_tax_credit = fields.Many2one('account.account')
    a_tax_debit = fields.Many2one('account.account')

    # Saldi
    file_saldi = fields.Binary()
    account_credit_id = fields.Many2one('account.account')
    account_debit_id = fields.Many2one('account.account')
    account_bilancio_apertura = fields.Many2one('account.account')
    journal_saldi_id = fields.Many2one('account.journal')
    date_saldi = fields.Date()

    # Reverse Charge
    journal_ita_rc = fields.Many2one('account.journal')
    journal_intra_rc = fields.Many2one('account.journal')
    journal_extra_rc = fields.Many2one('account.journal')
    journal_payment = fields.Many2one('account.journal')
    transitory_account = fields.Many2one('account.account')
    bank_account_rc = fields.Many2one(
        comodel_name='account.account',
        help='Questo conto verrà impostato come conto bancario, conto ricevute in sospeso '
             'e conto pagamenti in sospeso su tutti i registri RC'
    )

    # Termini di Pagamento
    account_payment_term_ids = fields.One2many(comodel_name='setup.account.payment.term', inverse_name='wizard_id')

    # Ritenta d'acconto
    withholding_tax_ids = fields.One2many(comodel_name='setup.withholding.tax', inverse_name='wizard_id')
    withholding_credit_account_id = fields.Many2one('account.account')
    withholding_debit_account_id = fields.Many2one('account.account')
    withholding_journal_id = fields.Many2one('account.journal')
    withholding_payment_term_id = fields.Many2one('account.payment.term')

    # Data range
    years_to_cover = fields.Integer(string="N° anni da creare", default=1)
    create_months = fields.Boolean(string="Mesi")
    create_quarters = fields.Boolean(string="Trimestri")
    create_years = fields.Boolean(string="Anni")

    ####################################################
    #               ONE2MANY FIELDS INIT               #
    ####################################################

    def _init_setup_main(self, filename, model):
        """Funzione principale usata per inizializzare i field One2many del wizard"""

        path = f"static/file/{filename}"
        excel_file = xlrd.open_workbook(_get_absolute_path(path))

        for sheet in excel_file.sheets():
            for row in range(sheet.nrows):
                if row == 0:
                    continue

                row_values = sheet.row_values(row)

                if row_values[0] != '' and row_values[1] != '':
                    setup_account_tax_vals = {
                        'wizard_id': self.id,
                        'huroos_id': str(int(row_values[0])),
                        'name': row_values[1],
                        'install': True
                    }
                    self.env[model].create(setup_account_tax_vals)

    def _init_setup_tax(self):
        self._init_setup_main("account_tax_import.xlsx", "setup.account.tax")

    def _init_setup_journal(self):
        self._init_setup_main("account_journal_import.xlsx", "setup.account.journal")

    def _init_setup_payment_term(self):
        self._init_setup_main("account_payment_term_import.xlsx", "setup.account.payment.term")

    def _init_withholding_tax(self):
        self._init_setup_main("withholding_tax_import.xlsx", "setup.withholding.tax")

    ####################################################
    #            END OF ONE2MANY FIELDS INIT           #
    ####################################################

    def download_sample_pdc(self):
        return {
            "type": "ir.actions.act_url",
            "url": '/huroos_setup_accounting/static/file/pdc_sample.xlsx',
            "target": "new",
        }

    def download_sample_saldi(self):
        return {
            "type": "ir.actions.act_url",
            "url": '/huroos_setup_accounting/static/file/saldi_sample.xlsx',
            "target": "new",
        }

    def create_fiscal_position(self):

        fiscal_position_ids = self.env['account.fiscal.position'].search([]).unlink()

        rc_type_ita_id = self.env['account.rc.type'].search([('huroos_id', '=', '1')])
        rc_type_intra_id = self.env['account.rc.type'].search([('huroos_id', '=', '2')])
        rc_type_extra_id = self.env['account.rc.type'].search([('huroos_id', '=', '3')])

        tax_sale_22_id = self.env['account.tax'].search([('huroos_id', '=', '1')])
        tax_sale_10_id = self.env['account.tax'].search([('huroos_id', '=', '2')])
        tax_sale_4_id = self.env['account.tax'].search([('huroos_id', '=', '4')])
        tax_rc_import_id = self.env['account.tax'].search([('huroos_id', '=', '15')])
        tax_rc_ita_id = self.env['account.tax'].search([('huroos_id', '=', '11')])
        tax_rc_intra_id = self.env['account.tax'].search([('huroos_id', '=', '9')])
        tax_rc_extra_id = self.env['account.tax'].search([('huroos_id', '=', '10')])
        tax_san_marino_id = self.env['account.tax'].search([('huroos_id', '=', '18')])
        tax_art_41_id = self.env['account.tax'].search([('huroos_id', '=', '16')])
        tax_art_8_id = self.env['account.tax'].search([('huroos_id', '=', '17')])
        tax_art_8c_id = self.env['account.tax'].search([('huroos_id', '=', '19')])
        tax_split_22_id = self.env['account.tax'].search([('huroos_id', '=', '33')])

        # ITA
        vals_ita = {
            'name': 'ITALIA',
            'auto_apply': True,
            'sequence': 0,
            'huroos_id': '1',
        }

        # ACQUISTI INTRA
        vals_intra = {
            'name': 'ACQUISTI INTRA CEE',
            'auto_apply': True,
            'sequence': 1,
            'huroos_id': '2',
            'rc_type_id': rc_type_intra_id.id if rc_type_intra_id else False,
            'tax_ids': [(0, 0, {
                'tax_src_id': tax_rc_import_id.id if tax_rc_import_id else False,
                'tax_dest_id': tax_rc_intra_id.id if tax_rc_intra_id else False,
            })]
        }

        # ACQUISTI EXTRA
        vals_extra = {
            'name': 'ACQUISTI EXTRA CEE',
            'auto_apply': True,
            'sequence': 2,
            'huroos_id': '3',
            'rc_type_id': rc_type_extra_id.id if rc_type_extra_id else False,
            'tax_ids': [(0, 0, {
                'tax_src_id': tax_rc_import_id.id if tax_rc_import_id else False,
                'tax_dest_id': tax_rc_extra_id.id if tax_rc_extra_id else False,
            })]
        }

        # ACQUISTI ITA RC
        vals_ita_rc = {
            'name': 'ACQUISTI ITALIA RC',
            'auto_apply': True,
            'sequence': 3,
            'huroos_id': '4',
            'rc_type_id': rc_type_ita_id.id if rc_type_ita_id else False,
            'tax_ids': [(0, 0, {
                'tax_src_id': tax_rc_import_id.id if tax_rc_import_id else False,
                'tax_dest_id': tax_rc_ita_id.id if tax_rc_ita_id else False,
            })]
        }

        # VENDITE EXTRA
        vals_vendite_extra = {
            'name': 'VENDITE EXTRA CEE',
            'auto_apply': True,
            'sequence': 4,
            'huroos_id': '5',
            'tax_ids': [
                (0, 0, {
                    'tax_src_id': tax_sale_22_id.id if tax_sale_22_id else False,
                    'tax_dest_id': tax_art_8_id.id if tax_art_8_id else False,
                }),
                (0, 0, {
                    'tax_src_id': tax_sale_10_id.id if tax_sale_10_id else False,
                    'tax_dest_id': tax_art_8_id.id if tax_art_8_id else False,
                }),
                (0, 0, {
                    'tax_src_id': tax_sale_4_id.id if tax_sale_4_id else False,
                    'tax_dest_id': tax_art_8_id.id if tax_art_8_id else False,
                })
            ]
        }

        # VENDITE INTRA
        vals_vendite_intra = {
            'name': 'VENDITE INTRA CEE',
            'auto_apply': True,
            'sequence': 5,
            'huroos_id': '6',
            'tax_ids': [
                (0, 0, {
                    'tax_src_id': tax_sale_22_id.id if tax_sale_22_id else False,
                    'tax_dest_id': tax_art_41_id.id if tax_art_41_id else False,
                }),
                (0, 0, {
                    'tax_src_id': tax_sale_10_id.id if tax_sale_10_id else False,
                    'tax_dest_id': tax_art_41_id.id if tax_art_41_id else False,
                }),
                (0, 0, {
                    'tax_src_id': tax_sale_4_id.id if tax_sale_4_id else False,
                    'tax_dest_id': tax_art_41_id.id if tax_art_41_id else False,
                })
            ]
        }

        # DICHIARAZIONE D'INTENTO
        vals_dichiarazione_intento = {
            'name': "DICHIARAZIONE D'INTENTO",
            'auto_apply': True,
            'sequence': 6,
            'huroos_id': '7',
            'tax_ids': [
                (0, 0, {
                    'tax_src_id': tax_sale_22_id.id if tax_sale_22_id else False,
                    'tax_dest_id': tax_art_8c_id.id if tax_art_8c_id else False,
                }),
                (0, 0, {
                    'tax_src_id': tax_sale_10_id.id if tax_sale_10_id else False,
                    'tax_dest_id': tax_art_8c_id.id if tax_art_8c_id else False,
                }),
                (0, 0, {
                    'tax_src_id': tax_sale_4_id.id if tax_sale_4_id else False,
                    'tax_dest_id': tax_art_8c_id.id if tax_art_8c_id else False,
                })
            ]
        }

        # SAN MARINO
        vals_san_marino = {
            'name': 'SAN MARINO',
            'sequence': 7,
            'huroos_id': '8',
            'auto_apply': True,
            'country_id': self.env['res.country'].search([('code', '=', 'SM')]).id,
            'tax_ids': [(0, 0, {
                'tax_src_id': tax_sale_22_id.id if tax_sale_22_id else False,
                'tax_dest_id': tax_san_marino_id.id if tax_san_marino_id else False,
            })]
        }

        # SPLIT PAYMENT
        model_split_payment = self.env['ir.module.module'].search([('name', '=', 'l10n_it_split_payment')])
        if model_split_payment and model_split_payment.state == 'installed':
            vals_split_payment = {
                'name': 'SCISSIONE PAGAMENTI',
                'sequence': 8,
                'huroos_id': '9',
                'auto_apply': True,
                'split_payment': True,
                'tax_ids': [(0, 0, {
                    'tax_src_id': tax_sale_22_id.id if tax_sale_22_id else False,
                    'tax_dest_id': tax_split_22_id.id if tax_split_22_id else False,
                })]
            }
            self.env['account.fiscal.position'].create(vals_split_payment)

        self.env['account.fiscal.position'].create(vals_ita)
        self.env['account.fiscal.position'].create(vals_ita_rc)
        self.env['account.fiscal.position'].create(vals_intra)
        self.env['account.fiscal.position'].create(vals_extra)
        self.env['account.fiscal.position'].create(vals_vendite_extra)
        self.env['account.fiscal.position'].create(vals_vendite_intra)
        self.env['account.fiscal.position'].create(vals_dichiarazione_intento)
        self.env['account.fiscal.position'].create(vals_san_marino)

        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.setup.accounting",
            "target": "new",
            "res_id": self.id
        }

    def create_rc_automatism(self):
        # Assegnazione dei conti bancari
        if self.bank_account_rc:
            for journal in [self.journal_ita_rc, self.journal_intra_rc, self.journal_extra_rc, self.journal_payment]:
                if journal:
                    journal.default_account_id = self.bank_account_rc
                    journal.payment_debit_account_id = self.bank_account_rc
                    journal.payment_credit_account_id = self.bank_account_rc

        # Creazione Tipi di inversione contabile
        rc_type = self.env['account.rc.type'].search([]).unlink()

        #ITA RC

        rc_22_ita_id = self.env['account.tax'].search([('huroos_id', '=', '11')])
        rc_22_auto_ita_id = self.env['account.tax'].search([('huroos_id', '=', '14')])

        vals_ita_rc = {
            'name': 'REVERSE CHARGE ITA',
            'method': 'selfinvoice',
            'fiscal_document_type_id': self.env['fiscal.document.type'].search([('code', '=', 'TD16')], limit=1).id,
            'partner_type': 'other',
            'partner_id': self.env.company.partner_id.id,
            'journal_id': self.journal_ita_rc.id,
            'payment_journal_id': self.journal_payment.id,
            'transitory_account_id': self.transitory_account.id,
            'huroos_id': '1',
            'tax_ids': [(0, 0, {
                'purchase_tax_id': rc_22_ita_id.id,
                'sale_tax_id': rc_22_auto_ita_id.id,
            })]
        }

        #INTRA RC

        rc_22_intra_id = self.env['account.tax'].search([('huroos_id', '=', '9')])
        rc_22_auto_intra_id = self.env['account.tax'].search([('huroos_id', '=', '12')])

        vals_intra_rc = {
            'name': 'REVERSE CHARGE INTRA CEE',
            'method': 'selfinvoice',
            'fiscal_document_type_id': self.env['fiscal.document.type'].search([('code', '=', 'TD18')], limit=1).id,
            'partner_type': 'other',
            'partner_id': self.env.company.partner_id.id,
            'journal_id': self.journal_intra_rc.id,
            'payment_journal_id': self.journal_payment.id,
            'transitory_account_id': self.transitory_account.id,
            'huroos_id': '2',
            'tax_ids': [(0, 0, {
                'purchase_tax_id': rc_22_intra_id.id,
                'sale_tax_id': rc_22_auto_intra_id.id,
            })]
        }

        # EXTRA RC

        rc_22_extra_id = self.env['account.tax'].search([('huroos_id', '=', '10')])
        rc_22_auto_extra_id = self.env['account.tax'].search([('huroos_id', '=', '13')])

        vals_extra_rc = {
            'name': 'REVERSE CHARGE EXTRA CEE',
            'method': 'selfinvoice',
            'fiscal_document_type_id': self.env['fiscal.document.type'].search([('code', '=', 'TD17')], limit=1).id,
            'partner_type': 'other',
            'partner_id': self.env.company.partner_id.id,
            'journal_id': self.journal_extra_rc.id,
            'payment_journal_id': self.journal_payment.id,
            'transitory_account_id': self.transitory_account.id,
            'huroos_id': '3',
            'tax_ids': [(0, 0, {
                'purchase_tax_id': rc_22_extra_id.id,
                'sale_tax_id': rc_22_auto_extra_id.id,
            })]
        }

        self.env['account.rc.type'].create(vals_ita_rc)
        self.env['account.rc.type'].create(vals_intra_rc)
        self.env['account.rc.type'].create(vals_extra_rc)

        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.setup.accounting",
            "target": "new",
            "res_id": self.id
        }

    def upload_saldi(self):
        if self.file_saldi and self.account_credit_id and self.account_debit_id and self.account_bilancio_apertura and self.date_saldi and self.journal_saldi_id:
            book = xlrd.open_workbook(file_contents=b64decode(self.file_saldi))

            vals = {
                'journal_id': self.journal_saldi_id.id,
                'date': self.date_saldi,
                'ref': 'APERTURA SALDI',
                'line_ids': []
            }

            total_balance = 0

            for sheet in book.sheets():
                for row in range(sheet.nrows):
                    if row >= 1:
                        row_values = sheet.row_values(row)
                        type = str(row_values[0]).upper()
                        account_code = row_values[1]
                        balance = row_values[2]

                        account_id = None
                        partner_id = None
                        if type == 'G':
                            account_code = str(account_code)
                            account_id = self.env['account.account'].search([('code', '=', account_code )])
                        if type == 'C':
                            account_id = self.account_credit_id
                            partner_id = self.env['res.partner'].search([('name', '=', account_code), ('type', 'in', ['contact', 'invoice'])], limit=1)
                            if not partner_id:
                                partner_id = self.env['res.partner'].create({'name': account_code})
                        if type == 'F':
                            account_id = self.account_debit_id
                            partner_id = self.env['res.partner'].search([('name', '=', account_code), ('type', 'in', ['contact', 'invoice'])], limit=1)
                            if not partner_id:
                                partner_id = self.env['res.partner'].create({'name': account_code})

                        if not account_id:
                            raise UserError("Non è stato trovato il conto " + account_code)

                        if balance > 0:
                            # Debit
                            vals['line_ids'].append((0, 0, {
                                'debit': abs(balance),
                                'partner_id': partner_id.id if partner_id else False,
                                'account_id': account_id.id,
                                'credit': 0,
                                'tax_ids': False
                            }))
                            vals['line_ids'].append((0, 0, {
                                'credit': abs(balance),
                                'account_id': self.account_bilancio_apertura.id,
                                'debit': 0,
                                'tax_ids': False
                            }))

                        else:
                            # Credit
                            vals['line_ids'].append((0, 0, {
                                'credit': abs(balance),
                                'partner_id': partner_id.id if partner_id else False,
                                'account_id': account_id.id,
                                'debit': 0,
                                'tax_ids': False
                            }))
                            vals['line_ids'].append((0, 0, {
                                'debit': abs(balance),
                                'account_id': self.account_bilancio_apertura.id,
                                'credit': 0,
                                'tax_ids': False
                            }))

            # Creo Registrazione
            self.env['account.move'].create(vals)

        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.setup.accounting",
            "target": "new",
            "res_id": self.id
        }

    def upload_pdc(self):
        if self.pdc_file_import:
            # Se la company attiva corrisponde alla main_company cerco tra le proprietà azienda generali
            # (senza company_id)
            company = self.env.company.id if self.env.company != self.env.ref('base.main_company') else False

            property_account_payable = self.env['ir.property'].sudo().search([
                ('name', '=', 'property_account_payable_id'),
                ('company_id', '=', company)
            ])
            if property_account_payable:
                property_account_payable.unlink()

            property_account_receivable = self.env['ir.property'].sudo().search([
                ('name', '=', 'property_account_receivable_id'),
                ('company_id', '=', company)
            ])
            if property_account_receivable:
                property_account_receivable.unlink()

            property_account_expense = self.env['ir.property'].sudo().search([
                ('name', '=', 'property_account_expense_categ_id'),
                ('company_id', '=', company)
            ])
            if property_account_expense:
                property_account_expense.unlink()

            property_account_income = self.env['ir.property'].sudo().search([
                ('name', '=', 'property_account_income_categ_id'),
                ('company_id', '=', company)
            ])
            if property_account_income:
                property_account_income.unlink()

            # Blocco non necessario dato che i parametri si aggiornano in automatico in base alle proprietà azienda
            """
            partner_ids = self.env['res.partner'].search([('active', 'in', [True, False])])
            for partner in partner_ids:
                partner.write({
                    'property_account_receivable_id': False,
                    'property_account_payable_id': False,
                })
            """

            journal_ids = self.env['account.journal'].search([('active', 'in', [True, False])])
            for journal in journal_ids:
                journal.write({
                    'default_account_id': False,
                    'suspense_account_id': False,
                    'profit_account_id': False,
                    'payment_debit_account_id': False,
                    'payment_credit_account_id': False,
                })

            account_ids = self.env['account.account'].search([])
            for account in account_ids:
                try:
                    account.unlink()
                except Exception as e:
                    account.deprecated = True

            book = xlrd.open_workbook(file_contents=b64decode(self.pdc_file_import))
            for sheet in book.sheets():
                for row in range(sheet.nrows):
                    if row >= 1:
                        row_values = sheet.row_values(row)
                        user_type_id = self.env['account.account.type'].search([('name', '=', row_values[2])])
                        vals = {
                            'code': row_values[0],
                            'name': row_values[1],
                            'user_type_id': user_type_id.id,
                            'reconcile': bool(row_values[3])
                        }
                        account_id = self.env['account.account'].search([('code', '=', row_values[0])])
                        if not account_id:
                            self.env['account.account'].create(vals)
                        else:
                            account_id.write(vals)

        self.button_next()
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.setup.accounting",
            "target": "new",
            "res_id": self.id
        }

    def create_vat_registries(self):
        sale_tax_registry = self.env['account.tax.registry'].create({
            'name': 'VENDITE',
            'layout_type': 'customer'
        })
        purchase_tax_registry = self.env['account.tax.registry'].create({
            'name': 'ACQUISTI',
            'layout_type': 'supplier'
        })
        return sale_tax_registry, purchase_tax_registry

    def create_journal(self):
        path = "static/file/account_journal_import.xlsx"
        excel_file = xlrd.open_workbook(_get_absolute_path(path))
        huroos_id_to_create = self.account_journal_ids.filtered(lambda journal: journal.install).mapped('huroos_id')

        if huroos_id_to_create:
            company = self.env.company.id if self.env.company != self.env.ref('base.main_company') else False
            self.env['ir.property'].sudo().search([('name', '=', 'property_stock_journal'), ('company_id', '=', company)]).unlink()
            self.env['account.journal'].search([]).unlink()

        # Controllo se il modulo dei corrispettivi è installato
        module_corrispettivi = self.env['ir.module.module'].search([('name', '=', 'l10n_it_corrispettivi')])

        # Controllo se il modulo dei registri IVA è installato, e in caso creo i registri iva ACQUISTI e VENDITE
        module_vat_registries = self.env['ir.module.module'].search([('name', '=', 'l10n_it_vat_registries')])
        if module_vat_registries.state == 'installed':
            sale_tax_registry, purchase_tax_registry = self.create_vat_registries()
        else:
            sale_tax_registry, purchase_tax_registry = False, False

        for sheet in excel_file.sheets():
            for row in range(sheet.nrows):
                if row == 0:
                    continue

                row_values = sheet.row_values(row)
                # 0: huroos_id, 1: Nome, 2: Tipologia, 3: Codice breve

                if not all(row_values) or str(int(row_values[0])) not in huroos_id_to_create:
                    continue

                journal_vals = {
                    'sequence': int(row_values[0]),
                    'huroos_id': str(int(row_values[0])),
                    'name': row_values[1],
                    'type': row_values[2],
                    'code': row_values[3],
                    'edi_format_ids': False
                }

                if module_corrispettivi.state == 'installed' and journal_vals['name'] == 'CORRISPETTIVI':
                    journal_vals['corrispettivi'] = True

                if module_vat_registries.state == 'installed' and journal_vals['type'] == 'sale':
                    journal_vals['tax_registry_id'] = sale_tax_registry.id

                elif module_vat_registries.state == 'installed' and journal_vals['type'] == 'purchase':
                    journal_vals['tax_registry_id'] = purchase_tax_registry.id

                self.env['account.journal'].create(journal_vals)

        self.button_next()
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.setup.accounting",
            "target": "new",
            "res_id": self.id
        }

    def create_tax(self):
        path = "static/file/account_tax_import.xlsx"
        excel_file = xlrd.open_workbook(_get_absolute_path(path))
        taxes_to_create = list()
        huroos_id_to_create = self.account_tax_ids.filtered(lambda tax: tax.install).mapped('huroos_id')

        if huroos_id_to_create:
            self.env['account.tax'].search([]).unlink()

        for sheet in excel_file.sheets():
            last_huroos_id = False
            for row in range(sheet.nrows):
                if row == 0:
                    continue

                row_values = sheet.row_values(row)
                # 0: huroos_id, 1: Nome imposta, 2: Tipo imposta, 3: Importo, 4: Calcolo Imposta,
                # 5: Etichetta su fatture, 6: Codice natura esenzione, 7: Riferimento normativo, 8: % Ripartizione,
                # 9: Basata su

                if row_values[0] != '':
                    # Esempio: 2.0 > 2 > '2'
                    last_huroos_id = str(int(row_values[0]))

                # Creo il dizionario solo se almeno le prime due colonne sono compilate
                if row_values[0] and row_values[1]:
                    if str(int(row_values[0])) not in huroos_id_to_create:
                        continue
                    tax_vals = {
                        'huroos_id': str(int(row_values[0])),
                        'name': row_values[1],
                        'type_tax_use': row_values[2],
                        'amount': row_values[3],
                        'amount_type': row_values[4],
                        'active': True,
                        'description': row_values[5],
                        'payability': row_values[6],
                        'kind_id': self.env['account.tax.kind'].search([('code', '=', row_values[7])], limit=1).id if row_values[7] else False,
                        'law_reference': row_values[8] or False,
                        'invoice_repartition_line_ids': [],
                        'refund_repartition_line_ids': []
                    }
                    taxes_to_create.append(tax_vals)

                if row_values[9] != '' and row_values[10] != '' and last_huroos_id in huroos_id_to_create:
                    repartition_vals = (0, 0, {'factor_percent': row_values[9], 'repartition_type': row_values[10]})
                    tax_vals['invoice_repartition_line_ids'].append(repartition_vals)
                    tax_vals['refund_repartition_line_ids'].append(repartition_vals)

        for tax in taxes_to_create:
            if not tax['invoice_repartition_line_ids'] and not tax['refund_repartition_line_ids']:
                tax.pop('invoice_repartition_line_ids')
                tax.pop('refund_repartition_line_ids')

            self.env['account.tax'].create(tax)

        self.button_next()
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.setup.accounting",
            "target": "new",
            "res_id": self.id
        }

    def create_payment_terms(self):
        # Controllo dell'esistenza del modulo delle riba (OPZIONALE)
        model_riba = self.env['ir.module.module'].search([('name', '=', 'l10n_it_ricevute_bancarie')])

        # Controllo dell'esistenza del modulo dei termini di pagamento fiscali (OBBLIGATORIO)
        model_fiscal_payment_term = self.env['ir.module.module'].search([('name', '=', 'l10n_it_fiscal_payment_term')])
        if not model_fiscal_payment_term or model_fiscal_payment_term.state != 'installed':
            raise UserError("Per poter procedere devi prima installare il modulo l10n_it_fiscal_payment_term.")

        path = "static/file/account_payment_term_import.xlsx"
        excel_file = xlrd.open_workbook(_get_absolute_path(path))
        huroos_id_to_create = self.account_payment_term_ids.filtered(
            lambda payment_term: payment_term.install
        ).mapped('huroos_id')

        if huroos_id_to_create:
            self.env['account.payment.term'].search([]).unlink()

        payment_terms_to_create = list()

        for sheet in excel_file.sheets():
            last_huroos_id = False
            for row in range(sheet.nrows):
                if row == 0:
                    continue

                row_values = sheet.row_values(row)

                if row_values[0] != '':
                    last_huroos_id = str(int(row_values[0]))

                if row_values[0] and row_values[1]:
                    if str(int(row_values[0])) not in huroos_id_to_create:
                        continue
                    payment_term_vals = {
                        'name': row_values[1],
                        'note': row_values[2],
                        'fatturapa_pt_id': self.env['fatturapa.payment_term'].search([('code', '=', row_values[3])]).id if row_values[3] else False,
                        'fatturapa_pm_id': self.env['fatturapa.payment_method'].search([('code', '=', row_values[4])]).id if row_values[4] else False,
                        'line_ids': []
                    }
                    if row_values[4] == 'MP12' and model_riba and model_riba.state == 'installed':
                        payment_term_vals['riba'] = True

                    payment_terms_to_create.append(payment_term_vals)

                if row_values[5] != '' and last_huroos_id in huroos_id_to_create:
                    condition_line_vals = {
                        'value': row_values[5],
                        'value_amount': row_values[6],
                        'amount_round': row_values[7],
                        'days': row_values[8],
                        'weeks': row_values[9],
                        'months': row_values[10],
                        'payment_days': int(row_values[11]) if row_values[11] else False,
                        'option': row_values[12]
                    }
                    payment_term_vals['line_ids'].append((0, 0, condition_line_vals))

        for payment_term in payment_terms_to_create:
            if not payment_term['line_ids']:
                payment_term.pop('line_ids')

            self.env['account.payment.term'].create(payment_term)

        self.button_next()
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.setup.accounting",
            "target": "new",
            "res_id": self.id
        }

    def create_ritenute_acconto(self):
        module_withholding_tax = self.env['ir.module.module'].search([('name', '=', 'l10n_it_withholding_tax')])
        if module_withholding_tax.state != 'installed':
            raise UserError("Il modulo l10n_it_withholding_tax per le ritenute d'acconto non è installato.")

        if not all([self.withholding_credit_account_id, self.withholding_debit_account_id, self.withholding_journal_id,
                    self.withholding_payment_term_id]):
            raise UserError("Prima di procedere devi compilare tutti i campi.")

        path = "static/file/withholding_tax_import.xlsx"
        excel_file = xlrd.open_workbook(_get_absolute_path(path))
        huroos_id_to_create = self.withholding_tax_ids.filtered(
            lambda withholding_tax: withholding_tax.install
        ).mapped('huroos_id')

        if huroos_id_to_create:
            self.env['withholding.tax'].search([]).unlink()

        withholding_taxes_to_create = list()

        for sheet in excel_file.sheets():
            last_huroos_id = False
            for row in range(sheet.nrows):
                if row == 0:
                    continue

                row_values = sheet.row_values(row)

                if row_values[0] != '':
                    last_huroos_id = str(int(row_values[0]))

                if row_values[0] and row_values[1]:
                    if str(int(row_values[0])) not in huroos_id_to_create:
                        continue
                    withholding_tax_vals = {
                        'name': row_values[1],
                        'code': row_values[2] if not str(row_values[2]).replace(".", "").isnumeric() else int(row_values[2]),
                        'account_receivable_id': self.withholding_credit_account_id.id,
                        'account_payable_id': self.withholding_debit_account_id.id,
                        'journal_id': self.withholding_journal_id.id,
                        'payment_term': self.withholding_payment_term_id.id,
                        'payment_reason_id': self.env.ref(f'l10n_it_payment_reason.{row_values[3].lower()}').id,
                        'wt_types': row_values[4],
                        'rate_ids': []
                    }
                    withholding_taxes_to_create.append(withholding_tax_vals)

                if row_values[5] != '' and row_values[6] != '' and last_huroos_id in huroos_id_to_create:
                    withholding_tax_vals['rate_ids'].append((0, 0, {'base': row_values[5], 'tax': row_values[6]}))

        for withholding_tax in withholding_taxes_to_create:
            if not withholding_tax['rate_ids']:
                withholding_tax.pop('rate_ids')

            self.env['withholding.tax'].create(withholding_tax)

        self.button_next()
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.setup.accounting",
            "target": "new",
            "res_id": self.id
        }

    def assign_account(self):
        ir_property = self.env['ir.property']

        # Se la company corrisponde alla main_company, creo proprietà azienda generali (senza company_id),
        # altrimenti creo delle proprietà specifiche per la company.
        # Ogni proprietà specifica deve avere sempre una controparte generale.
        company = self.env.company.id if self.env.company != self.env.ref('base.main_company') else False

        if self.a_partner_credit:
            fields = self.env['ir.model.fields'].search([('name', '=', 'property_account_receivable_id')])
            for f in fields:
                vals = {
                    'company_id': company,
                    'name': 'property_account_receivable_id',
                    'fields_id': f.id,
                    'type': 'many2one',
                    'value_reference': 'account.account,' + str(self.a_partner_credit.id)
                }
                receivable_propr_id = ir_property.search([
                    ('name', '=', 'property_account_receivable_id'),
                    ('fields_id', '=', f.id),
                    ('company_id', '=', company)
                ])
                if receivable_propr_id:
                    receivable_propr_id.write(vals)
                else:
                    ir_property.create(vals)

        if self.a_partner_debit:
            fields = self.env['ir.model.fields'].search([('name', '=', 'property_account_payable_id')])
            for f in fields:
                vals = {
                    'company_id': company,
                    'name': 'property_account_payable_id',
                    'fields_id': f.id,
                    'type': 'many2one',
                    'value_reference': 'account.account,' + str(self.a_partner_debit.id)
                }
                payable_propr_id = ir_property.search([
                    ('name', '=', 'property_account_payable_id'),
                    ('fields_id', '=', f.id),
                    ('company_id', '=', company)
                ])
                if payable_propr_id:
                    payable_propr_id.write(vals)
                else:
                    ir_property.create(vals)

        if self.a_product_income:
            fields = self.env['ir.model.fields'].search([('name', '=', 'property_account_income_categ_id')])
            for f in fields:
                vals = {
                    'company_id': company,
                    'name': 'property_account_income_categ_id',
                    'fields_id': f.id,
                    'type': 'many2one',
                    'value_reference': 'account.account,' + str(self.a_product_income.id)
                }
                income_categ_propr_id = ir_property.search([
                    ('name', '=', 'property_account_income_categ_id'),
                    ('fields_id', '=', f.id),
                    ('company_id', '=', company)
                ])
                if income_categ_propr_id:
                    income_categ_propr_id.write(vals)
                else:
                    ir_property.create(vals)

            journal_ids = self.env['account.journal'].search([('type', '=', 'sale')])
            for journal in journal_ids:
                journal.default_account_id = self.a_product_income.id

        if self.a_product_expense:
            fields = self.env['ir.model.fields'].search([('name', '=', 'property_account_expense_categ_id')])
            for f in fields:
                vals = {
                    'company_id': company,
                    'name': 'property_account_expense_categ_id',
                    'fields_id': f.id,
                    'type': 'many2one',
                    'value_reference': 'account.account,' + str(self.a_product_expense.id)
                }
                expense_categ_propr_id = ir_property.search([
                    ('name', '=', 'property_account_expense_categ_id'),
                    ('fields_id', '=', f.id),
                    ('company_id', '=', company)
                ])
                if expense_categ_propr_id:
                    expense_categ_propr_id.write(vals)
                else:
                    ir_property.create(vals)

            journal_ids = self.env['account.journal'].search([('type', '=', 'purchase')])
            for journal in journal_ids:
                journal.default_account_id = self.a_product_expense.id

        if self.a_suspense:
            self.env.company.account_journal_suspense_account_id = self.a_suspense.id
            fields = self.env['ir.model.fields'].search([('name', '=', 'suspense_account_id')])
            for f in fields:
                vals = {
                    'company_id': company,
                    'name': 'property_account_suspense_id',
                    'fields_id': f.id,
                    'type': 'many2one',
                    'value_reference': 'account.account,' + str(self.a_suspense.id)
                }
                suspense_propr_id = ir_property.search([
                    ('name', '=', 'property_account_suspense_id'),
                    ('fields_id', '=', f.id),
                    ('company_id', '=', company)
                ])
                if suspense_propr_id:
                    suspense_propr_id.write(vals)
                else:
                    ir_property.create(vals)

        if self.a_utili:
            fields = self.env['ir.model.fields'].search([('name', '=', 'profit_account_id')])
            for f in fields:
                vals = {
                    'company_id': company,
                    'name': 'property_account_profit_id',
                    'fields_id': f.id,
                    'type': 'many2one',
                    'value_reference': 'account.account,' + str(self.a_utili.id)
                }
                profit_propr_id = ir_property.search([
                    ('name', '=', 'property_account_profit_id'),
                    ('fields_id', '=', f.id),
                    ('company_id', '=', company)
                ])
                if profit_propr_id:
                    profit_propr_id.write(vals)
                else:
                    ir_property.create(vals)

        if self.a_perdite:
            fields = self.env['ir.model.fields'].search([('name', '=', 'loss_account_id')])
            for f in fields:
                vals = {
                    'company_id': company,
                    'name': 'property_account_loss_id',
                    'fields_id': f.id,
                    'type': 'many2one',
                    'value_reference': 'account.account,' + str(self.a_perdite.id)
                }
                loss_propr_id = ir_property.search([
                    ('name', '=', 'property_account_loss_id'),
                    ('fields_id', '=', f.id),
                    ('company_id', '=', company)
                ])
                if loss_propr_id:
                    loss_propr_id.write(vals)
                else:
                    ir_property.create(vals)

        if self.a_tax_credit:
            tax_ids = self.env['account.tax'].search([('type_tax_use', '=', 'purchase')])
            for tax in tax_ids:
                cont = 0
                for line in tax.invoice_repartition_line_ids:
                    if line.factor_percent and cont == 1:
                        line.account_id = self.a_tax_credit.id
                    cont += 1
                cont = 0
                for line in tax.refund_repartition_line_ids:
                    if line.factor_percent and cont == 1:
                        line.account_id = self.a_tax_credit.id
                    cont += 1
                tax.vat_statement_account_id = self.a_tax_credit.id

        if self.a_tax_debit:
            tax_ids = self.env['account.tax'].search([('type_tax_use', '=', 'sale')])
            for tax in tax_ids:
                cont = 0
                for line in tax.invoice_repartition_line_ids:
                    if line.factor_percent and cont == 1:
                        line.account_id = self.a_tax_debit.id
                    cont += 1
                cont = 0
                for line in tax.refund_repartition_line_ids:
                    if line.factor_percent and cont == 1:
                        line.account_id = self.a_tax_debit.id
                    cont += 1
                tax.vat_statement_account_id = self.a_tax_debit.id

        self.button_next()
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.setup.accounting",
            "target": "new",
            "res_id": self.id
        }

    def installa_moduli(self):
        ir_module = self.env['ir.module.module']

        # Disinstalla Modulo Base Odoo
        odoo_edi = ir_module.search([('name', '=', 'l10n_it_edi')])
        if odoo_edi:
            if odoo_edi.state == 'installed':
                odoo_edi.button_immediate_uninstall()

        # Contabilità Avanzata
        ir_module.search([('name', '=', 'account_accountant')]).button_immediate_install()

        # Installa Moduli
        if self.module_e_invoice_out:
            ir_module.search([('name', '=', 'l10n_it_fatturapa_out')]).button_immediate_install()
        if self.module_e_invoice_in:
            ir_module.search([('name', '=', 'l10n_it_fatturapa_in')]).button_immediate_install()
        if self.module_reverse_charge:
            ir_module.search([('name', '=', 'l10n_it_fatturapa_out_rc')]).button_immediate_install()
        if self.module_corrispettivi:
            ir_module.search([('name', '=', 'l10n_it_corrispettivi')]).button_immediate_install()
            ir_module.search([('name', '=', 'huroos_report_corrispettivi')]).button_immediate_install()
            ir_module.search([('name', '=', 'l10n_it_corrispettivi_fatturapa_out')]).button_immediate_install()
        if self.module_ddt:
            ir_module.search([('name', '=', 'l10n_it_delivery_note')]).button_immediate_install()
            ir_module.search([('name', '=', 'l10n_it_delivery_note_batch')]).button_immediate_install()
            ir_module.search([('name', '=', 'l10n_it_fatturapa_out_dn')]).button_immediate_install()
            ir_module.search([('name', '=', 'huroos_dn_invoice_group')]).button_immediate_install()
        if self.module_intrastat:
            ir_module.search([('name', '=', 'l10n_it_intrastat_statement')]).button_immediate_install()
            ir_module.search([('name', '=', 'l10n_it_intrastat')]).button_immediate_install()
        if self.module_riba:
            ir_module.search([('name', '=', 'l10n_it_ricevute_bancarie')]).button_immediate_install()
            ir_module.search([('name', '=', 'huroos_riba_unsolved')]).button_immediate_install()
            ir_module.search([('name', '=', 'huroos_riba_bank')]).button_immediate_install()
        if self.module_vat_registries:
            ir_module.search([('name', '=', 'l10n_it_vat_registries')]).button_immediate_install()
        if self.module_vat_statement:
            ir_module.search([('name', '=', 'account_vat_period_end_statement')]).button_immediate_install()
        if self.module_lipe:
            ir_module.search([('name', '=', 'l10n_it_vat_statement_communication')]).button_immediate_install()
        if self.module_withholding_tax:
            ir_module.search([('name', '=', 'l10n_it_withholding_tax')]).button_immediate_install()
            ir_module.search([('name', '=', 'l10n_it_withholding_tax_payment')]).button_immediate_install()
            ir_module.search([('name', '=', 'l10n_it_withholding_tax_reason')]).button_immediate_install()
            ir_module.search([('name', '=', 'huroos_payment_rda')]).button_immediate_install()
        if self.module_declaration_intent:
            ir_module.search([('name', '=', 'l10n_it_declaration_of_intent')]).button_immediate_install()
        if self.module_aruba:
            ir_module.search([('name', '=', 'huroos_aruba_fe')]).button_immediate_install()
        if self.module_competenza_iva:
            ir_module.search([('name', '=', 'huroos_data_iva')]).button_immediate_install()
        if self.module_massive_operations:
            ir_module.search([('name', '=', 'huroos_massive_operations')]).button_immediate_install()
        if self.module_template_registrazioni:
            ir_module.search([('name', '=', 'huroos_move_template')]).button_immediate_install()
        if self.module_split_payment:
            ir_module.search([('name', '=', 'l10n_it_split_payment')]).button_immediate_install()

        self.button_next()
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.setup.accounting",
            "target": "new",
            "res_id": self.id
        }

    def state_exit_step_5(self):
        # REVERSE CHARGE
        journal_ita_rc = self.env['account.journal'].search([('huroos_id', '=', '9')])
        journal_intra_rc = self.env['account.journal'].search([('huroos_id', '=', '10')])
        journal_extra_rc = self.env['account.journal'].search([('huroos_id', '=', '11')])
        journal_payment = self.env['account.journal'].search([('huroos_id', '=', '12')])
        transitory_account = self.env['account.account'].search([('code', '=', '99999999')])

        if journal_ita_rc:
            self.journal_ita_rc = journal_ita_rc.id
        if journal_payment:
            self.journal_payment = journal_payment.id
        if journal_intra_rc:
            self.journal_intra_rc = journal_intra_rc.id
        if journal_extra_rc:
            self.journal_extra_rc = journal_extra_rc.id
        if transitory_account:
            self.transitory_account = transitory_account.id

    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'step_7':
            self.state_exit_step_5()

        elif self.state == 'step_9':
            default_payment_term = self.env['account.payment.term'].search([('name', '=', '16 DEL MESE SUCCESSIVO')])
            if default_payment_term:
                self.withholding_payment_term_id = default_payment_term

    def create_month_ranges(self, year, date_range_type):
        for month in MONTHS:
            month_number = MONTHS.index(month) + 1
            last_day_in_month = calendar.monthrange(year, month_number)[1]
            date_range_vals = {
                'name': f'{month} {year}',
                'type_id': date_range_type.id,
                'date_start': f'{year}-{month_number}-01',
                'date_end': f'{year}-{month_number}-{last_day_in_month}'
            }
            exist = self.env['date.range'].search([('name', '=', date_range_vals['name'])])
            if not exist:
                self.env['date.range'].create(date_range_vals)

    def create_quarter_ranges(self, year, date_range_type):
        month_number = 1
        for i in range(1, 5):
            date_range_vals = {
                'name': f'Q{i} {year}',
                'type_id': date_range_type.id,
                'date_start': f'{year}-{month_number}-01',
                'date_end': f'{year}-{month_number + 2}-{calendar.monthrange(year, month_number + 2)[1]}'
            }
            exist = self.env['date.range'].search([('name', '=', date_range_vals['name'])])
            if not exist:
                self.env['date.range'].create(date_range_vals)
            month_number += 3

    def create_date_range(self):
        if self.years_to_cover > 10:
            raise UserError("Impossibile creare intervalli superiori a 10 anni.")

        if sum([self.create_months, self.create_quarters, self.create_years]) > 1:
            raise UserError("Puoi selezionare solo una delle opzioni, per evitare di sovrapporre i periodi fiscali.")

        account_fiscal_year_model = self.env['ir.module.module'].search([('name', '=', 'account_fiscal_year')])
        if not account_fiscal_year_model or account_fiscal_year_model.state != 'installed':
            raise UserError("Modulo account_fiscal_year mancante. Per procedere al setup "
                            "degli intervalli data installare prima il modulo.")

        date_range_type = self.env.ref('account_fiscal_year.fiscalyear')
        current_year = fields.Date.today().year
        for i in range(self.years_to_cover):
            if self.create_months:
                self.create_month_ranges(current_year + i, date_range_type)

            if self.create_quarters:
                self.create_quarter_ranges(current_year + i, date_range_type)

            if self.create_years:
                date_range_vals = {
                    'name': f'{current_year + i}',
                    'type_id': date_range_type.id,
                    'date_start': f'{current_year + i}-01-01',
                    'date_end': f'{current_year + i}-12-31'
                }
                exist = self.env['date.range'].search([('name', '=', date_range_vals['name'])])
                if not exist:
                    self.env['date.range'].create(date_range_vals)

        self.button_next()
        return {
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "wizard.setup.accounting",
            "target": "new",
            "res_id": self.id
        }


class SetupAccountTax(models.TransientModel):
    _name = 'setup.account.tax'

    name = fields.Char()
    install = fields.Boolean()
    huroos_id = fields.Char()
    wizard_id = fields.Many2one('wizard.setup.accounting')


class SetupAccountJournal(models.TransientModel):
    _name = 'setup.account.journal'

    name = fields.Char()
    install = fields.Boolean()
    huroos_id = fields.Char()
    wizard_id = fields.Many2one('wizard.setup.accounting')


class SetupAccountPaymentTerm(models.TransientModel):
    _name = "setup.account.payment.term"

    name = fields.Char()
    install = fields.Boolean()
    huroos_id = fields.Char()
    wizard_id = fields.Many2one('wizard.setup.accounting')


class SetupWithholdingTax(models.TransientModel):
    _name = "setup.withholding.tax"

    name = fields.Char()
    install = fields.Boolean()
    huroos_id = fields.Char()
    wizard_id = fields.Many2one('wizard.setup.accounting')
