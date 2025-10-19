from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    registration_type_descr = fields.Selection([
        ('null', ''),
        ('nota_accredito_fornitore', 'Nota di Accredito Fattura Fornitore'),
    ], default='null')

    @api.model_create_multi
    def create(self, vals_list):
        rslt = super(AccountMove, self).create(vals_list)
        rslt.compute_registration_type()
        return rslt

    def write(self, vals):
        registration_type_descr = self.compute_registration_type()
        vals.update({'registration_type_descr': registration_type_descr})
        res = super(AccountMove, self).write(vals)
        return res


    def compute_registration_type(self):
        for move in self:

            registration_type_descr = 'null'
            fiscal_document_type = False
            move_type = move.move_type
            attachment_in_id = move.fatturapa_attachment_in_id
            amount_total = move.amount_total

            if move.fiscal_document_type_id:
                fiscal_document_type = move.fiscal_document_type_id.code
            if attachment_in_id:
                amount_total = attachment_in_id.invoices_total

            if fiscal_document_type == 'TD01' and move_type == 'in_invoice' and amount_total < 0:
                #Nota Accredito Fornitore
                registration_type_descr = 'nota_accredito_fornitore'

            return registration_type_descr

    def apply_registration_automatism(self):
        for move in self:
            prev_fiscal_document_type_id = move.fiscal_document_type_id
            if move.registration_type_descr == 'nota_accredito_fornitore':
                move.write({
                    'move_type': 'in_refund',
                    'fiscal_document_type_id': prev_fiscal_document_type_id.id,
                    'registration_type_descr': 'nota_accredito_fornitore'
                })
                if move.amount_total < 0:
                    for line in move.invoice_line_ids:
                        line.price_unit = -line.price_unit





