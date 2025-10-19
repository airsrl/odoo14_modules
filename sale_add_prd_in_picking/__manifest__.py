# -*- coding: utf-8 -*-
{
    'name': "Sale add product in picking",
    'summary': "Adds one or more products in the picking list when the SO is confirmed.",
    'description': """Adds one or more products in the picking list when the order is confirmed. Configuration: set the products you want to add in the product category. 
                    Whenever a SO is confirmed the module checks every product, and adds any additional products of the current product category (if any). """,
    'author': "Huroos srl",
    'web': "www.huroos.com",
    'images': ['static/description/icon.png'],
    'website': 'https://huroos.com',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '14.0.1.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock'],
    # always loaded
    'data': [
        'views/product_category.xml'
    ]

}
