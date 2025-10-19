from odoo import fields, models, api, _
from odoo.exceptions import UserError, AccessError, MissingError


class AccountResequenceWizard(models.TransientModel):
    _inherit = 'account.resequence.wizard'

    notify_text = fields.Text('Notifica')

    def resequence(self):
        checked = self.env.context.get('checked',False)
        if 'fatturapa_attachment_out_id' in self.env['account.move']._fields and not checked:
            move_fatturapa_xml= self.move_ids.filtered(lambda m:m.fatturapa_attachment_out_id)
            if move_fatturapa_xml:
                return self.check_fatturapa_xml(self.move_ids)
        return super().resequence()


    def check_fatturapa_xml(self,move_fatturapa_xml):

        note = f"<p<> {'Le fatture' if len(move_fatturapa_xml) > 1 else 'La fattura'} : {','.join(move_fatturapa_xml.mapped('name'))} <br/> "\
               f"{'contengono' if len(move_fatturapa_xml) > 1 else 'contiene'} l\'xml della fattura elettronica esportata.<br/> " \
              f"In caso di riordinamento  riesportare l'e-fattura.<br/> " \
               f"Clicca <b>'Prosegui'</b> per riordinare le fatture. <p>"
        self.notify_text=note
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': self._name,
            'views': [(self.env.ref('huroos_correct_journal.account_resequence_view_exception').id, 'form')],
            'res_id': self.id,
            'target': 'new',

        }