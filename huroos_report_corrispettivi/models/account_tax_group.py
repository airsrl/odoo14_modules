# -*- coding: utf-8 -*-
# Powered by Karanveer Singh.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

from odoo import api,fields,models


class AccountTaxGroup(models.Model):
    _inherit = "account.tax.group"

    include_report_corrispettivi = fields.Boolean(default=True)
    label_report_corrispettivi_imponibile = fields.Char()
    label_report_corrispettivi_tassa = fields.Char()