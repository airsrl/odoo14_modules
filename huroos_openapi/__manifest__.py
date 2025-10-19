# Copyright 2024 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)
# Powered by Marco Frascerra

{
    'name': "Huroos | OpenAPI",
    'summary': """Integrazione delle funzionalità fornite dagli endpoint di OpenAPI in Odoo""",
    'description': """Integrazione delle funzionalità fornite dagli endpoint di OpenAPI in Odoo""",

    'author': "Huroos - www.huroos.com",
    'category': 'Accounting',
    'version': '14.0.1',
    'license': 'LGPL-3',

    'depends': ['l10n_it_fiscalcode', 'l10n_it_pec', 'l10n_it_fatturapa'],

    'data': [
        'security/ir.model.access.csv',

        'data/openapi_engine_data.xml',

        'wizard/res_partner_data_fetch.xml',
        'wizard/visura_camerale_request.xml',

        'views/assets.xml',
        'views/res_partner.xml',
        'views/openapi_engine_views.xml',
        'views/res_config_settings.xml',
        'views/res_partner_visura_camerale.xml'
    ],

    'qweb': [
        'static/src/xml/res_partner_data_fetch_header_button.xml'
    ]
}
