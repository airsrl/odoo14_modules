# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Conto analitico per voci piano dei conti',
    'version': '14.0.2',
    'summary': 'Nella voce del piano dei conti è possibile scegliere un conto analitico di default. Alla creazione di nuove righe fattura, Conto analitico e Etichette analitiche vengono compilati automaticamente in base ai valori di default del contatto scelto',
    'description': "Il rendiconto analitico visualizza anche le etichette analitiche",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['base','contacts','account_reports','account','l10n_it_fatturapa_in','l10n_it_fatturapa_import_zip'],
    'data': [
        'views/account_account.xml',
        'views/res_partner.xml',
    ],
}
