from odoo import models


class AnalyticReport(models.AbstractModel):
    _inherit = "account.analytic.report"

    def _generate_analytic_tag_lines(self, analityc_account, parent_id):

        lines = list()

        tag_line_vals = {'Senza etichetta': 0}

        for analityc_account_line in analityc_account.line_ids:
            if not analityc_account_line.tag_ids:
                tag_line_vals['Senza etichetta'] += analityc_account_line.amount

            else:
                tags = ', '.join(analityc_account_line.tag_ids.mapped('name'))
                if tags not in tag_line_vals:
                    tag_line_vals.update({tags: analityc_account_line.amount})
                else:
                    tag_line_vals[tags] += analityc_account_line.amount

        for tag in tag_line_vals:
            lines.append({
                'id': 'analytic_account_line_%s' % tag,
                'name': tag,
                'columns': [{'name': analityc_account.code},
                            {'name': analityc_account.partner_id.display_name},
                            {'name': self.format_value(tag_line_vals[tag])}],
                'level': 8,
                'unfoldable': False,
                'caret_options': 'analytic.account.line',
                'parent_id': parent_id
            })

        return lines

    def _generate_analytic_account_lines(self, analytic_accounts, parent_id=False):
        lines = []

        for account in analytic_accounts:
            lines.append({
                'id': 'analytic_account_%s' % account.id,
                'name': account.name,
                'columns': [{'name': account.code},
                            {'name': account.partner_id.display_name},
                            {'name': self.format_value(account.balance)}],
                'level': 4,
                'unfoldable': False,
                'caret_options': 'account.analytic.account',
                'parent_id': parent_id
            })
            is_splittable = bool(account.line_ids.tag_ids)
            if is_splittable:
                lines[-1]['unfoldable'] = False
                lines[-1]['unfolded'] = False
                lines += self._generate_analytic_tag_lines(account, lines[-1]['id'])

        return lines
