from odoo import models


class AccountVatPeriodEndStatement(models.Model):
    _inherit = "account.vat.period.end.statement"

    def compute_amounts(self):
        res = super(AccountVatPeriodEndStatement, self).compute_amounts()

        # if it is annual, attach generic lines of previous statements to this one
        for statement in self:
            if statement.annual and statement.date_range_ids:
                # delete previous generic lines of this statement
                statement.generic_vat_account_line_ids.unlink()
                previous_statements = self.search([('fiscal_year', '=', statement.fiscal_year), ('annual', '=', False)])

                generic_lines = []
                for previous_statement in previous_statements:
                    for line in previous_statement.generic_vat_account_line_ids:
                        new_gen_line = {'account_id': line.account_id.id,
                                        'statement_id': statement.id,
                                        'amount': line.amount,
                                        'name': line.name}
                        generic_lines.append(new_gen_line)

                if generic_lines:
                    self.env['statement.generic.account.line'].create(generic_lines)

        return res
