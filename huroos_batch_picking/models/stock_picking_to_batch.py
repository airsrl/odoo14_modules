from odoo import models, fields, api
from odoo.exceptions import UserError


class StockPickingToBatch(models.TransientModel):
    _inherit = 'stock.picking.to.batch'

    group_by = fields.Selection([('picking', 'Picking'), ('product', 'Prodotto')], default='picking')

    def get_moves_by_product(self, pickings):
        moves = []
        move_lines = []
        moves_dict = {}
        lot_enabled = self.env.user.has_group('stock.group_production_lot')
        for pick in pickings:
            for move in pick.move_ids_without_package:
                if not lot_enabled:
                    #La Chiave è il Prodotto + Ubica Sorgente
                    key = (str(move.product_id.id) + '-' + str(move.location_id.id))
                else:
                    # La Chiave è il Prodotto + Ubica Sorgente + lotto
                    key = (str(move.product_id.id) + '-' + str(move.location_id.id))
                    if move.move_line_ids[0].lot_id:
                        key = key + '-' + move.move_line_ids[0].lot_id.name
                if key not in moves_dict:
                    moves_dict[key] = [move]
                else:
                    moves_dict[key].append(move)

        for key, stock_move_ids in moves_dict.items():
            product_uom_qty = sum([x.product_uom_qty for x in stock_move_ids])
            reserved = sum([x.reserved_availability for x in stock_move_ids])
            vals = {
                'product_id': stock_move_ids[0].product_id.id,
                'location_id': stock_move_ids[0].location_id.id,
                'location_dest_id': stock_move_ids[0].location_dest_id.id,
                'product_uom': stock_move_ids[0].product_uom.id,
                'name': stock_move_ids[0].name,
                'product_uom_qty': product_uom_qty,
            }
            if lot_enabled:
                move_line_vals = stock_move_ids[0]._prepare_move_line_vals(quantity=0)
                move_line_vals.pop('move_id')
                move_line_vals.pop('picking_id')
                move_line_vals['product_uom_qty'] = stock_move_ids[0].product_uom_qty
                if stock_move_ids[0].move_line_ids[0].lot_id:
                    move_line_vals['lot_id'] = stock_move_ids[0].move_line_ids[0].lot_id.id
                    move_line_vals['lot_name'] = stock_move_ids[0].move_line_ids[0].lot_id.name
                    #move_line_vals['qty_done'] = 1

                move_lines.append((0, 0, move_line_vals))
                vals.update({'move_line_ids': move_lines})


            moves.append((0, 0, vals))
        return moves, move_lines




    def attach_pickings(self):

        self.ensure_one()
        pickings = self.env['stock.picking'].browse(self.env.context.get('active_ids'))
        if self.mode == 'new':
            company = pickings.company_id
            if len(company) > 1:
                raise UserError(("Seleziona Picking della stessa Azienda"))

            batch = self.env['stock.picking.batch'].create({
                'user_id': self.user_id.id,
                'company_id': company.id,
                'picking_type_id': pickings[0].picking_type_id.id,
            })

            if self.group_by == 'product':
                first_picking = pickings[0]
                move_ids, move_line_ids = self.get_moves_by_product(pickings)
                picking_vals = {
                    'picking_type_id': pickings[0].picking_type_id.id,
                    'partner_id': first_picking.company_id.partner_id.id,
                    'location_id': first_picking.location_id.id,
                    'location_dest_id': first_picking.location_dest_id.id,
                    'origin': first_picking.origin,
                    'move_line_ids_without_package': move_line_ids
                }
                #pickings.do_unreserve()
                pickings.unlink()
                picking_id = self.env['stock.picking'].create(picking_vals)
                picking_id.action_confirm()
                picking_id.write({'batch_id': batch.id})

        else:
            batch = self.batch_id

        if self.group_by != 'product':
            pickings.write({'batch_id': batch.id})