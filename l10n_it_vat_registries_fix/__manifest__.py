# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'l10n_it_vat_registries_fix',
    'version': '1.0.0.0',
    'summary': 'Correction in the TOTAL column of the report Registro IVA',
    'description': "Correction in the TOTAL column of the report Registro IVA",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['l10n_it_vat_registries', 'account_vat_period_end_statement'],
    'data': [
        'report/report_registro_iva.xml',
        'report/account_reports_view.xml',
        'report/report_vatperiodendstatement.xml',
    ],
    'images':['static/description/icon.png'],
}
