# -*- coding: utf-8 -*-
# Part of huroos srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 huroos srl (<http://www.addoons.it>)

{
    'name': 'Modifica Movimenti Contabili',
    'version': '14.0.1.2.6',
    'category': 'Localization/Italy',
    'summary': 'Permette di Modificare i movimenti Contabili',
    "author": "hello@huroos.com",
    'website': 'www.huroos.com',
    'license': 'LGPL-3',
    "depends": [
        'account',
        'account_accountant',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/change_account.xml',
    ],
    'installable': True,
}
