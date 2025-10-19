from odoo import fields, models, api
INVOICE_STATUSES = [
    ("no", "Nothing to invoice"),
    ("to invoice", "To invoice"),
    ("invoiced", "Fully invoiced"),
]
DOMAIN_INVOICE_STATUSES = [s[0] for s in INVOICE_STATUSES]

class StockDeliveryNoteLine(models.Model):
    _inherit = "stock.delivery.note.line"

    @api.model
    def _prepare_detail_lines(self, moves):
        lines = []
        for move in moves:

            name = move.name
            # if move.product_id.description_sale:
            #     name += "\n" + move.product_id.description_sale

            line = {
                "move_id": move.id,
                "name": name,
                "product_id": move.product_id.id,
                "product_qty": move.product_uom_qty,
                "product_uom_id": move.product_uom.id,
            }

            if move.sale_line_id:
                order_line = move.sale_line_id
                order = order_line.order_id

                line["price_unit"] = order_line.price_unit
                line["currency_id"] = order.currency_id.id
                line["discount"] = order_line.discount
                line["tax_ids"] = [(6, False, order_line.tax_id.ids)]
                line["invoice_status"] = DOMAIN_INVOICE_STATUSES[1]

            lines.append(line)

        return lines
