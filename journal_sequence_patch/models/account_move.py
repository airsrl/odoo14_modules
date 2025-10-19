from odoo import fields, models, api
from odoo.exceptions import UserError
from datetime import date


class AccountMove(models.Model):
    _inherit = 'account.move'


    @api.depends('posted_before', 'state', 'journal_id', 'date')
    def _compute_name(self):
        for move in self:
            if not move.journal_id.sequence_id:
              return super(AccountMove, self)._compute_name()
            sequence_id = move._get_sequence()
            if not sequence_id:
                raise UserError('Please define a sequence on your journal.')
            if not move.sequence_generated and move.state == 'draft':
                move.name = '/'
            elif not move.sequence_generated and move.state != 'draft':
                #move.name = sequence_id.with_context({'ir_sequence_date': self.invoice_date, 'bypass_constrains': True}).next_by_id(sequence_date=self.invoice_date)
                #fix con Kev per Errore Uncredit AK
                move.name = sequence_id.with_context({'ir_sequence_date': move.invoice_date or date.today(), 'bypass_constrains': True}).next_by_id(sequence_date=move.invoice_date)
                move.sequence_generated = True
