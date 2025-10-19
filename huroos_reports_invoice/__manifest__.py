# Copyright 2023 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)
# Powered by Marco Frascerra

{
    'name': "Huroos INVOICE report",
    'summary': """Modulo per impostare report customizzati da Huroos srl per Fatture""",
    'description': """Modulo per impostare report customizzati da Huroos srl per Fatture""",
    'author': "Huroos - www.huroos.com",
    'category': 'Tools',
    'version': '14.0.1.0',
    'depends': ['huroos_reports_custom_external_layout', 'account', 'huroos_payments_due', 'huroos_riba_bank'],
    'data': [
        'data/custom_invoice_paperformat.xml',

        'report/invoice_template.xml'
    ]
}
