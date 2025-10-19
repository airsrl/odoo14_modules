from odoo import models, _
from odoo.exceptions import ValidationError
import json


class WithholdingTax(models.Model):
    _inherit = 'withholding.tax.move'

    def generate_account_move(self):
        """
        Creation of account move to increase credit/debit vs tax authority
        """
        if self.wt_account_move_id:
            raise ValidationError(
                _("Warning! Wt account move already exists: %s")
                % (self.wt_account_move_id.name)
            )
        # Move - head
        move_vals = {
            "ref": _("WT %s - %s")
                   % (self.withholding_tax_id.code, self.credit_debit_line_id.move_id.name),
            "journal_id": self.withholding_tax_id.journal_id.id,
            "date": self.payment_line_id.move_id.date,
        }
        # Move - lines
        move_lines = []
        for _type in ("partner", "tax"):
            ml_vals = {
                "ref": _("WT %s - %s - %s")
                       % (
                           self.withholding_tax_id.code,
                           self.partner_id.name,
                           self.credit_debit_line_id.move_id.name,
                       ),
                "name": "%s" % (self.credit_debit_line_id.move_id.name),
                "date": move_vals["date"],
            }
            # Credit/Debit line
            if _type == "partner":
                ml_vals["partner_id"] = self.payment_line_id.partner_id.id
                ml_vals["account_id"] = self.credit_debit_line_id.account_id.id
                ml_vals[
                    "withholding_tax_generated_by_move_id"
                ] = self.payment_line_id.move_id.id
                if self.payment_line_id.credit:
                    ml_vals["credit"] = abs(self.amount)
                else:
                    ml_vals["debit"] = abs(self.amount)
            # Authority tax line
            elif _type == "tax":
                ml_vals["name"] = "{} - {}".format(
                    self.withholding_tax_id.code,
                    self.credit_debit_line_id.move_id.name,
                )
                if self.payment_line_id.credit:
                    ml_vals["debit"] = abs(self.amount)
                    if self.credit_debit_line_id.move_id.move_type in [
                        "in_refund",
                        "out_refund",
                    ]:
                        ml_vals[
                            "account_id"
                        ] = self.withholding_tax_id.account_payable_id.id
                    else:
                        ml_vals[
                            "account_id"
                        ] = self.withholding_tax_id.account_receivable_id.id
                else:
                    ml_vals["credit"] = abs(self.amount)
                    if self.credit_debit_line_id.move_id.move_type in [
                        "in_refund",
                        "out_refund",
                    ]:
                        ml_vals[
                            "account_id"
                        ] = self.withholding_tax_id.account_receivable_id.id
                    else:
                        ml_vals[
                            "account_id"
                        ] = self.withholding_tax_id.account_payable_id.id
            # self.env['account.move.line'].create(move_vals)
            move_lines.append((0, 0, ml_vals))

        move_vals["line_ids"] = move_lines

        # Bugfix. Quando si annulla una fattura già precedente validata e pagata il sistema duplica la ritenuta d'acconto
        # Bisogna quindi prima verificare se è già presente una ritenuta. Se è presente utilizza questa altrimenti ne crea una nuova
        exist_rda_id = self.env['account.move'].search(
            [('ref', '=', move_vals['ref']), ('date', '=', move_vals['date'])])
        rda_id = False
        for rda in exist_rda_id:
            for line in rda.line_ids:
                if line.debit == move_vals['line_ids'][0][2].get('debit') and line.reconciled:
                    rda_id = rda
        if rda_id:
            move = rda_id
        else:
            move = (
                self.env["account.move"]
                .with_context(default_move_type="entry")
                .create(move_vals)
            )
        if move.state != 'posted':
            move.action_post()

        # Save move in the wt move
        self.wt_account_move_id = move.id

        # Find lines for reconcile
        line_to_reconcile = False
        for line in move.line_ids:
            if (
                    line.account_id.user_type_id.type in ["payable", "receivable"]
                    and line.partner_id
            ):
                line_to_reconcile = line
                break

        #Aggiunta FIX solo se non esiste RDA
        if line_to_reconcile and not rda_id:
            if self.credit_debit_line_id.move_id.move_type in [
                "in_refund",
                "out_invoice",
            ]:
                debit_move_id = self.credit_debit_line_id.id
                credit_move_id = line_to_reconcile.id
            else:
                debit_move_id = line_to_reconcile.id
                credit_move_id = self.credit_debit_line_id.id

            partial_reconcile_vals = {
                    "debit_move_id": debit_move_id,
                    "credit_move_id": credit_move_id,
                    "amount": abs(self.amount),
                    "credit_amount_currency": abs(self.amount),
                    "debit_amount_currency": abs(self.amount),
                }
            self.env["account.partial.reconcile"].with_context(no_generate_wt_move=True).create(partial_reconcile_vals)

            # Se sto riconciliando con Nota di Credito
            if self.credit_debit_line_id.move_id.move_type in ["in_refund", "out_invoice"] \
                    and partial_reconcile_vals['amount'] == self.payment_line_id.move_id.withholding_tax_amount \
                    and self.payment_line_id.move_id.amount_residual == 0:
                self.fix_in_refund(self.credit_debit_line_id.move_id, self.payment_line_id.move_id)

    def fix_in_refund(self, in_refund_id, move_id):
        if not in_refund_id.invoice_payments_widget:
            return False

        reconciled_vals = json.loads(in_refund_id.invoice_payments_widget).get('content', False)
        if not reconciled_vals:
            return False

        partial_id = int()
        for rec in reconciled_vals:
            if rec['name'] == in_refund_id.name and rec['amount'] == in_refund_id.withholding_tax_amount:
                partial_id = rec['partial_id']
                journal_entry_id = rec['move_id']

        if partial_id:
            in_refund_id.js_remove_outstanding_partial(partial_id)
            # Elimino le dichiarazioni RdA
            self.env['withholding.tax.statement'].search([('invoice_id', 'in', [move_id.id, in_refund_id.id])]).unlink()
            # Elimino movimento RdA
            wt_tax_move = self.env['withholding.tax.move'].search([('account_move_id', '=', move_id.id)])
            wt_account_move_id = wt_tax_move.wt_account_move_id
            wt_tax_move.unlink()
            # Elimino movimento di pagamento RdA
            wt_account_move_id.with_context(force_delete=True).unlink()
