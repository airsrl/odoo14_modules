# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Pagamento Ritenute Acconto',
    'version': '14.0.0.0',
    'summary': '',
    'description': "Correzioni importo ritenute Acconto e rimozione errore duplicazione rda ad annullamento fattura",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['account', 'l10n_it_withholding_tax','account_due_list'],
    'data': [
        'views/account_due_list.xml'
    ],
}