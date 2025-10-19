{
    "name": "ITA - Contabilità Lipe",
    "summary": "ITA - Contabilità Lipe",
    "version": "14.0.1.0",
    "development_status": "Production/Stable",
    "category": "Hidden",
    "author": "Huroos",
    "website": "https://github.com/OCA/l10n-italy",
    "license": "AGPL-3",
    "depends": [
        "account_asset", "l10n_it_account", "l10n_it_vat_statement_communication",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/comunicazione_liquidazione.xml",
        "wizards/export_liquidazione.xml",
    ],
    "installable": True,
}

