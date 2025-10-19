# Copyright 2022 Huroos Srl

from odoo import models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):

    _inherit = "account.move"


    def _recompute_tax_lines(self, **kwargs):
        """
        As the taxes are recalculated based on a single discount, we need to
        simulate a multiple discount by changing the unit price. Values are
        restored after the original process is done
        """
        print(self.env.context)
        old_values_by_line_id = {}
        new_values_by_line_id = {}
        digits = self.line_ids._fields["price_unit"]._digits
        self.line_ids._fields["price_unit"]._digits = (16, 16)
        for line in self.line_ids:
            aggregated_discount = line._compute_aggregated_discount(line.discount)
            old_values_by_line_id[line.id] = {
                "price_unit": line.price_unit,
                "discount": line.discount,
            }
            price_unit = line.price_unit * (1 - aggregated_discount / 100)
            #line.update({"price_unit": price_unit, "discount": 0})
            new_values_by_line_id[line.id] = {
                "price_unit": price_unit,
                "discount": 0,
            }

        data_update = []
        for key, value in new_values_by_line_id.items():
            data_update.append((1, key, value))
        self.env['account.move.line'].update(data_update)

        self.line_ids._fields["price_unit"]._digits = digits
        res = super(AccountMove, self)._recompute_tax_lines(**kwargs)

        data_update = []
        for line in self.line_ids:
            if line.id not in old_values_by_line_id:
                continue
            #line.update(old_values_by_line_id[line.id])

        for key, value in old_values_by_line_id.items():
            data_update.append((1, key, value))
        self.env['account.move.line'].update(data_update)

        return res



    def _has_discount(self):
        self.ensure_one()
        return any(
            [
                line._compute_aggregated_discount(line.discount) > 0
                for line in self.invoice_line_ids
            ]
        )
