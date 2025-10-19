from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    openapi_token = fields.Char(
        string="Token",
        config_parameter="huroos_openapi.openapi_token"
    )
    openapi_sandbox_token = fields.Char(
        string="Token sandbox",
        config_parameter="huroos_openapi.openapi_sandbox_token"
    )
    openapi_force_credentials = fields.Boolean(
        string="Forza credenziali",
        config_parameter="huroos_openapi.openapi_force_credentials",
        help="Se selezionato invertirà le credenziali "
             "(Es: se ti trovi in produzione utilizzarà le credenziali di staging e viceversa)."
    )
