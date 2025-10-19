# -*- coding: utf-8 -*-
{
    'name': "Huroos Shippypro Connector",
    'summary': """Modulo connessione con ShippyPro""",
    'description': """Modulo connessione con ShippyPro""",
    'author': "Huroos srl - SC",
    'images': ['static/description/icon.png'],
    'website': 'www.huroos.com',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '14.0.2.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock', 'delivery'],
    'data': [
        'security/ir.model.access.csv',

        'views/delivery_carrier.xml',
        'views/stock_picking.xml',
        'views/res_company.xml',

        'views/shippy_pro_get_tracking_numbers.xml',
        'views/shippy_pro_update_carriers.xml',

        'report/etichette.xml'
    ]

}
