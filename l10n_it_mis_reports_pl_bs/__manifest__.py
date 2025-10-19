# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'ITA - MIS builder - Bilancio civilistico',
    'summary': 'Modelli "MIS Builder" per il conto economico e lo stato patrimoniale',
    'author': 'Dinamiche Aziendali srl,'
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/l10n-italy',
    'category': 'Reporting',
    'version': '14.0.1.0.1',
    'license': 'AGPL-3',
    "depends": [
        "account",
        "board",
        "report_xlsx",  # OCA/reporting-engine
        "date_range",  # OCA/server-ux
    ],
    'data': [
        "wizard/mis_builder_dashboard.xml",

        'datas/mis_report_styles.xml',
        'datas/mis_report_pl.xml',
        'datas/mis_report_bs.xml',
        "datas/ir_cron.xml",

        "views/mis_report.xml",
        "views/mis_report_instance.xml",
        "views/mis_report_style.xml",

        "security/ir.model.access.csv",
        "security/mis_builder_security.xml",

        "report/mis_report_instance_qweb.xml",
        "report/mis_report_instance_xlsx.xml",
    ],
    "qweb": ["static/src/xml/mis_report_widget.xml"],
    'installable': True,
    "application": True,
}