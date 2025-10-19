# -*- coding: utf-8 -*-
# Part of huroos srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 huroos srl (<http://www.addoons.it>)

{
    'name': 'Data Competenza IVA',
    'version': '14.0.1.2.6',
    'category': 'Localization/Italy',
    'summary': 'Gestione data competenza IVA. Es: Fattura ricevuta entro il 15 del mese successivo. Registrazione nel mese corrente e iva nel mese precedente.',
    "author": "hello@huroos.com",
    'website': 'www.huroos.com',
    'license': 'LGPL-3',
    "depends": [
        'account',
        'account_accountant',
        'l10n_it_account',
        'l10n_it_fatturapa',
        'account_tax_balance',
        'l10n_it_reverse_charge',
        'account_vat_period_end_statement',
        'l10n_it_vat_registries',
    ],
    "data": [
        'views/date_iva.xml',
        'views/res_config_settings.xml',
        'views/report_registro_iva.xml',
    ],
    'installable': True,
}
