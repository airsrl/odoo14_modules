# Copyright 2020 Lorenzo Battistini @ TAKOBI
# Copyright 2021 Alex Comba - Agile Business Group
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Huroos | Autofattura",
    "summary": "Integrazione TD20 e inversione",
    "version": "14.0",
    "development_status": "Beta",
    "category": "Hidden",
    "website": "www.huroos.com",
    "author": "Huroos Srl",
    "maintainers": ["eLBati"],
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "auto_install": True,
    "depends": [
        "l10n_it_fiscal_document_type",
        'l10n_it_fatturapa_out'
    ],
    "data": [
        "views/invoice_it_template.xml",
        'views/account_move.xml'
    ],
}
