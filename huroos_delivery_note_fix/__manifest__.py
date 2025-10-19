# -*- coding: utf-8 -*-
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Huroos delivery note fix',
    'version': '14.0.0.0',
    'summary': '',
    'description': "Fix funzionalità DDT",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'Localization/Italy',
    'depends': ['l10n_it_delivery_note'],
    "images": ["static/description/icon.png"],
    'data': [
        'security/ir.model.access.csv',
        'wizard/wizard_ddt_changenumber.xml',
        'views/stock_delivery_note.xml'
    ],
}
