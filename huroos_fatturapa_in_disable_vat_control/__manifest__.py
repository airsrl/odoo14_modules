# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2023 Huroos Srl. (<https://www.huroos.com>).

{
    "name": "Huroos | Disable VAT Control ricezione FE",
    "summary": "Disable VAT Control in Ricezione fatture elettroniche",
    'description': """
        Salta il controllo sulla partita IVA durante l'import zip delle FE
    """,

    'author': "Huroos Srl",
    "website": "https://www.huroos.com",

    "category": "Accounting",
    "version": "16.0.1",
    "license": "AGPL-3",

    "depends": [
        "l10n_it_fatturapa_in",
        "huroos_fe_import_zip"
    ],
    "data": [],
    "installable": True,
}
