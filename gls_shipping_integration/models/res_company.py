# -*- coding: utf-8 -*-
from odoo import fields, models, api


class GLSResCompany(models.Model):
    _inherit = 'res.company'

    use_gls_italy_shipping_provider = fields.Boolean(copy=False, string="Are You Using GLS Italy?",
                                                     help="If use GLS Italy shipping Integration than value set TRUE.",
                                                     default=False)

    gls_italy_sede = fields.Char(string="Sede", help="Enter gls italy's sede number")
    gls_italy_customer_code = fields.Char(string="Customer Code", help="Enter gls italy's customer code")
    gls_italy_password = fields.Char(string="Password", help="Enter gls italy's account password")
    gls_italy_api_url = fields.Char(string="API URl", help="Enter gls italy api url", default="https://labelservice.gls-italy.com/ilswebservice.asmx")

    gls_italy_contract_code = fields.Char(string="Contract Code base", help="Enter gls contract code Italy")
    gls_italy_contract_code_2 = fields.Char(string="Contract Code 2")
    gls_italy_contract_code_3 = fields.Char(string="Contract Code 3")
    gls_italy_contract_code_4 = fields.Char(string="Contract Code 4")
    gls_italy_contract_code_5 = fields.Char(string="Contract Code 5")