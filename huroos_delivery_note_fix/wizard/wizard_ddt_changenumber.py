from odoo import fields, models, api,_
from odoo.exceptions import UserError

class WizardDdtChangenumber(models.TransientModel):
    _name = 'wizard.ddt.changenumber'
    _description = 'Wiz. modifica DDT numerazione'

    name = fields.Char()
    delivery_note_id = fields.Many2one('stock.delivery.note',string='DDT')
    type_id = fields.Many2one(
       related='delivery_note_id.type_id',string='Tipologia ',store=True)
    sequence_id = fields.Many2one(related="type_id.sequence_id",store=True)
    prefix = fields.Char(related='sequence_id.prefix')
    number_new= fields.Integer('Nuova numerazione')
    number_next_actual = fields.Integer(related="sequence_id.number_next_actual")


    def _check_max_sequence(self):
        last_sequence = self.number_next_actual - self.sequence_id.number_increment
        if self.number_new > last_sequence and last_sequence > 1 :
            raise UserError(_('Numerazione ancora da definire!'))

    def confirm(self):
        renumber_sequence = self.env.context.get('renumber_sequence',False)
        if self.delivery_note_id and self.number_new:
            suffix = self.sequence_id.suffix if self.sequence_id.suffix else ""
            self.delivery_note_id.name = f'{self.prefix}{self.number_new}{suffix}'.strip()
            self.delivery_note_id._check_uniq_name()
            next_number = self.number_new + self.sequence_id.number_increment
            if renumber_sequence:
                self.sequence_id.write({'number_next_actual': next_number})
                delivery_notes_to_change =  self.get_next_delivery_note(self.delivery_note_id,self.type_id)
                for ddt in delivery_notes_to_change:
                    ddt.name = self.sequence_id.next_by_id()
            else:
                self._check_max_sequence()

    def get_next_delivery_note(self,ddt,type):
        return self.env['stock.delivery.note'].search([('id','>',ddt.id),('type_id','=',type.id),('state','not in',['draft'])],order='id asc')

