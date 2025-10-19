# -*- coding: utf-8 -*-
# Powered by MArco Corbetta.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2023 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Data pagamenti',
    'version': '14.0.0.0',
    'summary': '',
    'description': "Aggiunta colonna data pagamento a lista movimenti",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['account', 'account_due_list', 'account_due_list_aging_comment'],
    'images': ['static/description/icon.png'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_due_list.xml'
    ],
}
