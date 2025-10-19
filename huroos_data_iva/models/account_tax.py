from odoo import models, fields

class AccountTax(models.Model):
    _inherit = "account.tax"

    def _account_tax_ids_with_moves(self):
        """
            Calcola il totale tasse per data competenza IVA
        """
        competence_iva = self.env['ir.config_parameter'].sudo().get_param('huroos_data_iva.account_competence_iva')
        if not competence_iva:
            r = super(AccountTax, self)._account_tax_ids_with_moves()
            return r
        else:
            from_date, to_date, company_ids, _ = self.get_context_values()
            company_ids = tuple(company_ids)
            req = """
                   SELECT id
                   FROM account_tax at
                   WHERE
                   company_id = %s AND
                   EXISTS (
                     SELECT 1 FROM account_move_Line aml
                     WHERE
                       date_iva >= %s AND
                       date_iva <= %s AND
                       company_id = %s AND (
                         tax_line_id = at.id OR
                         EXISTS (
                           SELECT 1 FROM account_move_line_account_tax_rel
                           WHERE account_move_line_id = aml.id AND
                             account_tax_id = at.id
                         )
                       )
                   )
           """
            self.env.cr.execute(req, (company_ids, from_date, to_date, company_ids))
            return [r[0] for r in self.env.cr.fetchall()]


    def get_move_line_partial_domain(self, from_date, to_date, company_ids):
        competence_iva = self.env['ir.config_parameter'].sudo().get_param('huroos_data_iva.account_competence_iva')
        if not competence_iva:
            r = super(AccountTax, self).get_move_line_partial_domain(from_date, to_date, company_ids)
            return r
        else:
            return [
                ('date_iva', '<=', to_date),
                ('date_iva', '>=', from_date),
                ('company_id', 'in', company_ids),
            ]