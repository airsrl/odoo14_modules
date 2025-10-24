import datetime

from odoo import fields, models, api
from ..code import odoo_utils as ou


class catalogo_prodotti(models.Model):
    _name = "ak_connettore.catalogo_prodotti"
    _description = "Prodotto"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sync_last_date = fields.Datetime(string="Aggiornato da distr.", readonly=True, copy=False)
    sync_to_odoo_last_date = fields.Datetime(string="Aggiornato in Odoo", readonly=True, copy=False)
    sync_source = fields.Char(string="Source", readonly=True, copy=False)
    sync_hash = fields.Char(string="Hash", readonly=True, copy=False)

    importare_in_odoo = fields.Boolean(string="Sincronizzare con Odoo", default=False)

    name = fields.Char(string="Nome")
    marchio_id = fields.Many2one('ak_connettore.marchio', string="Marchio")
    distributore_id = fields.Many2one('ak_connettore.distributore', string="Distributore")
    distributore_product_id = fields.Char(string="ID prodotto distributore", copy=False)
    odoo_product_id = fields.Many2one('product.template', string="Prodotto Odoo", copy=False)
    ean = fields.Char(string="EAN", copy=False)
    categoria_fornitore = fields.Char(string="Cat. fornitore")
    codice_articolo = fields.Char(string="Cod. articolo")
    descrizione = fields.Char(string="Descrizione")
    produttore = fields.Char(string="Produttore")
    descrizione_produttore = fields.Char(string="Desc. produttore")
    iva = fields.Float(string="IVA", default=0.22)
    descrizione_iva = fields.Char(string="Desc. iva")
    peso = fields.Float(string="Peso")
    giacenza_distributore = fields.Float(string="Giacenza distr.", copy=False)
    giacenza_odoo = fields.Float(string="Giacenza Odoo", compute="_compute_giacenza_odoo")
    prezzo = fields.Float(string="Prezzo distr.")
    prezzo_calcolato = fields.Float(string="Prezzo + margine", compute="_coumpute_prezzo_calcolato")
    prezzo_calcolato_ivato = fields.Float(string="Prezzo + margine + IVA", compute="_coumpute_prezzo_calcolato_ivato")
    prezzo_imposto = fields.Float(string="Prezzo imposto")
    prezzo_bloccato = fields.Boolean("Prezzo bloccato", default=True)
    note = fields.Text(string="Note")
    url_product = fields.Char(string='Url prodotto')
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        compute='_compute_currency_id'
    )

    def _compute_currency_id(self):
        self.currency_id = self.env.company.currency_id

    @api.depends('odoo_product_id')
    def _compute_giacenza_odoo(self):
        """Recupera la giacenza del prodotto a magazzino in Odoo"""
        for record in self:
            record.giacenza_odoo = 0
            if record.odoo_product_id:
                record.giacenza_odoo = record.odoo_product_id.qty_available

    def _coumpute_prezzo_calcolato(self):
        default_iva = 0.22
        """ Calcolo del prezzo in base al setup_margini
            L'arrotondamento (quello al 0,9 etc) dovrebbe essere sul prezzo ivato """
        env_setup_margini = self.env['ak_connettore.setup_margini']
        for record in self:
            record.prezzo_calcolato = record.prezzo or 0

            if record.prezzo and record.prezzo > 0:
                margine = env_setup_margini.search([('da', '<', record.prezzo), ('a', '>=', record.prezzo)], limit=1)
                if margine:
                    prezzo_arrotondato = prezzo_calcolato = (record.prezzo * (1 + float(margine['ricarico'])))
                    if margine['arrotondamento']:
                        prezzo_arrotondato = ou.get_rounded_amount(prezzo_calcolato, float(margine['arrotondamento']), record.iva or default_iva)

                    record.prezzo_calcolato = prezzo_arrotondato

    def _coumpute_prezzo_calcolato_ivato(self):
        for record in self:
            record.prezzo_calcolato_ivato = record.prezzo_calcolato * (1 + record.iva)

    def sync_catalogo_prodotto_odoo(self, forza_importare_in_odoo=True):
        """Aggiorna il prodotto in Odoo (product.template)"""

        qta_minima_distributore_aggiornamento_prezzi = 2

        env_product_template = self.env['product.template']
        env_ak_categorie = self.env['ak_connettore.categoria']

        # Recupero le rotte di magazzino per impostare il MTO e l'acquisto
        route_mto = self.sudo().env.ref('stock.warehouse0').mto_pull_id.route_id.id
        buy_route = self.sudo().env.ref('stock.warehouse0').buy_pull_id.route_id.id

        for record in self:
            try:
                odoo_product_id = None
                if record.importare_in_odoo or forza_importare_in_odoo:
                    # Cat prodotto da sincronizzare col prodotto Odoo
                    if record.odoo_product_id:
                        odoo_product_id = record.odoo_product_id
                    else:
                        # Cat prodotto non collegato ad un prodotto Odoo, lo cerco per EAN
                        if record.ean:
                            odoo_product_id = env_product_template.search([('barcode', '=', record.ean)], limit=1)
                            record.odoo_product_id = odoo_product_id

                    if not odoo_product_id:
                        # Creo il prodotto (visto che non esiste come odoo_product_id collegato al Cat prodtto e non si trova per EAN)
                        ak_categoria = env_ak_categorie.search([('name', '=', record.categoria_fornitore)], limit=1)

                        if ak_categoria and ak_categoria.categoria_mappata:
                            categ_id = ak_categoria.categoria_mappata.id
                        else:
                            categ_id = None

                        # Dati prodotto
                        product = {
                            'type': 'product',
                            'categ_id': categ_id or 1,
                            'default_code': record.ean,
                            'barcode': record.ean,
                            'name': record.name,
                            'seller_code': record.distributore_product_id,
                            'sale_ok': True,
                            'purchase_ok': True,
                            'description': record.descrizione,
                            'standard_price': record.prezzo,
                            'sync_last_date': record.sync_last_date,
                            'sync_hash': record.sync_hash,
                            'sync_source': record.sync_source,
                            'route_ids': [(6, 0, [route_mto, buy_route])]  # Di default i nuovi prodotti hanno MTO più acquisto
                        }

                        if not record.prezzo_bloccato:
                            # Se il prezzo non è 'bloccato' impostiamo il prezzo calcolato
                            # altrimenti non viene modificato
                            product['list_price'] = record.prezzo_calcolato
                            product['wp_price'] = record.prezzo_calcolato

                        odoo_product_id = env_product_template.create(product)

                    ou.LogInfo(f'odoo_product_id: {odoo_product_id}.')

                    if odoo_product_id:
                        # Cerco nel catalogo prodotti cercando il prezzo più basso fra tutti i distributori
                        # che hanno quel prodotto sincronizzato con quelli di Odoo
                        # e che hanno la giacenza minima > di qta_minima_distributore_aggiornamento_prezzi
                        odoo_product_id._get_best_dealer_catalogo_fornitore()

                        # Aggiorno il tab acquisto fornitori
                        if record.giacenza_distributore >= qta_minima_distributore_aggiornamento_prezzi:
                            ou.get_or_create_fornitore_prodotto(
                                record.env,
                                odoo_product_id=odoo_product_id,
                                idFornitore=record.distributore_id.contact_id.id,
                                productCodeForn=record.codice_articolo,
                                prezzo=record.prezzo
                            )
                        else:
                            odoo_product_id.seller_ids.filtered(lambda r: r.name <= record.distributore_id.contact_id).unlink()

                        # Aggiorno catalogo_prodotto con l'id del prodotto di Odoo
                        record.write(
                            {
                                'odoo_product_id': odoo_product_id.id,
                                'importare_in_odoo': True,
                                'sync_to_odoo_last_date': datetime.datetime.utcnow()
                            }
                        )
                else:
                    # Cat prodotto da NON sincronizzare col prodotto Odoo
                    # quindi sostituire eventualmente il fornitore ed eventualmente rimuoverlo dai potenziali fornitori scheda acquisti
                    if record.odoo_product_id:
                        # Cat prodotto da non importare, ma se è stato precedentemente collegato ad un prodotto Odoo
                        record.odoo_product_id._get_best_dealer_catalogo_fornitore()
                        # elimino il fornitore dai possibili fornitori nella scheda acquisto
                        record.odoo_product_id.seller_ids.filtered(lambda r: r.name <= record.distributore_id.contact_id).unlink()
                        # Aggiorno catalogo_prodotto con l'id del prodotto di Odoo
                        record.write(
                            {
                                'sync_to_odoo_last_date': datetime.datetime.utcnow()
                            }
                        )
            except Exception as ex:
                ou.LogError(f'sync_catalogo_prodotti_odoo {record.id} - {record.name[0:20]} - {ex}')
                ou.LogException(ex)
                pass

    def scheduler_sync_catalogo_prodotto_odoo(self, max_limit=1000):
        try:
            products = self.env['ak_connettore.catalogo_prodotti'].search([('importare_in_odoo', '=', True)])
            res_prod_to_sinc = products.filtered(lambda x: not x.sync_to_odoo_last_date or not x.sync_last_date or (x.sync_last_date > x.sync_to_odoo_last_date))
            ou.LogInfo(f'Num sync catalogo fornitori in Odoo {len(res_prod_to_sinc)}. Elaboro i primi {max_limit}.')
            for prod in res_prod_to_sinc[0:max_limit]:
                try:
                    # Nell'azione dello scheduler automatico importiamo solo i prodotti con il flag importare_in_odoo = True
                    # la forzatura viene lanciata solo dal pulsante presente nella form del catalogo prodotti
                    prod.sync_catalogo_prodotto_odoo(forza_importare_in_odoo=False)
                except Exception as ex:
                    ou.LogError(f'scheduler_sync_catalogo_prodotto_odoo {ex}')
                    ou.LogException(ex)
        except Exception as ex:
            ou.LogError(f'scheduler_sync_catalogo_prodotto_odoo {ex}')
            ou.LogException(ex)
