from odoo import api, fields, models


class StockDeliveryNoteInvoiceWizard(models.TransientModel):
    _inherit = "stock.delivery.note.invoice.wizard"
    _description = "Delivery Note Invoice"

    group_line = fields.Boolean(string="Group Line")
    group_by=fields.Selection([('ddt_number','Numero DDT'),('ddt_date','Data DDT')],default='ddt_date',required=True)


    def create_invoices(self):
        delivery_note_ids = self.env["stock.delivery.note"].browse(
            self._context.get("active_ids", [])
        )
        delivery_note_ids.action_invoice(self.invoice_method,self.group_by)
        for invoice in delivery_note_ids.mapped("invoice_ids"):
            invoice.invoice_date = self.invoice_date

        return True

