# -*- coding: utf-8 -*-
# Part of huroos srl. See LICENSE file for full copyright and licensing details.
# Copyright 2019 huroos srl (<http://www.addoons.it>)

{
    'name': 'Valorizzazione Magazzino',
    'version': '14.0.0.0.1',
    'category': 'Localization/Italy',
    'summary': 'Valorizzazione del Magazzino CMP, FIFO, LIFO',
    "author": "hello@huroos.com",
    'website': 'www.huroos.com',
    'license': 'LGPL-3',
    "depends": [
        'stock', 'account', 'purchase', 'sale', 'mrp'
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/warehouse_valuation.xml',
        'views/warehouse_valuation_line_detail.xml',
        'views/product_template.xml',
        'report/warehouse_valuation.xml',
    ],
    'installable': True,
}
