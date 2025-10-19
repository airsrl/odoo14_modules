# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

from odoo import models, fields, api
from odoo.tools import datetime
from odoo.tools.float_utils import float_compare, float_round


class AccountMove(models.Model):
    _inherit = 'account.move'

    account_move_template = fields.Many2one('account.move.template')

    @api.onchange('account_move_template')
    def onchange_template(self):
        account_move_lines = [(5, 0)]
        if self.account_move_template:
            self.journal_id = self.account_move_template.account_journal_id.id
            for line in self.account_move_template.move_line_ids:
                account_move_lines.append((0, 0, {
                    'account_id': line.account_id.id,
                    'name': line.line_description,
                    'is_debit': line.is_debit,
                    'is_credit': line.is_credit,
                    'account_move_template': True,
                }))
            self.line_ids = account_move_lines


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    is_debit = fields.Boolean()
    is_credit = fields.Boolean()
    account_move_template = fields.Boolean()

