from odoo import api, models
from odoo.tools.misc import formatLang


class AccountReconciliation(models.AbstractModel):
    _inherit = "account.reconciliation.widget"

    @api.model
    def _prepare_js_reconciliation_widget_move_line(self, statement_line, line, recs_count=0):
        js_vals = super(AccountReconciliation, self)._prepare_js_reconciliation_widget_move_line(statement_line, line, recs_count=recs_count)

        if line.move_id.withholding_tax_amount:
            amount_str = formatLang(self.env, abs(line.move_id.amount_net_pay), currency_obj=line.company_currency_id)
            js_vals['amount_str'] = amount_str
            js_vals['total_amount_str'] = amount_str

            if js_vals['credit'] != 0:
                js_vals['credit'] = line.move_id.amount_net_pay

            if js_vals['debit'] != 0:
                js_vals['debit'] = line.move_id.amount_net_pay

        return js_vals
