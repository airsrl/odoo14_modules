# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': "Huroos altri dati gestionali",
    'version': "1.0.0.0",
    'author': "AIR-kp",
    'summary': 'Aggiunge il campo altri dati gestionali a fatturapa',
    'description' : 'Aggiunge il campo altri dati gestionali a fatturapa',
    'license':'OPL-1',
    'category': "Extra Tools",
    'data':[
            'views/res_partner.xml',
            'views/account_move_line.xml',
            'views/datigestionali.xml',
            'data/fatturapa.xml',
            'security/ir.model.access.csv'
            ],
    'website': 'https://www.huroos.com',
    'depends': ['account','l10n_it_fatturapa_out'],
    'installable': True,
    'auto_install': False,
    'images': ['static/description/icon.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
