# -*- coding: utf-8 -*-
{
    'name': "sale_product_tester",
    'summary': "Righe prodotto test",
    'description': "Inserisce una riga di prodotto test",
    'author': "Huroos srl",
    'web': "www.huroos.com",
    'images': ['static/description/icon.png'],
    'website': 'https://huroos.com',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '14.0.2.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_stock','l10n_it_delivery_note'],
    'data': ['report/report_stockpicking_operations.xml',
             'views/product_template.xml',
            'views/sale_order.xml',
            'views/stock_picking.xml'
    ]

}
