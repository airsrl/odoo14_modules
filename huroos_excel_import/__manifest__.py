# Copyright 2022 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

{
    'name': "Huroos Excel import",
    'summary': """Import records from an Excel file.""",
    'description': """Import records from an Excel file.""",
    'author': "Huroos SC - www.huroos.com",
    'category': 'Tools',
    'version': '14.0.1.0',
    'depends': ['sale', 'report_xlsx'],
    'external_dependencies': {
        'python': ['pandas']
    },
    'data': [
        "report/excel_template.xml",

        "wizard/excel_import_view.xml",

        "security/ir.model.access.csv"
    ]
}
