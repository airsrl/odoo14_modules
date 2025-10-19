# -*- coding: utf-8 -*-
# Part of huroos srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 huroos srl (<http://www.addoons.it>)

{
    'name': 'Configurazione Contabilità',
    'version': '14.0.1.2.7',
    'category': 'Localization/Italy',
    'summary': 'Permette di configurare in modo guidato la localizzazione Italiana',
    "author": "hello@huroos.com",
    'website': 'www.huroos.com',
    'license': 'LGPL-3',
    "depends": [
        'account',
        'account_accountant',
        'l10n_it_account',
        'account_payment_term_extension',
        'l10n_it_fiscal_payment_term'
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/wizard_setup_accounting.xml',
    ],
    'installable': True,
}
