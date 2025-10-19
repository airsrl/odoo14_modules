from odoo.addons.l10n_it_mis_reports_pl_bs.models.mis_safe_eval import NameDataError, mis_safe_eval
from odoo.addons.l10n_it_mis_reports_pl_bs.models.expression_evaluator import ExpressionEvaluator as EE


class ExpressionEvaluator(EE):
    def __init__(
        self,
        aep,
        date_from,
        date_to,
        additional_move_line_filter=None,
        aml_model=None,
    ):
        super().__init__(
            aep,
            date_from,
            date_to,
            additional_move_line_filter,
            aml_model,
        )

    def eval_expressions_by_account(self, expressions, locals_dict, show_void_moves):
        if not self.aep:
            return
        exprs = [e and e.name or "AccountingNone" for e in expressions]
        for account_id, replaced_exprs in self.aep.replace_exprs_by_account_id(exprs, show_void_moves):
            vals = []
            drilldown_args = []
            name_error = False
            for expr, replaced_expr in zip(exprs, replaced_exprs):
                val = mis_safe_eval(replaced_expr, locals_dict)
                vals.append(val)
                if replaced_expr != expr:
                    drilldown_args.append({"expr": expr, "account_id": account_id})
                else:
                    drilldown_args.append(None)
            yield account_id, vals, drilldown_args, name_error
