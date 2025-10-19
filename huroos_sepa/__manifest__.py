# -*- coding: utf-8 -*-
# Part of huroos srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 huroos srl (<http://www.addoons.it>)

{
    'name': 'SEPA',
    'version': '14.0.1.2.6',
    'category': 'Localization/Italy',
    'summary': 'Gestione Distinte pagamenti SEPA CBI 00.04.00',
    "author": "hello@huroos.com",
    'website': 'www.huroos.com',
    'license': 'LGPL-3',
    "depends": [
        'account_sepa',
        'account_batch_payment'
    ],
    "data": [
        'views/sepa.xml'
    ],
    'installable': True,
    'external_dependencies': {
        'python': [
            'PyXB-X',
        ],
    }
}
