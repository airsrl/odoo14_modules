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