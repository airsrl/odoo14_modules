# -*- coding: utf-8 -*-
# Powered by Marco Frascerra.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2023 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Raggruppamento scritture contabili',
    'summary': "Inserisce la possibilità di raggruppare le scritture contabili. Modifica colonne e ordinamento rendiconto OCA mastrino",
    'description': "Modulo che inserisce la possibilità di raggruppare le scritture contabili.",

    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'version': '14.0.1',

    'depends': ['account', 'account_reports', 'account_financial_report'],

    'data': [
        'views/res_config_settings.xml',
        'views/search_template_view.xml',
        'report/templates/general_ledger.xml',
        'wizard/general_ledger_wizard_view.xml'
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
