from odoo import api, fields, models

class GeneralLedgerReportWizard(models.TransientModel):
    _inherit = "general.ledger.report.wizard"

    group_journal_items = fields.Boolean(
        string="Raggruppa movimenti contabili",
        default=True
    )

    @api.model
    def _prepare_report_general_ledger(self):
        data = super(GeneralLedgerReportWizard, self)._prepare_report_general_ledger()

        data["group_journal_items"] = self.group_journal_items
        return data