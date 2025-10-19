# -*- coding: utf-8 -*-
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Huroos delay payment',
    'version': '14.0.0.0',
    'summary': '',
    'description': "Ritardo data pagamenti in base al mese",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['account','huroos_payments_due'],
    "images": ["static/description/icon.png"],
    'data': [
        'security/ir.model.access.csv',
        'data/huroos.month.csv',
        'views/res_partner.xml',

    ],
}
