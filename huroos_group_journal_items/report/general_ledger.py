from odoo import api, models
from odoo.tools import float_is_zero

class GeneralLedgerReport(models.AbstractModel):
    _inherit = "report.account_financial_report.general_ledger"

    @api.model
    def _get_move_line_data(self, move_line):
        move_line_data = super(GeneralLedgerReport, self)._get_move_line_data(move_line)

        account_move = self.env['account.move'].search([('id','=',move_line["move_id"][0])])
        document_date = account_move.invoice_date
        move_line_data["document_date"]= document_date

        return move_line_data

    # Unico cambiamento: sorted(move_lines, key=lambda k: (k["date"]) -> sorted(move_lines, key=lambda k: (k["date"],k["entry"]))
    def _create_account(self, account, acc_id, gen_led_data, rec_after_date_to_ids):
        move_lines = []
        for ml_id in gen_led_data[acc_id].keys():
            if not isinstance(ml_id, int):
                account.update({ml_id: gen_led_data[acc_id][ml_id]})
            else:
                move_lines += [gen_led_data[acc_id][ml_id]]
        move_lines = sorted(move_lines, key=lambda k: (k["date"],k["entry"]))
        move_lines = self._recalculate_cumul_balance(
            move_lines,
            gen_led_data[acc_id]["init_bal"]["balance"],
            rec_after_date_to_ids,
        )
        account.update({"move_lines": move_lines})
        return account

    # Unico cambiamento: sorted(move_lines, key=lambda k: (k["date"]) -> sorted(move_lines, key=lambda k: (k["date"],k["entry"]))
    def _get_list_grouped_item(
        self, data, account, rec_after_date_to_ids, hide_account_at_0, rounding
    ):
        list_grouped = []
        for data_id in data.keys():
            group_item = {}
            move_lines = []
            if not isinstance(data_id, int):
                account.update({data_id: data[data_id]})
            else:
                for ml_id in data[data_id].keys():
                    if not isinstance(ml_id, int):
                        group_item.update({ml_id: data[data_id][ml_id]})
                    else:
                        move_lines += [data[data_id][ml_id]]
                move_lines = sorted(move_lines, key=lambda k: (k["date"],k["entry"]))
                move_lines = self._recalculate_cumul_balance(
                    move_lines,
                    data[data_id]["init_bal"]["balance"],
                    rec_after_date_to_ids,
                )
                group_item.update({"move_lines": move_lines})
                if (
                    hide_account_at_0
                    and float_is_zero(
                        data[data_id]["init_bal"]["balance"],
                        precision_rounding=rounding,
                    )
                    and group_item["move_lines"] == []
                ):
                    continue
                list_grouped += [group_item]
        return account, list_grouped

    def _calculate_grouping(self, grouped_ml, move_line):
        entry_id = move_line["entry_id"]
        if entry_id not in grouped_ml.keys():
            grouped_ml[entry_id] = move_line
        else:
            if move_line["name"] not in grouped_ml[entry_id]["name"]:
                grouped_ml[entry_id]["name"] += ', ' + move_line["name"]
            if move_line["ref_label"] not in grouped_ml[entry_id]["ref_label"]:
                grouped_ml[entry_id]["ref_label"] += ', ' + move_line["ref_label"]
            grouped_ml[entry_id]["debit"] += move_line["debit"]
            grouped_ml[entry_id]["credit"] += move_line["credit"]
            grouped_ml[entry_id]["balance"] += (move_line["debit"] - move_line["credit"])

        return grouped_ml

    def _get_grouped_ml(self, account):
        # Se group_by != False, account rappresenta un item di account["list_grouped"] da cui poter modificare le move_lines
        grouped_ml = {}
        for move_line in account["move_lines"]:
            grouped_ml = self._calculate_grouping(
                grouped_ml,
                move_line,
            )
        list_grouped_ml = []
        for entry_id in grouped_ml.keys():
            list_grouped_ml.append(grouped_ml[entry_id])
        return list_grouped_ml

    @api.model
    def _get_report_values(self, docids, data):

        values = super(GeneralLedgerReport, self)._get_report_values(docids, data)

        general_ledger = values["general_ledger"]
        grouped_by = data["grouped_by"]

        if data["group_journal_items"]:
            for account in general_ledger:
                if grouped_by and account.get(grouped_by):
                    for item in account["list_grouped"]:
                        item["move_lines"] = self._get_grouped_ml(item)
                else:
                    account["move_lines"] = self._get_grouped_ml(account)

        return values