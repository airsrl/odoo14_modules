# Copyright 2023 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)
# Powered by Marco Frascerra

{
    'name': "Huroos | Gestione cespiti",
    'summary': """Estensione del modulo OCA 'https://github.com/OCA/l10n-italy/tree/14.0/assets_management'.""",
    'description': """Estensione del modulo OCA 'https://github.com/OCA/l10n-italy/tree/14.0/assets_management'.""",

    'author': "Huroos - www.huroos.com",
    'website': "www.huroos.com",
    'category': 'Accounting',
    'version': '14.0.2',

    'depends': ['assets_management'],

    'data': [
        'wizard/asset_generate_depreciation_view.xml',

        'views/asset_asset_view.xml',

        'report/asset_previsional.xml',
        'report/asset_journal.xml',
        'report/paperformat.xml',
        'report/layout.xml'
    ]
}
