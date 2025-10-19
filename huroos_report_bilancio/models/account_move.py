from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    exclude_from_report = fields.Boolean(string='Exclude from report', default=False)

    def write(self, vals):
        res = super(AccountMove, self).write(vals)
        if 'exclude_from_report' in vals:
            for move in self:
                move_line_ids = self.env['account.move.line'].search([('move_id', '=', move.id)])
                move_line_ids.write({'escludi_report_bilancio': vals['exclude_from_report']})
        return res
