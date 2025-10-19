# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Automatismi Fatture Acquisto',
    'version': '1.0.0.0',
    'summary': 'Aggiunge un suggerimento sulle bozze fatture fornitore per capire la tipologia di registrazione: Es. Intra, Extra, Italia, Conguaglio, Nota di Credito..',
    'description': "Aggiunge un suggerimento sulle bozze fatture fornitore per capire la tipologia di registrazione: Es. Intra, Extra, Italia, Conguaglio, Nota di Credito..",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['l10n_it_fatturapa_in', 'account'],
    'data': [
        'views/account_view.xml',
    ],
    'images': ['static/description/icon.png'],
}
