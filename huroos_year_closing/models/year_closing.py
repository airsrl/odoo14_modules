from odoo import fields, models
from odoo.exceptions import ValidationError
from datetime import timedelta

TODAY = fields.date.today()


class YearClosing(models.Model):
    _name = 'year.closing'
    _description = 'Chiusura Anno Fiscale'

    name = fields.Char(
        string="Periodo"
    )
    date_from = fields.Date(
        string="Da",
        default=fields.date(TODAY.year, 1, 1),
        required=True
    )
    date_to = fields.Date(
        string="A",
        default=fields.date(TODAY.year, 12, 31),
        required=True
    )
    profit_loss_account_id = fields.Many2one(
        comodel_name='account.account',
        string="Conto Profitti e Perdite",
        required=True
    )
    sp_opening_closing_account_id = fields.Many2one(
        comodel_name='account.account',
        string="Conto Chiusura e Apertura SP",
        required=True
    )
    ce_account_ids = fields.Many2many(
        comodel_name='year.closing.line',
        relation='ce_account_closing_line_rel',
        copy=False
    )
    sp_account_ids = fields.Many2many(
        comodel_name='year.closing.line',
        relation='sp_account_closing_line_rel',
        copy=False
    )
    journal_closing = fields.Many2one(
        comodel_name='account.journal',
        string="Registro Chiusura",
        required=True
    )
    journal_opening = fields.Many2one(
        comodel_name='account.journal',
        string="Registro Apertura",
        required=True
    )
    move_year_ids = fields.Many2many(
        comodel_name='account.move'
    )
    profit_loss_amount = fields.Float(
        string="Utile/Perdita Rilevata",
        readonly=True
    )
    analytic_account_id = fields.Many2one(
        comodel_name='account.analytic.account',
        string="Conto Analitico"
    )
    can_generate_closing = fields.Boolean(
        help="Flag tecnico per nascondere il bottone di chiusura dell'anno fiscale finchè non si sono calcolati i conti"
    )
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Azienda",
        default=lambda self: self.env.company
    )

    def generate_closing(self):
        # Categorie dei conti
        credito = self.env.ref('account.data_account_type_receivable').id
        debito = self.env.ref('account.data_account_type_payable').id

        if self.move_year_ids:
            if any(move.state == 'posted' for move in self.move_year_ids):
                raise ValidationError("Sono già presenti delle scritture confermate. Per procedere assicurarsi "
                                      "che tutte le scritture siano in stato bozza.")
            else:
                self.move_year_ids.unlink()

        move_ids = list()

        # 1. Chisura Conto Economico
        move_ce_closing = {
            'date': self.date_to,
            'journal_id': self.journal_closing.id,
            'ref': 'Chiusura Conto Economico',
            'remove_from_outstanding_credits_debits': True,
            'line_ids': []
        }

        total_balance_costi = 0
        total_balance_ricavi = 0

        account_excluded = self.sp_opening_closing_account_id + self.profit_loss_account_id

        for account in self.ce_account_ids.macro_account_id:

            move_line_ids = self.env['account.move.line'].search([
                ('account_id', 'not in', account_excluded.ids),
                ('parent_state', '=', 'posted'),
                ('account_id', '=', account.id),
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to)
            ])

            balance = sum(line.balance for line in move_line_ids)

            # COSTI
            if account.user_type_id.internal_group == "expense":
                total_balance_costi += balance
                # Aggiunta Riga account.move.line
                line_vals = {
                    'account_id': account.id,
                    'analytic_account_id': self.analytic_account_id.id if self.analytic_account_id else False,
                    'debit': abs(balance) if balance < 0 else 0,  # Se credito mette in debito
                    'credit': abs(balance) if balance > 0 else 0  # Se debito mette in credito
                }
                move_ce_closing['line_ids'].append((0, 0, line_vals))

            # RICAVI
            elif account.user_type_id.internal_group == "income":
                total_balance_ricavi += balance
                # Aggiunta Riga account.move.line
                line_vals = {
                    'account_id': account.id,
                    'analytic_account_id': self.analytic_account_id.id if self.analytic_account_id else False,
                    'debit': abs(balance) if balance < 0 else 0,  # Se credito mette in debito
                    'credit': abs(balance) if balance > 0 else 0  # Se debito mette in credito
                }
                move_ce_closing['line_ids'].append((0, 0, line_vals))

        profit_loss_costi_value = total_balance_costi
        profit_loss_ricavi_value = total_balance_ricavi

        # Contropartita Finale
        differenza = abs(profit_loss_ricavi_value) - abs(profit_loss_costi_value)
        move_ce_closing['line_ids'].append((0, 0, {
            'account_id': self.profit_loss_account_id.id,
            'debit': abs(differenza) if differenza < 0 else 0,  # Se debito mette in credito
            'credit': abs(differenza) if differenza > 0 else 0  # Se credito mette in debito
        }))

        self.profit_loss_amount = - differenza
        move_ce_closing_id = self.env['account.move'].create(move_ce_closing)
        move_ids.append(move_ce_closing_id.id)

        # Chiusura/Apertura Stato Patrimoniale
        move_sp_closing = {
            'date': self.date_to,
            'journal_id': self.journal_closing.id,
            'ref': 'Chiusura Stato Patrimoniale',
            'remove_from_outstanding_credits_debits': True,
            'line_ids': []
        }
        move_sp_opening = {
            'date': self.date_to + timedelta(days=1),
            'journal_id': self.journal_opening.id,
            'ref': 'Apertura Stato Patrimoniale',
            'remove_from_outstanding_credits_debits': True,
            'line_ids': []
        }
        sp_datas = {
            'general_account': {},
            'partners': {}
        }

        for account in self.sp_account_ids.macro_account_id:
            move_line_ids = self.env['account.move.line'].search([
                ('account_id', 'not in', account_excluded.ids),
                ('parent_state', '=', 'posted'),
                ('account_id', '=', account.id),
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to)
            ])

            for line in move_line_ids:
                if account.user_type_id.id == credito or account.user_type_id.id == debito:
                    # Se conto Debito o Credito è un conto Partner
                    if line.partner_id:
                        # La chiave è data dal ID conto + ID partner,
                        # perchè potrebbero esserci partner che sono sia fornitori che clienti
                        key_partner = str(account.id) + str(line.partner_id.id)
                        if key_partner not in sp_datas['partners']:
                            sp_datas['partners'][key_partner] = {
                                'account_id': account.id,
                                'balance': line.balance,
                                'partner_id': line.partner_id.id
                            }
                        else:
                            sp_datas['partners'][key_partner]['balance'] += line.balance

                    else:
                        # Valore generico di debito o credito
                        if account.id not in sp_datas['general_account']:
                            sp_datas['general_account'][account.id] = {
                                'account_id': account.id,
                                'balance': line.balance,
                            }
                        else:
                            sp_datas['general_account'][account.id]['balance'] += line.balance

                else:
                    # Conto generico di stato patrimoniale
                    if account.id not in sp_datas['general_account']:
                        sp_datas['general_account'][account.id] = {
                            'account_id': account.id,
                            'balance': line.balance,
                        }
                    else:
                        sp_datas['general_account'][account.id]['balance'] += line.balance

        final_balance = 0
        # Chiusura Stato Patrimoniale Partner
        for key, partner_data in sp_datas['partners'].items():
            account_id = partner_data['account_id']
            balance = partner_data['balance']
            if round(balance, 2) != 0:
                partner_id = partner_data['partner_id']
                final_balance += balance
                move_sp_closing['line_ids'].append((0, 0, {
                    'account_id': account_id,
                    'partner_id': partner_id,
                    'analytic_account_id': self.analytic_account_id.id if self.analytic_account_id else False,
                    'debit': abs(balance) if balance < 0 else 0,  # Se credito mette in debito
                    'credit': abs(balance) if balance > 0 else 0  # Se debito mette in credito
                }))
        # Chiusura Stato Patrimoniale General Account
        for key, general_data in sp_datas['general_account'].items():
            account_id = general_data['account_id']
            balance = general_data['balance']
            final_balance += balance
            move_sp_closing['line_ids'].append((0, 0, {
                'account_id': account_id,
                'analytic_account_id': self.analytic_account_id.id if self.analytic_account_id else False,
                'debit': abs(balance) if balance < 0 else 0,  # Se credito mette in debito
                'credit': abs(balance) if balance > 0 else 0  # Se debito mette in credito
            }))

        # Contropartita Finale Chiusura Stato Patrimoniale
        move_sp_closing['line_ids'].append((0, 0, {
            'account_id': self.sp_opening_closing_account_id.id,
            'analytic_account_id': self.analytic_account_id.id if self.analytic_account_id else False,
            'debit': abs(final_balance) if final_balance > 0 else 0,  # Se credito mette in debito
            'credit': abs(final_balance) if final_balance < 0 else 0  # Se debito mette in credito
        }))

        move_sp_closing_id = self.env['account.move'].create(move_sp_closing)
        move_ids.append(move_sp_closing_id.id)

        final_balance = 0
        # Apertura Stato Patrimoniale Partner
        for key, partner_data in sp_datas['partners'].items():
            account_id = partner_data['account_id']
            balance = partner_data['balance']
            if round(balance, 2) != 0:
                partner_id = partner_data['partner_id']
                final_balance += balance
                move_sp_opening['line_ids'].append((0, 0, {
                    'account_id': account_id,
                    'partner_id': partner_id,
                    'debit': abs(balance) if balance > 0 else 0,  # Se credito mette in debito
                    'credit': abs(balance) if balance < 0 else 0  # Se debito mette in credito
                }))
        # Apertura Stato Patrimoniale General Account
        for key, general_data in sp_datas['general_account'].items():
            account_id = general_data['account_id']
            balance = general_data['balance']
            final_balance += balance
            move_sp_opening['line_ids'].append((0, 0, {
                'account_id': account_id,
                'debit': abs(balance) if balance > 0 else 0,  # Se credito mette in debito
                'credit': abs(balance) if balance < 0 else 0  # Se debito mette in credito
            }))

        # Contropartita Finale Apertura Stato Patrimoniale
        move_sp_opening['line_ids'].append((0, 0, {
            'account_id': self.sp_opening_closing_account_id.id,
            'debit': abs(final_balance) if final_balance < 0 else 0,  # Se credito mette in debito
            'credit': abs(final_balance) if final_balance > 0 else 0  # Se debito mette in credito
        }))

        move_sp_opening_id = self.env['account.move'].create(move_sp_opening)
        move_ids.append(move_sp_opening_id.id)
        self.move_year_ids = move_ids

    def get_grouped_accounts_data(self, account_ids, account_excluded=None):
        data = [(5,)]
        for account in account_ids:
            debit = 0
            credit = 0
            balance = 0
            table_html = '<table><th>CONTO</th><th>SALDO</th>'

            move_line_ids = self.env['account.move.line'].search([
                ('account_id', 'not in', account_excluded.ids),
                ('parent_state', '=', 'posted'),
                ('account_id', '=', account.id),
                ('date', '>=', self.date_from),
                ('date', '<=', self.date_to)
            ])

            for line in move_line_ids:
                debit += line.debit
                credit += line.credit
                balance += line.balance

            if not debit and not credit:
                # Non inserisco il conto nel bilancio se sia credito che debito sono a zero
                continue

            if move_line_ids:
                table_html += '<tr><td>' + account.name + '</td><td>' + str(round(debit - credit, 2)) + '</td></tr>'

            table_html += '</table>'

            vals = {
                'macro_account_id': account.id,
                'debit': debit,
                'credit': credit,
                'balance': balance,
                'account_balance_html': table_html
            }
            data.append((0, 0, vals))

        return data

    def compute_closing(self):
        account_excluded = self.sp_opening_closing_account_id + self.profit_loss_account_id

        # Macro Conto Economico
        account_ids = self.env['account.account'].search([('user_type_id.internal_group', 'in', ('expense', 'income'))])
        self.ce_account_ids = self.get_grouped_accounts_data(account_ids, account_excluded)

        # Macro Stato Patrimoniale
        account_ids = self.env['account.account'].search(
            [('user_type_id.internal_group', 'in', ('asset', 'liability', 'equity'))])
        self.sp_account_ids = self.get_grouped_accounts_data(account_ids, account_excluded)

        # Abilito il bottone di chiusura dell'anno fiscale
        self.can_generate_closing = True


class YearClosingLine(models.Model):
    _name = 'year.closing.line'

    macro_account_id = fields.Many2one(
        comodel_name='account.account',
        string="Conto",
        required=True
    )
    debit = fields.Float(
        string="Dare"
    )
    credit = fields.Float(
        string="Avere"
    )
    balance = fields.Float(
        string="Saldo"
    )
    account_ids = fields.Many2many('account.account', 'year_closing_line_account')
    account_balance_html = fields.Html()
