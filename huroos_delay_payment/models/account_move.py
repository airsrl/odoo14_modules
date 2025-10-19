import datetime
from collections import OrderedDict
from odoo import models, fields,api,_
from odoo.tools import UserError, relativedelta, logging


class AccountMove(models.Model):
    _inherit = 'account.move'


    @api.depends('line_ids', 'invoice_payment_term_id', 'invoice_date', 'invoice_date_due', 'amount_tax',
                 'amount_untaxed')
    def _compute_payment_due_ids(self):
        """Calcolo delle scadenze pagamento della fattura"""

        for move in self:
            if not move.line_ids:
                move.payment_due_ids.unlink()
                continue

            move.payment_due_ids.unlink()
            payment_due_data = list()

            if move.invoice_payment_term_id:
                payment_terms = move.invoice_payment_term_id.compute(
                    value=move.amount_total,
                    date_ref=move.invoice_date,
                    currency=move.currency_id
                )
            else:
                if move.invoice_date_due:
                    payment_terms = [(move.invoice_date_due.strftime('%Y-%m-%d'), move.amount_total)]
                else:
                    payment_terms = []

            for term in payment_terms:

                amount = round(term[1], 2)

                move_line_id = False
                for line in move.line_ids:
                    if line.date_maturity == payment_terms[0] \
                            and float_compare(line.amount_currency, amount, precision_digits=2) \
                            and line.account_internal_type in ['debit', 'credit']:
                        move_line_id = line
                # Gestione scadenze posticipate
                data_scadenza = fields.Date.from_string(term[0])
                mese_scadenza = data_scadenza.month
                mesi_ritardo_scadenza = []
                if move.partner_id.months_due_date_delay:
                    for mese in move.partner_id.months_due_date_delay:
                        mesi_ritardo_scadenza.append(int(mese.code))
                    if mese_scadenza in mesi_ritardo_scadenza:
                        data_scadenza += relativedelta(days=move.partner_id.due_date_delay)
                else:
                    data_scadenza += relativedelta(days=move.partner_id.due_date_delay)
                due_vals = {
                    'move_id': move.id,
                    'amount': term[1],
                    'due_date': data_scadenza,
                    'fatturapa_payment_method_id': move.invoice_payment_term_id.fatturapa_pm_id.id,
                    'move_line_id': move_line_id.id if move_line_id else False
                }
                payment_due_data.append(due_vals)

            self.env['payment.due.item'].create(payment_due_data)