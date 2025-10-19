from odoo import models, fields, api,_
from odoo.exceptions import ValidationError


class AccountPayment(models.Model):
    _inherit = 'account.payment'


    @api.constrains('payment_method_id', 'journal_id')
    def _check_bank_account(self):
        """
        Ereditiamo questa funzione per rimuovere il controllo del BIC mancante.
        Precedentemente era obbligatorio
        """
        if self.payment_method_id == self.env.ref('account_sepa.account_payment_method_sepa_ct'):
            if not self.journal_id.bank_account_id or not self.journal_id.bank_account_id.acc_type == 'iban':
                raise ValidationError(_(
                    "The journal '%s' requires a proper IBAN account to pay via SEPA. Please configure it first.") % self.journal_id.name)
            if not self.journal_id.bank_account_id.bank_bic:
                return True
