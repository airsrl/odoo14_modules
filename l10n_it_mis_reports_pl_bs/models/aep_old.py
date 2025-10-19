from odoo.addons.l10n_it_mis_reports_pl_bs.models.aep import AccountingExpressionProcessor as AEP
from odoo.addons.l10n_it_mis_reports_pl_bs.models.accounting_none import AccountingNone
from odoo.tools.float_utils import float_is_zero


class AccountingExpressionProcessor(AEP):
    def __init__(self, companies, currency=None, account_model="account.account"):
        super().__init__(companies, currency=None, account_model="account.account")

    def replace_exprs_by_account_id(self, exprs, show_void_moves):
        """Replace accounting variables in a list of expression
        by their amount, iterating by accounts involved in the expression.

        yields account_id, replaced_expr

        This method must be executed after do_queries().
        """

        def f(mo):
            field, mode, acc_domain, ml_domain = self._parse_match_object(mo)
            key = (ml_domain, mode)
            # first check if account_id is involved in
            # the current expression part
            if account_id not in self._account_ids_by_acc_domain[acc_domain]:
                return "(AccountingNone)"
            # here we know account_id is involved in acc_domain
            account_ids_data = self._data[key]
            debit, credit = account_ids_data.get(
                account_id, (AccountingNone, AccountingNone)
            )
            if field == "bal":
                v = debit - credit
            elif field == "pbal":
                if debit >= credit:
                    v = debit - credit
                else:
                    v = AccountingNone
            elif field == "nbal":
                if debit < credit:
                    v = debit - credit
                else:
                    v = AccountingNone
            elif field == "deb":
                v = debit
            elif field == "crd":
                v = credit
            # in initial balance mode, assume 0 is None
            # as it does not make sense to distinguish 0 from "no data"
            if (
                    v is not AccountingNone
                    and mode in (self.MODE_INITIAL, self.MODE_UNALLOCATED)
                    and float_is_zero(v, precision_digits=self.dp)
            ):
                v = AccountingNone
            return "(" + repr(v) + ")"

        account_ids = set()
        for expr in exprs:
            for mo in self._ACC_RE.finditer(expr):
                field, mode, acc_domain, ml_domain = self._parse_match_object(mo)
                if not show_void_moves:
                    key = (ml_domain, mode)
                    account_ids_data = self._data[key]
                for account_id in self._account_ids_by_acc_domain[acc_domain]:
                    if show_void_moves:
                        account_ids.add(account_id)
                    elif account_id in account_ids_data:
                        account_ids.add(account_id)

        for account_id in account_ids:
            yield account_id, [self._ACC_RE.sub(f, expr) for expr in exprs]
