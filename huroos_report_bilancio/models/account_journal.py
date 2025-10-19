from odoo import models, fields, api


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    exclude_from_report = fields.Boolean(string='Exclude from report', default=False)

    def write(self, vals):
        res = super(AccountJournal, self).write(vals)
        if 'exclude_from_report' in vals:
            for journal in self:
                journal_move_ids = self.env['account.move'].search([('journal_id', '=', journal.id)])
                journal_move_ids.write({'exclude_from_report': vals['exclude_from_report']})
        return res
