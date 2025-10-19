
{
    "name": "HUROOS - Dichiarazione di intento fix",
    "summary": "FIX nota dichirarazione in fattura",
    'author': 'Huroos Srl',
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    "depends": [
        "l10n_it_declaration_of_intent",
    ],
    "data": [
        'data/ir_cron.xml',
        'views/account_move.xml',
        'wizard/declaration_wizard.xml'
    ],
    'images': ['static/description/icon.png'],

}
