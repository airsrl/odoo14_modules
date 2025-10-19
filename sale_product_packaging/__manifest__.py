# -*- coding: utf-8 -*-
{
    'name': "Prodotto imballaggio",
    'summary': "Product as packaging",
    'description': "Inserisce box prodotti",
    'author': "Huroos srl",
    'web': "www.huroos.com",
    'images': ['static/description/icon.png'],
    'website': 'https://huroos.com',
    'category': 'Inventory',
    'version': '14.0.2.0',
    # any module necessary for this one to work correctly
    'depends': ['sale_product_tester'],
    'data': [ 'report/report_ddt.xml',
             'views/product_packaging.xml',
            'views/product_template.xml',

    ]

}
