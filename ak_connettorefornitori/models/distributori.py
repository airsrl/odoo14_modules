from odoo import fields, models, api
import datetime
from ..code import odoo_utils as ou

from odoo.exceptions import MissingError


def get_catalogo_prodotto(name, distributore_id, distributore_product_id, ean, categoria_fornitore,
                          codice_articolo, descrizione, produttore, descrizione_produttore, iva, descrizione_iva,
                          peso, giacenza_distributore, prezzo, note):
    catalogo_prodotto = {
        'name': name,
        'distributore_id': distributore_id,
        'distributore_product_id': distributore_product_id,
        'ean': ean,
        'categoria_fornitore': categoria_fornitore,
        'codice_articolo': codice_articolo,
        'descrizione': descrizione,
        'produttore': produttore,
        'descrizione_produttore': descrizione_produttore,
        'iva': iva,
        'descrizione_iva': descrizione_iva,
        'peso': peso,
        'giacenza_distributore': giacenza_distributore,
        'prezzo': prezzo,
        'note': note
    }
    return catalogo_prodotto


class distributore(models.Model):
    _name = "ak_connettore.distributore"
    _description = "Distributore"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nome", required=True)
    contact_id = fields.Many2one('res.partner', string="Contatto", required=True)
    abilitato = fields.Boolean(string="Abilitato", required=True, default=True)
    id_anag = fields.Integer(string="ID Anag")
    gg_spec = fields.Integer(string="GG Spec.")
    url = fields.Char(string="URL")
    host = fields.Char(string="Host")
    directory = fields.Char(string="Directory")
    login = fields.Char(string="Login")
    password = fields.Char(string="Password")
    dropshipping = fields.Boolean(string="Dropshipping", default=False)
    ultimo_sync = fields.Datetime(string="Ultimo sync", readonly=True)
    note = fields.Text(string="Note")

    categorie_ids = fields.One2many('ak_connettore.categoria', 'categoria_mappata', string="Categorie")
    categorie_count = fields.Char(string="Num categorie", compute="_compute_products_count")

    @api.depends("categorie_ids")
    def _compute_products_count(self):
        self.categorie_count = '0'
        env_categoria = self.env["ak_connettore.categoria"]
        cat_tot = env_categoria.search([("distributore_id", "in", self.ids)])
        cat_val = env_categoria.search([("distributore_id", "in", self.ids), ("categoria_mappata", "!=", False)])
        if cat_tot:
            self.categorie_count = f"{len(cat_val)} su {len(cat_tot)}"

    def button_widget_categorie(self):
        return {'name': 'Categoria',
                'type': 'ir.actions.act_window',
                'res_model': 'ak_connettore.categoria',
                'view_id': False,
                'domain': "[('distributore_id','=', active_id)]",
                'view_mode': 'tree,form'}

    def sync_catalogo_prodotto(self, catalogo_prodotto):
        """ Inserisce un prodotto nella tabella catalogo prodotti """

        # ou.LogInfo(f'sync_catalogo_prodotto: {catalogo_prodotto}')

        sync_last_date = datetime.datetime.now()
        sync_source = self.name

        catalogo_prodotto['sync_hash'] = ou.GetHash(catalogo_prodotto)
        catalogo_prodotto['sync_source'] = sync_source
        catalogo_prodotto['sync_last_date'] = sync_last_date
        catalogo_prodotto['distributore_id'] = self.id

        # Cerco il prodotto per id prodotto e id fornitore
        env_catalogo_prodotti = self.env['ak_connettore.catalogo_prodotti']
        searched_prd = None
        if 'distributore_product_id' in catalogo_prodotto:
            # Cerco il prodotto per il codice del distributore
            searched_prd = env_catalogo_prodotti.search(
                [("distributore_product_id", "=", catalogo_prodotto['distributore_product_id']),
                 ("distributore_id", "=", self.id)], limit=1)

        # Se non viene trovato cerca per barcode o codice articolo
        if not searched_prd and catalogo_prodotto['ean'] and catalogo_prodotto['ean'] != '0000000000000' and catalogo_prodotto['ean'] != '':
            searched_prd = env_catalogo_prodotti.search([("ean", "=", catalogo_prodotto['ean'])])
            if searched_prd and len(searched_prd) > 1:
                raise BaseException(f'Trovati {len(searched_prd)} prodotti con ean {catalogo_prodotto["ean"]}')

        if not searched_prd:
            new_prd = env_catalogo_prodotti.create(catalogo_prodotto)
            ou.LogInfo(f"{catalogo_prodotto['codice_articolo']} - {catalogo_prodotto['name'][0:20]} INS: {new_prd.id}")
        else:
            searched_prd.write(catalogo_prodotto)
            ou.LogInfo(f"{catalogo_prodotto['codice_articolo']} - {catalogo_prodotto['name'][0:20]} UPD: {searched_prd.id}")

        self.update({'ultimo_sync': sync_last_date})
        return True

    def sync_categorie(self):
        """Aggiorna la tabella delle categorie con le nuove categorie del catalogo prodotti """
        env_categoria = self.env['ak_connettore.categoria']
        env_cat_prodotti = self.env['ak_connettore.catalogo_prodotti']

        # Recupero tutte le categorie esistenti
        categorie = env_categoria.search_read([], ['name', 'distributore_id'])

        # Ricerco le cateogorie dei prodotti importati
        src_filter = [] if not self.id else [('distributore_id', '=', self.id)]
        categorie_cat_prodotti = env_cat_prodotti.read_group(src_filter,
                                                             fields=['categoria_fornitore', 'distributore_id'],
                                                             groupby=['categoria_fornitore', 'distributore_id'],
                                                             lazy=False)

        # Cerco ed eventualmente inserisco le nuove categorie
        for cat in categorie_cat_prodotti:
            found = next((c for c in categorie if
                          c['name'].lower() == cat['categoria_fornitore'].lower() and c['distributore_id'] == cat[
                              'distributore_id']), None)
            if not found:
                env_categoria.create({'name': cat['categoria_fornitore'], 'distributore_id': cat['distributore_id'][0]})

    def distributore_sync_products(self):
        """ Seleziona quale API chiamare in base al nome del fornitore.
        Non è una gran genialata ma per il momento dovrebbe bastare """

        # L'IMPORTAZIONE DEGLI ARTICOLI DAI FORNITORI E' STATO
        # SPOSTOSTATO SU SCRIPT ESTERNO CHE GIRA SUL SERVER DI AK

        # name = self.name.lower()
        # if 'tech' in name:
        #     self.techdata_sync_products()
        #     return
        # if 'gross' in name:
        #     self.cg_sync_products()
        #     return
        # if 'runner' in name:
        #     self.runner_sync_products()
        #     return
        # if 'bestit' in name:
        #     self.bestit_sync_products()
        #     return
        # if 'brevi' in name:
        #     self.brevi_sync_products()
        #     return
        # if 'abaco' in name:
        #     self.abaco_sync_products()
        #     return
        # if 'ingram' in name:
        #     return self.ingram_sync_products()
        # if 'next' in name:
        #     return self.next_sync_products()
        # if 'loginform' in name:
        #     return self.loginform_sync_products()
        # if 'focelda' in name:
        #     return self.focelda_sync_products()
        # # if 'esprinet' in name:
        # #     return self.esprinet_sync_products()
        raise MissingError(f'FUNZIONE SPOSTATA SU SCRIPT ESTERNO CHE GIRA SUL SERVER DI AK')

    def reset_all_distributor_stock(self):
        """ If the distributor is not active ('abilitato' == False), reset the stock for all of its products that
            are synchronized on Odoo. Update the sync_last_date, or the product won't be updated on Odoo.
            Once the distributor is active again, stock quantity will be updated automatically. """

        self.ensure_one()
        if not self.abilitato:
            self.env['ak_connettore.catalogo_prodotti'].search([('distributore_id', '=', self.id),
                                                                ('importare_in_odoo', '=', True)]).write(
                {'giacenza_distributore': 0,
                 'sync_last_date': datetime.datetime.utcnow(),
                 'sync_hash': ''})
