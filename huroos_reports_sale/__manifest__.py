# Copyright 2023 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)
# Powered by Marco Frascerra

{
    'name': "Huroos SALE report",
    'summary': """Modulo per impostare report customizzati da Huroos srl per Ordini di Vendita""",
    'description': """Modulo per impostare report customizzati da Huroos srl per Ordini di Vendita""",
    'author': "Huroos - www.huroos.com",
    'category': 'Tools',
    'version': '14.0.1.0',
    'depends': ['huroos_reports_custom_external_layout', 'sale_management'],
    'data': [
        'data/custom_sale_paperformat.xml',

        'report/sale_order_template.xml'
    ]
}
