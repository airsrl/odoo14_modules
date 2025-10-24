# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'AK Informatica - Customizzazioni air connettore fornitori',
    'version': "1.0.0.1",
    'author': "AIR-sc",
    'summary': 'Customizzazioni sviluppate da air srl per AK Informatica',
    'description': 'Customizzazioni sviluppate da air srl per AK Informatica',
    'license': 'OPL-1',
    'category': "Extra Tools",
    'data': [
             'views/menu.xml',
             'views/distributori.xml',
             'views/categorie.xml',
             'views/marchi.xml',
             'views/catalogo_prodotti.xml',
             'views/setup_margini.xml',
             'views/product_template.xml',
             'data/scheduler.xml',
             'security/ir.model.access.csv',
             ],
    'website': 'https://www.air-srl.com',
    'depends': ['sale', 'stock', 'purchase_stock'],
    'installable': True,
    'auto_install': False,
	"images": ['static/description/icon.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
