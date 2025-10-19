{
    'name': 'Huroos Birthdate Fiscalcode',
    'version': '14.0',
    'summary': 'Calcola il giorno di nascita dal codice fiscale',
    'description': 'Aggiunge la data di nascita, il mese di nascita e il giorno di nascita dal codice fiscale',
    "category": "Extra Tools",
    'author': 'Huroos Srl',
    'website': 'www.huroos.com',
    'depends': ['base', 'l10n_it_fiscalcode'],
    "data": ['views/res_partner.xml'],
    "external_dependencies": {"python": ["python-codicefiscale"]},

}
