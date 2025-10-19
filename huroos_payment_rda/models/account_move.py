from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def js_assign_outstanding_line(self, line_id):
        """
        Override per gestire Note di Credito e RdA. Se non è presente NC funziona in modo std
        """
        self.ensure_one()
        lines = self.env['account.move.line'].browse(line_id)
        lines += self.line_ids.filtered(lambda line: line.account_id == lines[0].account_id and not line.reconciled)

        for invoice in lines.move_id:
            if invoice.move_type == 'in_refund':
                return lines.with_context(no_exchange_difference=True).reconcile()

        return lines.reconcile()

    @api.depends(
        "invoice_line_ids.price_subtotal",
        "withholding_tax_line_ids.tax",
        "amount_total"
    )
    def _compute_amount_withholding_tax(self):
        super(AccountMove, self)._compute_amount_withholding_tax()

        # Fix in caso il pagamento sia completamente estinto ma RdA va a negativo
        for invoice in self:
            if invoice.amount_residual == 0 and invoice.amount_net_pay_residual < 0:
                invoice.amount_net_pay_residual = 0

    def create_wt_statement(self):
        """
        Create one statement for each withholding tax
        """
        self.ensure_one()
        wt_statement_obj = self.env["withholding.tax.statement"]
        for inv_wt in self.withholding_tax_line_ids:
            wt_base_amount = inv_wt.base
            wt_tax_amount = inv_wt.tax
            if self.move_type in ["in_refund", "out_refund"]:
                wt_base_amount = -1 * wt_base_amount
                wt_tax_amount = -1 * wt_tax_amount
            val = {
                "wt_type": "",
                "date": self.date,
                "move_id": self.id,
                "invoice_id": self.id,
                "partner_id": self.partner_id.id,
                "withholding_tax_id": inv_wt.withholding_tax_id.id,
                "base": wt_base_amount,
                "tax": wt_tax_amount,
            }

            #FIX SE ANNULLI FATTURA DUPLICA STATEMENT RITENUTA
            already_exist = wt_statement_obj.search([('date', '=', self.date),('withholding_tax_id', '=', inv_wt.withholding_tax_id.id),
                                                     ('invoice_id', '=', self.id), ('partner_id', '=', self.partner_id.id),
                                                     ('base', '=', wt_base_amount), ('tax', '=', wt_tax_amount)], limit=1)
            if not already_exist:
                wt_statement_obj.create(val)
            else:
                already_exist.write(val)


class AccountPartialReconcile(models.Model):
    _inherit = "account.partial.reconcile"

    @api.model
    def generate_wt_moves(self):
        wt_statement_obj = self.env["withholding.tax.statement"]
        # Reconcile lines
        line_payment_ids = []
        line_payment_ids.append(self.debit_move_id.id)
        line_payment_ids.append(self.credit_move_id.id)
        domain = [("id", "in", line_payment_ids)]
        rec_line_model = self.env["account.move.line"]
        rec_lines = rec_line_model.search(domain)

        # Search statements of competence
        wt_statements = wt_statement_obj.browse()
        rec_line_statement = rec_line_model.browse()
        for rec_line in rec_lines:
            domain = [("move_id", "=", rec_line.move_id.id)]
            wt_statements = wt_statement_obj.search(domain)
            if wt_statements:
                rec_line_statement = rec_line
                break

        # In caso di RC non crea il wt_statement perchè viene sovrascritta la action_post()
        if not wt_statements:
            self.credit_move_id.move_id.create_wt_statement()
            for rec_line in rec_lines:
                domain = [("move_id", "=", rec_line.move_id.id)]
                wt_statements = wt_statement_obj.search(domain)
                if wt_statements:
                    rec_line_statement = rec_line
                    break

        # Search payment move
        rec_line_payment = rec_line_model.browse()
        for rec_line in rec_lines:
            if rec_line.id != rec_line_statement.id:
                rec_line_payment = rec_line
        # Generate wt moves
        wt_moves = []
        for wt_st in wt_statements:
            # Se l'importo dovuto della fattura è zero, non creo la ritenuta
            if wt_st.move_id.amount_residual == 0:
                continue

            # Fix in caso di Reverse Charge (prima controllo che il modulo sia installato)
            rc_module = self.env['ir.module.module'].search([('name', '=', 'l10n_it_reverse_charge')])
            if rc_module and rc_module.state == 'installed' \
                    and self.credit_move_id.move_id.rc_self_invoice_id \
                    and self.amount == self.credit_move_id.move_id.amount_tax:
                amount_wt = self.credit_move_id.move_id.withholding_tax_amount
            else:
                amount_wt = wt_st.get_wt_competence(self.amount)

            # Date maturity
            p_date_maturity = False
            payment_lines = wt_st.withholding_tax_id.payment_term.compute(
                amount_wt, rec_line_payment.date or False
            )
            if payment_lines and payment_lines[0]:
                p_date_maturity = payment_lines[0][0]
            wt_move_vals = {
                "statement_id": wt_st.id,
                "date": rec_line_payment.date,
                "partner_id": rec_line_statement.partner_id.id,
                "reconcile_partial_id": self.id,
                "payment_line_id": rec_line_payment.id,
                "credit_debit_line_id": rec_line_statement.id,
                "withholding_tax_id": wt_st.withholding_tax_id.id,
                "account_move_id": rec_line_payment.move_id.id or False,
                "date_maturity": p_date_maturity or rec_line_payment.date_maturity,
                "amount": amount_wt,
            }
            wt_move_vals = self._prepare_wt_move(wt_move_vals)

            wt_move = self.env["withholding.tax.move"].search([('statement_id', '=', wt_st.id),
                                                                     ('date', '=', rec_line_payment.date),
                                                                     ('partner_id', '=', rec_line_statement.partner_id.id),
                                                                     ('withholding_tax_id', '=', wt_st.withholding_tax_id.id),
                                                                     ('amount', '=', amount_wt)], limit=1)

            if not wt_move:
                wt_move = self.env["withholding.tax.move"].create(wt_move_vals)
            else:
                wt_move.write(wt_move_vals)

            wt_moves.append(wt_move)
            # Generate account move
            wt_move.generate_account_move()
        return wt_moves