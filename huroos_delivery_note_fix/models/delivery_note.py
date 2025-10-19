from odoo import fields, models, api,_
from odoo.exceptions import UserError

class StockDeliveryNote(models.Model):
    _inherit = "stock.delivery.note"



    def _check_uniq_name(self):
        sql=f"""select * from stock_delivery_note  where name = '{self.name}' and company_id = {self.company_id.id} """
        self.env.cr.execute(sql)
        exist = self.env.cr.dictfetchall()
        if exist:
            raise UserError(_("The number of the delivery note must be unique!."))
    def button_change_name(self):
        wiz_form = self.env.ref('huroos_delivery_note_fix.wizard_ddt_change_number_form_view')
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.ddt.changenumber',
            'view_mode': 'form',
            'views': [(wiz_form.id, 'form')],
            'target': 'new',
            'context': {'default_delivery_note_id':self.id},
        }
    # def _compute_boolean_flags(self):
    #     can_change_number = self.user_has_groups(
    #         "l10n_it_delivery_note.can_change_number"
    #     )
    #     show_product_information = self.user_has_groups(
    #         "l10n_it_delivery_note_base.show_product_related_fields"
    #     )
    #
    #     for note in self:
    #         note.can_change_number = can_change_number
    #         note.show_product_information = show_product_information
