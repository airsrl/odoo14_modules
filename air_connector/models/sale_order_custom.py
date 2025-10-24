from odoo import api, fields, models
from ..code import woocommerce_utils as wu
from ..code import odoo_utils as ou
from datetime import date, datetime


class sale_order_template(models.Model):
    _inherit = "sale.order"

    ecommerce_order_id = fields.Char('Order id.', copy=False, readonly=True)
    ecommerce_order_ref = fields.Char('Order ref.', copy=False, readonly=True)

    def SetOrderStatusWPcancelled(self):
        wp_order_status = 'cancelled'

        for record in self:
            if record.state == 'cancel':
                # No order ref
                if not record.ecommerce_order_ref:
                    return

                # Updating order status on WP
                wp_order_upd_res = wu.wp_set_order_status(self, record.ecommerce_order_id, wp_order_status)

                # Recording note on the sale order
                if not wp_order_upd_res:
                    msg_body = f"ATTENZIONE - Stato ordine {record.ecommerce_order_ref} non aggiornato su WordPress"
                    ou.post_log_msg(record, msg_body, ou.Log_msg_type.Warn)
                else:
                    msg_body = f"Ordine {record.ecommerce_order_ref} annullato su WordPress"
                    ou.post_log_msg(record, msg_body, ou.Log_msg_type.Info)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    pricelist_item_id = fields.Many2one('product.pricelist.item',
                                        string='pricelist item',
                                        compute='compute_pricelist_item_id',
                                        store=True)

    # cerca una riga di una pricelist che abbia il prodotto con qta in promo
    def find_product_promo(self):
        for rec in self:

            today = datetime.now()
            rules = self.env['product.pricelist.item'].search(
                ['|',
                 ('product_tmpl_id', '=', rec.product_template_id.id),
                 ('product_id', '=', rec.product_id.id),
                 ('min_quantity', '<=', rec.product_uom_qty),
                 ('fixed_price', '=', rec.price_unit),
                 ('qty_salable', '>', 0)
                 ]
            )
            rule_active = rules.filtered(lambda r: (r.date_start is False or r.date_start <= today) and (
                        r.date_end is False or r.date_end >= today))
            if len(rule_active) > 1:
                rule_active = rule_active[0]
            return rule_active

    @api.depends('product_id', 'price_unit')
    def compute_pricelist_item_id(self):
        for rec in self:
            if rec.state in ['draft']:
                rec.pricelist_item_id = False

                if not rec.product_id:
                    return

                pricelist_item_id = rec.find_product_promo()
                rec.pricelist_item_id = pricelist_item_id.id
