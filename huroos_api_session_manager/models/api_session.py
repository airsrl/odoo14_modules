# Copyright 2022 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

import secrets
import string
from datetime import datetime
from datetime import timedelta
from odoo import fields, models, api
from odoo.exceptions import UserError, AccessError

import logging
_logger = logging.getLogger(__name__)

DATETIME_FORMAT = "%Y-%m-%d %H:%M"
AUTH_TOKEN_LENGHT = 25
AUTH_TOKEN_HOURS_DURATION = 12


def _get_new_auth_token(auth_token_lenght=AUTH_TOKEN_LENGHT, token_hours_duration=AUTH_TOKEN_HOURS_DURATION):
    # Creating auth_token
    alphabet = string.ascii_letters + string.digits
    auth_token = ''.join(secrets.choice(alphabet) for i in range(auth_token_lenght))
    auth_token = auth_token
    expiration_date = datetime.utcnow() + timedelta(hours=token_hours_duration)

    return auth_token, expiration_date


class ApiAuthentication(models.Model):
    _name = "api.auth"
    _description = "API auth password"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string="Name",
        required=True,
        tracking=True
    )
    active = fields.Boolean(
        string="Active",
        tracking=True,
        default=True
    )
    description = fields.Text(
        string="Description"
    )

    def _get_password(self):
        return f"API_{''.join(secrets.choice('0123456789') for i in range(10))}"
    password = fields.Char(
        string="Password",
        required=True,
        copy=False,
        default=_get_password
    )
    validity_start = fields.Date(
        string="Validity start date",
        tracking=True,
        default=datetime.utcnow()
    )
    validity_end = fields.Date(
        string="Validity end date",
        tracking=True
    )
    contact_id = fields.Many2one(
        comodel_name='res.partner',
        tracking=True
    )
    api_session_ids = fields.One2many(
        comodel_name="api.session",
        inverse_name="api_auth_id",
        string="Sessions",
        readonly=True
    )


class ApiSession(models.Model):
    _name = "api.session"
    _description = "API token session"

    auth_token = fields.Char(
        string="Token",
        readonly=True,
        copy=False
    )
    auth_token_expiration = fields.Datetime(
        string="Token expiration",
        readonly=True,
        copy=False
    )
    api_auth_id = fields.Many2one(
        comodel_name='api.auth',
        readonly=True
    )

    @api.model_create_multi
    def create(self, vals_list):

        for vals in vals_list:
            # Creating token
            auth_token, expiration_date = _get_new_auth_token()
            vals["auth_token"] = auth_token
            vals["auth_token_expiration"] = expiration_date

        res = super(ApiSession, self).create(vals_list)
        return res


class ApiSessionUtils(models.AbstractModel):
    """
    Classe abstract per esporre le funzioni di richiesta token e verifica validità token
    """
    _name = "api_session.utils"
    _description = "API session utils"

    def get_auth_token(self, password):
        if not password:
            raise AccessError(f"Password errata.")

        api_auth = self.env["api.auth"].search(
            [('password', '=', password)],
            limit=1
        )
        if not api_auth:
            raise AccessError(f"Password errata.")
        api_auth.ensure_one()
        if not api_auth.active:
            raise AccessError(f"Autorizzazione API non attiva.")
        now = datetime.utcnow().date()
        if api_auth.validity_start and api_auth.validity_start > now:
            raise AccessError(
                f"Autorizzazione API non attiva, data attivazione: {api_auth.validity_start.strftime('%d-%m-%Y')}")
        if api_auth.validity_end and api_auth.validity_end < now:
            raise AccessError(
                f"Autorizzazione API non attiva, data disattivazione: {api_auth.validity_end.strftime('%d-%m-%Y')}")

        api_session_data = {
            "api_auth_id": api_auth.id
        }
        api_session = self.env["api.session"].create(api_session_data)
        return api_session

    def check_auth_token_is_valid(self, auth_token):
        if not auth_token:
            raise AccessError(f"Token errato.")

        api_session = self.env["api.session"].search(
            [('auth_token', '=', auth_token)],
            limit=1
        )

        is_valid = False
        if not api_session:
            raise AccessError(f"Token not valid.")
        elif api_session.auth_token_expiration < datetime.utcnow():
            raise AccessError(f"Token expired.")
        elif not api_session.api_auth_id.active:
            raise AccessError(f"API password expired.")
        else:
            is_valid = True

        log_entry = {
            'create_uid': self.env.uid,
            'type': 'server',
            'name': 'huroos_api_session_manager',
            'level': 'info',
            'path': 'huroos-function',
            'line': '0',
            'func': 'check_auth_token_is_valid',
            'message': f"{api_session.api_auth_id.name} token: {auth_token} is valid: {is_valid}"
        }
        self.env['ir.logging'].create(log_entry)

        return is_valid


