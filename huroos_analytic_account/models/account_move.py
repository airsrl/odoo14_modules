from odoo import models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_tax_grouping_key_from_base_line(self, base_line, tax_vals):
        """ Adds analytic account and analytic tags to the lines of the account.move field line_ids
        generated from a tax repartition and that don't have a configured default_tax_account """

        grouping_dict = super(AccountMove, self)._get_tax_grouping_key_from_base_line(base_line, tax_vals)
        tax_repartition_line = self.env['account.tax.repartition.line'].browse(tax_vals['tax_repartition_line_id'])

        if base_line.analytic_account_id and not base_line._get_default_tax_account(tax_repartition_line):
            grouping_dict["analytic_account_id"] = base_line.analytic_account_id

        if base_line.analytic_tag_ids and not base_line._get_default_tax_account(tax_repartition_line):
            grouping_dict["analytic_tag_ids"] = base_line.analytic_tag_ids.ids

        return grouping_dict


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.onchange('account_id')
    def set_default_analytic_account_from_invoice_line_account(self):
        for rec in self:
            if not rec.move_id.partner_id.analytic_account_id:
                rec.analytic_account_id = rec.account_id.analytic_account_id
            else:
                rec.analytic_account_id = rec.move_id.partner_id.analytic_account_id

    @api.model
    def default_get(self, default_fields):
        res = super(AccountMoveLine, self).default_get(default_fields)

        partner = self.env['res.partner'].browse(res.get('partner_id'))
        if partner.analytic_account_id:
            res['analytic_account_id'] = partner.analytic_account_id.id
        if partner.analytic_tag_ids:
            res['analytic_tag_ids'] = partner.analytic_tag_ids.ids

        return res
