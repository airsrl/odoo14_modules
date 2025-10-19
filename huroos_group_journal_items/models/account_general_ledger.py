from odoo import api, models


def get_amount_float(formatted_string, currency):
    # Esempio: formatted_string = '30,00 €'
    if formatted_string and isinstance(formatted_string, str) and currency in formatted_string:
        value = formatted_string.split(f'{currency}')[0]
        value = value.replace('.', '')
        value = value.replace(',', '.')
        try:
            return float(value)
        except ValueError:
            return 0

    elif isinstance(formatted_string, float) or isinstance(formatted_string, int):
        return formatted_string

    else:
        return 0


class AccountGeneralLedgerReport(models.AbstractModel):
    _inherit = "account.general.ledger"

    filter_group_journal_items = True

    def _group_lines(self, lines):
        currency_symbol = self.env.company.currency_id.symbol
        to_remove = list()
        current_line = dict()

        debit_index, credit_index, balance_index = 3, 4, 5
        # Se c'è il multi currency ci sarà una colonna in più, quindi incremento gli indici
        if self.user_has_groups('base.group_multi_currency'):
            debit_index, credit_index, balance_index = debit_index + 1, credit_index + 1, balance_index + 1

        for line in lines:
            if line.get('class') == 'o_account_reports_initial_balance':
                continue

            if line.get('parent_id') and line.get('caret_options') in ['account.move', 'account.payment']:
                # Inizializzo la riga se non esiste ancora
                if not current_line:
                    current_line = line

                    current_line_debit = get_amount_float(current_line['columns'][debit_index]['name'], currency_symbol)
                    current_line_credit = get_amount_float(current_line['columns'][credit_index]['name'], currency_symbol)
                    current_line['columns'][balance_index]['name'] = self.format_value( current_line_debit - current_line_credit)

                    # Inizializzo l'etichetta, che sarà tipo "NOME FATTURA-etichetta 1, etichetta 2..."
                    label = current_line['columns'][1]['name'].split('-')[-1]
                    current_line['columns'][1]['name'] = f"{current_line['name']}-{label}"
                    current_line['columns'][1]['title'] = label
                    continue

                # Se le righe hanno lo stesso nome, significa che provengono dalla stessa fattura, quindi le raggruppo
                if line.get('name') == current_line.get('name') and line['parent_id'] == current_line['parent_id']:

                    current_line_debit = get_amount_float(current_line['columns'][debit_index]['name'], currency_symbol)
                    current_line_credit = get_amount_float(current_line['columns'][credit_index]['name'],
                                                           currency_symbol)

                    line_debit = get_amount_float(line['columns'][debit_index]['name'], currency_symbol)
                    line_credit = get_amount_float(line['columns'][credit_index]['name'], currency_symbol)

                    # Aggiorno la riga principale sommando i valori dell'attuale riga
                    current_line['columns'][debit_index]['name'] = self.format_value(current_line_debit + line_debit)
                    current_line['columns'][credit_index]['name'] = self.format_value(current_line_credit + line_credit)
                    current_line['columns'][balance_index]['name'] = self.format_value(
                        (current_line_debit + line_debit) - (current_line_credit + line_credit)
                    )

                    # Aggiungo la l'etichetta se non è già presente
                    if line['columns'][1]['name'].split('-')[-1] not in current_line['columns'][1]['name']:
                        label += f", {line['columns'][1]['name'].split('-')[-1]}"
                        current_line['columns'][1]['name'] = f"{current_line['name']}-{label}"
                        current_line['columns'][1]['title'] = label

                    to_remove.append(line)

                else:
                    current_line = line

                    current_line_debit = get_amount_float(current_line['columns'][debit_index]['name'], currency_symbol)
                    current_line_credit = get_amount_float(current_line['columns'][credit_index]['name'], currency_symbol)
                    current_line['columns'][balance_index]['name'] = self.format_value(current_line_debit - current_line_credit)

                    # Inizializzo l'etichetta, che sarà tipo "NOME FATTURA-etichetta 1, etichetta 2..."
                    label = current_line['columns'][1]['name'].split('-')[-1]
                    current_line['columns'][1]['name'] = f"{current_line['name']}-{label}"
                    current_line['columns'][1]['title'] = label

        # Cancello le righe che ho sommato alla principale
        for line_to_remove in to_remove:
            lines.remove(line_to_remove)

    @api.model
    def _get_general_ledger_lines(self, options, line_id=None):
        lines = super(AccountGeneralLedgerReport, self)._get_general_ledger_lines(options, line_id=line_id)

        if options.get('group_journal_items'):
            self._group_lines(lines)

        return lines

    @api.model
    def _load_more_lines(self, options, line_id, offset, load_more_remaining, balance_progress):
        lines = super(AccountGeneralLedgerReport, self)._load_more_lines(options, line_id, offset, load_more_remaining, balance_progress)

        if options.get('group_journal_items'):
            self._group_lines(lines)

        return lines

