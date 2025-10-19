# -*- coding: utf-8 -*-
# Powered by Karanveer Singh.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

from odoo import models, fields, api
from odoo.tools import datetime
from odoo.tools.float_utils import float_compare, float_round


class AccountAccount(models.Model):
    _inherit = 'account.account'

    area = fields.Selection([('conto_economico', 'Conto Economico'), ('stato_patrimoniale', 'Stato Patrimoniale'),
                             ('conti_ordine', "Conti D'ordine")], default='stato_patrimoniale')
    hierarchy_type = fields.Selection([("macroaggragate", "Macroaggregato"), ("aggregate", "Aggregato"),
                                          ("sottoconto_terzo_livello", "Sottoconto Terzo Livello"),
                                          ("sottoconto_quarto_livello", "Sottoconto Quarto Livello"),
                                          ("sottoconto_quinto_livello", "Sottoconto Quinto Livello"),
                                          ("sottoconto_sesto_livello", "Sottoconto Sesto Livello")])
    macroaggregate_id = fields.Many2one('account.account', string="Macroaggregato")
    aggregate_id = fields.Many2one('account.account', string='Aggregato')
    sottoconto_terzo_livello = fields.Many2one('account.account', string='Sottoconto Terzo Livello')
    sottoconto_quarto_livello = fields.Many2one('account.account', string='Sottoconto Quarto Livello')
    sottoconto_quinto_livello = fields.Many2one('account.account', string='Sottoconto Quinto Livello')
    sottoconto_sesto_livello = fields.Many2one('account.account', string='Sottoconto Sesto Livello')
