from odoo import fields, models, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'





    dati_gestionali_ids = fields.One2many('air.dati.gestionali', 'invoice_line_id')


    def create(self,values):
        invoice_lines = super(AccountMoveLine, self).create(values)
        for invoice_line in invoice_lines:
            invoice= invoice_line.move_id
            if invoice.move_type == 'out_invoice' and invoice.partner_id:
                if invoice.partner_id.dati_gestionali_ids:


                    for line in invoice.partner_id.dati_gestionali_ids:

                        val= {   "invoice_line_id":self.id,
                                        "tipo_dato": line.tipo_dato,
                                        "rif_testo": line.rif_testo,
                                        "rif_numero": line.rif_numero,
                                        "rif_date": line.rif_date

                                    }
                        invoice_line.dati_gestionali_ids=[(0,0,val)]
        return invoice_lines
    def show_dati_gestionali(self):

        view_id=self.env.ref('air_altridati_gestionali.gestionali_form_view').id
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'account.move.line',
            'views': [(view_id, 'form')],
            'target': 'new',
            'flags': {'initial_mode': 'edit'},
            'res_id':self.id


        }

class AirDatiGestionali(models.Model):
    _name = 'air.dati.gestionali'

    invoice_line_id = fields.Many2one('account.move.line')
    tipo_dato=fields.Char()
    rif_testo=fields.Char()
    rif_numero=fields.Float( digits=(8,2))
    rif_date=fields.Date()
