from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        res =super(AccountMove, self).action_post()

        invoice = self
        if invoice.move_type in ['out_invoice']:

            self.env['report.fornitori.data'].create_report_fornitori_data(invoice)
        elif invoice.move_type in ['out_refund']:
            self.env['report.fornitori.data'].create_report_fornitori_data(invoice,refund=True)
        return res

    # def create_report_data(self):
    #     invoices=self.env['account.move'].search([])
    #
    #     for invoice in invoices:
    #         report = self.env['report.fornitori.data'].search([('move_id', '=', invoice.id)])
    #         if not report:
    #             if invoice.move_type in ['out_invoice']:
    #
    #                 self.env['report.fornitori.data'].create_report_fornitori_data(invoice)
    #             elif invoice.move_type in ['out_refund']:
    #                 self.env['report.fornitori.data'].create_report_fornitori_data(invoice,refund=True)
class stock_move_line_custom(models.Model):
    _inherit = "stock.move.line"

    #RESI I CAMPI STORED (KP)
    in_out_move = fields.Float(String='Qt in/out', compute='compute_in_out_move',store=True)
    movimenti_prodotto = fields.Float(String="Prezzo", compute='compute_products_unit_value',store=True)


    @api.depends('location_id','qty_done')
    def compute_in_out_move(self):
        return super(stock_move_line_custom, self).compute_in_out_move()


    @api.depends('move_id','qty_done','move_id.sale_line_id.price_unit','move_id.purchase_line_id.price_unit')
    def compute_products_unit_value(self):
        return super(stock_move_line_custom, self).compute_products_unit_value()

