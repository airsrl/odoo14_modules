# Copyright 2022 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

from odoo import fields, models, api, _


class ReturnPicking(models.TransientModel):
    _inherit = 'stock.return.picking'

    @api.onchange("label_url")
    def move_to_stage_attesa_ricezione(self):
        for record in self:
            stage = self.env['helpdesk.stage'].search([('name', '=', 'Ricezione merce')], limit=1)
            if stage:
                if record.ticket_id:
                    record.ticket_id.stage_id = stage.id if stage and record.ticket_id.stage_id.sequence < stage.sequence else record.ticket_id.stage_id.id
                else:
                    ticket_id = self.env['helpdesk.ticket'].search([('picking_ids', 'in', record.picking_id.id)], limit=1)
                    if ticket_id:
                        ticket_id.stage_id = stage.id if stage and ticket_id.stage_id.sequence < stage.sequence else ticket_id.stage_id.id

    def _create_returns(self):
        new_picking, picking_type_id = super(ReturnPicking, self)._create_returns()
        new_picking_id = self.env['stock.picking'].browse(new_picking)
        if new_picking_id.carrier:
            for line in new_picking_id.move_lines:
                line.quantity_done = line.product_uom_qty
            try:
                new_picking_id.start_shippypro_routine()
            except:
                pass
        return new_picking, picking_type_id

    def create_returns(self):
        res = super(ReturnPicking, self).create_returns()

        stage = self.env.ref('huroos_mra_ticketing.stage_attesa_ricezione', raise_if_not_found=False)
        if not stage:
            stage = self.env['helpdesk.stage'].search([('name', '=', 'ATTESA RICEZIONE MERCE')], limit=1)
        if stage:
            if self.ticket_id:
                self.ticket_id.stage_id = stage.id if stage and self.ticket_id.stage_id.sequence < stage.sequence else self.ticket_id.stage_id.id
            else:
                ticket_id = self.env['helpdesk.ticket'].search([('picking_ids', 'in', self.picking_id.id)], limit=1)
                if ticket_id:
                    ticket_id.stage_id = stage.id if stage and ticket_id.stage_id.sequence < stage.sequence else ticket_id.stage_id.id
        return res

    @api.depends('ticket_id.sale_order_id.picking_ids', 'ticket_id.partner_id.commercial_partner_id')
    def _compute_suitable_picking_ids(self):
        for r in self:
            picking_type_id = self.env['stock.picking.type'].search([('code', '=', 'outgoing')])
            domain = [('state', '=', 'done'), ('picking_type_id', 'in', picking_type_id.ids)]
            if r.sale_order_id:
                domain += [('id', 'in', r.sale_order_id.picking_ids._origin.ids)]
            elif r.partner_id:
                domain += [('partner_id', 'child_of', r.partner_id.commercial_partner_id._origin.id)]
            r.suitable_picking_ids = self.env['stock.picking'].search(domain)


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.onchange("label_url")
    def set_shippy_pro_label_url_ticket(self):
        if not len(self.ids) > 0:
            return
        ticket_id = self.env['helpdesk.ticket'].search([('picking_ids', 'in', self.ids[0])], limit=1)
        if ticket_id:
            ticket_id.label_url = self.label_url
