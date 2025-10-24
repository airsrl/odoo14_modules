import datetime
import time

from woocommerce import API

from odoo.exceptions import UserError
from . import odoo_utils as ou


def get_wp_api(self):
    # WP access configuration
    config_sudo = self.env['res.config.settings'].sudo()
    url = config_sudo.get_values()['wp_url']
    consumer_key = config_sudo.get_values()['wp_consumer_key']
    consumer_secret = config_sudo.get_values()['wp_consumer_secret']
    version = config_sudo.get_values()['wp_version']

    if not url or url == '':
        raise UserError('Missing or wrong Url parameter in settings')
    if not consumer_key or consumer_key == '':
        raise UserError('Missing or wrong Consumer key parameter in settings')
    if not consumer_secret or consumer_secret == '':
        raise UserError('Missing or wrong Consumer secret parameter in settings')
    if not version or version == '':
        raise UserError('Missing or wrong Version parameter in settings')

    return API(url=url, consumer_key=consumer_key, consumer_secret=consumer_secret, version=version)


wp_categories = []
def wp_get_all_categories(wp_api):
    global wp_categories
    num_page = 1
    page_size = 100
    wp_categories = wp_categories_partial = wp_api.get("products/categories", params={'per_page': page_size, 'page': num_page}).json()
    while len(wp_categories_partial) == page_size and num_page < 10:
        num_page += 1
        wp_categories_partial = wp_api.get("products/categories", params={'per_page': page_size, 'page': num_page}).json()
        for c in wp_categories_partial:
            wp_categories.append(c)


def wp_get_tag(wp_api, tag_name):
    wp_api.version = 'wp/2'
    wp_tags = wp_api.get(f"product_tag")
    j_wp_tags = wp_tags.json()
    tag_id = next(x for x in j_wp_tags if x['name'] == tag_name)
    if tag_id and len(tag_id) == 1:
        return tag_id['id']
    else:
        return None


def wp_get_or_create_category_id(wp_api, category_name):
    global wp_categories

    # Cerco le categorie in wp
    if not wp_categories or len(wp_categories) == 0:
        wp_get_all_categories(wp_api)

    # Splitto la categoria per trovare eventuali categorie/sottocategorie
    categorie = category_name.split('/')
    # Controllo che ci siano le categorie, se non ci sono blocco tutto
    if len(wp_categories) == 0:
        raise Exception(f"wp_categories non presenti. Found: {len(wp_categories)}.")
        return -1
    else:
        res = []
        category_parent_id = None
        category_id = None
        for cat in categorie:
            cat = cat.strip()
            category_id = None

            # Check category exists
            wp_search_category = next((x for x in wp_categories if x['name'].lower() == cat.lower() and (
                    (not category_parent_id) or (category_parent_id and x['parent'] == category_parent_id))), None)

            # Get or create
            if wp_search_category:
                category_id = wp_search_category['id']
                category_parent_id = category_id
            else:
                slug = cat.lower().replace(' ', '-')
                data = {'name': cat, 'slug': slug}
                if category_parent_id:
                    data['parent'] = category_parent_id

                wp_new_category = wp_api.post("products/categories", data).json()

                category_id = wp_new_category['id']
                category_parent_id = category_id

                # Ricarico l'elenco delle categorie
                wp_get_all_categories(wp_api)

            res.append({"id": category_id})

    # Returning category data
    return res


wp_attributes = []
def wp_get_all_attributes(wp_api):
    global wp_attributes
    num_page = 1
    page_size = 100
    wp_attributes = wp_attributes_partial = wp_api.get("products/attributes",
                                                       params={'per_page': page_size, 'page': num_page}).json()
    while len(wp_attributes_partial) == page_size and num_page < 10:
        num_page += 1
        wp_attributes_partial = wp_api.get("products/attributes",
                                           params={'per_page': page_size, 'page': num_page}).json()
        for a in wp_attributes_partial:
            wp_attributes.append(a)


def wp_get_or_create_attribute_id(wp_api, attribute_name):
    global wp_attributes

    if len(wp_attributes) == 0:
        wp_get_all_attributes(wp_api)

    # Searching for the attribute
    for entry in wp_attributes:
        if entry['name'].lower() == attribute_name.lower():
            wp_attributeId = entry['id']
            return wp_attributeId

    # Create the attribute
    wp_attributeId = wp_api.post("products/attributes", {"name": attribute_name}).json()['id']
    wp_get_all_attributes(wp_api)

    return wp_attributeId


def wp_sync_stock_qty(self, product_id):
    res = ''
    sku = ''
    try:
        wp_api = get_wp_api(self)
        wp_product_quantity_field = ou.get_config_value(self.env, 'wp_product_quantity_field')  # get_wp_product_quantity_field(self)

        # Get the product
        odoo_product = self.env['product.product'].browse(product_id)
        if not odoo_product:
            res = f'Sync stock product product not found {product_id}'
            return False, res
        else:
            odoo_product = odoo_product.product_tmpl_id

        if not odoo_product or not odoo_product.wp_product_id or not odoo_product.wp_to_sync:
            res = f'Sync stock non da sincronizzare su WP'
            return True, res

        # Get variants num
        variant_count = int(odoo_product.product_variant_count)

        # wp_sync_stock = bool(odoo_product.wp_sync_stock)
        wp_sync_stock = bool(odoo_product.wp_stock_type in ['stock_qty', 'always_available', 'preorder'])
        wp_product_id = odoo_product.wp_product_id
        wp_sold_with_no_stock = bool(odoo_product.wp_stock_type == 'always_available')
        sku = odoo_product.wp_sku
        ou.log_info(f'odoo_product: {odoo_product} - sku: {sku}')

        odoo_total_product_availability = odoo_product.wp_availability_dealer + odoo_product.wp_availability_store + odoo_product.wp_availability_warehouse

        if not wp_sync_stock:
            res = f'Sync stock {odoo_product.default_code}: {wp_sync_stock}. WP id: {wp_product_id or "-"}'
            return True, res

        # Searching for the product on WP
        wp_products = None
        if wp_product_id:
            wp_products = wp_api.get(f'products/{wp_product_id}').json()

        # Not found by id
        if not wp_products or ('data' in wp_products and wp_products['data']['status'] == 404):
            wp_products = wp_api.get("products", params={'sku': sku})
            if wp_products:
                wp_products_res = wp_products.json()
                if len(wp_products_res) == 1:
                    wp_product = wp_products_res[0]
                    wp_product_id = wp_product['id']
                else:
                    wp_product_id = None
            else:
                wp_product_id = None

        # Stock management
        wp_product_data = {}
        if not wp_sold_with_no_stock:
            wp_product_data['stock_quantity'] = odoo_total_product_availability
            wp_product_data['manage_stock'] = odoo_product.type == "product" and variant_count == 1
            upd_qty = odoo_product[wp_product_quantity_field]
        else:
            wp_product_data['stock_status'] = 'instock'
            wp_product_data['manage_stock'] = False
            upd_qty = 'status instock'

        meta_data = []
        # Disponibilità prodotto (on-line, negozio, magazzino) in base alla quantità presente nel relativo magazzino
        meta_data.append({'key': 'disponibile_online', 'value': odoo_product.wp_to_sync})
        meta_data.append({'key': 'disponibile_negozio', 'value': odoo_product.wp_availability_store > 0})
        meta_data.append({'key': 'disponibile_sede', 'value': odoo_product.wp_availability_warehouse > 0})

        # Preorder - METADATI
        meta_data.append({'key': '_wc_pre_orders_enabled', 'value': 'yes' if odoo_product.wp_stock_type == 'preorder' and odoo_total_product_availability <= 0 else 'no'})
        if odoo_product.wp_stock_type == 'preorder':
            wp_product_data['manage_stock'] = False
            odoo_total_product_availability = odoo_product.wp_availability_dealer + odoo_product.wp_availability_store + odoo_product.wp_availability_warehouse
            if odoo_total_product_availability > 0:
                wp_product_data['manage_stock'] = True
                wp_product_data['stock_quantity'] = odoo_total_product_availability
                wp_product_data['backorders'] = 'no'
            else:
                wp_product_data['manage_stock'] = True
                wp_product_data['stock_quantity'] = 0
                wp_product_data['backorders'] = 'notify'

            meta_data.append({'key': '_wc_pre_orders_fee', 'value': float(odoo_product.wp_preorder_fee)})
            if odoo_product.wp_preorder_fee:
                meta_data.append({'key': '_wc_pre_orders_fee', 'value': float(odoo_product.wp_preorder_fee)})
            if odoo_product.wp_preorder_start:
                dt = time.mktime(odoo_product.wp_preorder_start.timetuple())
                meta_data.append({'key': '_wc_pre_orders_availability_datetime', 'value': dt})

        wp_product_data['meta_data'] = meta_data

        if variant_count == 1:
            wp_product = wp_api.post(f"products/{wp_product_id}", wp_product_data)
        else:
            ou.log_info(f"products/{odoo_product.wp_product_id}/variations/{odoo_product.wp_product_id}")
            wp_product = wp_api.post(f"products/{odoo_product.wp_product_id}/variations/{wp_product_id}", wp_product_data)

        if not wp_product or not bool(wp_product.ok):
            res = f'Sync stock {sku} NOT upd on WP. {wp_product.reason} {wp_product.text}'
            ou.log_warn(res)
            return False, res
        else:
            res = f'Sync stock {sku} upd {upd_qty} on WP. {wp_product.reason}: {wp_product_id}'
            ou.log_info(res)

    except Exception as ex:
        ou.log_exception(ex)
        res = f'📌 *** ERROR *** wp_sync_stock_qty {sku} - ex: {ex}'
        ou.log_error(ex)

        return False, res

    return True, res


def wp_product_set_to_private(self, product_id):
    res = ''
    status = 'private'
    try:
        wp_api = get_wp_api(self)
        # Get the product
        odoo_product = self.env['product.template'].browse(product_id)
        if not odoo_product or not odoo_product.wp_product_id:
            raise Exception(f'wp_product_set_to_private: Product template not found: {product_id}')

        wp_product = wp_api.post(f"products/{odoo_product.wp_product_id}", {'status': status})

        if not wp_product or not bool(wp_product.ok):
            res = f'Sync prd {odoo_product.default_code} set status {status} on WP. {wp_product.reason}: {product_id}'
            raise Exception(res)
        else:
            res = f'Sync prd {odoo_product.default_code} set status {status}. WP {wp_product.reason} {odoo_product.wp_product_id}'

        return wp_product.json()['status'] == status, res
    except Exception as e:
        ou.log_exception(e)
        return False, e


def wp_sync_product_image(self, product_id):
    res = ''
    try:
        # Get the product
        odoo_product = self.env['product.template'].browse(product_id)
        # Immagine prodotto
        if odoo_product.wp_image_attachment_id:

            base_url = self.env['ir.config_parameter'].get_param('web.base.url')
            # DA LOCALHOST NON CARICO L'IMMAGINE (CHIARAMENTE NON HA SENSO)
            if 'localhost' not in base_url:
                img_url = f'{base_url}/web/image/{odoo_product["wp_image_attachment_id"]}/prd_img_{odoo_product["id"]}.jpg'
                wp_product_data = {'images': [{'src': img_url}]}
                wp_api = get_wp_api(self)
                if odoo_product.wp_product_id:
                    res_wp = wp_api.post(f"products/{odoo_product.wp_product_id}", wp_product_data)
                    ou.log_info(f'wp_product {res_wp} {wp_product_data}')
                    if not res_wp.ok:
                        res = f'Sync prd img {odoo_product.default_code} NOT upd on WP. {res_wp.reason} - {res_wp.text}'
                        ou.log_warn(res)
                        return False, f'wp_product: {res_wp.text}'
                    else:
                        res = f'Sync prd img {odoo_product.default_code} upd on WP. {res_wp.reason}: {odoo_product.wp_product_id}'
                        ou.log_info(res)
                else:
                    res = f'Sync prd img {odoo_product.default_code} wp_product_id is empty'

            else:
                res = 'LOCALHOST'
    except Exception as e:
        ou.log_exception(e)
        return False, res

    return True, res


def wp_sync_product(self, product_id):
    res = ''

    try:
        wp_api = get_wp_api(self)
        wp_product_quantity_field = ou.get_config_value(self.env, 'wp_product_quantity_field')  # get_wp_product_quantity_field(self)

        # Get the product
        odoo_product = self.env['product.template'].browse(product_id)

        if not odoo_product:
            raise Exception(f'Product template not found. product_id: {product_id}')

        wp_to_sync = bool(odoo_product.wp_to_sync)
        wp_product_id = odoo_product.wp_product_id
        wp_sold_with_no_stock = odoo_product.wp_stock_type == 'always_available'
        name = odoo_product.wp_product_name or odoo_product.name
        sku = odoo_product.wp_sku

        # Calcolata come la somma fra quantità fra i 2 magazzini + la quantità del fornitore (wp_availability_dealer)
        odoo_total_product_availability = odoo_product.wp_availability_dealer + odoo_product.wp_availability_store + odoo_product.wp_availability_warehouse

        # ou.log_info(f 'odoo_product wp_category: {odoo_product.wp_category}')

        # Searching for the product on WP
        wp_product = None
        if wp_product_id:
            wp_product = wp_api.get(f'products/{wp_product_id}').json()

        # ou.log_info(f'wp_product: {wp_product}')

        # Not found by id
        if not wp_product or ('data' in wp_product and wp_product['data']['status'] == 404):
            wp_products = wp_api.get("products", params={'sku': sku})
            if wp_products:
                wp_products_res = wp_products.json()
                if len(wp_products_res) == 1:
                    wp_product = wp_products_res[0]
                    wp_product_id = wp_product['id']
                else:
                    wp_product_id = None
            else:
                wp_product_id = None

        if wp_to_sync:
            if not wp_product_id:
                # Crate new product in draft status
                status = 'draft'
            else:
                # Keep current status
                status = None
        else:
            ou.log_info(f'Synchronize on WP not to be sync. product_id: {product_id}')
            return True, f'Synchronize on WP not to be sync. product_id: {product_id}'

        if not sku:
            ou.log_warn(f'wp_sku is empty. product_id: {product_id}')

        # Get or create category in WP
        wp_category_id = None
        category = odoo_product.wp_category or odoo_product.categ_id.name if odoo_product.categ_id and not odoo_product.categ_id.wp_avoid_sync else None
        if category:
            wp_category_id = wp_get_or_create_category_id(wp_api, category)

        # Get variants num
        variant_count = int(odoo_product['product_variant_count'])
        # ou.log_info(f'variant_count: {variant_count}')

        # WP object data
        wp_product_data = {'name': name,
                           'regular_price': str(odoo_product.list_price),
                           'sku': sku,
                           'manage_stock': True}

        product_type = 'simple'

        # Stock management
        if wp_sold_with_no_stock:
            wp_product_data['stock_status'] = 'instock'
            wp_product_data['manage_stock'] = False
            wp_product_data['backorders'] = 'no'
        else:
            wp_product_data['stock_quantity'] = odoo_total_product_availability
            wp_product_data['manage_stock'] = odoo_product["type"] == "product" and variant_count == 1
            wp_product_data['backorders'] = 'no'

        if variant_count > 1:
            product_type = 'variable'
        if odoo_product.wp_stock_type == 'external':
            product_type = 'external'
            wp_product_data['external_url'] = odoo_product.wp_referral
            wp_product_data['manage_stock'] = False

        # Prezzo ed eventuale listino del prodotto ed il relativo TAG
        if odoo_product.wp_price_list_id and odoo_product.wp_price_list_id.wp_tag_listino:
            list_tag = f'Listino {odoo_product.wp_price_list_id.wp_tag_listino}'
        else:
            list_tag = None
        if odoo_product.wp_price > 0:
            # Aggiorno anche il prezzo in offerta
            wp_product_data['sale_price'] = str(odoo_product.wp_price)
        else:
            wp_product_data['sale_price'] = str(odoo_product.list_price)

        if wp_product and wp_product.get('tags'):
            # Aggiorno i tag del prodotto in base al listino
            j_product = wp_product
            wp_product_tags = j_product['tags']
            # Elimino tutti i tag Listino_
            wp_product_tags = list(filter(lambda x: not x['name'].startswith('Listino '), wp_product_tags))
        else:
            wp_product_tags = []
        if list_tag:
            wp_product_tags.append({'name': list_tag})

        # Aggiorno i tag del prodotto
        wp_product_data['tags'] = wp_product_tags

        # Setting product type
        wp_product_data['type'] = product_type

        # Brand
        if 'marchio_id' in odoo_product and odoo_product['marchio_id']:
            wp_product_data['brands'] = [odoo_product.marchio_id.name] if odoo_product.marchio_id else None

        # Metadata (scheda tecnica, prevendite, etc...)
        meta_data = []

        # Schede tecniche - METADATI
        scheda_tecnica = ''
        if 'scheda_tecnica' in odoo_product and odoo_product["scheda_tecnica"]:
            scheda_tecnica = str(odoo_product["scheda_tecnica"]).replace('<p><br></p>', '')
        if scheda_tecnica and scheda_tecnica != '':
            meta_data.append({'key': 'tabella_prodotto_html', 'value': scheda_tecnica})
            meta_data.append({'key': 'abilita_tabella_prodotto_html', 'value': True})

        # Preorder - METADATI
        meta_data.append({'key': '_wc_pre_orders_enabled', 'value': 'yes' if odoo_product.wp_stock_type == 'preorder' and odoo_total_product_availability <= 0 else 'no'})
        if odoo_product.wp_stock_type == 'preorder':
            wp_product_data['manage_stock'] = False

            if odoo_total_product_availability > 0:
                wp_product_data['manage_stock'] = True
                wp_product_data['stock_quantity'] = odoo_total_product_availability
                wp_product_data['backorders'] = 'no'
            else:
                wp_product_data['manage_stock'] = True
                wp_product_data['stock_quantity'] = 0
                wp_product_data['backorders'] = 'notify'

            meta_data.append({'key': '_wc_pre_orders_fee', 'value': float(odoo_product.wp_preorder_fee)})
            if odoo_product.wp_preorder_fee:
                meta_data.append({'key': '_wc_pre_orders_fee', 'value': float(odoo_product.wp_preorder_fee)})
            if odoo_product.wp_preorder_start:
                dt = time.mktime(odoo_product.wp_preorder_start.timetuple())
                meta_data.append({'key': '_wc_pre_orders_availability_datetime', 'value': dt})

        # Shadow product
        meta_data.append({'key': 'shadow_enable', 'value': odoo_product.wp_stock_type == 'shadow'})
        if odoo_product.wp_stock_type == 'shadow' and odoo_product.wp_shadow_start:
            dt_start = time.mktime(odoo_product.wp_shadow_start.timetuple())
            meta_data.append({'key': 'shadow_start', 'value': dt_start})
        else:
            meta_data.append({'key': 'shadow_start', 'value': ''})

        if odoo_product.wp_stock_type == 'shadow' and odoo_product.wp_shadow_end:
            dt_end = time.mktime(odoo_product.wp_shadow_end.timetuple())
            meta_data.append({'key': 'shadow_end', 'value': dt_end})
        else:
            meta_data.append({'key': 'shadow_end', 'value': ''})

        # Disponibilità prodotto (on-line, negozio, magazzino) in base alla quantità presente nel relativo magazzino
        meta_data.append({'key': 'disponibile_online', 'value': odoo_product.wp_to_sync})
        meta_data.append({'key': 'disponibile_negozio', 'value': odoo_product.wp_availability_store > 0})
        meta_data.append({'key': 'disponibile_sede', 'value': odoo_product.wp_availability_warehouse > 0})

        # Salvo i metadati
        wp_product_data['meta_data'] = meta_data

        if odoo_product["wp_short_description"]:
            wp_short_description = str(odoo_product["wp_short_description"]).replace('<p><br></p>', '')
            if wp_short_description != '':
                wp_product_data["short_description"] = wp_short_description

        if odoo_product["wp_long_description"]:
            wp_long_description = str(odoo_product["wp_long_description"]).replace('<p><br></p>', '')
            if wp_long_description != '':
                wp_product_data["description"] = wp_long_description

        if wp_category_id:
            wp_product_data["categories"] = wp_category_id

        if status:
            wp_product_data["status"] = status

        # Creating attributes if there are product variants
        if variant_count > 1:
            variant_lines = self.env['product.template.attribute.line'].search([('product_tmpl_id', '=', product_id)])

            attributes = []
            for variant_line in variant_lines:
                odoo_attribute = variant_line.attribute_id.name
                wp_attribute_id = wp_get_or_create_attribute_id(wp_api, odoo_attribute)
                if wp_attribute_id:
                    attribute = {
                        'id': wp_attribute_id,
                        'visible': True,
                        'variation': True
                    }

                variant_values = self.env['product.template.attribute.value'].search(
                    [('product_tmpl_id', '=', product_id),
                     ('attribute_id', '=', variant_line.attribute_id.id)])

                # Building attributes values
                options = []
                for variant_value in variant_values:
                    options.append(variant_value.name)

                attribute['options'] = options
                attributes.append(attribute)

            # Update attributes in WP object data
            wp_product_data['attributes'] = attributes

        # Create or update product on WP
        if wp_product_id:  # UPDATE
            # ou.log_info(f'wp_product_data: {wp_product_data}')
            wp_product = wp_api.post(f"products/{wp_product_id}", wp_product_data)

            if not wp_product.ok:  # if 'id' not in wp_product:
                ou.log_warn(f'wp_product: {wp_product} wp_product_data: {wp_product_data}')
                return False, f'Sync prd {sku} upd in WP. {wp_product.reason} {wp_product.text}'
            else:
                res = f'Sync prd {sku} upd on WP. {wp_product.reason}: {wp_product_id}'
                ou.log_info(res)
        else:  # CREATE
            wp_product = wp_api.post("products", wp_product_data)

            if not wp_product.ok:  # if 'id' not in wp_product:
                ou.log_warn(f'wp_product: {wp_product} wp_product_data: {wp_product_data}')
                return False, f'Sync prd {sku} ins in WP. {wp_product.reason} {wp_product.text}'
            else:
                wp_product_id = wp_product.json()['id']
                res = f'Sync prd {sku} ins in WP. {wp_product.reason}: {wp_product_id}'
                ou.log_info(res)

        # ** ** ** ** ** ** ** *          ** ** ** ** ** ** ** *
        # ** ** ** ** ** ** ** * VARIANTS ** ** ** ** ** ** ** *
        # ** ** ** ** ** ** ** *          ** ** ** ** ** ** ** *

        if variant_count > 1:
            # ou.log_info(f'Product {sku} has {variant_count} variants')

            odoo_variants = self.env['product.product'].search(
                [
                    ('sale_ok', '=', True),
                    ('product_tmpl_id', '=', product_id)
                ]
            )
            odoo_variants_wp_ids = []
            for variant in odoo_variants:
                sku = variant['wp_sku']
                wp_variation_id = variant['wp_product_id']

                if not sku:
                    ou.log_warn(f'Variant has no sku: {variant["id"]}')
                    continue

                # Searching for the variation-product on WP
                wp_variations = None
                if wp_variation_id:
                    wp_variations = wp_api.get(f'products/{wp_variation_id}').json()

                # Not found by id
                if not wp_variations or ('data' in wp_variations and wp_variations['data']['status'] == 404):
                    wp_variations = wp_api.get("products", params={'sku': sku}).json()
                    if wp_variations:
                        if len(wp_variations) == 1:
                            wp_variation = wp_variations[0]
                            wp_variation_id = wp_variation['id']
                        else:
                            wp_variation_id = None
                    else:
                        wp_variation_id = None

                lst_price = float(variant["lst_price"])

                # WP variation data object
                variation_data = {
                    "name": variant["display_name"],
                    "sku": sku,
                    'regular_price': str(lst_price),
                    'manage_stock': True,
                    "stock_quantity": variant[wp_product_quantity_field],
                }

                # Setting attributes
                values = self.env['product.template.attribute.value'].browse(
                    variant.product_template_attribute_value_ids.id)

                attributes = []
                for value in values:
                    wp_attribute_id = wp_get_or_create_attribute_id(wp_api, value.attribute_id.name)
                    attribute = {
                        'id': wp_attribute_id,
                        'name': value.attribute_id.name,  # nella v12 non è attribute_line_id ma attribute_id
                        'option': value['name']
                    }
                    attributes.append(attribute)

                variation_data['attributes'] = attributes

                # Creating or updating variation
                if wp_variation_id:  # UPDATE
                    wp_variant = wp_api.post(f"products/{wp_product_id}/variations/{wp_variation_id}",
                                             variation_data).json()
                    if 'id' not in wp_variant:
                        res = f'UPDATE wp_variation_id: {wp_variation_id} - wp_variant: {wp_variant}'
                        ou.log_warn(res)
                        return False, res
                    else:
                        ou.log_info(f'Variant {sku} updated on wp. wp_variation_id: {wp_variant["id"]}')
                else:  # CREATE
                    wp_variant = wp_api.post("products/%s/variations" % str(wp_product_id), variation_data).json()
                    if 'id' not in wp_variant:
                        res = f'CREATE wp_variant: {wp_variant}'
                        ou.log_warn(res)
                        return False, res
                    else:
                        ou.log_info(f'Variant {sku} created on wp. wp_variation_id: {wp_variant["id"]}')
                        wp_variation_id = wp_variant['id']

                # Updating product.product
                variant.update({'wp_last_sync_date': datetime.datetime.now()})
                if not variant['wp_product_id']:
                    variant.update({'wp_product_id': wp_variation_id})

                odoo_variants_wp_ids.append(wp_variation_id)

            # Removing deleted variants from WP
            wordpress_variations = wp_api.get(f'products/{wp_product_id}/variations').json()
            for wp_variation in wordpress_variations:
                if wp_variation['id'] not in odoo_variants_wp_ids:
                    wp_api.post(f"products/{wp_product_id}/variations/{wp_variation['id']}", {'status': 'draft'}).json()
                    ou.log_info(
                        f'Variant {wp_variation["sku"]} set to draft on wp. wp_variation_id: {wp_variation["id"]}')

        # Updating product.template
        odoo_product_upd_res = self.env['product.template'].browse(product_id)
        odoo_product_upd = odoo_product_upd_res[0]
        if not odoo_product_upd['wp_product_id'] or odoo_product['wp_product_id'] != wp_product_id:
            odoo_product_upd.update({'wp_product_id': wp_product_id, 'wp_last_sync_date': datetime.datetime.now()})
        else:
            odoo_product_upd.update({'wp_last_sync_date': datetime.datetime.now()})

    except Exception as ex:
        ou.log_exception(ex)
        res = f'📌 *** ERROR *** wp_sync_product - ex: {ex}'
        ou.log_error(ex)

        return False, res

    return True, res


def wp_get_order_infos(self, order_id):
    try:
        wp_api = get_wp_api(self)
        wp_ord = wp_api.get(f'orders/{order_id}').json()

        # WP access configuration
        config_sudo = self.env['res.config.settings'].sudo()
        url = config_sudo.get_values()['wp_url']
        if not url.endswith('/'):
            url += '/'
        if not wp_ord or not 'id' in wp_ord:
            # Writing text in the log notes
            ou.post_log_msg(self, f'Something went wrong searching for the order {order_id}:<br/>'
                                  f'{wp_ord}', ou.Log_msg_type.Warn)
            return False

        wp_status = wp_ord['status']
        wp_order_ref = wp_ord['order_key']
        wp_customer_note = wp_ord['customer_note']
        wp_payment_method = f"{wp_ord['payment_method']} - {wp_ord['payment_method_title']}"
        wp_transaction_id = wp_ord['transaction_id'] or ''
        wp_date_paid = ou.get_local_date_time(wp_ord['date_paid_gmt']) if wp_ord['date_paid_gmt'] else ''

        wp_order_href = f'{url}wp-admin/post.php?post={order_id}&action=edit'
        text_res = f'<b><a href="{wp_order_href}" target="_blank">WP order #{order_id}</a></b><br/>' \
                   f'Status: {wp_status}<br/>' \
                   f'Payment method: {wp_payment_method}<br/>' \
                   f'Payment date: {wp_date_paid}<br/>'

        if wp_transaction_id and wp_transaction_id != '':
            text_res += f'Transaction id: {wp_transaction_id}<br/>'
        text_res += f'<br/>Customer notes: {wp_customer_note}'

        # Writing text in the log notes
        ou.post_log_msg(self, text_res, ou.Log_msg_type.Info)
        return True
    except Exception as ex:
        ou.log_exception(ex)
        res = f'📌 *** ERROR *** wp_get_order_infos - ex: {ex}'
        ou.log_error(ex)

        return False


def wp_set_order_status(self, wp_order_id, status):
    try:
        # Get the product
        wp_api = get_wp_api(self)
        wp_order = wp_api.post(f"orders/{wp_order_id}", {'status': status}).json()

        return wp_order['status'] == status
    except Exception as ex:
        ou.log_exception(ex)
        res = f'📌 *** ERROR *** wp_set_order_status wp_order_id: {wp_order_id} status: {status} - ex: {ex}'
        ou.log_error(ex)

        return False


def wp_upd_tracking_info(self, custom_tracking_provider, custom_tracking_link, tracking_number, date_shipped):
    try:
        # Get the product
        wp_api = get_wp_api(self)
        tracking_data = {'key': '_wc_shipment_tracking_items', 'value': [
            {'tracking_provider': '',
             'custom_tracking_provider': custom_tracking_provider,
             'custom_tracking_link': custom_tracking_link,
             'tracking_number': tracking_number,
             'date_shipped': datetime.datetime.timestamp(date_shipped)}]}

        meta_data = [tracking_data]
        wp_order_data = {'meta_data': meta_data}
        meta_data.append(tracking_data)
        wp_order_res = wp_api.post(f"orders/{self.sale_id.ecommerce_order_id}", wp_order_data).json()

        return wp_order_res.ok
    except Exception as ex:
        ou.log_exception(ex)
        res = f'📌 *** ERROR *** wp_upd_tracking_info record: {self.id} - ex: {ex}'
        ou.log_error(ex)

        return False


def wp_sync_product_pricelist(self, product_id):
    res = ''
    sku = None
    try:
        wp_api = get_wp_api(self)

        # Get the product
        odoo_product = self.env['product.template'].browse(product_id)

        if not odoo_product:
            raise Exception(f'wp_sync_product_pricelist: Product product not found: {product_id}')

        if not odoo_product.wp_product_id or not bool(odoo_product.wp_to_sync):
            res = f'Sync prd pricelist non da sincronizzare su WP'
            return True, res

        wp_product_id = odoo_product.wp_product_id
        wp_product = wp_api.get(f"products/{wp_product_id}")
        if not wp_product or not bool(wp_product.ok):
            res = f'Sync prd pricelist {odoo_product.default_code} not updated on WP. {wp_product.reason}: {product_id}'
            raise Exception(res)

        wp_product_data = {}

        # recompute wp_price and pricelist in case it is not updated yet
        odoo_product.compute_wp_price_list_id()

        # Prezzo ed eventuale listino del prodotto ed il relativo TAG
        if odoo_product.wp_price_list_id:
            list_tag = f'Listino {odoo_product.wp_price_list_id.wp_tag_listino}'
        else:
            list_tag = None
        if odoo_product.wp_price > 0:
            # Aggiorno anche il prezzo in offerta
            wp_product_data['sale_price'] = str(odoo_product.wp_price)
        else:
            wp_product_data['sale_price'] = str(odoo_product.list_price)

        # Aggiorno i tag del prodotto in base al listino
        j_product = wp_product.json()

        if j_product and j_product.get('tags'):
            wp_product_tags = j_product['tags']
            # Elimino tutti i tag Listino_
            wp_product_tags = list(filter(lambda x: not x['name'].startswith('Listino '), wp_product_tags))
        else:
            wp_product_tags = []

        if list_tag:
            wp_product_tags.append({'name': list_tag})

        # Aggiorno i tag del prodotto
        wp_product_data['tags'] = wp_product_tags

        wp_post_res = wp_api.post(f"products/{wp_product_id}", wp_product_data)
        ou.log_info(f'wp_post_res: {wp_post_res} - {wp_product_data}')
        if not wp_post_res or not bool(wp_post_res.ok):
            res = f'Sync product pricelist {odoo_product.default_code} NOT updated on WP. {wp_post_res.reason}: {wp_product_id}'
            raise Exception(res)
        else:
            res = f'Sync product {odoo_product.default_code} updated on WP. {wp_post_res.reason}: {wp_product_id}'

        return True, res
    except Exception as e:
        ou.log_exception(e)
        return False, e
