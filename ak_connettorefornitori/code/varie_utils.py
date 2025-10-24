import zipfile
from ftplib import FTP
import urllib
import csv
import pandas as pd
# import pandas_access as mdb
import io
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def ftp_get_txt_values(ftp_host, ftp_user, ftp_pass, filename, delimiter):
    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_pass)

    # get filenames on ftp home/root
    remoteFilenames = ftp.nlst()
    if '/' not in filename and filename not in remoteFilenames:
        raise BaseException(f'File {filename} non trovato sul server')

    # Leggo il file
    download_file = io.BytesIO()
    ftp.retrbinary("RETR {}".format(filename), download_file.write)
    download_file.seek(0)  # after writing go back to the start of the virtual file
    csv_righe_file = pd.read_csv(download_file, delimiter=delimiter, keep_default_na=False, encoding='latin1')
    rows = csv_righe_file.values

    return rows


# **********NEXT**********
def next_get_txt_values(url):
    resp_text = urllib.request.urlopen(url).read().decode('UTF-8')
    data_string = io.StringIO(resp_text)
    reader = csv.DictReader(data_string, delimiter=";")
    product_list = []
    for row in reader:
        product_list.append(dict(row))
    return product_list


# **********FOCELDA**********
def focelda_get_txt_values(url):
    resp_text = urllib.request.urlopen(url).read().decode('UTF-8')
    data_string = io.StringIO(resp_text)
    reader = csv.DictReader(data_string, delimiter=";")
    product_list = []
    for row in reader:
        product_list.append(dict(row))
    return product_list


# **** INgram *********
def ingram_get_txt_values(ftp_host, ftp_user, ftp_pass, filename, delimiter):
    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_pass)

    # get filenames on ftp home/root
    remoteFilenames = ftp.nlst()
    if filename not in remoteFilenames:
        raise BaseException(f'File {filename} non trovato sul server')

    # Leggo il file
    download_file = io.BytesIO()
    with open(filename, 'wb') as fp:
        ftp.retrbinary("RETR {}".format(filename), download_file.write)
    download_file.seek(0)  # after writing go back to the start of the virtual file
    csv_righe_file = pd.read_csv(download_file, delimiter=delimiter, keep_default_na=False, encoding='latin1')
    rows = csv_righe_file.values

    return rows


def ftp_get_xls_values(ftp_host, ftp_user, ftp_pass, filename):
    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_pass)

    # get filenames on ftp home/root
    remoteFilenames = ftp.nlst()
    if filename not in remoteFilenames:
        raise BaseException(f'File {filename} non trovato sul server')

    # Leggo il file
    download_file = io.BytesIO()
    ftp.retrbinary("RETR {}".format(filename), download_file.write)
    download_file.seek(0)  # after writing go back to the start of the virtual file
    csv_righe_file = pd.read_excel(download_file, keep_default_na=False)
    rows = csv_righe_file.values

    return rows


def ftp_get_zip(ftp_host, ftp_user, ftp_pass, filename):
    ftp = FTP(ftp_host)
    ftp.login(ftp_user, ftp_pass)
    remote_file_names = ftp.nlst()
    if filename in remote_file_names:
        with open(filename, 'wb') as file:
            ftp.retrbinary('RETR %s' % filename, file.write)
            file.close()
            ftp.quit()
            return file.name
    else:
        ftp.quit()
        raise BaseException(f'File {filename} non trovato sul server')


def get_file_from_zip(zip_file):
    extracted_file_name = ''
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall()
        if len(zip_ref.namelist()) == 1:
            extracted_file_name = zip_ref.namelist()[0]
        zip_ref.close()
    return extracted_file_name

# # chiedere a Simo i campi giusti da aggiungere
# def get_values_from_mdb_db(filename):
#     df = mdb.read_table(filename, "articoli", dtype={'DataPromoDa': object, 'DataPromoA': object})
#     products_list = []
#     for index, row in df.iterrows():
#         # print(row['DataPromoDa'], row['DataPromoA'])
#         product = {'distributore_product_id': row['CodiceProduttore'],
#                    'name': row['DescProd'],
#                    'codice_articolo': row['Codice'],
#                    'categoria_fornitore': row['Prod'],
#                    'descrizione': row['DescFam'],
#                    'prezzo': row['PrezzoRivenditore'],
#                    'ean': row['EAN'] if row['EAN'] and row['EAN'] != '0000000000000' and row['EAN'] != '' else '',
#                    'produttore': row['Prod'],
#                    'giacenza_distributore': row['TempoGaranziaEndUser']}
#         products_list.append(product)
#     return products_list
