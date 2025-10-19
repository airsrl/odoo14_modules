# -*- coding: utf-8 -*-
# Powered by Karanveer Singh.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

from odoo import models, api, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    escludi_report_bilancio = fields.Boolean(readonly=True)
    invoice_date = fields.Date(
        related='move_id.invoice_date',
        store=True,
        readonly=True,
        index=True,
        copy=False,
        group_operator='min'
    )
