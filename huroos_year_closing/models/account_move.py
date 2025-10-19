from odoo import fields, models
import json


class AccountMove(models.Model):
    _inherit = "account.move"

    remove_from_outstanding_credits_debits = fields.Boolean(
        string="Escludi da debiti/crediti in sospeso",
        help="Tutte le registrazioni selezionate saranno escluse dai debiti/crediti in sospeso proposti "
             "nelle scritture da riconciliare."
    )

    def _compute_payments_widget_to_reconcile_info(self):
        super(AccountMove, self)._compute_payments_widget_to_reconcile_info()
        # Dopo aver calcolato i debiti/crediti in sospeso nelle scritture, controllo che tra questi non
        # ci siano movimenti relativi a scritture con il flag 'remove_from_outstanding_credits_debits'
        # e in caso li rimuovo
        for move in self:
            outstanding_credits_debits_json = json.loads(move.invoice_outstanding_credits_debits_widget)

            if not outstanding_credits_debits_json:
                continue

            new_content = list()
            for outstanding_value in outstanding_credits_debits_json['content']:
                outstanding_move = self.browse(outstanding_value['move_id'])
                if not outstanding_move.remove_from_outstanding_credits_debits:
                    new_content.append(outstanding_value)

            if not new_content and move.invoice_has_outstanding:
                move.invoice_has_outstanding = False
                outstanding_credits_debits_json['title'] = ""

            outstanding_credits_debits_json['content'] = new_content
            move.invoice_outstanding_credits_debits_widget = json.dumps(outstanding_credits_debits_json)
