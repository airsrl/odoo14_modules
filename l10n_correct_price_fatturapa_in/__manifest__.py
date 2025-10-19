# -*- coding: utf-8 -*-
# Part of AIR. See LICENSE file for full copyright and licensing details.
{
    'name': "Creazione OdA da Xml e correzione prezzo",
    'version': "1.0.0.0",
    'author': "AIR-kp, flp-AIR,AIR-Leo",
    'summary': 'Crea un OdA da Xml e corregge il prezzo se disallineato quando viene importata una e-fattura',
    'description' : 'Crea un OdA da Xml e corregge il prezzo se disallineato quando viene importata una e-fattura',
    'license':'OPL-1',
    'category': "Extra Tools",
    'data':['views/fatturapa_in.xml', 'views/OdA.xml'],
    'website': 'https://www.air-srl.com',
    'depends': ['l10n_it_fatturapa_in', 'purchase','stock'],
    'installable': True,
    'auto_install': False,
    'images':['static/description/icon.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
