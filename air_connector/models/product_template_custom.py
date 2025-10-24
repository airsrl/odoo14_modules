from odoo import api, fields, models, _
from datetime import datetime
from ..code import connector_utils as cu
from ..code import odoo_utils as ou
from ..code import woocommerce_utils as wu


class product_template_custom(models.Model):
    _inherit = "product.template"

    wp_sku = fields.Char(
        string="Sku code"
    )
    wp_product_id = fields.Char(
        string="WP product id",
        readonly=True,
        copy=False
    )
    wp_to_sync = fields.Boolean(
        string="Synchronize on Woocommerce",
        help="Check if you want this product to be Synchronized on WP.",
        default=False
    )
    wp_sync_stock = fields.Boolean(
        string="Synchronize stock qtys",
        help="Check if you want to Synchronized the stock quantitys on WP.",
        default=False
    )
    wp_stock_type = fields.Selection(
        [
            ('stock_qty', 'Stock qty'),
            ('always_available', 'Always available'),
            ('preorder', 'Preorder'),
            ('shadow', 'Shadow'),
            ('external', 'External/referral')
        ], string="Stock type", default='stock_qty'
    )
    wp_preorder_start = fields.Date(
        string="Preorder start"
    )
    wp_preorder_fee = fields.Monetary(
        string="Preorder fee"
    )
    wp_price = fields.Float(
        string="WP price", digits="Product Price",
    )
    wp_price_list_id = fields.Many2one(
        string="WP pricelist",
        comodel_name="product.pricelist",
        readonly=True
    )

    wp_shadow_start = fields.Date(
        string="Shadow start"
    )
    wp_shadow_end = fields.Date(
        string="Shadow end"
    )

    wp_short_description = fields.Html(
        string="Short description"
    )
    wp_long_description = fields.Html(
        string="Long description"
    )
    wp_sold_with_no_stock = fields.Selection(
        [('Yes', 'Yes'), ('No', 'No')],
        string="Can be sold with no stock",
        default='No',
        help="Check if you want this product be sold even when out of stock."
    )
    wp_product_name = fields.Char(
        string="Product name",
        help="Keep empty to use product name."
    )
    wp_category = fields.Char(
        string="Category",
        help="Keep empty to use product category."
    )
    wp_last_sync_date = fields.Datetime(
        string="Last sync date",
        readonly=True,
        copy=False
    )
    wp_image_attachment_id = fields.Integer(
        string="Odoo image attachment id",
        readonly=True,
        copy=False
    )
    wp_referral = fields.Char(
        string="Referral link"
    )
    wp_availability_warehouse = fields.Integer(
        string="Available Warehouse",
        compute='compute_warehouse_stock'
    )
    wp_availability_store = fields.Integer(
        string="Available Store",
        compute='compute_store_stock'
    )
    wp_availability_dealer = fields.Integer(
        string="Available Dealer",
        readonly=True,
        copy=False
    )

    def compute_warehouse_stock(self):
        warehouse_code = 'SEDE'
        warehouse_id = self.env['stock.location'].search([('location_id', '=', warehouse_code)], limit=1)

        product_product_ids = self.product_variant_ids
        warehouse_quantity = 0

        quant_env = self.env['stock.quant']
        for product_product_id in product_product_ids:
            warehouse_quantity += quant_env._get_available_quantity(product_product_id, warehouse_id)

        if warehouse_quantity:
            self.wp_availability_warehouse = warehouse_quantity
        else:
            self.wp_availability_warehouse = 0

    def compute_store_stock(self):
        store_code = 'NE_BG'
        store_id = self.env['stock.location'].search([('location_id', '=', store_code)], limit=1)

        product_product_ids = self.product_variant_ids
        store_quantity = 0

        quant_env = self.env['stock.quant']
        for product_product_id in product_product_ids:
            store_quantity += quant_env._get_available_quantity(product_product_id, store_id)

        if store_quantity:
            self.wp_availability_store = store_quantity
        else:
            self.wp_availability_store = 0

    @api.onchange('wp_stock_type')
    def set_preorder_product(self):
        if self.wp_stock_type == 'preorder':
            product_id = self.id
            wu.wp_sync_product(self, product_id)

    def compute_wp_price_list_id(self):
        """ Cerca il listino con il prezzo più economico per il prodotto corrente"""
        qty = 1
        date = datetime.utcnow().date()
        index = 0
        for record in self:
            index += 1
            if index % 100 == 0:
                ou.log_info(index)
            try:
                pricelist_env = self.env['product.pricelist.item']

                # Listini per singolo prodotto
                pricelist_item_by_product_tmpl = pricelist_env.search_read(
                    [
                        ('product_tmpl_id', '=', record.id),
                        '|', ('qty_promo', '=', 0), ('qty_salable', '>', 0),
                        '|', ('date_start', '<=', date), ('date_start', '=', False),
                        '|', ('date_end', '>=', date), ('date_end', '=', False),
                        ('applied_on', 'in', ['1_product'])
                    ],
                    ['pricelist_id']
                )

                # Listini per categoria prodotto
                pricelist_item_product_category = pricelist_env.search_read(
                    [
                        ('applied_on', '=', '2_product_category'),
                        '|', ('qty_promo', '=', 0), ('qty_salable', '>', 0),
                        '|', ('date_start', '<=', date), ('date_start', '=', False),
                        '|', ('date_end', '>=', date), ('date_end', '=', False),
                        ('categ_id', 'parent_of', record.categ_id.id)
                    ],
                    ['pricelist_id']
                )

                # Listini generici
                pricelist_item_gloabl = pricelist_env.search_read(
                    [
                        ('applied_on', '=', '3_global'),
                        '|', ('qty_promo', '=', 0), ('qty_salable', '>', 0),
                        '|', ('date_start', '<=', date), ('date_start', '=', False),
                        '|', ('date_end', '>=', date), ('date_end', '=', False),
                    ],
                    ['pricelist_id']
                )

                # Cerco in tutti i listini quello con il prezzo più economico
                pricelist_item = pricelist_item_by_product_tmpl + pricelist_item_gloabl + pricelist_item_product_category
                if pricelist_item:
                    pricelist_list = [self.env['product.pricelist'].browse(plist['pricelist_id'][0]) for plist in
                                      pricelist_item]

                    pricelist_price = []
                    for pricelist in pricelist_list:
                        final_price, rule_id = pricelist.get_product_price_rule(record, qty, None)
                        pricelist_price.append(
                            {
                                'pricelist_id': pricelist,
                                'final_price': final_price
                            }
                        )
                    if pricelist_price:
                        minPricedItem = min(pricelist_price, key=lambda x: x['final_price'])
                        price_list_id = minPricedItem['pricelist_id']
                        price_data = {}
                        if record.wp_price_list_id != price_list_id:
                            price_data.update({'wp_price_list_id': price_list_id.id})
                        if record.wp_price != minPricedItem['final_price']:
                            price_data.update({'wp_price': minPricedItem['final_price']})
                        if price_data:
                            record.write(price_data)
                    else:
                        if record.wp_price_list_id:
                            record.wp_price_list_id = None
                else:
                    price_data = {}
                    if record.wp_price_list_id:
                        price_data.update({'wp_price_list_id': None})
                    if record.wp_price != record.list_price:
                        price_data.update({'wp_price': record.list_price})
                    if price_data:
                        record.write(price_data)
            except Exception as e:
                ou.log_error(f'product.template - compute_wp_price_list_id - {e}')

    @api.onchange('wp_price_list_id')
    def on_change_wp_price_list_id(self):
        for record in self:
            if record.wp_price_list_id:
                price = record.wp_price_list_id.get_product_price(record._origin, 1, None, datetime.today(), None)
                record.wp_price = price
            else:
                record.wp_price = record.list_price

    @api.model
    def create(self, values):
        res = None

        try:
            if 'wp_to_sync' in values and bool(values['wp_to_sync']):
                # Imposto di default il codice EAN (barcode) del prodotto per i nuovi prodotti da sincronizzare su WP
                if 'wp_sku' not in values and 'barcode' in values and values['barcode']:
                    values['wp_sku'] = values['barcode']

                if 'wp_price' in values and values['wp_price']:
                    values['wp_price'] = 0

                # Immagine prodotto WP
                if 'wp_to_sync' in values and bool(values['wp_to_sync']):
                    if values['image_1920']:
                        # Carico l'immagine per il prodotto su WP
                        image_datas = values['image_1920']
                        uploaded_img = ou.upload_doc_attachment(
                            self.env,
                            f'prd_img_{self.default_code}',
                            image_datas,
                            'product.template',
                            self.id,
                            True
                        )
                        if uploaded_img:
                            values['wp_image_attachment_id'] = uploaded_img.id
                    else:
                        # Immagine di default
                        default_image = ou.get_default_image(self.env)
                        values['image_1920'] = default_image['datas']
                        values['wp_image_attachment_id'] = default_image['id']

                    res = super(product_template_custom, self).create(values)

                    if res and res.id:
                        """ Adding entry to Connector log for product image"""
                        cu.add_new_log_entry(
                            self,
                            'product.template',
                            res.id,
                            'sync_product_image',
                            cu.log_status.pending,
                            'product.template - create'
                        )
                        """ Adding entry to Connector log for product infos"""
                        cu.add_new_log_entry(
                            self,
                            'product.template',
                            res.id,
                            'sync_product',
                            cu.log_status.pending,
                            'product.template - create'
                        )
            else:
                res = super(product_template_custom, self).create(values)
        except Exception as e:
            ou.log_error(f'product.template - create - {e}')

        if not res:
            res = super(product_template_custom, self).create(values)
        return res

    def write(self, values):
        try:
            for record in self:

                if 'wp_to_sync' in values and not bool(values['wp_to_sync']):
                    # Rimuovo la pubblicazione del prodotto da WP rendendolo privato
                    cu.add_new_log_entry(
                        self,
                        'product.template',
                        record.id,
                        'sync_product_set_to_private',
                        cu.log_status.pending,
                        'product.template - write'
                    )

                if 'wp_to_sync' in values and not record.wp_sku and record.default_code and 'wp_sku' not in values:
                    values['wp_sku'] = record.default_code

                # - AGGIORNAMENTO IMMAGINE PRODOTTO -
                if record.wp_to_sync or ('wp_to_sync' in values and bool(values['wp_to_sync'])):
                    if 'image_1920' in values:
                        ou.log_info(f'PT image_1920')
                        if not values['image_1920']:
                            ou.log_info(f'Immagine rimossa, metto quella di default')
                            # Cancello la vecchia immagine
                            ou.delete_doc_attachment(self.env, record.wp_image_attachment_id)
                            # Immagine rimossa, metto quella di default
                            default_image = ou.get_default_image(self.env)
                            values['image_1920'] = default_image['datas']
                            values['wp_image_attachment_id'] = default_image['id']
                        else:
                            ou.log_info(f'Immagine modificata, aggiorno l\'immagine')
                            # Immagine modificata, aggiorno l'immagine
                            # Cancello la vecchia immagine
                            ou.delete_doc_attachment(self.env, record.wp_image_attachment_id)
                            # Carico l'immagine per il prodotto su WP
                            image_datas = values['image_1920']
                            uploaded_img = ou.upload_doc_attachment(
                                self.env,
                                f'prd_img_{record.default_code}',
                                image_datas,
                                'product.template',
                                record.id,
                                True)
                            if uploaded_img:
                                values['wp_image_attachment_id'] = uploaded_img.id

                        """ Adding entry to Connector log for product image"""
                        cu.add_new_log_entry(
                            self,
                            'product.template',
                            record.id,
                            'sync_product_image',
                            cu.log_status.pending,
                            'product.template - write'
                        )
                    else:
                        if not record.wp_image_attachment_id:
                            if not record.image_1920:
                                # Immagine mancante, metto quella di default
                                default_image = ou.get_default_image(self.env)
                                ou.log_info(f'default_image {default_image}')
                                values['image_1920'] = default_image['datas']
                                values['wp_image_attachment_id'] = default_image['id']
                            else:
                                # Immagine modificata, aggiorno l'immagine
                                # Carico l'immagine per il prodotto su WP
                                image_datas = record.image_1920
                                uploaded_img = ou.upload_doc_attachment(
                                    self.env,
                                    f'prd_img_{record.default_code}',
                                    image_datas, 'product.template',
                                    record.id,
                                    True
                                )
                                if uploaded_img:
                                    values['wp_image_attachment_id'] = uploaded_img.id
                            """ Adding entry to Connector log for product image"""
                            cu.add_new_log_entry(
                                self,
                                'product.template',
                                record.id,
                                'sync_product_image',
                                cu.log_status.pending,
                                'product.template - write'
                            )

        except Exception as e:
            ou.log_error(f'product.template - write - {e}')

        res = super(product_template_custom, self).write(values)

        """ Adding entry to Connector log """
        for record in self:
            if 'wp_last_sync_date' not in values and record.wp_to_sync and bool(
                    record.wp_to_sync):  # To avoid going into an infinite loop...
                cu.add_new_log_entry(
                    record,
                    'product.template',
                    record.id,
                    'sync_product',
                    cu.log_status.pending,
                    'product.template - write'
                )
        return res
