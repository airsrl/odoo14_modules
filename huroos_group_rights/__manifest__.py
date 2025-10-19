# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': "Huroos - Access group rights",
    'version': "1.0.0.0",
    'author': "AIR-mf",
    'summary': 'Huroos - Access group rights',
    'description' : 'Huroos - Access group rights',
    'license':'OPL-1',
    'category': "Extra Tools",
    'data':[
        'security/ir.model.access.csv',
        'views/res_groups.xml',
        'wizard/access_wizard.xml',



            ],
    'website': 'https://www.huroos.com',
    'depends': ['base'],
    'installable': True,
    'auto_install': False,
    'images':['static/description/icon.png'],

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
