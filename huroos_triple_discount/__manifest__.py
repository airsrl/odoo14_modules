# Copyright 2022 Huroos Srl
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Triple Discount Invoice & Sales",
    "summary": "Triple Discount Patch",
    "version": "14.0.1.0.0",
    "category": "Sales Management",
    "license": "AGPL-3",
    "author": "Huroos Srl",
    "website": "www.huroos.com",
    "depends": ["base", "account", "sale_management", "purchase_discount"],
    "data": [
        'views/account_move.xml',
        'report/invoice.xml',
        "views/sale_order_report.xml",
        "views/sale_order_view.xml",
        'views/product_supplierinfo_view.xml',
        'views/purchase_view.xml',
        'views/res_partner_view.xml',
    ],
    "installable": True,
}
