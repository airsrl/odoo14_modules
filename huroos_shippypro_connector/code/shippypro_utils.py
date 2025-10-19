# Copyright 2022 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

import base64
import requests
import json
from datetime import datetime
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

# Standard Base64 Encoding
# https://www.shippypro.com/ShippyPro-API-Documentation/#authorization-header
shippyPRO_API_URL = "https://www.shippypro.com/api/v1"


def get_carriers(env):
    """ Retriving the available carriers from ShippyPRO """
    authentication_code = env.company.authentication_code
    if not authentication_code:
        return []
    encodedBytes = base64.b64encode((authentication_code + ':').encode("ASCII"))
    encoded_authentication_code = str(encodedBytes, "ASCII")

    values = {
        "Method": "GetCarriers",
        "Params": {}
    }
    values = json.dumps(values)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + encoded_authentication_code
    }
    sp_resp = requests.get(
        shippyPRO_API_URL,
        headers=headers,
        data=values
    )
    carriers_list = []
    if sp_resp.ok:
        resp_json = json.loads(sp_resp.text)
        if "Carriers" in resp_json:
            carriers_json = resp_json['Carriers']
            for carrier_type in carriers_json:
                for carrier in carriers_json[carrier_type]:
                    carriers_list.append(
                        (
                            carrier['CarrierID'],
                            carrier_type,
                            carrier['Label'],
                            carrier['CarrierService']
                        )
                    )

    return carriers_list


def shippy_pro_put_order(stock_picking):
    """ Creates an order on ShippyPRO """

    if stock_picking.shippy_pro_order_number and stock_picking.shippy_pro_order_number != "":
        raise UserError(f"ShippyPRO order number already exists: {stock_picking.shippy_pro_order_number}")

    env = stock_picking.env

    item_array = []
    items_count = 0
    parcels_array = []

    authentication_code = stock_picking.env.company.authentication_code
    APIOrdersID = stock_picking.env.company.APIOrdersID
    imageurl = stock_picking.env.company.image_url_path or ''
    encodedBytes = base64.b64encode((authentication_code + ':').encode("ASCII"))  # authkey + ':'
    encoded_authentication_code = str(encodedBytes, "ASCII")

    if not authentication_code:
        raise UserError("Authentication code missing, please set the parameter in company settings.")
    if not imageurl:
        raise UserError(
            "Good image URL missing, please set the parameter in company settings.")
    if not APIOrdersID:
        raise UserError(
            "API orders ID missing, please set the parameter in company settings."
            "SHIPPYPRO: You need to add an APIOrders marketplace in order to use this request."
            "You can retrieve your own APIOrdersID by clicking on Edit button inside the marketplace page.")

    if stock_picking.picking_type_id.code == "outgoing":
        for move in stock_picking.move_lines:
            if move.move_line_ids:
                for mov_l in move.move_line_ids:
                    if mov_l.product_qty > 0:
                        item_dict = {
                            "title": move.product_id.display_name,
                            "imageurl": imageurl,
                            "quantity": int(mov_l.product_qty),
                            "price": mov_l.product_id.list_price,
                            "sku": move.product_id.default_code
                        }
                        item_array.append(item_dict)

            items_count += int(mov_l.product_qty)

        to_address = {
            "name": stock_picking.partner_id.name,
            "company": stock_picking.partner_id.parent_id.name if stock_picking.partner_id.parent_id else '',
            "street1": stock_picking.partner_id.street or '',
            "street2": stock_picking.partner_id.street2 or '',
            "city": stock_picking.partner_id.city or '',
            "state": stock_picking.partner_id.state_id.name,
            "zip": stock_picking.partner_id.zip or '',
            "country": stock_picking.partner_id.country_id.code,
            "phone": stock_picking.partner_id.phone or '',
            "email": stock_picking.partner_id.email or ''
        }

    elif stock_picking.picking_type_id.code == "incoming":
        for move in stock_picking.move_ids_without_package:
            if move.product_uom_qty > 0:
                item_dict = {
                    "title": move.product_id.display_name,
                    "imageurl": imageurl,
                    "quantity": int(move.product_uom_qty),
                    "price": move.product_id.list_price,
                    "sku": move.product_id.default_code
                }
                item_array.append(item_dict)

            items_count += int(move.quantity_done)
            
        to_address = {
            "name": env.company.name, 
            "company": '',
            "street1": env.company.street or '',
            "street2": env.company.street2 or '',
            "city": env.company.city or '',
            "state": env.company.state_id.name or '',
            "zip": env.company.zip or '',
            "country": env.company.country_id.code or '',
            "phone": env.company.phone or '',
            "email": env.company.email or ''
        }
    else:
        raise UserError(f"Picking type {stock_picking.picking_type_id.code} is not suitable for ShippyPRO")

    # Packages/parcels
    if stock_picking.has_packages:
        parcels_array.clear()
        packages = stock_picking.package_ids
        for package in packages:
            parcel_weight = package.shipping_weight
            packaging_id = package.packaging_id or env.company.delivery_package_type_id
            if not packaging_id:
                raise UserError(f"parcel type not set for {package.name}. You can set e dafult packaging type in company settings.")
            length = packaging_id.packaging_length
            height = packaging_id.height
            width = packaging_id.width
            parcels_array.append(
                {
                    "length": length,
                    "width": width,
                    "height": height,
                    "weight": parcel_weight
                }
            )
    else:
        parcels_array.append({"length": 1, "width": 1, "height": 1, "weight": 1})

    values = {
        "Method": "PutOrder",
        "Params": {
            "to_address": to_address,
            "parcels": parcels_array,
            "items": item_array,
            "TransactionID": stock_picking.origin,
            "Date": int(datetime.timestamp(datetime.now())),
            "Currency": "EUR",
            "ItemsCount": sum(c['quantity'] for c in item_array),
            "ContentDescription": "Goods",
            "Total": sum(c['price'] for c in item_array),
            "Status": "",
            "APIOrdersID": int(APIOrdersID),
            "ShipmentAmountPaid": 0,
            "Incoterm": "DAP",
            "BillAccountNumber": "",
            "PaymentMethod": "",
            "ShippingService": "",
            "Note": stock_picking.note if stock_picking.note and bool(stock_picking.note) else ''
        }
    }
    values = json.dumps(values)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + encoded_authentication_code
    }
    sp_resp = requests.get(
        shippyPRO_API_URL,
        headers=headers,
        data=values
    )

    # Logging result
    if sp_resp.ok:
        stock_picking.message_post(
            body=f"""<b>Shipping sent to ShippyPro</b><br/>
            <details>
                <summary>Details</summary>
                <code>
                {values}
                </code>
            </details>""",
            author_id=2
        )
        stock_picking.update({'shippy_pro_sent_date': datetime.now()})
        return True
    elif '401' or '403' in sp_resp:
        _logger.info(sp_resp)
        raise UserError(f"Authentication failed, please check authentication params in company settings.<br><br/>{sp_resp.text}")
    else:
        stock_picking.message_post(
            body=f"""<b>Shipping NOT sent to ShippyPro</b><br/>
            <details>
                <summary>Details</summary>
                <code>
                {values}
                </code>
                <br/>
                <br/>
                {sp_resp.text}
            </details>""",
            author_id=2
        )
        return False


def shippy_pro_ship_order(stock_picking):
    """ Creatse a confirmed shipping in ShippyPRO """

    if stock_picking.shippy_pro_order_number and stock_picking.shippy_pro_order_number != "":
        raise UserError(f"ShippyPRO order number already exists: {stock_picking.shippy_pro_order_number}")

    env = stock_picking.env
    item_array = []
    items_count = 0
    parcels_array = []

    authentication_code = env.company.authentication_code
    imageurl = env.company.image_url_path or ''
    encodedBytes = base64.b64encode((authentication_code + ':').encode("ASCII"))  # authkey + ':'
    encoded_authentication_code = str(encodedBytes, "ASCII")

    if stock_picking.picking_type_id.code == "outgoing":
        for move in stock_picking.move_lines:
            if move.move_line_ids:
                for mov_l in move.move_line_ids:
                    if mov_l.qty_done > 0:
                        item_dict = {
                            "title": move.product_id.display_name,
                            "imageurl": imageurl,
                            "quantity": int(mov_l.product_qty),
                            "price": mov_l.product_id.list_price,
                            "sku": move.product_id.default_code
                        }
                        item_array.append(item_dict)

            items_count += int(move.quantity_done)

        to_address = {
            "name": stock_picking.partner_id.name,
            "company": stock_picking.partner_id.parent_id.name if stock_picking.partner_id.parent_id else '',
            "street1": stock_picking.partner_id.street or '',
            "street2": stock_picking.partner_id.street2 or '',
            "city": stock_picking.partner_id.city or '',
            "state": stock_picking.partner_id.state_id.name or '',
            "zip": stock_picking.partner_id.zip or '',
            "country": stock_picking.partner_id.country_id.code or '',
            "phone": stock_picking.partner_id.phone or '-',
            "email": stock_picking.partner_id.email or ''
        }
        
        from_address = {
            "name": env.company.name, 
            "company": '',
            "street1": env.company.street or '',
            "street2": env.company.street2 or '',
            "city": env.company.city or '',
            "state": env.company.state_id.name or '',
            "zip": env.company.zip or '',
            "country": env.company.country_id.code or '',
            "phone": env.company.phone or '-',
            "email": env.company.email or ''
        }
        
    elif stock_picking.picking_type_id.code == "incoming":
        for move in stock_picking.move_ids_without_package:
            if move.move_line_ids:
                for mov_l in move.move_line_ids:
                    if mov_l.qty_done > 0:
                        item_dict = {
                            "title": move.product_id.display_name,
                            "imageurl": imageurl,
                            "quantity": int(mov_l.product_uom_qty),
                            "price": mov_l.product_id.list_price,
                            "sku": move.product_id.default_code
                        }
                        item_array.append(item_dict)

            items_count += int(move.quantity_done)
            
        to_address = {
            "name": env.company.name, 
            "company": '',
            "street1": env.company.street or '',
            "street2": env.company.street2 or '',
            "city": env.company.city or '',
            "state": env.company.state_id.name or '',
            "zip": env.company.zip or '',
            "country": env.company.country_id.code or '',
            "phone": env.company.phone or '-',
            "email": env.company.email or ''
        }
        
        from_address = {
            "name": stock_picking.partner_id.name,
            "company": stock_picking.partner_id.parent_id.name if stock_picking.partner_id.parent_id else '',
            "street1": stock_picking.partner_id.street or '',
            "street2": stock_picking.partner_id.street2 or '',
            "city": stock_picking.partner_id.city or '',
            "state": stock_picking.partner_id.state_id.name or '',
            "zip": stock_picking.partner_id.zip or '',
            "country": stock_picking.partner_id.country_id.code or '',
            "phone": stock_picking.partner_id.phone or '-',
            "email": stock_picking.partner_id.email or ''
        }
    else:
        raise UserError(f"Picking type {stock_picking.picking_type_id.code} is not suitable for ShippyPRO")
    
    # Packages/parcels
    if stock_picking.has_packages:
        parcels_array.clear()
        packages = stock_picking.package_ids
        for package in packages:
            parcel_weight = package.shipping_weight
            packaging_id = package.packaging_id or env.company.delivery_package_type_id
            if not packaging_id:
                raise UserError(f"parcel type not set for {package.name}. You can set e dafult packaging type in company settings.")
            length = packaging_id.packaging_length
            height = packaging_id.height
            width = packaging_id.width
            parcels_array.append(
                {
                    "length": length,
                    "width": width,
                    "height": height,
                    "weight": parcel_weight
                }
            )
    else:
        parcels_array.append({"length": 1, "width": 1, "height": 1, "weight": 1})

    values = {
        "Method": "Ship",
        "Params": {
            "to_address": to_address,  # Based on incoming/outgoing stock movement tyee
            "from_address": from_address,  # Based on incoming/outgoing stock movement tyee
            "parcels": parcels_array,
            "TotalValue": str(sum(c['price'] * c['quantity'] for c in item_array)),
            "TransactionID": stock_picking.origin,
            "ContentDescription": "Goods",
            "Insurance": 0,
            "InsuranceCurrency": "EUR",
            "CashOnDelivery": 0,
            "CashOnDeliveryCurrency": "EUR",
            "CashOnDeliveryType": 0,
            "CarrierName": stock_picking.carrier.carrier_type,
            "CarrierService": stock_picking.carrier.carrier_label,
            "CarrierID": int(stock_picking.carrier.carrier_id),
            "OrderID": stock_picking.origin,
            "RateId": "",
            "Incoterm": "DAP",
            "BillAccountNumber": "",
            "Note": stock_picking.note if stock_picking.note and bool(stock_picking.note) else '',
            "Async": False
        }
    }
    _logger.info(values)
    values = json.dumps(values)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + encoded_authentication_code
    }
    sp_resp = requests.get(
        shippyPRO_API_URL,
        headers=headers,
        data=values
    )

    if sp_resp.ok:
        resp_json = json.loads(sp_resp.text)
        if 'LabelURL' in resp_json and resp_json['LabelURL'] and 'NewOrderID' in resp_json and resp_json['NewOrderID']:
            resp_json = json.loads(sp_resp.text)
            stock_picking.label_url = resp_json['LabelURL']
            stock_picking.shippy_pro_order_number = resp_json['NewOrderID']
            stock_picking.message_post(
                body=f"""<b>Shipping confirmed in ShippyPro</b><br/>
                    <details>
                        <summary>Details</summary>
                        <code>
                        {values}
                        </code>
                    </details>""",
                author_id=2)
        elif '401' or '403' in sp_resp["status_code"]:
            _logger.info(sp_resp)
            raise UserError(
                f"Authentication failed, please check authentication params in company settings.\n\n{sp_resp.text}")
        else:
            stock_picking.message_post(
                body=f"""<b>Shipping NOT confirmed in ShippyPro</b><br/>
                    <details>
                        <summary>Details</summary>
                        <code>
                        {resp_json}
                        </code>
                    </details>""",
                author_id=2)
            return False


def task_exec_get_tracking_numbers(record):
    """ Retriving the missing tracking infos from ShippyPRO to stock.picking """
    try:
        env = record.env
        authentication_code = env.company.authentication_code
        encodedBytes = base64.b64encode((authentication_code + ':').encode("ASCII"))  # authkey + ':'
        encoded_authentication_code = str(encodedBytes, "ASCII")

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + encoded_authentication_code
        }

        # Searching missing trackings in stock.picking
        stock_picking_list = record.env['stock.picking'].sudo().search(
            ['|',
             ('shippy_pro_tracking_number', '=', False),  # OR
             ('shippy_pro_tracking_number', '=', ''),
             ('shippy_pro_order_number', '!=', False)])

        if stock_picking_list:
            for picking in stock_picking_list:
                try:
                    values = {
                        "Method": "GetOrder",
                        "Params": {
                            "OrderID": int(picking['shippy_pro_order_number'])
                        }
                    }
                    values = json.dumps(values)

                    sp_resp = requests.get(
                        shippyPRO_API_URL,
                        headers=headers,
                        data=values
                    )
                    picking_to_update = env['stock.picking'].browse(picking['id'])
                    to_upd = picking_to_update[0]

                    if sp_resp.ok:
                        resp_json = json.loads(sp_resp.text)
                        if 'Error' in resp_json and resp_json['Error']:
                            to_upd.update(
                                {
                                    'shippy_pro_tracking_number': False,
                                    'shippy_pro_tracking_external_link': False
                                }
                            )
                        else:
                            to_upd.update(
                                {
                                    'shippy_pro_tracking_number': resp_json['TrackingNumber'] if resp_json['TrackingNumber'] and resp_json['TrackingNumber'] != '' else False,
                                    'shippy_pro_tracking_external_link': resp_json['TrackingExternalLink'],

                                    'carrier_tracking_ref': to_upd['carrier_tracking_ref'] or resp_json['TrackingNumber']
                                }
                            )
                    else:
                        to_upd.update(
                            {
                                'shippy_pro_tracking_number': False,
                                'shippy_pro_tracking_external_link': False
                            }
                        )
                except Exception as ex:
                    logging.error(f"task_exec_get_tracking_numbers - stock_picking_to_update {picking_to_update['id'] if picking_to_update else ''}: {ex}")
                    continue

    except Exception as ex:
        logging.error(f"task_exec_get_tracking_numbers: {ex}")
