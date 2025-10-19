from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        if not 'electronic_invoice_subjected' in vals or vals['electronic_invoice_subjected'] == False:
            vals['codice_destinatario'] = False

        return super(ResPartner, self).create(vals)

    def write(self, vals):
        if 'electronic_invoice_subjected' in vals and vals['electronic_invoice_subjected'] == False :
            vals['codice_destinatario'] = False
            if 'pec_destinatario' in vals:
                vals.pop('pec_destinatario')
        result = super(ResPartner, self).write(vals)
        return result





