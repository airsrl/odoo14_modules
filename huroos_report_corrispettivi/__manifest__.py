# -*- coding: utf-8 -*-
# Powered by Karanveer Singh.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Report Corrispettivi e Registrazione',
    'version': '14.0.1.0',
    'summary': '',
    'description': "Report Corrispettivi e Registrazione",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['account', 'report_xlsx', 'l10n_it_corrispettivi', 'delete_paid_invoice'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_tax_views.xml',
        'report/report_xls_receipts.xml',
        'wizard/wizard_report_corrispettivi.xml',
        'views/import_corrispettivi.xml',
    ],
}