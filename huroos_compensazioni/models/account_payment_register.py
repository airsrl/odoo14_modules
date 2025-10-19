from odoo import fields, models, api


class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    def _get_bill_ids_domain(self):
        if 'active_id' in self.env.context:
            invoice = self.env['account.move'].browse(self.env.context['active_id'])
            move_type = '-'  # Dummy value
            if invoice.move_type == 'in_invoice':
                move_type = 'out_invoice'
            if invoice.move_type == 'out_invoice':
                move_type = 'in_invoice'
            return f"[('partner_id', '=', partner_id), ('move_type', '=', '{move_type}'), ('payment_state', '=', 'not_paid'), ('state', '=', 'posted')]"
        else:
            return "[('partner_id', '=', partner_id), ('move_type', 'in', ['in_invoice', 'out_invoice']), ('payment_state', '=', 'not_paid'), ('state', '=', 'posted')]"

    bill_ids = fields.Many2many(
        comodel_name="account.move",
        string="Fatture passive",
        domain=_get_bill_ids_domain,
        copy=False
    )

    def _get_default_show_compensazione(self):
        if 'active_id' in self.env.context:
            invoice = self.env['account.move'].browse(self.env.context['active_id'])
            move_type = '-'  # Dummy value
            if invoice.move_type == 'in_invoice':
                move_type = 'out_invoice'
            if invoice.move_type == 'out_invoice':
                move_type = 'in_invoice'
            domain = [('partner_id', '=', invoice.partner_id.id), ('move_type', '=', f'{move_type}'), ('payment_state', '=', 'not_paid'), ('state', '=', 'posted')]
            invoices_compensazione = self.env['account.move'].search(domain)
            return invoices_compensazione and len(invoices_compensazione) > 0
        else:
            return False

    show_compensazione = fields.Boolean(
        default=_get_default_show_compensazione,
        string="Compensazione"
    )
    compensazione_journal_id = fields.Many2one(
        comodel_name="account.journal",
        string="Registro",
        default=lambda self: int(self.env['ir.config_parameter'].sudo().get_param('huroos_compensazioni.journal'))
    )
    debit_account_id = fields.Many2one(
        comodel_name="account.account",
        default=lambda self: int(self.env['ir.config_parameter'].sudo().get_param('huroos_compensazioni.debit_account'))
    )
    credit_account_id = fields.Many2one(
        comodel_name="account.account",
        default=lambda self: int(self.env['ir.config_parameter'].sudo().get_param('huroos_compensazioni.credit_account'))
    )
    importo_compensazione = fields.Float(
        compute='_get_importo_compensazione',
        readonly=True
    )
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        compute='_compute_currency_id'
    )
    account_bank_statement_id = fields.Many2one(
        comodel_name='account.bank.statement',
        domain="[('date','=',context_today().strftime('%Y-%m-%d')), ('state','=', 'open')]"
    )
    journal_type = fields.Selection(
        related='journal_id.type'
    )

    def _compute_currency_id(self):
        self.currency_id = self.env.company.currency_id

    @api.onchange('bill_ids')
    def _get_importo_compensazione(self):
        amount_total = self.bill_ids.mapped('amount_total')
        self.importo_compensazione = sum(amount_total)

    @api.onchange('payment_date')
    def _get_default_account_bank_id(self):
        # Cerco e imposto il registro contanti del giorno corrente (se presente)
        default_account_bank_id = self.env['account.bank.statement'].search([('date', '=', fields.datetime.utcnow().strftime('%Y-%m-%d'))], limit=1)
        if default_account_bank_id:
            self.account_bank_statement_id = default_account_bank_id.id

    @api.depends('importo_compensazione')
    def _compute_amount(self):
        super(AccountPaymentRegister, self)._compute_amount()
        self.amount -= self.importo_compensazione

    @api.depends('importo_compensazione')
    def _compute_payment_difference(self):
        super(AccountPaymentRegister, self)._compute_payment_difference()
        self.payment_difference -= self.importo_compensazione

    def _create_payments(self):

        res = super(AccountPaymentRegister, self)._create_payments()

        # Se si va in compensazione
        if self.show_compensazione and self.importo_compensazione > 0:
            invoice = self.env['account.move'].browse(self.env.context['active_id'])

            move_lines = list()
            for passive_invoice in self.bill_ids:
                passive_invoice_line = {
                    'partner_id': self.partner_id.id,
                    'name': f"Compensazione {passive_invoice.name}"
                }
                if invoice.move_type == 'out_invoice':
                    passive_invoice_line.update(
                        {
                            'account_id': self.credit_account_id.id,
                            'credit': passive_invoice.amount_total
                        }
                    )
                elif invoice.move_type == 'in_invoice':
                    passive_invoice_line.update(
                        {
                            'account_id': self.debit_account_id.id,
                            'debit': passive_invoice.amount_total
                        }
                    )

                move_lines.append((0, 0, passive_invoice_line))

            to_compensate_line = {
                'partner_id': self.partner_id.id,
                'name': f"Compensazione {invoice.name}"
            }
            if invoice.move_type == 'out_invoice':
                to_compensate_line.update(
                    {
                        'account_id': self.debit_account_id.id,
                        'debit': self.importo_compensazione
                    }
                )
            elif invoice.move_type == 'in_invoice':
                to_compensate_line.update(
                    {
                        'account_id': self.credit_account_id.id,
                        'credit': self.importo_compensazione
                    }
                )

            move_lines.append((0, 0, to_compensate_line))

            move_vals = {
                'ref': f"Compensazione {self.partner_id.name}",
                'date': fields.Date.today(),
                'journal_id': self.compensazione_journal_id.id,
                'move_type': 'entry',
                'line_ids': move_lines
            }

            compensazione = self.env['account.move'].sudo().with_context(default_move_type="entry").create(move_vals)
            compensazione.action_post()

            # Se pagamento cash creo la scrittura per registrare il pagamento (positivo o negativo in base al tipo fattura attiva/passiva)
            if self.journal_type == 'cash':
                if invoice.move_type == 'in_invoice':
                    cash_amount = self.amount * -1
                if invoice.move_type == 'out_invoice':
                    cash_amount = self.amount

                account_bank_statement_line_values = {
                    'date': fields.datetime.utcnow().strftime('%Y-%m-%d'),
                    'payment_ref': f'Cash {invoice.name}',
                    'partner_id': invoice.partner_id.id,
                    'amount': cash_amount
                }
                self.account_bank_statement_id.write({'line_ids': [(0, 0,  account_bank_statement_line_values)]})

            # Forzo la riconciliazione delle fatture con le registrazioni appena create
            if invoice.move_type == 'out_invoice':
                to_compensate_line_obj = self.env['account.move.line'].search([('move_id', '=', compensazione.id), ('credit', '=', 0)], limit=1)
                passive_invoice_line_ids = self.env['account.move.line'].search([('move_id', '=', compensazione.id), ('debit', '=', 0)])

            elif invoice.move_type == 'in_invoice':
                to_compensate_line_obj = self.env['account.move.line'].search([('move_id', '=', compensazione.id), ('debit', '=', 0)], limit=1)
                passive_invoice_line_ids = self.env['account.move.line'].search([('move_id', '=', compensazione.id), ('credit', '=', 0)])

            for passive_invoice in self.bill_ids:
                passive_invoice.js_assign_outstanding_line(to_compensate_line_obj.id)

            for line in passive_invoice_line_ids:
                invoice.js_assign_outstanding_line(line.id)

        return res
