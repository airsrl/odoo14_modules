from odoo import _, models
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare


class WizardAccountMoveManageAsset(models.TransientModel):
    _inherit = "wizard.account.move.manage.asset"

    def get_update_asset_vals(self):
        self.ensure_one()
        asset = self.asset_id
        asset_name = asset.make_name()
        digits = self.env["decimal.precision"].precision_get("Account")

        grouped_move_lines = {}
        for line in self.move_line_ids:
            move = line.move_id
            if move not in grouped_move_lines:
                grouped_move_lines[move] = self.env["account.move.line"]
            grouped_move_lines[move] |= line

        vals = {"depreciation_ids": []}
        for dep in asset.depreciation_ids.filtered(
            lambda d: d.type_id in self.depreciation_type_ids
        ):
            residual = dep.amount_residual
            balances = 0

            dep_vals = {"line_ids": []}
            for move, lines in grouped_move_lines.items():
                move_num = move.name

                move_type = "in" if all(line.debit > 0 for line in lines) else "out"
                if not move_type:
                    raise ValidationError(
                        _(
                            "Could not retrieve depreciation line type from"
                            " move `{}` (type `{}`)."
                        ).format(move_num, move_type)
                    )

                # Compute amount and sign to preview how much the line
                # balance will be: if it's going to write off the
                # whole residual amount and more, making it become lower
                # than zero, raise error
                # todo probabilmente si può evitare questo calcolo
                amount = 0
                if lines:
                    amount = abs(
                        sum(
                            line.currency_id._convert(
                                line.debit - line.credit,
                                dep.currency_id,
                                line.company_id,
                                line.date,
                            )
                            for line in lines
                        )
                    )
                sign = 1
                if move_type == "out":
                    sign = -1
                # Block updates if the amount to be written off is higher than
                # the residual amount
                if sign < 0 and float_compare(residual, amount, digits) < 0:
                    raise ValidationError(
                        _(
                            "Could not update `{}`: not enough residual amount"
                            " to write off move `{}`.\n"
                            "(Amount to write off: {}; residual amount: {}.)\n"
                            "Maybe you should try to dismiss this asset"
                            " instead?"
                        ).format(asset_name, move_num, -amount, residual)
                    )
                balances += sign * amount
                # end todo

                dep_line_vals = {
                    "asset_accounting_info_ids": [
                        (
                            0,
                            0,
                            {
                                "move_line_id": line.id,
                                "relation_type": self.management_type,
                            },
                        )
                        for line in lines
                    ],
                    "amount": amount,
                    "date": move.date,
                    "move_type": move_type,
                    "name": _("From move(s) ") + move_num,
                }
                dep_vals["line_ids"].append((0, 0, dep_line_vals))

            if balances < 0 and residual + balances < 0:
                raise ValidationError(
                    _(
                        "Could not update `{}`: not enough residual amount to"
                        " write off.\n"
                        "(Amount to write off: {}; residual amount: {}.)\n"
                        "Maybe you should try to dismiss this asset instead?"
                    ).format(asset_name, balances, residual)
                )

            vals["depreciation_ids"].append((1, dep.id, dep_vals))

        return vals
