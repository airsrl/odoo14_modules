from odoo import fields, models


# Classe non utilizzata al momento
class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    journal_items_grouped = fields.Boolean(
        string="Raggruppa movimenti contabili",
        config_parameter="huroos_group_journal_items.journal_items_grouped"
    )
