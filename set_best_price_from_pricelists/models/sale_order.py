from odoo import fields, models, api
from datetime import datetime, date
from odoo.tools.misc import formatLang, get_lang

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    pricelist_option = fields.Selection(
        [
            ('standard', 'Applica listino '),
            ('most_convenient_line', 'Applica su ogni riga listino più conveniente')
        ],
        string='Modalità listino',
        default='standard',
        required=True
    )

    @api.onchange('pricelist_id', 'order_line', 'pricelist_option')
    def _onchange_pricelist_id(self):
        if self.order_line and self.pricelist_id and self._origin.pricelist_id != self.pricelist_id and self.pricelist_option == 'standard':
            self.show_update_pricelist = True
        elif self._origin.pricelist_option == 'most_convenient_line' and self.pricelist_option == 'standard':
            self.show_update_pricelist = True
        else:
            self.show_update_pricelist = False

    def set_most_convenient_pricelist_line(self):
        """Cerca le righe che hanno un prodotto """
        for line in self._get_update_prices_lines():
            # inserisce il pricelist nella riga
            line.pricelist_id = line.find_best_price_pricelist()
            line.product_uom_change()
            line.discount = 0.0
            line._onchange_discount()

    def update_prices(self):
        res = super(SaleOrder, self).update_prices()
        for line in self._get_update_prices_lines():
            line.pricelist_id = self.pricelist_id.id
        return res


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id')
    def product_id_change(self):
        # RISCRITTA SE C'E LA PRESENZA DI PRICELIST IN RIGA
        res = super(SaleOrderLine, self).product_id_change()

        if self.order_id.pricelist_option == 'most_convenient_line':
            if not self.product_id:
                return
            lang = get_lang(self.env, self.order_id.partner_id.lang).code
            pricelist_id = self.find_best_price_pricelist()
            product = self.product_id.with_context(
                lang=lang,
                partner=self.order_id.partner_id,
                quantity=self.product_uom_qty,
                date=self.order_id.date_order,
                pricelist=pricelist_id.id if pricelist_id else None,
                uom=self.product_uom.id
            )
            if pricelist_id and self.order_id.partner_id:
                price_unit = product._get_tax_included_unit_price(
                    self.company_id,
                    self.order_id.currency_id,
                    self.order_id.date_order,
                    'sale',
                    fiscal_position=self.order_id.fiscal_position_id,
                    product_price_unit=self._get_display_price(product),
                    product_currency=self.order_id.currency_id
                )
                if price_unit:
                    self.write(
                        {
                            'pricelist_id': pricelist_id.id if pricelist_id else None,
                            'price_unit': price_unit
                        }
                    )

        return res

    def _get_display_price(self, product):
        # RISCRITTA SE C'E LA PRESENZA DI PRICELIST IN RIGA
        if self.order_id.pricelist_option == 'most_convenient_line' and self.pricelist_id:
            no_variant_attributes_price_extra = [
                ptav.price_extra for ptav in self.product_no_variant_attribute_value_ids.filtered(
                    lambda ptav:
                    ptav.price_extra and
                    ptav not in product.product_template_attribute_value_ids
                )
            ]
            if no_variant_attributes_price_extra:
                product = product.with_context(
                    no_variant_attributes_price_extra=tuple(no_variant_attributes_price_extra)
                )

            if self.pricelist_id.discount_policy == 'with_discount':
                return product.with_context(pricelist=self.pricelist_id.id, uom=self.product_uom.id).price
            product_context = dict(
                self.env.context,
                partner_id=self.order_id.partner_id.id,
                date=self.order_id.date_order,
                uom=self.product_uom.id
            )

            final_price, rule_id = self.pricelist_id.with_context(product_context).get_product_price_rule(
                product or self.product_id, self.product_uom_qty or 1.0, self.order_id.partner_id)
            base_price, currency = self.with_context(product_context)._get_real_price_currency(product, rule_id,
                                                                                               self.product_uom_qty,
                                                                                               self.product_uom,
                                                                                               self.pricelist_id.id)
            if currency != self.pricelist_id.currency_id:
                base_price = currency._convert(
                    base_price, self.pricelist_id.currency_id,
                    self.order_id.company_id or self.env.company, self.order_id.date_order or fields.Date.today())
            # negative discounts (= surcharge) are included in the display price
            return max(base_price, final_price)
        else:
            # FUNZIONE BASE
            return super(SaleOrderLine, self)._get_display_price(product)

    @api.onchange('product_id', 'price_unit', 'product_uom', 'product_uom_qty', 'tax_id')
    def _onchange_discount(self):
        res = super(SaleOrderLine, self)._onchange_discount()
        if self.order_id.pricelist_option == 'most_convenient_line' and self.pricelist_id:
            # OVERWRITE FUNZIONE BASE INSERENDO LA PRICELIST_ID DELLA RIGA
            if not (self.product_id and self.product_uom and
                    self.order_id.partner_id and self.pricelist_id and
                    self.pricelist_id.discount_policy == 'without_discount' and
                    self.env.user.has_group('product.group_discount_per_so_line')):
                return

            self.discount = 0.0
            product = self.product_id.with_context(
                lang=self.order_id.partner_id.lang,
                partner=self.order_id.partner_id,
                quantity=self.product_uom_qty,
                date=self.order_id.date_order,
                pricelist=self.pricelist_id.id,
                uom=self.product_uom.id,
                fiscal_position=self.env.context.get('fiscal_position')
            )

            product_context = dict(self.env.context, partner_id=self.order_id.partner_id.id,
                                   date=self.order_id.date_order,
                                   uom=self.product_uom.id)

            price, rule_id = self.pricelist_id.with_context(product_context).get_product_price_rule(
                self.product_id, self.product_uom_qty or 1.0, self.order_id.partner_id)
            new_list_price, currency = self.with_context(product_context)._get_real_price_currency(product, rule_id,
                                                                                                   self.product_uom_qty,
                                                                                                   self.product_uom,
                                                                                                   self.pricelist_id.id)

            if new_list_price != 0:
                if self.pricelist_id.currency_id != currency:
                    # we need new_list_price in the same currency as price, which is in the SO's pricelist's currency
                    new_list_price = currency._convert(
                        new_list_price, self.pricelist_id.currency_id,
                        self.order_id.company_id or self.env.company, self.order_id.date_order or fields.Date.today())
                discount = (new_list_price - price) / new_list_price * 100
                if (discount > 0 and new_list_price > 0) or (discount < 0 and new_list_price < 0):
                    self.discount = discount
        return res

    @api.onchange('product_uom', 'product_uom_qty')
    def product_uom_change(self):
        res = super(SaleOrderLine, self).product_uom_change()
        if self.order_id.pricelist_option == 'most_convenient_line' and self.pricelist_id:
            # OVERWRITE FUNZIONE BASE INSERENDO LA PRICELIST_ID DELLA RIGA
            if not self.product_uom or not self.product_id:
                self.price_unit = 0.0
                return
            # Cambia pricelist in base alla qtà minima più conveniente
            new_pricelist = self.find_best_price_pricelist(self.product_uom_qty)
            if new_pricelist != self.pricelist_id:
                self.pricelist_id = new_pricelist.id
            if self.pricelist_id and self.order_id.partner_id:
                product = self.product_id.with_context(
                    lang=self.order_id.partner_id.lang,
                    partner=self.order_id.partner_id,
                    quantity=self.product_uom_qty,
                    date=self.order_id.date_order,
                    pricelist=self.pricelist_id.id,
                    uom=self.product_uom.id,
                    fiscal_position=self.env.context.get('fiscal_position')
                )
                self.price_unit = product._get_tax_included_unit_price(
                    self.company_id,
                    self.order_id.currency_id,
                    self.order_id.date_order,
                    'sale',
                    fiscal_position=self.order_id.fiscal_position_id,
                    product_price_unit=self._get_display_price(product),
                    product_currency=self.order_id.currency_id
                )
        return res

    def find_best_price_pricelist(self, qty=0):
        date=datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
        pricelist_item_by_product = self.env['product.pricelist.item'].search([ ('product_tmpl_id', '=', self.product_template_id.id),('date_end', '=', date)],limit=1)
        if not qty:
            qty = self.product_uom_qty
        """Cerca la pricelist con il prezzo più basso per prodotto partendo dalle righe"""
        if self.product_id:
            pricelist_price = []
            pricelist_item_by_product = self.env['product.pricelist.item'].search_read(
                [
                    ('product_id', '=', self.product_id.id),
                    ('date_start', '<=', date),
                    ('date_end', '>=', date),
                    ('min_quantity', '<=', qty),
                    ('applied_on', 'in', ['0_product_variant'])
                ],
                ['pricelist_id']
            )
            pricelist_item_by_product_tmpl = self.env['product.pricelist.item'].search_read(
                [
                    ('product_tmpl_id', '=', self.product_template_id.id),
                    ('date_start', '<=', date),
                    ('date_end', '>=', date),
                    ('min_quantity', '<=', qty),
                    ('applied_on', 'in', ['1_product'])
                ],
                ['pricelist_id']
            )
            pricelist_item_general_product = self.env['product.pricelist.item'].search_read(
                [
                    ('applied_on', '=', '3_global'),
                    ('date_start', '<=', date),
                    ('date_end', '>=', date),
                    ('min_quantity', '<=', qty)],
                ['pricelist_id']
            )
            pricelist_item_product_category = self.env['product.pricelist.item'].search_read(
                [
                    ('applied_on', '=', '2_product_category'),
                    ('date_start', '<=', date),
                    ('date_end', '>=', date),
                    ('categ_id', '=', self.product_id.categ_id.id),
                    ('min_quantity', '<=', qty)],
                ['pricelist_id']
            )
            pricelist_allways_valid = self.env['product.pricelist.item'].search_read(
                ['|', '|',
                 '&',
                 ('date_start', '=', False),
                 ('date_end', '=', False),
                 '&',
                 ('date_start', '=', False),
                 ('date_end', '>=', date),
                 '&',
                 ('date_start', '<=', date),
                 ('date_end', '=', False)
                 ],
                ['pricelist_id']
            )
            pricelist_item = pricelist_item_by_product + pricelist_item_general_product + pricelist_item_product_category +  pricelist_allways_valid
            if pricelist_item or pricelist_item_by_product_tmpl:
                pricelist_list = [self.env['product.pricelist'].browse(plist['pricelist_id'][0]) for plist in
                                  pricelist_item]

                for pricelist in pricelist_list:
                    final_price, rule_id = pricelist.get_product_price_rule(
                        self.product_id, self.product_uom_qty or 1.0, self.order_id.partner_id,date=date)
                    if rule_id :
                        pricelist_price.append(
                            {
                                'pricelist_id': pricelist,
                                'final_price': final_price

                            }
                        )
                pricelist_by_product_tmpl_list = [self.env['product.pricelist'].browse(plist['pricelist_id'][0]) for plist
                                              in pricelist_item_by_product_tmpl]
                for pricelist in pricelist_by_product_tmpl_list:
                    final_price, rule_id = pricelist.get_product_price_rule(
                        self.product_template_id, self.product_uom_qty or 1.0, self.order_id.partner_id,date=date)
                    if rule_id :
                        pricelist_price.append(
                            {
                                'pricelist_id': pricelist,
                                'final_price': final_price
                            }
                        )
                if pricelist_price:
                    minPricedItem = min(pricelist_price, key=lambda x: x['final_price'])
                    return minPricedItem['pricelist_id']

            else:

                return self.order_id.pricelist_id

    pricelist_id = fields.Many2one('product.pricelist',
                                   string='Pricelist',
                                   readonly=True)
