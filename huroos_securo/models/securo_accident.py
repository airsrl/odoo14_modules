# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SecuroAccident(models.Model):
    _name = 'securo.accident'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Sinitri'

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)
    name = fields.Char(string="Titolo")
    relieved_on = fields.Date(string="Rilevato il")
    relieved_by = fields.Many2one('res.partner',
                                  string="Rilevato da")
                                  #domain="[('company_id', '=', company_id)]")
    solved_on = fields.Date(string="Risolta il")
    solved_by = fields.Many2one('res.partner',
                                string="Risolta da",)
                                #domain="[('company_id', '=', company_id)]")
    driver_id = fields.Many2one('hr.employee',
                                string="Conducente",)
                                #domain="[('company_id', '=', company_id)]")
    vehicle_id = fields.Many2one('fleet.vehicle',
                                 string="Veicolo",)
                                 #domain="[('company_id', '=', company_id)]")
    reason = fields.Text(string="Cos'è successo")
    location = fields.Char('Luogo')
    cause = fields.Text(string="Cause")
    action = fields.Text(string="Azioni fatte")
    severity = fields.Selection(
        [("low", "Bassa"),
         ("medium", "Media"),
         ("high", "Alta")], default='low', copy=False)
    to_do = fields.Char(string="Azioni da intraprendere")
    cost = fields.Float('Costo previsto')
    date_by = fields.Date(string="Entro il")
    attachment = fields.Many2many('ir.attachment',
                                  'attachment_accident_rel',
                                  'accident_id',
                                  'attach_id',
                                  string='Documenti')
    status = fields.Selection(
        [
            ('open','Aperta'),
            ('close','Chiusa')
        ],
        string='Stato',
        default='open')