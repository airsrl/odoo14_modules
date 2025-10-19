# -*- coding: utf-8 -*-
# Part of Huroos Srl See LICENSE file for full copyright and licensing details.
# Copyright 2023 Huroos Srl (<https://www.huroos.com>)

{
    'name': 'Huroos | Chiusura Anno Contabile',
    'version': '14.0.2',
    'author': "Huroos Srl",
    'website': 'https://www.huroos.com',
    'license': 'LGPL-3',
    'category': 'Accounting',

    "depends": [
        'account',
        'account_fiscal_year',
        'account_tax_balance',
        'base_vat',
    ],

    "data": [
        'security/ir.model.access.csv',
        'security/rules.xml',

        'views/year_closing.xml',
        'views/account_move.xml'
    ]
}
