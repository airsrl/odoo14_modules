from odoo import models, fields, api
from ..code import connector_utils as cu
from ..code import odoo_utils as ou


class product_pricelist_custom(models.Model):
    _inherit = "product.pricelist"

    def write(self, values):
        try:
            for record in self:
                for prd_tmp_id in record.item_ids.mapped("product_tmpl_id"):
                    ou.log_info(f'prd_tmp_id - {prd_tmp_id.id}')
                    if prd_tmp_id.wp_to_sync and bool(prd_tmp_id.wp_to_sync):
                        cu.add_new_log_entry(self, 'product.template', prd_tmp_id.id, 'sync_pricelist',
                                             cu.log_status.pending, 'product.pricelist - write')
        except Exception as e:
            ou.log_error(f'product_pricelist_custom - write - {e}')

        write_res = super(product_pricelist_custom, self).write(values)
        return write_res

    def scheduler_pricelist_upd(self):
        # Per ogni prodotto che va su WP ricalcolo il listino più conveniente e aggiorno il prezzo
        pr = self.env['product.template'].search([('wp_to_sync', '=', True)])
        try:
            pr.compute_wp_price_list_id()
        except Exception as e:
            ou.log_error(f'product_pricelist_custom - scheduler_pricelist_upd - {e}')


class ProductPricelistItem(models.Model):
    _inherit = 'product.pricelist.item'

    qty_promo = fields.Float('Qty max promo')
    qty_salable = fields.Float('Qty residua', compute='compute_qty_salable', store=True)
    sale_line_ids = fields.One2many('sale.order.line', 'pricelist_item_id', string='Ordini')

    @api.depends('sale_line_ids.state', 'sale_line_ids.product_uom_qty', 'sale_line_ids', 'qty_promo')
    def compute_qty_salable(self):
        for rec in self:
            qty_sold = sum([line.product_uom_qty for line in
                            rec.sale_line_ids.filtered(lambda line: line.state not in ['draft', 'cancel'])])
            rec.qty_salable = rec.qty_promo - qty_sold

            # if the promo is expired, immediately recompute the pricelist linked to the product
            if rec.qty_promo and rec.qty_salable <= 0:
                if rec.product_tmpl_id and rec.product_tmpl_id.wp_to_sync:
                    rec.product_tmpl_id.compute_wp_price_list_id()
                elif not rec.product_tmpl_id and rec.product_id and rec.product_id.product_tmpl_id.wp_to_sync:
                    rec.product_id.product_tmpl_id.compute_wp_price_list_id()
