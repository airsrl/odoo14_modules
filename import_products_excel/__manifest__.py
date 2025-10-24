{
    'name': 'Import prodotti e varianti',
    'description': 'Importa prodotti e varianti da un file Excel',
    'version': '1',
    'license': 'OPL-1',
    'depends':	[
        'base',
        'product',
        'stock',
        'sale',
        'purchase',
    ],
    'external_dependencies': {
        'python': ['pandas','zipfile36','xlrd']
    },

    'author': "air-srl",
    'data': [
        'views/menu_estrazione.xml',
        'views/product_view.xml',
        'security/ir.model.access.csv'
    ],

    "images": ['static/description/icon.png'],
}
