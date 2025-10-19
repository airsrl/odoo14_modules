from odoo import fields, models


class CompensazioniSetting(models.TransientModel):
    _inherit = "res.config.settings"

    journal = fields.Many2one(
        comodel_name="account.journal",
        string="Registro di default",
        config_parameter="huroos_compensazioni.journal"
    )
    credit_account = fields.Many2one(
        comodel_name="account.account",
        string="Conto di credito",
        config_parameter="huroos_compensazioni.credit_account"
    )
    debit_account = fields.Many2one(
        comodel_name="account.account",
        string="Conto di debito",
        config_parameter="huroos_compensazioni.debit_account"
    )

