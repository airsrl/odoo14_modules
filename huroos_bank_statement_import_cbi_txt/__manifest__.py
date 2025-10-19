# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Importa estratti conti Bancari CBI',
    'category': 'Accounting/Accounting',
    'version': '1.0',
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'description': '''
        Il modulo permette di importare gli estratti conti bancari italiani in formato .cbi.txt
    ''',
    'depends': ['account_bank_statement_import'],
    'data': [
        'wizard/account_bank_statement_import_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
