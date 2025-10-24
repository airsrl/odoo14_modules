from odoo import models, api
from ..code import woocommerce_utils as wu
from ..code import odoo_utils as ou
from ..code import connector_utils as cu

class stock_picking_custom(models.Model):
    _inherit = "stock.picking"

    def _action_done(self):
        res = super(stock_picking_custom, self)._action_done()
        try:
            self.SyncOrderStatusWP()
        except Exception as ex:
            ou.log_info(f'_action_done: {ex}')
            pass
        return res

    def write(self, values):
        res = super(stock_picking_custom, self).write(values)
        if 'carrier_tracking_ref' in values:
            try:
                stock_picking = self.env['stock.picking'].browse(self.id)
                if stock_picking and stock_picking.carrier_tracking_ref:
                    custom_tracking_link = ''
                    tracking_upd_res = wu.wp_upd_tracking_info(self, stock_picking.carrier_id.name if stock_picking.carrier_id else 'VETTORE', custom_tracking_link, stock_picking.carrier_tracking_ref, stock_picking.scheduled_date)
                    ou.log_info(f'tracking_upd_res: {tracking_upd_res}')  # DEBUG
            except Exception as ex:
                ou.log_info(f'_action_done: {ex}')
                pass
        return res

    def SyncOrderStatusWP(self):
        wp_order_status = 'completed'
        for record in self:
            ou.log_info(f'stock.picking - SyncOrderStatusWP record: {record.id}')
            if record and record.sale_id and record.sale_id:

                # No sale order!?
                if not record.sale_id:
                    return

                # No order ref
                if not record.sale_id.ecommerce_order_id:
                    return

                # Not a final stock movement
                if not record.location_dest_id.usage == 'customer':
                    return

                # Updating order status on WP
                wp_order_upd_res = wu.wp_set_order_status(self, record.sale_id.ecommerce_order_id, wp_order_status)

                # Recording note on the sale order
                if not wp_order_upd_res:
                    msg_body = f"ATTENZIONE - Stato ordine {record.sale_id.riferimento_ordine} non aggiornato su WordPress"
                    ou.post_log_msg(record.sale_id, msg_body, ou.Log_msg_type.Warn)


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _action_cancel(self):
        res = super(StockMove, self)._action_cancel()
        try:
            for rec in self:
                cu.add_new_log_entry(self, 'product.product', rec.product_id.id, 'sync_stock_qty', cu.log_status.pending, 'stock.move - _action_cancel')
        except Exception as ex:
            ou.log_info(f'stock.move _action_cancel: {ex}')

        return res

    def _action_assign(self):
        try:
            for rec in self:
                cu.add_new_log_entry(self, 'product.product', rec.product_id.id, 'sync_stock_qty', cu.log_status.pending, 'stock.move - _action_assign')
        except Exception as ex:
            ou.log_info(f'stock.move _action_assign: {ex}')
        return super(StockMove, self)._action_assign()
