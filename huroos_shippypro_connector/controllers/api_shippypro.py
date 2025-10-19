# import base64
# import werkzeug
# from odoo import _, exceptions, http, tools
# from odoo.http import request
# import json
# import logging
# from datetime import datetime
#
# _logger = logging.getLogger(__name__)
#
#
# class api_shippypro(http.Controller):
#     @http.route(['/shippypro/tracking_update'], type='json', auth='public')
#     def tracking_update(self, **post):
#         _logger.info(f'tracking_update')
#         try:
#             data = json.loads(request.httprequest.data)
#             _logger.info(f'data: {data}')
#
#             #  values = {
#             #     "Event": "TRACKING_UPDATE",
#             #     "tracking" : "1ZA103756899507566",
#             #     "date": 1489659960,
#             #     "message": "DELIVERED",
#             #     "city": "MOTRIL",
#             #     "est_delivery_date": "1489659960",
#             #     "first_status_date": "1489646578",
#             #     "late": "0",
#             #     "code": 6,
#             #     "OrderID": "191252",
#             #     "TransactionID": "ORDER2365",
#             #     "TrackingCarrier": "UPS",
#             #     "TrackingCarrierID": "123",
#             #     "MarketplaceID": "123",
#             #     "MarketplacePlatform": "Amazon",
#             #     "ExternalLink": "https://www.carrierwebsite.com/tracking/123"
#             # }
#
#             if not data["tracking"] or data["tracking"] == '':
#                 return '{"response": "OK"}'
#
#             data_upd = {"carrier_tracking_ref": data["tracking"]}
#             if data["est_delivery_date"] and data["est_delivery_date"] != '':
#                 data_upd['shippy_pro_data_arrivo_stimata'] = datetime.fromtimestamp(int(data["est_delivery_date"]))
#
#             stock_picking = request.env['stock.picking'].sudo().search([('origin', '=', data['TransactionID'])])
#             for record in stock_picking:
#                 record.update(data_upd)
#
#                 record.message_post(body=f"""<b>Tracking aggiornato: {data["tracking"]}</b><br/>
#                                             <details>
#                                                 <summary>Dettagli</summary>
#                                                 <code>
#                                                 {data}
#                                                 </code>
#                                             </details>""", author_id=2)
#
#             return '{"response": "OK"}'
#         except Exception as e:
#             _logger.error(f'tracking_update: - {e}')
#             return '{"response": "KO"}'
