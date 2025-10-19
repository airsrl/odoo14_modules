from odoo import models, fields, api


class AccountReconciliationWidget(models.AbstractModel):
    _inherit = 'account.reconciliation.widget'

    @api.model
    def _get_query_reconciliation_widget_receivable_payable_lines(self, statement_line, domain=[]):
        r = super(AccountReconciliationWidget, self)._get_query_reconciliation_widget_receivable_payable_lines(statement_line, domain=domain)
        domain = domain + [
            ('account_id.internal_type', 'in', ('receivable', 'payable')),
            '|', ('reconciled', '=', False), ('payment_id', '=', False),
        ]
        tables, where_clause, where_params = self._prepare_reconciliation_widget_query(statement_line, domain=domain)

        query = '''
            SELECT ''' + self._get_query_select_clause() + '''
            FROM ''' + tables + '''
            WHERE ''' + where_clause + '''
        '''
        return query, where_params

