# -*- coding: utf-8 -*-
# Powered by Andrea Ferrari.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2023 Huroos Srl. (<https://www.huroos.com>).

{
    'name': "Huroos - Fatturapa Private Invoice",
    'summary': """Applica codice ISO-99999999999 ai soggetti privati esteri che non presentano CF e P.IVA.""",
    'description': """Ricopre la casistica dei soggetti privati esteri che non presentano CF e P.IVA.
     inserendo il codice ISO-99999999999. nelle fatture elettroniche""",
    'author': "Huroos Srl",
    'website': "www.huroos.com",
    'category': 'Accounting',
    'version': '14.0.1',

    'depends': [
        'l10n_it_fatturapa_out'
    ],

    'data': [
        'views/res_partner.xml',
    ],
    'demo': [],
    'application': False,
    'installable': True,
}
