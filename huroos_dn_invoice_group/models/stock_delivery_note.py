from odoo import models, _
from odoo.exceptions import UserError
from odoo.addons.l10n_it_delivery_note.models.stock_delivery_note import DATE_FORMAT,DOMAIN_INVOICE_STATUSES

class StockDeliveryNote(models.Model):
    _inherit = 'stock.delivery.note'

    def set_to_invoice(self):
        self.invoice_status = 'to invoice'

        for line in self.line_ids:
            line.invoice_status = 'to invoice'

        self.state = 'confirm'

    def action_invoice(self, invoice_method=False,group_by=False):
        #self.ensure_one()

        # Control if all orders are in state = sale, if not raise an error
        for order in self.sale_ids:
            if order.state != 'sale':
                raise UserError(_("L'operazione non può essere effettuata con ordini non confermati "
                                  "relativi al presente DDT. Si prega di confermare la ordine %s per continuare.")
                                  % order.name)


        orders_lines = self.mapped("sale_ids.order_line").filtered(
            lambda l: l.product_id
        )

        downpayment_lines = orders_lines.filtered(lambda l: l.is_downpayment)
        invoiceable_lines = orders_lines.filtered(lambda l: l.is_invoiceable)

        cache = self._fix_quantities_to_invoice(invoiceable_lines - downpayment_lines)



        for downpayment in downpayment_lines:
            order = downpayment.order_id
            order_lines = order.order_line.filtered(
                lambda l: l.product_id and not l.is_downpayment
            )

            if order_lines.filtered(lambda l: l.need_to_be_invoiced):
                cache[downpayment] = downpayment.fix_qty_to_invoice()


        invoice_ids = self.sale_ids.filtered(
            lambda o: o.invoice_status == DOMAIN_INVOICE_STATUSES[1]
        )._create_invoices(final=True)


        for line, vals in cache.items():
            line.write(vals)

        orders_lines._get_to_invoice_qty()

        for line in self.line_ids:
            line.write({"invoice_status": "invoiced"})
        if all(line.invoice_status == "invoiced" for line in self.line_ids):
            self.write(
                {"invoice_ids": [(4, invoice_id) for invoice_id in invoice_ids.ids]}
            )
            self._compute_invoice_status()
            invoices = self.env["account.move"].browse(invoice_ids.ids)
            invoices.group_lines_by_ddt(group_by)


