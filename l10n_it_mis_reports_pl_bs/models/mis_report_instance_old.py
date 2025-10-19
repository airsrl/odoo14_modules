from odoo import models, fields, _
from odoo.exceptions import UserError
from .expression_evaluator import ExpressionEvaluator

class MisReportInstance(models.Model):

    _inherit = "mis.report.instance"
    _description = "MIS Report Instance"

    show_void_moves = fields.Boolean(default=True, string="Mostra anche i conti senza movimenti")

    def _add_column_move_lines(self, aep, kpi_matrix, period, label, description):
        if not period.date_from or not period.date_to:
            raise UserError(
                _("Column %s with move lines source must have from/to dates.")
                % (period.name,)
            )
        expression_evaluator = ExpressionEvaluator(
            aep,
            period.date_from,
            period.date_to,
            period._get_additional_move_line_filter(),
            period._get_aml_model_name(),
        )
        self.report_id._declare_and_compute_period(
            expression_evaluator,
            kpi_matrix,
            period.id,
            label,
            description,
            period.subkpi_ids,
            period._get_additional_query_filter,
            no_auto_expand_accounts=self.no_auto_expand_accounts,
            show_void_moves=self.show_void_moves,
        )
