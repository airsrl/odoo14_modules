# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).
import datetime
from odoo import api, fields, models


class ImportCorrispettivi(models.Model):
    _name = "import.corrispettivi"


    from_date = fields.Date()
    to_date = fields.Date()
    journal_id = fields.Many2one('account.journal')
    currency_id = fields.Many2one('res.currency')
    tax_id = fields.Many2one('account.tax')
    income_account_id = fields.Many2one('account.account')
    credit_account_id = fields.Many2one('account.account')
    liquidity_journal_id = fields.Many2one('account.journal')
    line_ids = fields.One2many('corrispettivi.line', 'import_corr_id')
    state = fields.Selection([('draft', 'BOZZA'),  ('post', 'REGISTRATI')])
    move_ids = fields.Many2many('account.move')


    @api.onchange('from_date', 'to_date')
    def onchange_date(self):
        if self.from_date and self.to_date:
            self.line_ids = False
            values = []
            range_dates = [self.from_date + datetime.timedelta(days=x) for x in range(0, (self.to_date-self.from_date).days + 1)]
            for dt in range_dates:
                values.append((0,0, {
                    'day': int(dt.strftime('%d')),
                    'day_name': dt.strftime('%A'),
                    'date': dt
                }))
            self.line_ids = values


    def post(self):

        moves = []
        for line in self.line_ids:
            if line.amount != 0:
                res = self.tax_id.compute_all(line.amount, self.currency_id, 1)
                income = res['total_excluded']
                tax = round(line.amount - res['total_excluded'], 2)
                account_tax = False
                for tax_line in self.tax_id.invoice_repartition_line_ids:
                    if tax_line.account_id:
                        account_tax = tax_line.account_id

                move_vals = {
                    'partner_id': self.env.ref('base.public_partner').id,
                    'payment_reference': "Corrispettivi del " + line.date.strftime('%d-%m-%Y'),
                    'journal_id': self.journal_id.id,
                    'corrispettivo': True,
                    'move_type': 'out_invoice',
                    'invoice_date': line.date,
                    'invoice_line_ids': [
                        (0, 0, {
                            'account_id': self.income_account_id.id,
                            'price_unit': line.amount,
                            'quantity': 1,
                            'currency_id': self.currency_id.id,
                            'tax_ids': [(4, self.tax_id.id)],
                            'name': "Corrispettivi del " + line.date.strftime('%d-%m-%Y'),
                        }),
                    ]
                }


                move_id = self.env['account.move'].create(move_vals)
                move_id.action_post()
                moves.append(move_id.id)

                #Registra Pagamento
                payment = self.env['account.payment'].create({
                    'amount': line.amount,
                    'ref': "Pagamento Corrispettivo " + move_id.name,
                    'journal_id': self.liquidity_journal_id.id,
                    'partner_id': move_id.partner_id.id,
                    'date': line.date,
                })
                payment.action_post()
                domain = [('account_internal_type', 'in', ('receivable', 'payable')), ('reconciled', '=', False)]
                payment_move_line = payment.move_id.line_ids.filtered_domain(domain)
                invoice_move_line = move_id.line_ids.filtered_domain(domain)
                for account in payment_move_line.account_id:
                    payment.is_reconciled = True
                    payment.is_matched = True
                    (payment_move_line + invoice_move_line).filtered_domain([('account_id', '=', account.id), ('reconciled', '=', False)]).reconcile()
                    print("Riconciliato")

        self.move_ids = moves
        self.state = 'post'

    def cancel(self):
        for move in self.move_ids:
            move.with_context(force_delete=True).force_delete_invoice_and_related_payment()
        self.state = 'draft'




