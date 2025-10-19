# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': "POS corrispettivi",
    'version': "1.0.0.0",
    'author': "AIR-kp",
    'summary': 'Genera cor. da ric. pagate e senza cliente',
    'description' : 'Genera corrispettivi da ric. pagate e senza cliente',
    'license':'OPL-1',
    'category': "Extra Tools",
    'data':['views/template.xml',
            'data/schedule_order_pos.xml'

            ],
    'website': 'https://www.huroos.com',
    'depends': ['point_of_sale','l10n_it_corrispettivi'],
    'installable': True,
    'auto_install': False,
    #'qweb': ['static/src/xml/Screens/PaymentScreen/PaymentScreen.xml'],
    'images':['static/description/icon.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
