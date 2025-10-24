from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
	_inherit = 'res.config.settings'

	# Wordpress settings
	wp_url = fields.Char(string='WP Url')
	wp_consumer_key = fields.Char(string='WP consumer_key')
	wp_consumer_secret = fields.Char(string='WP consumer_secret')
	wp_version = fields.Char(string='WP version', default='wc/v3')
	wp_product_quantity_field = fields.Selection([('qty_available', 'On hand quantity'), ('virtual_available', 'Virtual quantity')], string="Quantity field",
												 default='qty_available',
												 help="Value to use when updating stock quantity on WP.")
	wp_sync_max_limit = fields.Integer(string='Sync records max limit', default=50,
										help="Number of log records every sync should elaborate")

	# Order flow steps
	auto_create_invoice = fields.Boolean(string='Create invoice')
	auto_confirm_invoice = fields.Boolean(string='Confirm invoice')
	auto_register_payment = fields.Boolean(string='Register payment')

	wp_default_image = fields.Binary(string='Product default image',
									  help="Default image for product to be passed to WP if the product has no picture.")
	wp_product_fields_mapping = fields.Text(string='Odoo-WP product fields mapping array',
											help='Array of field mapping in the form [("odoo_field_1","wp_field_1"),("odoo_field_2","wp_field_2"),(...)]')

	def set_values(self):
		super(ResConfigSettings, self).set_values()
		icp_sudo = self.env['ir.config_parameter'].sudo()

		icp_sudo.set_param('air_connector.wp_url', self.wp_url)
		icp_sudo.set_param('air_connector.wp_consumer_key', self.wp_consumer_key)
		icp_sudo.set_param('air_connector.wp_consumer_secret', self.wp_consumer_secret)
		icp_sudo.set_param('air_connector.wp_version', self.wp_version)
		icp_sudo.set_param('air_connector.wp_product_quantity_field', self.wp_product_quantity_field)
		icp_sudo.set_param('air_connector.wp_sync_max_limit', self.wp_sync_max_limit)

		icp_sudo.set_param('air_connector.auto_create_invoice', self.auto_create_invoice)
		icp_sudo.set_param('air_connector.auto_confirm_invoice', self.auto_confirm_invoice)
		icp_sudo.set_param('air_connector.auto_register_payment', self.auto_register_payment)

		icp_sudo.set_param('air_connector.wp_default_image', self.wp_default_image)
		icp_sudo.set_param('air_connector.wp_product_fields_mapping', self.wp_product_fields_mapping)

	def get_values(self):
		res = super(ResConfigSettings, self).get_values()
		icp_sudo = self.env['ir.config_parameter'].sudo()
		res.update({
			'wp_url': icp_sudo.get_param('air_connector.wp_url'),
			'wp_consumer_key': icp_sudo.get_param('air_connector.wp_consumer_key'),
			'wp_consumer_secret': icp_sudo.get_param('air_connector.wp_consumer_secret'),
			'wp_version': icp_sudo.get_param('air_connector.wp_version'),
			'wp_product_quantity_field': icp_sudo.get_param('air_connector.wp_product_quantity_field'),
			'wp_sync_max_limit': icp_sudo.get_param('air_connector.wp_sync_max_limit'),

			'auto_create_invoice': icp_sudo.get_param('air_connector.auto_create_invoice'),
			'auto_confirm_invoice': icp_sudo.get_param('air_connector.auto_confirm_invoice'),
			'auto_register_payment': icp_sudo.get_param('air_connector.auto_register_payment'),
			'wp_default_image': icp_sudo.get_param('air_connector.wp_default_image'),
			'wp_product_fields_mapping': icp_sudo.get_param('air_connector.wp_product_fields_mapping')
		})
		return res
