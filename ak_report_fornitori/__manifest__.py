# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'AK Informatica- Report fornitori',
    'version': "1.0.0.1",
    'author': "AIR-sc",
    'summary': 'Customizzazioni sviluppate da air srl per AK Informatica',
    'description': 'Customizzazioni sviluppate da air srl per AK Informatica',
    'license': 'OPL-1',
    'category': "Extra Tools",
    'data': [
                'data/scheduler.xml',
                'data/template.xml',
                'security/ir.model.access.csv',
                'views/report_fornitori.xml',
                'views/report_fornitori_data.xml',
                'views/stock_warehouse.xml',
                'views/stock_picking_type_view.xml',
             ],
    'website': 'https://www.air-srl.com',
    'depends': ['ak_connettorefornitori','mail','air_connector'],
    'installable': True,
    'auto_install': False,
	"images": ['static/description/icon.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
