# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

{
    'name': 'Batch Picking',
    'version': '14.0.0.0',
    'summary': '',
    'description': "Raggruppa i batch picking per prodotto / ottimizza il flusso di prelievo Pick + Pack + Ship",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': ['account', 'stock', 'stock_barcode', 'stock_picking_batch', 'stock_barcode_picking_batch'],
    'data': [
        #'security/ir.model.access.csv',
        'views/stock_picking.xml',
    ],
}