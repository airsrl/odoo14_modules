# Copyright 2023 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)
# Powered by Marco Frascerra

{
    'name': "Imposte di bollo | Integrazione al modulo l10n_it_account_stamp",
    'summary': """Integrazione al modulo l10n_it_account_stamp.""",
    'description': """Inserisce una vista report per avere un quadro delle 
    imposte di bollo da pagare ai fini dell' F24.""",

    'author': "Huroos - www.huroos.com",
    'website': "www.huroos.com",
    'category': 'Accounting',
    'version': '14.0.1',

    'depends': ['l10n_it_account_stamp'],

    'data': [
        'security/ir.model.access.csv',

        'wizard/account_stamp_report.xml',

        'views/account_stamp_report_menu.xml'
    ]
}
