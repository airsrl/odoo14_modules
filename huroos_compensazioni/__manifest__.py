# Copyright 2022 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

# stock_restrict_lot --> https://github.com/OCA/stock-logistics-workflow/tree/14.0/stock_restrict_lot
{
    'name': "Compensazioni",
    'summary': """Consente di registrare il pagamento di fatture attive e passive specificando come metodo di pagamento la compensazione con una o più fatture da/verso lo stesso cliente/fornitore.""",
    'description': """Aggiunge un wizard nelle fatture di vendita per effettuare una compensazione con fatture passive di acquisto""",
    'author': "Huroos - www.huroos.com",
    'category': 'Tools',
    'version': '14.0.1.0',
    'depends': ['account', 'account_accountant'],
    'data': [
        'views/account_payment_register.xml',
        'views/res_config_settings_view.xml'
    ]
}
