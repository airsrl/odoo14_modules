# -*- coding: utf-8 -*-
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Huroos delete invoice line',
    'version': '14.0.0.0',
    'summary': '',
    'description': "Eliminazione massiva righe fattura",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['account','web'],
    "images": ["static/description/icon.png"],
    'qweb': [
            'static/src/xml/widget_view.xml',
        ],
    'data': [
        'security/ir.model.access.csv',
        'views/wizard_delete.xml',
        'views/account_move.xml',
        'views/web_assets.xml'
    ],
}
