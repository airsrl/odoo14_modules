# Copyright 2022 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

import logging
from odoo import http
from datetime import datetime
from datetime import timedelta
import secrets
import string
import json
import hashlib
from odoo.http import request, JsonRequest, Response
from odoo.tools import date_utils
import ast

_logger = logging.getLogger(__name__)

DATETIME_FORMAT = "%Y-%m-%d %H:%M"
AUTH_TOKEN_LENGHT = 25
AUTH_TOKEN_HOURS_DURATION = 12


def alternative_json_response(self, result=None, error=None):
    if error is not None:
        response = error
    if result is not None:
        response = result
    mime = 'application/json'
    body = json.dumps(response, default=date_utils.json_default)
    return Response(
        body, status=error and error.pop('http_status', 200) or 200,
        headers=[('Content-Type', mime), ('Content-Length', len(body))]
    )


def _get_hash(text):
    hash_res = hashlib.md5(str(text).encode('utf-8')).hexdigest()
    return hash_res


def _manage_exception(ex, error_code=500):
    return {
            "status": error_code,
            "detail": "Exception occurred",
            "data": {
                "exception": ex
            }
        }


def _check_api_rma_auth_token(json_data):

    if not json_data or "auth_token" not in json_data:
        raise ValueError(f"Missing auth_token parameter.")
    auth_token = json_data["auth_token"]

    api_rma_auth_token = request.env['ir.config_parameter'].sudo().get_param("api_rma_auth_token")
    api_rma_auth_token_expiration = request.env['ir.config_parameter'].sudo().get_param("api_rma_auth_token_expiration")

    auth_token_hashed = _get_hash(auth_token)
    if auth_token_hashed != api_rma_auth_token:
        raise ValueError(f"Parameter auth_token not correct: {auth_token}.")
    if (not api_rma_auth_token_expiration) or datetime.strptime(api_rma_auth_token_expiration, DATETIME_FORMAT) < datetime.utcnow():
        raise ValueError(f"auth_token expired.")

    if "data" not in json_data or not json_data["data"]:
        raise ValueError(f"Missing data value.")

    return json_data["data"]


class api(http.Controller):

    @http.route('/api/get_authentication/', type='json', auth="none", methods=['POST'], csrf=False)
    def get_authentication(self):

        request._json_response = alternative_json_response.__get__(request, JsonRequest)

        try:
            json_data = request.jsonrequest
            _logger.info(f"getAuthentication: {json_data}")

            # Get api_rma_password from system parameters
            api_rma_password = request.env['ir.config_parameter'].sudo().get_param("api_rma_password")

            # Checking authentication password
            if "api_rma_password" not in json_data:
                raise ValueError(f"Missing parameter: {api_rma_password}.")
            if json_data["api_rma_password"] != api_rma_password:
                raise ValueError(f"Parameter api_rma_password uncorrect: {json_data['api_rma_password']}.")

            # Creating auth_token
            alphabet = string.ascii_letters + string.digits
            auth_token = ''.join(secrets.choice(alphabet) for i in range(AUTH_TOKEN_LENGHT))
            expiration_date = datetime.utcnow() + timedelta(hours=AUTH_TOKEN_HOURS_DURATION)

            # Saving values in system parameters
            auth_token_hashed = _get_hash(auth_token)
            request.env['ir.config_parameter'].sudo().set_param("api_rma_auth_token_expiration", expiration_date.strftime(DATETIME_FORMAT))
            request.env['ir.config_parameter'].sudo().set_param("api_rma_auth_token", auth_token_hashed)

            return {
                "status": 200,
                "detail": "auth_token created",
                "data": {
                    "auth_token": auth_token,
                    "expiration_date": expiration_date
                }
            }
        except ValueError as ex:
            exception = _manage_exception(ex, 401)
            return exception
        except Exception as ex:
            exception = _manage_exception(ex, 500)
            return exception

    @http.route('/api/get_order/', type='json', auth="none", methods=['POST'], csrf=False)
    def get_order(self):

        request._json_response = alternative_json_response.__get__(request, JsonRequest)

        try:
            json_data = request.jsonrequest

            # Checking auth token
            data = _check_api_rma_auth_token(json_data)

            if not data or "order_number" not in data:
                raise ValueError(f"Missing parameter order_number.")

            order_number = data["order_number"].strip()
            order_src = request.env['sale.order'].sudo().search([("name", "=", order_number)])
            order_lines = []
            if order_src:
                order = request.env['sale.order'].sudo().browse(order_src["id"])

            for ol in order.order_line:
                if not ol.display_type:
                    order_lines.append(
                        {
                            "sku": ol.product_id.default_code,
                            "product": ol.product_id.display_name,
                            "qty": ol.product_uom_qty
                        }
                    )
            return {
                "status": 200,
                "detail": f"Order {order.name} {order.date_order.strftime(DATETIME_FORMAT)} - {len(order.order_line)} order lines",
                "data": {
                    "customer": f"{order.partner_id.display_name}",
                    "date": order.date_order.strftime(DATETIME_FORMAT),
                    "warehouse": order.warehouse_id.name,
                    "order_lines": order_lines
                }
            }
        except ValueError as ex:
            exception = _manage_exception(ex, 401)
            return exception
        except Exception as ex:
            exception = _manage_exception(ex, 500)
            return exception

    @http.route('/api/create_rma_ticket/', type='json', auth="none", methods=['POST'], csrf=False)
    def create_rma_ticket(self):

        request._json_response = alternative_json_response.__get__(request, JsonRequest)

        try:
            json_data = request.jsonrequest
            
            # Checking auth token
            data = _check_api_rma_auth_token(json_data)

            ticket_data = {
                "name": f"{data['customer_name']} - Order: {data['order']}",
                "json_return": data
            }
            new_ticket = request.env["helpdesk.ticket"].sudo().create(ticket_data)
            new_ticket.set_return_values_from_json()
            return {
                "status": 200,
                "detail": f"RMA ticket created",
                "data": {
                    "ticket_id": f"#{new_ticket.id}"
                }
            }
        except Exception as ex:
            exception = _manage_exception(ex, 500)
            return exception


