# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'AIR - connector Odoo-Woocommerce',
    'version': '1.0.0.1',
    'author': 'AIR-sc',
    'summary': 'Synchronize products, stocks, orders, etc... between Odoo and Woocommerce',
    'license': 'OPL-1',
    'category': 'Extra Tools',
    'depends': ['stock', 'sale', 'mail', 'sale_stock'],
    'website': 'https://www.air-srl.com',
    'installable': True,
    'auto_install': False,
    'data': [
             'security/ir.model.access.csv',

             'views/wp_config.xml',
             'views/product_template_custom.xml',
             'views/pricelist.xml',
             'views/sale_order_custom.xml',
             'views/connector_log_view.xml',
             'views/connector_log_scheduler.xml',
             'views/product_template_kanban_custom.xml',
             'views/stock_move_line_custom.xml',
             'views/product_pricelist_item.xml',
             'views/mrp_production_view.xml',
             'views/mrp_production_tag_view.xml',
             'views/product_category.xml',
    ],
    'images': ['static/description/icon.png'],

    # Check woocommerce dependecies
    'external_dependencies': {'python': ['woocommerce']}
}

