# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': "Huroos - Bank info on Invoice",
    'version': "14.0.1.0",
    'author': "Huroos srl",
    'summary': 'Huroos - Bank info on invoice',
    'description': 'Huroos - Aggiunta dati bancari in fattura',
    'license': 'AGPL-3',
    'category': "Extra Tools",
    'data': [

        'views/account_move.xml',
        'views/account_move_report.xml',

    ],
    'website': 'https://www.huroos.com',
    'depends': ['account'],
    'installable': True,
    'auto_install': False,
    'images': ['static/description/icon.png'],

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
