import logging, json, pytz
from . import python_utils as pu
from enum import Enum
import traceback

# Logging
logger = logging.getLogger(__name__)
errors = []

# Models dictionaries
fornitoreDict = dict()
categoryDict = dict()


class Log_msg_type(Enum):
	Info = 'INFO'
	Err = 'ERR'
	Warn = 'WARN'


# Return
def get_local_date_time(date_time_utc):
	timezoneLocal = pytz.timezone('Europe/Rome')
	utc = pytz.utc
	dateTimeLocal = utc.localize(date_time_utc).astimezone(timezoneLocal)
	return dateTimeLocal


def GetLogger():
	return logger


def log_info(msg):
	logger.info(msg)


def log_error(msg):
	logger.error(msg)


def log_warn(msg):
	logger.warning(msg)


def log_exception(ex):
	global errors
	logger.error("*** EXCEPTION ***")
	logger.error(traceback.format_exc())
	errors.append("%s - %s" % (pu.get_current_date_time(), ex))


def log_recap_eccezioni():
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
		log_warn(json.dumps(errors, indent=4, sort_keys=False))
		""" body = json.dumps(Eccezioni , indent=4, sort_keys=False)
        subject = f"CONNETTONE - {len(Eccezioni)} ECCEZIONI RISCONTRATE"
        email_to = cu.GetConfigValue('AIR_ErrorLog','emailSendErrorLog')
        eu.SendLogEmail(body,subject,email_to) """


def get_or_create_product_supplier(env, idProdotto, nomeFornitore, productCodeForn, prezzo, delay=None, product_uom=None):
	try:
		# ricerca id fornitore in base a nome
		m_res_partner = env["res.partner"]
		m_product_supplierinfo = env["product.supplierinfo"]

		if nomeFornitore in fornitoreDict:
			idFornitore = fornitoreDict[nomeFornitore]
		else:
			fornitore_search = m_res_partner.search(args=[['name', '=', nomeFornitore]], limit=1)

			# se non esiste, creare il fornitore (in base a nome)
			if not fornitore_search:
				new_fornitore = m_res_partner.create({'name': nomeFornitore, 'company_type': 'company'})
				idFornitore = new_fornitore.id
			else:
				idFornitore = fornitore_search.id

			fornitoreDict[nomeFornitore] = idFornitore

		# ricerca il fornitore di un prodotto, partendo dall'id del prodotto
		datiFornitore = m_product_supplierinfo.search(
			[['product_tmpl_id', '=', idProdotto], ['name', '=', idFornitore]], limit=1)

		# se esiste, aggiorna prezzo
		data = {'product_tmpl_id': idProdotto,
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
	except Exception as e:
		log_error(f'Fornitore: {nomeFornitore} idProdotto: {idProdotto} - {e}')
		return None


def get_or_create_category(env, odooCategoryName):
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
				category_search_res = m_product_category.search(
					[['name', '=', categoria], ['parent_id', '=', parent_id]], limit=1)

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
		log_error(f'GetOrCreateCategory {odooCategoryName} - {e}')
		return None

default_image_name = 'wp_default_image'
def get_default_image(env):
	try:
		default_img_src = env['ir.attachment'].search([('name', '=', default_image_name)], limit=1)
		# log_info(f'default_img_src: {default_img_src}')

		if not default_img_src:
			image_datas = get_config_value(env, 'wp_default_image')

			# Carico l'immagine per il prodotto su WP
			uploaded_img = upload_doc_attachment(env, default_image_name, image_datas, 'product.template', 0, True)
			# log_info(f'uploaded_img: {uploaded_img}')
			return {'id': uploaded_img.id, 'datas': uploaded_img.datas}
		else:
			return {'id': default_img_src[0].id, 'datas': default_img_src[0].datas}
	except Exception as e:
		log_error(f'get_default_image - {e}')
		return None
	return None


def delete_doc_attachment(env, attachment_id):
	# Evito di cancellare l'immagine di default
	env['ir.attachment'].search([('id', '=', attachment_id),
								 ('name', '!=', default_image_name)]).unlink()


def upload_doc_attachment(env, name, datas, res_model, id_risorsa, public=False):
	try:
		file_created = env['ir.attachment'].create({'name': name,
													'datas': datas,
													'res_id': id_risorsa,
													#'datas_fname': name,
													'res_model': res_model,
													'type': 'binary',
													'public': public})

	except Exception as e:
		log_error(f'upload_doc_attachment {name} {res_model} - {e}')
		return None
	return file_created


def get_config_value(env, name):
	config_sudo = env['res.config.settings'].sudo()
	value = config_sudo.get_values()[name]
	return value


def get_or_create_many2one(env, model, name):
	"""Restituisce o crea un record all'interno di una relazione one2many"""
	model = env[model]

	# Cerco per nome
	record = model.search([['name', '=', name]], limit=1)

	# Se esiste restituisco l'id, altrimenti lo creo e restituisco l'id
	if record:
		return record.id
	else:
		record = model.create({'name': name})
		return record.id


log_msg_type = []


def post_log_msg(record, body, msg_type: Log_msg_type, author_id=2):
	ico = '⚡'
	if not msg_type:
		msg_type = Log_msg_type.Info
	if msg_type != Log_msg_type.Info:
		ico = '📌'
	record.message_post(body=f"{ico} {msg_type.value}<br/>{body}", author_id=author_id)
