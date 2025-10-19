# Copyright 2023 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)
# Powered by Marco Frascerra

{
    'name': "Huroos DDT report",
    'summary': """Modulo per impostare report customizzati da Huroos srl per DDT""",
    'description': """Modulo per impostare report customizzati da Huroos srl per DDT""",
    'author': "Huroos - www.huroos.com",
    'category': 'Tools',
    'version': '14.0.1.0',
    'depends': ['huroos_reports_custom_external_layout', 'l10n_it_delivery_note'],
    'data': [
        'data/custom_ddt_paperformat.xml',

        'report/delivery_note_template.xml'
    ]
}
