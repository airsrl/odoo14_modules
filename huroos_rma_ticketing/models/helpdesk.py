# Copyright 2022 - Huroos srl - www.huroos.com
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html)

from odoo import fields, models, api, _
import json
import logging
import ast

_logger = logging.getLogger(__name__)


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    sale_order_id = fields.Many2one(
        comodel_name='sale.order',
        copy=False
    )
    sale_order_return_id = fields.Many2one(
        comodel_name='sale.order',
        copy=False
    )
    json_return = fields.Char(
        string="JSON return",
        copy=False
    )
    shippypro_label_url = fields.Char(
        string="Shipping label link",
        copy=False
    )
    
    def get_json_order_return_values(self):
        if not self.json_return:
            return None
        else:
            data = ast.literal_eval(self.json_return)
            return data
        
    def set_return_values_from_json(self):
        for record in self:
            try:
                """ Set the ticket infos from the JSON value """
                if not self.json_return:
                    return

                json_data = record.get_json_order_return_values()
                
                customer_email = json_data['customer_email'].strip() if "customer_email" in json_data else False
                
                _logger.info(f"customer_email: {customer_email}")
                
                order = json_data['order'].strip() if "order" in json_data else False
                if order and not order.startswith('#'):
                    order = '#' + order
                # Setting order number
                if order:
                    order_src = record.env['sale.order'].search([('name', '=', json_data['order'])], limit=1)
                    if order_src:
                        order_src.ensure_one()
                        record.sale_order_id = order_src.id

                # Return products list
                products = ""
                for p in json_data['products']:
                    product = self.env['product.product'].search(['|', ('default_code', '=', p['code']), ('barcode', '=', p['code'])], limit=1)
                    if product:
                        product = product[0]
                        products += f"\n    {p['qty']}x {product.display_name}"
                    else:
                        products += f"\n    {p['qty']}x {p['code']}"

                return_details = f"\n---------------------" \
                                 f"\nCustomer: {json_data['customer_name'] or (order.partner_id if order else '')} - {customer_email or ''}" \
                                 f"\nReason: {json_data['reason']}" \
                                 f"\nOrder: {(order_src.name + ' - ' + order_src.date_order.strftime('%d/%m/%Y')) if order_src else json_data['order']}" \
                                 f"\nNotes: {json_data['notes']}" \
                                 f"\nProducts:{products}"

                # Setting res partner
                if not record.partner_id:
                    res_partner_src = self.env["res.partner"].search([("email", "=", customer_email)], limit=1)
                    if res_partner_src:
                        record.partner_id = res_partner_src.id
                record.description = record.description or "" + return_details

            except Exception as ex:
                logging.error(f"_set_return_values_from_json: {record.id} - {json_data} {ex}")
                msg = f"""<b>Exception</b><br/>
                    <details>
                        <summary>Details - _set_return_values_from_json</summary>
                        <code>
                        {record.id}<br/><br/>
                        {json_data}<br/><br/>
                        {ex}
                        </code>
                    </details>"""
                self.message_post(
                    body=msg,
                    author_id=2
                )

    @api.onchange("shippypro_label_url")
    def set_shippy_pro_label_url_ticket(self):
        # TODO: AGGIORNARE LO STATO DEL TICKET ALLA RICEZIONE DELL'ETICHETTA DI SHIPPYPRO??
        return

    def create_goods_change(self):
        # Wizar order return
        self.ensure_one()
        if self.sale_order_id:
            form = self.env.ref("huroos_rma_ticketing.wizard_cambio_form_view")
            return {
                "name": _("Order return"),
                "type": "ir.actions.act_window",
                "res_model": "wizard.cambio",
                "views": [(form.id, "form")],
                "target": "new",
                "context": {
                    "default_helpdesk_id": self.id,
                },
            }
        else:
            raise UserWarning('Inserire l\'ordine di reso')

