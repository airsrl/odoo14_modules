{
    'name': 'Huroos report bilancio',
    'version': '14.0.2.0',
    'author': 'Huroos Srl',
    'summary': '',
    'description': "Report bilancio personalizzato",
    'website': 'https://www.huroos.com',
    'category': 'accounting',
    'depends': [
        'base', 'account_reports', 'account'
    ],
    'data': [
        "data/data.xml",
        "security/ir.model.access.csv",
        "wizard/genera_bilanci.xml",
        "wizard/wizard_import_chart_account_xls.xml",
        # "views/search_template_view.xml",
        "views/report_bilancio.xml",
        "views/huroos_report_bilancio_assets.xml",
        # "views/account_partner_ledger.xml",
        "views/account_move.xml",
        "views/account_move_line.xml",
        "views/account_account.xml",
        'views/account_journal_form_view.xml',
    ],

    'installable': True,

}