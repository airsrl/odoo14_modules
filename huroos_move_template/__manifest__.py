# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Template Registrazioni (F24, Stipendi ..)',
    'version': '14.0.0.0',
    'summary': '',
    'description': "Template Registrazioni (F24, Stipendi ..)",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_move.xml',
        'views/account_move_template.xml'
    ],
}
