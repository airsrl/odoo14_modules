# -*- coding: utf-8 -*-
{
    'name': "huroos_rma_ticketing",
    'summary': "Modulo gestione resi ticket tramite",
    'description': "Modulo gestione resi ticket tramite",
    'author': "Huroos srl",
    'images': ['static/description/icon.png'],
    'website': 'https://huroos.com',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '14.0.2.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'helpdesk_stock', 'huroos_shippypro_connector'],
    # always loaded
    'data': [
        'data/etichette.xml',
        'data/mail_template.xml',
        'data/stage_id.xml',

        'views/helpdesk.xml',
        'security/ir.model.access.csv',
        'wizard/wizard_cambio.xml'
    ]

}
