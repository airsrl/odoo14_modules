from odoo import fields, models, api
from datetime import date, datetime


class WizardReso(models.TransientModel):
    _name = 'wizard.cambio'

    helpdesk_id = fields.Many2one('helpdesk.ticket')
    line_ids = fields.One2many('wizard.cambio.line', 'wizard_id')

    def confirm(self):
        sale_order_env = self.env['sale.order']
        client_order_ref = f'Reso ordine {self.helpdesk_id.sale_order_id.name}'
        commento = f'Cambio merce ordine {self.helpdesk_id.sale_order_id.name} del {self.helpdesk_id.sale_order_id.date_order.strftime("%d/%m/%Y")}'
        product_lines = [(0, 0, {'display_type': 'line_note', 'name': commento})]
        tag_ids = []
        try:
            tag_ids = self.env.ref("huroos_rma_ticketing.etichetta_sale_reso").ids
        except:
            tags = self.env['crm.tag'].search([('name', '=', 'reso')], limit=1)
            if tags:
                tag_ids = tag_ids.ids
        for line in self.line_ids:
            product_id = line.product_id
            product_uom_qty = line.qty
            new_line = (0, 0, {'product_id': product_id.id, 'product_uom_qty': product_uom_qty, 'name': product_id.name,
                "product_uom": product_id.uom_id.id, 'price_unit': 0})
            product_lines.append(new_line)

        new_order = sale_order_env.create(
            {'partner_id': self.helpdesk_id.sale_order_id.partner_id.id, 'tag_ids': [(6, 0, tag_ids)],
                'order_line': product_lines, 'client_order_ref': client_order_ref})
        self.helpdesk_id.sale_order_return_id = new_order.id

        new_order.action_confirm


class WizardResoLine(models.TransientModel):
    _name = 'wizard.cambio.line'

    wizard_id = fields.Many2one('wizard.cambio')
    product_id = fields.Many2one('product.product')
    qty = fields.Float('Quantità')
