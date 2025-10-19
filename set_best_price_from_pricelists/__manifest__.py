# -*- coding: utf-8 -*-
{
    'name': "Set_best_price_from_pricelists",
    'summary': "Listino prezzo più conveniente per righe",
    'description': "Inserisce il listino all'interno delle righe",
    'author': "Huroos srl",
    'web': "www.huroos.com",
    'images': ['static/description/icon.png'],
    'website': 'https://huroos.com',
    'category': 'Sale',
    'version': '14.0.2.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'sale','product'],
    'data': [
            #  'views/product_template.xml',
            'views/sale_order.xml',
            # 'views/stock_picking.xml'
    ]

}
