from odoo import api, fields, models, _
from ..code import connector_utils as cu
from ..code import odoo_utils as ou


class stock_move_line_custom(models.Model):
    _inherit = "stock.move.line"

    in_out_move = fields.Float(string='Qty In/Out', compute='compute_in_out_move')
    movimenti_prodotto = fields.Float(string="Unit value", compute='compute_products_unit_value')
    products_value = fields.Float(string="Tot. value", compute='compute_products_value')

    def compute_products_value(self):
        for record in self:
            if record.move_id:
                record.products_value = record.movimenti_prodotto * record.in_out_move

    def compute_in_out_move(self):
        for record in self:
            if record.location_id.usage in ['inventory', 'supplier']:
                record.in_out_move = record.qty_done
            elif record.location_dest_id.usage in ['customer', 'inventory',
                                                   'production'] or 'produz' in record.location_dest_id.name.lower():
                record.in_out_move = record.qty_done * -1
            else:
                record.in_out_move = None

    def compute_products_unit_value(self):
        for record in self:
            if record.move_id and record.in_out_move != 0:
                svl = self.env['stock.valuation.layer'].search([('stock_move_id', '=', record.move_id.id)], limit=1)
                if record.move_id.sale_line_id:
                    # Se esiste la riga di vendita a prezzo di vendita
                    record.movimenti_prodotto = record.move_id.sale_line_id.price_unit
                elif record.move_id.purchase_line_id:
                    # Se esiste la riga di acquisto a prezzo di acquisto
                    record.movimenti_prodotto = record.move_id.purchase_line_id.price_unit
                elif record.move_id.picking_id and record.move_id.picking_id.pos_order_id:
                    # Se esiste la riga di vendita tramite pos
                    pos_lines_with_product = record.move_id.picking_id.pos_order_id.lines.filtered(lambda x: x.product_id == record.product_id)
                    record.movimenti_prodotto = pos_lines_with_product[0].price_unit if pos_lines_with_product else 0
                elif svl:
                    # Se esiste valutazione di magazzino
                    record.movimenti_prodotto = svl[0]['unit_cost']
                else:
                    record.movimenti_prodotto = 0

    def write(self, values):
        res = super(stock_move_line_custom, self).write(values)
        ou.log_info(f'stock.move.line - {values}')
        try:
            for record in self:
                # Adding rows to connector log
                if record.product_id and record.product_id.wp_to_sync and bool(record.product_id.wp_to_sync):
                    cu.add_new_log_entry(self, 'product.product', record.product_id.id, 'sync_stock_qty',
                                         cu.log_status.pending, 'stock.move.line - write')
        except Exception as ex:
            ou.log_error(f'stock.move.line - write - {ex}')
            ou.log_exception(ex)
        return res
