from odoo import _, models, fields
from .expression_evaluator import ExpressionEvaluator as EE
from .aep import AccountingExpressionProcessor as AEP
from odoo.addons.l10n_it_mis_reports_pl_bs.models.mis_report import AutoStruct, SubKPITupleLengthError, SubKPIUnknownTypeError
from odoo.addons.l10n_it_mis_reports_pl_bs.models.mis_safe_eval import DataError
from odoo.addons.l10n_it_mis_reports_pl_bs.models.accounting_none import AccountingNone
from odoo.addons.l10n_it_mis_reports_pl_bs.models.simple_array import SimpleArray, named_simple_array


class MisReport(models.Model):
    _inherit = "mis.report"

    def _get_net_income(self, expression_evaluator, subkpis, locals_dict, col_key, SimpleArray_cls):
        recompute_queue = []
        mis_report = self.env.ref('l10n_it_mis_reports_pl_bs.mis_report_pl')
        aep = mis_report._prepare_aep(self.env.companies, currency=None)
        compute_queue = mis_report.kpi_ids
        expression_evaluator2 = EE(
            aep,
            expression_evaluator.date_from,
            expression_evaluator.date_to,
            expression_evaluator.additional_move_line_filter,
            expression_evaluator.aml_model,
        )
        expression_evaluator2.aep_do_queries()
        for kpi in compute_queue:
            # build the list of expressions for this kpi

            expressions = kpi._get_expressions(subkpis)

            (
                vals,
                drilldown_args,
                name_error,
            ) = expression_evaluator2.eval_expressions(expressions, locals_dict)
            for drilldown_arg in drilldown_args:
                if not drilldown_arg:
                    continue
                drilldown_arg["period_id"] = col_key
                drilldown_arg["kpi_id"] = kpi.id

            if name_error:
                recompute_queue.append(kpi)
            else:
                # no error, set it in locals_dict so it can be used
                # in computing other kpis
                if not subkpis or not kpi.multi:
                    locals_dict[kpi.name] = vals[0]
                else:
                    locals_dict[kpi.name] = SimpleArray_cls(vals)
        return vals[0] if isinstance(vals[0], float) else 0

    def _prepare_aep(self, companies, currency=None):
        self.ensure_one()
        aep = AEP(companies, currency, self.account_model)
        for kpi in self.all_kpi_ids:
            for expression in kpi.expression_ids:
                if expression.name:
                    aep.parse_expr(expression.name)
        aep.done_parsing()
        return aep

    def _declare_and_compute_col(  # noqa: C901 (TODO simplify this fnction)
        self,
        expression_evaluator,
        kpi_matrix,
        col_key,
        col_label,
        col_description,
        subkpis_filter,
        locals_dict,
        no_auto_expand_accounts=False,
        show_void_moves=True,
    ):
        """This is the main computation loop.

        It evaluates the kpis and puts the results in the KpiMatrix.
        Evaluation is done through the expression_evaluator so data sources
        can provide their own mean of obtaining the data (eg preset
        kpi values for budget, or alternative move line sources).
        """

        if subkpis_filter:
            # TODO filter by subkpi names
            subkpis = [subkpi for subkpi in self.subkpi_ids if subkpi in subkpis_filter]
        else:
            subkpis = self.subkpi_ids

        SimpleArray_cls = named_simple_array(
            "SimpleArray_{}".format(col_key), [subkpi.name for subkpi in subkpis]
        )
        locals_dict["SimpleArray"] = SimpleArray_cls

        col = kpi_matrix.declare_col(
            col_key, col_label, col_description, locals_dict, subkpis
        )

        compute_queue = self.kpi_ids
        recompute_queue = []
        while True:
            if self.id == self.env.ref('l10n_it_mis_reports_pl_bs.mis_report_bs').id:
                # Search for the Net Income of the EEC Financial Statements - Profit and Loss
                net_income = self._get_net_income(expression_evaluator, subkpis, locals_dict, col_key, SimpleArray_cls)

            for kpi in compute_queue:
                # build the list of expressions for this kpi
                expressions = kpi._get_expressions(subkpis)

                (
                    vals,
                    drilldown_args,
                    name_error,
                ) = expression_evaluator.eval_expressions(expressions, locals_dict)
                for drilldown_arg in drilldown_args:
                    if not drilldown_arg:
                        continue
                    drilldown_arg["period_id"] = col_key
                    drilldown_arg["kpi_id"] = kpi.id

                # Calculate "current_earnings - net_income"
                if kpi.id == self.env.ref('l10n_it_mis_reports_pl_bs.mis_report_bsl_aix').id:
                    if vals[0] == 0:
                        vals[0] = net_income
                    else:
                        vals[0] = vals[0]

                if name_error:
                    recompute_queue.append(kpi)
                else:
                    # no error, set it in locals_dict so it can be used
                    # in computing other kpis
                    if not subkpis or not kpi.multi:
                        locals_dict[kpi.name] = vals[0]
                    else:
                        locals_dict[kpi.name] = SimpleArray_cls(vals)

                # even in case of name error we set the result in the matrix
                # so the name error will be displayed if it cannot be
                # resolved by recomputing later

                if subkpis and not kpi.multi:
                    # here we have one expression for this kpi, but
                    # multiple subkpis (so this kpi is most probably
                    # a sum or other operation on multi-valued kpis)
                    if isinstance(vals[0], tuple):
                        vals = vals[0]
                        if len(vals) != col.colspan:
                            raise SubKPITupleLengthError(
                                _(
                                    'KPI "{}" is valued as a tuple of '
                                    "length {} while a tuple of length {} "
                                    "is expected."
                                ).format(kpi.description, len(vals), col.colspan)
                            )
                    elif isinstance(vals[0], DataError):
                        vals = (vals[0],) * col.colspan
                    else:
                        raise SubKPIUnknownTypeError(
                            _(
                                'KPI "{}" has type {} while a tuple was '
                                "expected.\n\nThis can be fixed by either:\n\t- "
                                "Changing the KPI value to a tuple of length "
                                "{}\nor\n\t- Changing the "
                                "KPI to `multi` mode and giving an explicit "
                                "value for each sub-KPI."
                            ).format(kpi.description, type(vals[0]), col.colspan)
                        )
                if len(drilldown_args) != col.colspan:
                    drilldown_args = [None] * col.colspan

                kpi_matrix.set_values(kpi, col_key, vals, drilldown_args)

                if (
                    name_error
                    or no_auto_expand_accounts
                    or not kpi.auto_expand_accounts
                ):
                    continue

                for (
                    account_id,
                    vals,
                    drilldown_args,
                    _name_error,
                ) in expression_evaluator.eval_expressions_by_account(
                    expressions, locals_dict, show_void_moves
                ):
                    for drilldown_arg in drilldown_args:
                        if not drilldown_arg:
                            continue
                        drilldown_arg["period_id"] = col_key
                        drilldown_arg["kpi_id"] = kpi.id
                    kpi_matrix.set_values_detail_account(
                        kpi, col_key, account_id, vals, drilldown_args
                    )

            if len(recompute_queue) == 0:
                # nothing to recompute, we are done
                break
            if len(recompute_queue) == len(compute_queue):
                # could not compute anything in this iteration
                # (ie real Name errors or cyclic dependency)
                # so we stop trying
                break
            # try again
            compute_queue = recompute_queue
            recompute_queue = []

    def _declare_and_compute_period(
        self,
        expression_evaluator,
        kpi_matrix,
        col_key,
        col_label,
        col_description,
        subkpis_filter=None,
        get_additional_query_filter=None,
        locals_dict=None,
        no_auto_expand_accounts=False,
        show_void_moves=True,
    ):
        """Evaluate a report for a given period, populating a KpiMatrix.

        :param expression_evaluator: an ExpressionEvaluator instance
        :param kpi_matrix: the KpiMatrix object to be populated created
                           with prepare_kpi_matrix()
        :param col_key: the period key to use when populating the KpiMatrix
        :param subkpis_filter: a list of subkpis to include in the evaluation
                               (if empty, use all subkpis)
        :param get_additional_query_filter: a bound method that takes a single
                                            query argument and returns a
                                            domain compatible with the query
                                            underlying model
        :param locals_dict: personalized locals dictionary used as evaluation
                            context for the KPI expressions
        :param no_auto_expand_accounts: disable expansion of account details
        """
        self.ensure_one()

        # prepare the localsdict
        if locals_dict is None:
            locals_dict = {}

        # Evaluate subreports
        for subreport in self.subreport_ids:
            subreport_locals_dict = subreport.subreport_id._evaluate(
                expression_evaluator, subkpis_filter, get_additional_query_filter
            )
            locals_dict[subreport.name] = AutoStruct(
                **{
                    srk.name: subreport_locals_dict.get(srk.name, AccountingNone)
                    for srk in subreport.subreport_id.kpi_ids
                }
            )

        locals_dict.update(self.prepare_locals_dict())
        locals_dict["date_from"] = fields.Date.from_string(
            expression_evaluator.date_from
        )
        locals_dict["date_to"] = fields.Date.from_string(expression_evaluator.date_to)

        # fetch non-accounting queries
        locals_dict.update(
            self._fetch_queries(
                expression_evaluator.date_from,
                expression_evaluator.date_to,
                get_additional_query_filter,
            )
        )

        # use AEP to do the accounting queries
        expression_evaluator.aep_do_queries()

        self._declare_and_compute_col(
            expression_evaluator,
            kpi_matrix,
            col_key,
            col_label,
            col_description,
            subkpis_filter,
            locals_dict,
            no_auto_expand_accounts,
            show_void_moves=show_void_moves,
        )
