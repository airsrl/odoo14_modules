
from odoo import models, fields, api, _

import re




class AccountChartOfAccountReport(models.AbstractModel):
    _inherit = "account.coa.report"


    filter_unreconciled = False
    filter_partially_reconciled = False


class ReportAccountFinancialReport(models.Model):
    _inherit = "account.financial.html.report"


    unreconciled= fields.Boolean('Non riconciliate')
    partially_reconciled = fields.Boolean('Parzialmente riconciliate')
class AccountReport(models.AbstractModel):
    _inherit = 'account.report'

    filter_unreconciled = None
    filter_partially_reconciled = None
    @api.model
    def _get_options_domain(self, options):
        domain=super(AccountReport,self)._get_options_domain(options)
        domain += self._get_options_unreconcile_domain(options)
        domain += self._get_options_partially_reconciled_domain(options)
        return domain


    def _get_options_unreconcile_domain(self,options):
        if not options.get('unreconciled'):
            return []
        else:
          return [ ('move_id.stored_has_reconciled_entries', '=', False)]
    def _get_options_partially_reconciled_domain(self,options):
        if not options.get('partially_reconciled'):
            return []
        else:
            return [('move_id.stored_has_reconciled_entries', '=', True)]

class AccountGeneralLedgerReport(models.AbstractModel):
    _inherit = "account.general.ledger"


    filter_unreconciled = False
    filter_partially_reconciled = False

class AccountMove(models.Model):
    _inherit='account.move'

    #stored field has_reconciled_entries
    stored_has_reconciled_entries = fields.Boolean(compute="_compute_stored_has_reconciled_entries",store=True)

    @api.depends('line_ids','line_ids.matched_debit_ids','line_ids.matched_credit_ids')
    def _compute_stored_has_reconciled_entries(self):
        for move in self:
            move.stored_has_reconciled_entries = len(move.line_ids._reconciled_lines()) > 1