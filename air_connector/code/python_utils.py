import datetime
import hashlib

import re
import requests

def get_hash(text):
    hash_res = hashlib.md5(str(text).encode('utf-8')).hexdigest()
    return hash_res


def get_current_date_time() -> str:
    now = datetime.datetime.now()  # current date and time
    return now.strftime("%d.%m.%y %H:%M:%S")


def check_partita_iva(partita_iva, country="IT"):
    url = f"https://thenetworksolution.it/FattureCorrispettivi/Anagrafica.php?passwordScript=demo&pIva={partita_iva}"
    response = requests.get(url).json()

    return response


def check_existing_cf(cf, country="IT"):
    url = f"https://thenetworksolution.it/FattureCorrispettivi/Anagrafica.php?passwordScript=demo&cf={cf}&operazione=valida"
    response = requests.get(url)

    return response


def check_CF(codice_fiscale):
    CODICE_REGEXP = "^[0-9A-Z]{16}$"
    SETDISP = [1, 0, 5, 7, 9, 13, 15, 17, 19, 21, 2, 4, 18, 20,
               11, 3, 6, 8, 12, 14, 16, 10, 22, 25, 24, 23]
    ORD_ZERO = ord('0')
    ORD_A = ord('A')

    if 0 == len(codice_fiscale):
        return ""
    if (16 != len(codice_fiscale)):
        return ("La lunghezza del codice fiscale non è \n" +
                "corretta: il codice fiscale dovrebbe essere lungo\n" +
                "esattamente 16 caratteri.")
    codice_fiscale = codice_fiscale.upper()
    match = re.match(CODICE_REGEXP, codice_fiscale)
    if not match:
        return ("Il codice fiscale contiene dei caratteri non validi:\n" +
                "i soli caratteri validi sono le lettere e le cifre.")
    s = 0
    for i in range(1, 14, 2):
        c = codice_fiscale[i]
        if c.isdigit():
            s += ord(c) - ORD_ZERO
        else:
            s += ord(c) - ORD_A
    for i in range(0, 15, 2):
        c = codice_fiscale[i]
        if c.isdigit():
            c = ord(c) - ORD_ZERO
        else:
            c = ord(c) - ORD_A
        s += SETDISP[c]
    if (s % 26 + ORD_A != ord(codice_fiscale[15])):
        return ("Il codice fiscale non è corretto:\n" +
                "il codice di controllo non corrisponde.")
    return ''
