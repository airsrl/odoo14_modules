# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Correggi Registri (Fatture Validate)',
    'version': '14.0.0.0',
    'summary': '',
    'description': "Permette di correggere il registro su una fatttura già validata."
                   "Il sistema mantiene memorizzato il protocollo già staccato e lo ripropone in un successivo documento",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/correct_journal_wizard.xml',
        'wizard/resequence_wizard.xml'
    ],
}
