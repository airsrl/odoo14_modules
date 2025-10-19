# Copyright 2022 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

{
    'name': "Import record da Excel",
    'summary': """Importa record da un file Excel. Ottimizzato per utenti non esperti.""",
    'description': """Importa record da un file Excel. Ottimizzato per utenti non esperti.""",
    'author': "Huroos SC - www.huroos.com",
    'category': 'Tools',
    'version': '14.0.1.0',
    'depends': ['sale', 'report_xlsx'],
    'external_dependencies': {
        'python': ['pandas']
    },
    'data': [
        'security/ir.model.access.csv',

        'views/res_config_settings_view.xml',

        'report/excel_template.xml',

        'wizard/excel_import_easy_view.xml'
    ]
}
