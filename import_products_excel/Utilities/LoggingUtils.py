import datetime,logging,json,pytz
""" import LoggingUtils as lu
import ConfigUtils as cu """

# Logging
_logger = logging.getLogger(__name__)
errors = []

# Restituisce data-ora nel fuso italiano (perchè odoo giustamente se lo salva UTC)
def GetLocalDateTime(dateTimeUTC):
    timezoneLocal = pytz.timezone('Europe/Rome')
    utc = pytz.utc
    dateTimeLocal = utc.localize(dateTimeUTC).astimezone(timezoneLocal)
    return dateTimeLocal

def GetLogger():
    return logging

def GetDateTime() -> str:
    now = datetime.datetime.now()# current date and time
    return now.strftime("%d.%m.%y %H:%M:%S")

def LogInfo(msg):
    _logger = logging.getLogger(__name__)
    _logger.info(msg)

def LogError(msg):
    _logger = logging.getLogger(__name__)
    _logger.error(msg)

def LogWarn(msg):
    _logger = logging.getLogger(__name__)
    _logger.warn(msg)

def LogException(ex):
    global errors
    _logger = logging.getLogger(__name__)
    _logger.error("*** EXCEPTION ***")
    _logger.error(ex)
    errors.append("%s - %s"  %(GetDateTime(),ex))

def LogRecapEccezioni():
    global errors
    if(len(errors)== 0):
        logging.info("\n******************************************************")
        logging.info("*** NESSUN ERRORE RISCONTRATO DURANTE L'ESECUZIONE ***")
        logging.info("******************************************************")
    else:
        logging.warn("\n***************************************************")
        logging.warn(f"*** {len(errors)} ERRORI RISCONTRATI DURANTE L'ESECUZIONE ***")
        logging.warn("***************************************************")

    # Mando la mail con il riepilogo delle eccezioni
    if(len(errors) > 0):
        LogWarn(json.dumps(errors , indent=4, sort_keys=False))
        """ body = json.dumps(Eccezioni , indent=4, sort_keys=False)
        subject = f"CONNETTONE - {len(Eccezioni)} ECCEZIONI RISCONTRATE"
        email_to = cu.GetConfigValue('AIR_ErrorLog','emailSendErrorLog')
        eu.SendLogEmail(body,subject,email_to) """
