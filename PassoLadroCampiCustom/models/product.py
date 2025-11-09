import logging

import requests

from odoo import api, fields, models, _


class product_template_custom(models.Model):
	_inherit = "product.template"
	_description = "Campi aggiuntivi modulo product.template"

	default_code_padre = fields.Char(string="Riferimento interno padre")

	descrizione_breve = fields.Html(string="Descrizione breve")
	descrizione_lunga = fields.Html(string="Descrizione lunga")

	pubblica_su_ecommerce = fields.Boolean(string="Pubblica su e-commerce", help="Spuntare la casella per pubblicare l'articolo su ecommerce", default=True)
	classe_spedizione = fields.Selection([
						('Nessuna classe di spedizione', 'Nessuna classe di spedizione'),
						('Cassette', 'Cassette'),
						('Gourmet', 'Gourmet')   
						], string="Classe di spedizione")


class product_product_custom(models.Model):
	_inherit = "product.product"
	_description = "Campi aggiuntivi modulo product.product"

	pubblica_su_ecommerce = fields.Boolean(string="Pubblica su e-commerce",
										   help="Spuntare la casella per pubblicare la variante su ecommerce",
										   default=True)

	descrizione_breve = fields.Html(string="Descrizione breve")
	descrizione_lunga = fields.Html(string="Descrizione lunga")


class SaleOrder(models.Model):
	_inherit = 'sale.order'

	wc_amount = fields.Float(string="Totale Woocommerce")
	sync_wc = fields.Boolean(string="Sincronizzato Woocommerce")
	wc_total_diff = fields.Boolean(string="Diferenze totale Woocommerce")

	def import_woocommerce_data(self):
		orders = self.search([('sync_wc', '=', False), ('client_order_ref', '!=', False), ('date_order', '>=', '2025-10-01'), ('state', '=', 'sale'), ('invoice_status', '=', 'to invoice')], order='date_order asc')
		for order in orders:
			if 'PL' in order.client_order_ref:
				BASE_URL = "https://passoladro.it"  # senza / finale

				order_ref = int(order.client_order_ref.split("_")[2])

				base_url = BASE_URL.rstrip("/")
				url = f"{base_url}/wp-json/wc/v3/orders/{order_ref}"

				params = {
					"consumer_key": "ck_05fbce404918ec33f6ae580289144c6b9f09416b",
					"consumer_secret": "cs_db5f80a5cff624cde678c6ad8ed0eccad0c40f8e",
				}

				try:
					resp = requests.get(url, params=params)
					resp.raise_for_status()
				except requests.RequestException as e:
					raise RuntimeError(f"Errore chiamando WooCommerce: {e}")

				data = resp.json()

				wc_amount = float(data['total'])
				order.write({
					'wc_amount': wc_amount,
					'sync_wc': True
				})

				wc_amount_rounded = round(wc_amount, 2)
				odoo_amount_rounded = round(order.amount_total, 2)
				if wc_amount_rounded == odoo_amount_rounded:
					if order.invoice_status == 'to invoice':
						invoices = order._create_invoices(grouped=False, final=False)
						invoices.action_post()
						logging.info("FATTURA CREATA %s" % order.name)
				else:
					order.write({
						'wc_total_diff': True
					})

				self.env.cr.commit()
