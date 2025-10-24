from odoo import fields, models
from ..code import odoo_utils as ou
import logging

# Logging
logger = logging.getLogger(__name__)


class product_template_custom(models.Model):
    _inherit = 'product.template'

    seller_code = fields.Char('Codice Distributore')
    marchio_id = fields.Many2one('ak_connettore.marchio', string="Marchio")

    scheda_tecnica = fields.Html(string="Scheda tecnica")

    # sync_prezzo_bloccato = fields.Boolean("Prezzo bloccato")
    sync_last_date = fields.Datetime("Last synchronization", readonly=True)
    sync_source = fields.Char(string="Source", readonly=True)
    sync_hash = fields.Char(string="Hash", readonly=True)

    def _get_best_dealer_catalogo_fornitore(self, qta_minima_distributore_aggiornamento_prezzi=2):
        env_catalogo_prodotti = self.env['ak_connettore.catalogo_prodotti']

        for record in self:
            # Cerco nel catalogo prodotti cercando il prezzo più basso fra tutti i distributori
            # che hanno quel prodotto sincronizzato con quelli di Odoo
            # e che hanno la giacenza minima > di qta_minima_distributore_aggiornamento_prezzi

            # Tutti i distributori del prodotto corrente
            all_prod_distr_dealers = env_catalogo_prodotti.search(
                [
                    ('importare_in_odoo', '=', True),  # Flag importare in Odoo
                    ('odoo_product_id', '=', record.id),  # Prodotto Odoo collegato a elenco prodotti
                ], order='prezzo asc')
            logger.info(f'all_prod_distr_dealers: {all_prod_distr_dealers}')

            # Se un solo prodotto ha la spunta 'prezzo bloccato' non bisogna aggiornare il prezzo di vendita
            # nella scheda prodotto Odoo
            is_prezzo_bloccato = len([pd for pd in all_prod_distr_dealers if bool(pd['prezzo_bloccato'])])
            logger.info(f'is_prezzo_bloccato: {is_prezzo_bloccato}')

            # Distributori con la quantità minima necessaria
            qt_min_prod_distr_dealers = [pd for pd in all_prod_distr_dealers if
                                         pd['giacenza_distributore'] >= qta_minima_distributore_aggiornamento_prezzi]
            logger.info(f'qt_min_prod_distr_dealers: {qt_min_prod_distr_dealers}')

            # Distributore col miglior prezzo e la quantità minima necessaria
            cat_prod_best_dealer = qt_min_prod_distr_dealers[0] if len(qt_min_prod_distr_dealers) > 0 else None
            logger.info(f'cat_prod_best_dealer: {cat_prod_best_dealer}')

            if cat_prod_best_dealer:
                # Miglior distributore trovato con giacenza minima
                # Prezzo = quello del distributore
                # Giacenza = quella del distributore
                prd_data_upd = {
                    'standard_price': cat_prod_best_dealer.prezzo,
                    'wp_availability_dealer': cat_prod_best_dealer.giacenza_distributore,
                    'sync_source': cat_prod_best_dealer.distributore_id.name,
                    'sync_last_date': cat_prod_best_dealer.sync_last_date
                }
            else:
                # Nessun distributore ha la quantità minima
                # tengo buono il miglior distributore solo in base al prezzo
                cat_prod_best_dealer = all_prod_distr_dealers[0] if len(all_prod_distr_dealers) > 0 else None
                if cat_prod_best_dealer:
                    # Miglior distributore trovato senza giacenza minima
                    # Prezzo = quello del distributore
                    # Giacenza = 0
                    prd_data_upd = {
                        'standard_price': cat_prod_best_dealer.prezzo,
                        'wp_availability_dealer': 0,
                        'sync_source': cat_prod_best_dealer.distributore_id.name,
                        'sync_last_date': cat_prod_best_dealer.sync_last_date
                    }
                else:
                    # Nessun distributore disponibile
                    # Prezzo = 0
                    # Giacenza = 0
                    prd_data_upd = {
                        'standard_price': 0,
                        'wp_availability_dealer': 0,
                        'sync_source': None,
                        'sync_last_date': fields.datetime.utcnow()
                    }

            if cat_prod_best_dealer and not is_prezzo_bloccato:
                # Se il prezzo non è 'bloccato' impostiamo il prezzo di vendita calcolato
                # altrimenti non viene modificato
                prd_data_upd['list_price'] = cat_prod_best_dealer.prezzo_calcolato

                # Rimuovo sempre tutti gli eventuali distributori perchè tanto vengono aggiornati più sotto
            prd_data_upd['seller_ids'] = [(5, 0, 0)]

            # Aggiorno il prodotto Odoo
            logger.info(f'prd_data_upd: {prd_data_upd}')
            record.write(prd_data_upd)

            # Aggiorno l'elenco dei distributori
            for pd in qt_min_prod_distr_dealers:
                ou.get_or_create_fornitore_prodotto(
                    record.env,
                    odoo_product_id=record,
                    idFornitore=pd.distributore_id.contact_id.id,
                    productCodeForn=pd.codice_articolo,
                    prezzo=pd.prezzo
                )
