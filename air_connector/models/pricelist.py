from odoo import fields, models, api


class ProductPricelist(models.Model):
    _inherit = 'product.pricelist'

    date_start = fields.Date('Data inizio')
    date_end = fields.Date('Data fine')
    wp_tag_listino = fields.Char('Tag Woocommerce')

    def write(self, vals):
        res = super(ProductPricelist, self).write(vals)
        try:
            if self.date_start:
                for item in self.item_ids:
                    item.write({'date_start': self.date_start, 'date_end': self.date_end})
        except Exception as ex:
            pass
        return res

    @api.model
    def create(self, vals):
        res = super(ProductPricelist, self).create(vals)
        try:
            if res.date_start and res.date_start < res.date_end:
                for item in res.item_ids:
                    item.write({'date_start': res.date_start, 'date_end': res.date_end})
        except Exception as ex:
            pass
        return res
