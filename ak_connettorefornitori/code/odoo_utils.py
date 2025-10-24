import datetime
import hashlib
import json
import logging
import math
import pytz
import traceback

""" import LoggingUtils as lu
import ConfigUtils as cu """

# Logging
logger = logging.getLogger(__name__)
errors = []


def is_dev_environment(env) -> bool:
    base_url = env['ir.config_parameter'].get_param('web.base.url')
    return 'dev.odoo' in base_url


# Restituisce data-ora nel fuso italiano (perchè odoo giustamente se lo salva UTC)
def GetLocalDateTime(date_time_UTC):
    timezoneLocal = pytz.timezone('Europe/Rome')
    utc = pytz.utc
    dateTimeLocal = utc.localize(date_time_UTC).astimezone(timezoneLocal)
    return dateTimeLocal


def GetLogger():
    return logger


def GetDateTime() -> str:
    now = datetime.datetime.now()  # current date and time
    return now.strftime("%d.%m.%y %H:%M:%S")


def LogInfo(msg):
    # logger = logging.getLogger(__name__)
    logger.info(msg)


def LogError(msg):
    # logger = logging.getLogger(__name__)
    logger.error(msg)


def LogErrorToDB(msg, env):
    logger.error(msg)

    # Scrivo il messaggio nei log di Odoo ir.logging
    env_logging = env['ir.logging']
    log_entry = {'create_uid': env.uid,
                 'type': 'server',
                 'name': 'ak_connettorefornitori',
                 'level': 'code',
                 'line': '0',
                 'function': 'ak_connettorefornitori',
                 'message': msg}
    env_logging.create(log_entry)


def LogWarn(msg):
    # logger = logging.getLogger(__name__)
    logger.warning(msg)


def LogException(ex):
    global errors
    # logger = logging.getLogger(__name__)
    logger.error("*** EXCEPTION ***")
    logger.error(ex)
    logger.error(traceback.format_exc())
    errors.append("%s - %s" % (GetDateTime(), ex))


def LogRecapEccezioni():
    global errors
    if len(errors) == 0:
        logging.info("\n******************************************************")
        logging.info("*** NESSUN ERRORE RISCONTRATO DURANTE L'ESECUZIONE ***")
        logging.info("******************************************************")
    else:
        logging.warning("\n***************************************************")
        logging.warning(f"*** {len(errors)} ERRORI RISCONTRATI DURANTE L'ESECUZIONE ***")
        logging.warning("***************************************************")

    # Mando la mail con il riepilogo delle eccezioni
    if len(errors) > 0:
        LogWarn(json.dumps(errors, indent=4, sort_keys=False))
        """ body = json.dumps(Eccezioni , indent=4, sort_keys=False)
        subject = f"CONNETTONE - {len(Eccezioni)} ECCEZIONI RISCONTRATE"
        email_to = cu.GetConfigValue('AIR_ErrorLog','emailSendErrorLog')
        eu.SendLogEmail(body,subject,email_to) """


def GetHash(text):
    try:
        hash_res = hashlib.md5(str(text).encode('utf-8')).hexdigest()
        return hash_res
    except Exception as e:
        LogError(f'GetHash {text} - {e}')
        return None


def _sort_vendors_by_price(odoo_product_id):
    today = datetime.datetime.utcnow().date()

    # Filtering by date start/end
    filtered_res = odoo_product_id.seller_ids.filtered(lambda r: not r.date_start or r.date_start <= today)
    filtered_res = filtered_res.filtered(lambda r: not r.date_end or r.date_end >= today)

    # Sorted by price
    sorted_res = filtered_res.sorted(key=lambda r: r.price)
    seq = 1
    for srt in sorted_res:
        seq += 1
        srt.write({'sequence': seq})

    # Setting a higher sequence to the expired records
    expired = odoo_product_id.seller_ids.filtered(lambda r: r not in sorted_res)
    seq += 10
    for ex in expired:
        seq += 1
        ex.write({'sequence': seq})


def get_or_create_fornitore_prodotto(env, odoo_product_id, idFornitore, productCodeForn, prezzo, delay=None, product_uom=None):
    try:
        # ricerca id fornitore in base a nome
        m_product_supplierinfo = env["product.supplierinfo"]

        # ricerca il fornitore di un prodotto, partendo dall'id del prodotto
        datiFornitore = m_product_supplierinfo.search(
            [
                ('product_tmpl_id', '=', odoo_product_id.id),
                ('name', '=', idFornitore)
            ]
            , limit=1
        )

        # se esiste, aggiorna prezzo
        data = {
            'product_tmpl_id': odoo_product_id.id,
            'product_code': productCodeForn,
            'price': prezzo
        }
        if delay:
            data['delay'] = delay
        if product_uom:
            data['product_uom'] = product_uom

        if datiFornitore:
            datiFornitore.write(data)

        # altrimenti, inserisci nome fornitore e prezzo
        else:
            data['name'] = idFornitore
            idNewSupplier = m_product_supplierinfo.create(data)

        # Ordino i fornitori per prezzo crescente
        _sort_vendors_by_price(odoo_product_id)
    except Exception as e:
        LogError(f'Fornitore: {idFornitore} idProdotto: {odoo_product_id} - {e}')
        return None


categoryDict = dict()
def GetOrCreateCategory(env,  odooCategoryName):
    try:
        if not odooCategoryName: return None

        if odooCategoryName in categoryDict:
            return categoryDict[odooCategoryName]

        m_product_category = env["product.category"]

        # Splitto la categoria per trovare eventuali categorie/sottocategorie
        categorie = odooCategoryName.split('/')

        idCategory = None
        parent_id = None
        for x in range(len(categorie)):
            categoria = categorie[x].capitalize()
            data = {"name": categoria}

            if x == 0:
                category_search_res = m_product_category.search([['name', '=', categoria]], limit=1)
            else:
                category_search_res = m_product_category.search([['name', '=', categoria], ['parent_id', '=', parent_id]], limit=1)

            # Se non esiste lo creo
            if category_search_res:
                parent_id = idCategory = category_search_res.id
                categoryDict[categoria] = idCategory
            else:
                if parent_id:
                    data['parent_id'] = parent_id
                parent_id = idCategory = m_product_category.create(data).id
                categoryDict[categoria] = idCategory

        return idCategory
    except Exception as e:
        LogError(f'GetOrCreateCategory {odooCategoryName} - {e}')
        return None


def get_tot_dealer_product_info(env, catalogo_prodotto):
    qta_minima_distributore_aggiornamento_prezzi = 2
    """ Restituisce la somma delle disponibilità a magazzino di tutti
    i distributori e il prezzo minore del prodotto fra tutti i distributori """
    catalogo_prodotti_env = env['ak_connettore.catalogo_prodotti']
    minimum_price = standard_price = fornitore = availability_dealer = None

    if catalogo_prodotto.odoo_product_id:
        # Filtro per giacenza cercando il prezzo più basso fra tutti i distributori
        # che hanno quel prodotto sincronizzato con quelli di Odoo
        cat_prod_best_dealer = catalogo_prodotti_env.search(
            [
                ('importare_in_odoo', '=', True),  # Flag importare in Odoo
                ('odoo_product_id', '=', catalogo_prodotto.odoo_product_id.id),  # Prodotto Odoo collegato a elenco prodotti
                ('giacenza_distributore', '>=', qta_minima_distributore_aggiornamento_prezzi)  # Giacenza distributore superiore alla soglia minima
            ], order='prezzo asc', limit=1
        )

    elif catalogo_prodotto.giacenza_distributore > qta_minima_distributore_aggiornamento_prezzi:
        cat_prod_best_dealer = catalogo_prodotto

    if cat_prod_best_dealer:
        # I prezzi vanno aggiornati solo se il prodotto non ha la spunta "prezzo bloccato"
        # Valorizzo prezzo vendita/costo acquisto e fornitore con quello che ha il prezzo più basso (non bloccato)
        availability_dealer = cat_prod_best_dealer.giacenza_distributore
        minimum_price = cat_prod_best_dealer.prezzo_calcolato if not cat_prod_best_dealer.prezzo_bloccato else cat_prod_best_dealer.prezzo_imposto
        standard_price = cat_prod_best_dealer.prezzo
        fornitore = cat_prod_best_dealer.distributore_id.name

    return availability_dealer, minimum_price, standard_price, fornitore


def GetConfigurationValue(env, name):
    config_sudo = env['res.config.settings'].sudo()
    value = config_sudo.get_values()[name]
    return value


def get_rounded_amount(amount, roundupto, iva=0):
    res = None
    amount = amount * (1 + iva)
    if roundupto < 1:
        whole = int(amount)
        res = whole + roundupto
    elif roundupto < 10:
        whole = int(math.ceil(amount / 10.0)) * 10
        res = whole - (10 - roundupto)
    elif roundupto < 100:
        whole = int(math.ceil(amount / 100.0)) * 100
        res = whole - (100 - roundupto)

    res = res / (1 + iva)
    return res

