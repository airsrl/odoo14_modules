# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Importazione ZIP fatture Passive e Attive',
    'version': '14.0.0.0',
    'summary': '',
    'description': "Estende modulo OCA per importare correttamente fatture attiv e passive",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['account', 'l10n_it_account', 'l10n_it_fatturapa_import_zip'],
    'data': [
        'views/import_zip.xml'
    ],
}