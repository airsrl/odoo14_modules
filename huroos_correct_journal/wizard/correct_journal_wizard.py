from odoo import fields, models, api,_
from odoo.exceptions import UserError, AccessError, MissingError
from collections import defaultdict
from odoo.tools.misc import format_date
import json
import re

class CorrectJournalWizard(models.TransientModel):
    _name = 'correct.journal.wizard'
    _description = 'Remake the journal.'


    suitable_journal_ids = fields.Many2many('account.journal', compute='_compute_suitable_journal_ids')
    first_date = fields.Date(help="Date (inclusive) from which the numbers are resequenced.")
    end_date = fields.Date(help="Date (inclusive) to which the numbers are resequenced. If not set, all Journal Entries up to the end of the period are resequenced.")
    new_journal_id = fields.Many2one('account.journal',domain="[('id', 'in', suitable_journal_ids)]")
    move_ids = fields.Many2many('account.move')
    new_values = fields.Text(compute='_compute_new_values')
    preview_moves = fields.Text(compute='_compute_preview_moves')
    notify_text = fields.Text('Notifica')
    @api.depends('move_ids')
    def _compute_suitable_journal_ids(self):
        for m in self.mapped('move_ids'):
            journal_type = m.invoice_filter_type_domain or 'general'
            company_id = m.company_id.id or self.env.company.id
            domain = [('company_id', '=', company_id), ('type', '=', journal_type)]
            if len(self.mapped('move_ids')) == 1:
                domain.append(('id','not in',m.journal_id.ids))
            self.suitable_journal_ids = self.env['account.journal'].search(domain)
    @api.model
    def default_get(self, fields_list):
        values = super(CorrectJournalWizard, self).default_get(fields_list)
        if 'move_ids' not in fields_list:
            return values
        active_move_ids = self.env['account.move']
        if self.env.context['active_model'] == 'account.move' and 'active_ids' in self.env.context:
            active_move_ids = self.env['account.move'].browse(self.env.context['active_ids'])
        values['move_ids'] = [(6, 0, active_move_ids.ids)]
        return values





    @api.depends('new_values')
    def _compute_preview_moves(self):
        """Reduce the computed new_values to a smaller set to display in the preview."""
        for record in self:
            new_values = sorted(json.loads(record.new_values).values(), key=lambda x: x['server-date'], reverse=True)
            changeLines = []
            in_elipsis = 0
            for i, line in enumerate(new_values):
                if i < 3 or i == len(new_values) - 1:
                    if in_elipsis:
                        changeLines.append({'id': 'other_' + str(line['id']), 'current_name': _('... (%s other)', in_elipsis), 'new_by_name': '...','new_by_date':'...',  'date': '...'})
                        in_elipsis = 0
                    changeLines.append(line)
                else:
                    in_elipsis += 1

            record.preview_moves = json.dumps({
                'ordering': 'date',
                'changeLines': changeLines,
            })

    @api.depends('new_journal_id', 'move_ids')
    def _compute_new_values(self):
        """Compute the proposed new values.

        Sets a json string on new_values representing a dictionary thats maps account.move
        ids to a disctionay containing the name if we execute the action, and information
        relative to the preview widget.
        """


        self.new_values = "{}"
        for record in self :
            moves_by_period = defaultdict(lambda: record.env['account.move'])
            for move in record.move_ids._origin:  # Sort the moves by period depending on the sequence number reset
                moves_by_period['default'] += move


            new_values = {}
            if self.new_journal_id:
                # Con new creo un oggetto senza salvarlo nel db


                i = [] #creo indici in base alla data contabile
                for j, period_recs in enumerate(moves_by_period.values()):
                    new_name_list = []
                    # compute the new values period by period
                    for move in period_recs:


                        new_values[move.id] = {
                            'id': move.id,
                            'current_name': move.name,
                            'state': move.state,
                            'date': format_date(self.env, move.date),
                            'server-date': str(move.date),
                        }
                        record_with_journal =  self.env['account.move'].new({'name':'/',
                                                                     'date':move.date,
                                                                     'journal_id':self.new_journal_id.id})
                        record_with_journal._set_next_sequence()
                        #Se il nuovo journal ha una sequenza annuale, l'indice va in base all'anno, se mensile invece prende a riferimento mese e anno
                        sequence_number_reset = record_with_journal._deduce_sequence_number_reset(record_with_journal.name)
                        if sequence_number_reset == 'month':
                            if not any(d['year'] == move.date.year and d['month'] == move.date.month  for d in i):
                                i.append({
                                    'year':move.date.year,
                                    'month':move.date.month,
                                    'seq':0
                                })
                            index = next(item for item in i if item["year"] == move.date.year and item['month'] == move.date.month)
                        elif sequence_number_reset == 'year':
                            if not any(d['year'] == move.date.year  for d in i):
                                i.append({
                                    'year':move.date.year,
                                    'seq':0
                                })
                            index = next(item for item in i if item["year"] == move.date.year )
                        else:
                            if not i:
                                 i.append({'seq':0})
                            index =next(item for item in i)
                        last_sequence= record_with_journal._get_last_sequence(lock=False)

                        #creo una nuova sequenza e imposto il primo numero a 0
                        if not last_sequence:
                            seq_format, format_values = record_with_journal._get_sequence_format_param(record_with_journal.name)
                            format_values['seq'] = 0

                        else:
                            seq_format, format_values = record_with_journal._get_sequence_format_param(last_sequence)
                        format_values['seq'] += index['seq']
                        new_name_list.append(seq_format.format(**{
                            **format_values,
                            'year': move.date.year % (10 ** format_values['year_length']),
                            'month': move.date.month,
                            'seq':  format_values['seq'] +1,
                        }))
                        index['seq'] +=1
                    # For all the moves of this period, assign the name
                    for move, new_name in zip(period_recs, new_name_list):
                        new_values[move.id]['new_by_name'] = new_name
                        new_values[move.id]['new_by_date'] = new_name

            record.new_values = json.dumps(new_values)

    def change_journal(self):
        checked = self.env.context.get('checked',False)
        new_values = json.loads(self.new_values)
        self.move_ids._check_fiscalyear_lock_date()
        self.move_ids.posted_before = False
        if 'fatturapa_attachment_out_id' in self.env['account.move']._fields and not checked:
            move_fatturapa_xml= self.move_ids.filtered(lambda m:m.fatturapa_attachment_out_id )
            if move_fatturapa_xml:
                return self.check_fatturapa_xml(move_fatturapa_xml)
        for move_id in self.move_ids:
            if str(move_id.id) in new_values:
                move_id.name = '/'
                move_id.journal_id = self.new_journal_id.id
                move_id.name = new_values[str(move_id.id)]['new_by_date']
                move_id.posted_before = True if move_id.state == 'posted' else False
        #self.move_ids[-1]._set_next_sequence()

    def check_fatturapa_xml(self,move_fatturapa_xml):

        note = f"<p<> {'Le fatture' if len(move_fatturapa_xml) > 1 else 'La fattura'} : {','.join(move_fatturapa_xml.mapped('name'))} <br/> "\
               f"{'contengono' if len(move_fatturapa_xml) > 1 else 'contiene'} l\'xml della fattura elettronica esportata.<br/> " \
               f"In caso di cambio registro  riesportare l'e-fattura.<br/> " \
               f"Clicca <b>'Prosegui'</b> per cambiare il registro. <p>"
        self.notify_text=note
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'correct.journal.wizard',
            'views': [(self.env.ref('huroos_correct_journal.correct_journal_exception_view').id, 'form')],
            'res_id': self.id,
            'target': 'new'
        }




