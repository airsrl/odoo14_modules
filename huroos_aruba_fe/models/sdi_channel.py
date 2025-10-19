# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).
import datetime
import logging
import time

import requests
from pytz import timezone

from odoo import models, fields, api, _, exceptions

SDI_CHANNELS = [
    ('web', 'Web service')
]

SDI_PROVIDER = [
    ('aruba', 'ARUBA'),
]

class SdiChannel(models.Model):
    _inherit = 'sdi.channel'

    channel_type = fields.Selection(selection_add=SDI_CHANNELS, ondelete={'web': 'cascade'})
    provider = fields.Selection(selection=SDI_PROVIDER, ondelete={'aruba': 'cascade'})
    web_server_refresh_token = fields.Char()
    active_web_server = fields.Boolean()
    web_server_method_address = fields.Char(default='https://ws.fatturazioneelettronica.aruba.it')
    web_server_address = fields.Char(string='Web server address', default='https://auth.fatturazioneelettronica.aruba.it/auth/signin')
    web_server_login = fields.Char(string='Web server login')
    web_server_password = fields.Char(string='Web server password')
    web_server_token = fields.Char(string='Web server token')

    def get_default_ws(self):
        """
        Ritorna i webservices (Attivi) da utilizzare
        :return:
        """
        return self.search([('active_web_server', '=', True)])

    def web_auth(self):
        """
        Utilizza le credenziali fornite per ottenere il token
        se e' disponibile il refresh token utilizza questo
        """
        if self.provider == 'aruba':
            header = {'Content-Type': 'application/x-www-form-urlencoded'}

            last_auth = fields.Datetime.context_timestamp(self.with_context(tz='Europe/Rome'), self.write_date)
            now_date = datetime.datetime.now(timezone('Europe/Rome'))
            token_minutes_validity = abs((last_auth - now_date).total_seconds() / 60)

            if not self.web_server_token or token_minutes_validity > 25:
                #Si ottiene il token solo se Manca oppure è più vecchio di 25 minuti
                data = {
                    'grant_type': 'password',
                    'username': self.web_server_login,
                    'password': self.web_server_password,
                }

                r = False

                try:
                    r = requests.post(self.web_server_address, headers=header, data=data, timeout=5)
                except Exception as e:
                    time.sleep(10)
                    logging.info("Tentativo Connessione....")
                    self.web_auth()

                if r:
                    if r.status_code == 200:
                        r = r.json()
                        logging.info("Connessione OK")
                        if 'error' in r:
                            if r['error'] == 'invalid_grant':
                                # Il token e' scaduto
                                self.web_server_refresh_token = ''
                                self.web_server_token = ''
                                self.web_auth()
                        else:
                            self.web_server_token = r['access_token']
                            self.web_server_refresh_token = r['refresh_token']
                    else:
                        time.sleep(5)
                        logging.info("Ulteriore Tentativo Connessione....")
                        self.web_auth()
        else:
            raise exceptions.UserError(_('Only Aruba Provider is Supported'))


    @api.onchange('provider')
    def onchange_provider(self):
        self.web_server_method_address = 'https://ws.fatturazioneelettronica.aruba.it'
        self.web_server_address = 'https://auth.fatturazioneelettronica.aruba.it/auth/signin'
