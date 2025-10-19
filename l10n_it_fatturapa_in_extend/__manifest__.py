# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'l10n_it_fatturapa_in_extend',
    'version': '1.0.0.0',
    'summary': 'Add field e_invoice_received_date in account.move tree view of the module l10n_it_fatturapa',
    'description': "Add field e_invoice_received_date in account.move tree view of the module l10n_it_fatturapa",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['l10n_it_fatturapa_in', 'account'],
    'data': [
        'views/account_view.xml',
    ],
    'images': ['static/description/icon.png'],
}
