{
    'name': 'Air GLS Italy Shipping Integration ',
    'category': 'Website',
    'author': "Air",
    'version': '14.0',
    'summary': """api closeWorkdaybyshipmentnumber""",
    'description': """""",
    'depends': ['gls_shipping_integration'],
    'data': [
            'security/ir.model.access.csv',
            'data/scheduler.xml',
             #'views/delivery_carrier.xml',
            'wizard/wizard_closeworkday.xml'
             ],
    'images': ['static/description/icon.png'],
    'demo': [],
    'installable': True,
    'application': True,
}

