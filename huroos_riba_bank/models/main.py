from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _process_riba_partner(self):
        if self.invoice_payment_term_id.fatturapa_pm_id.code == 'MP12':
            self.bank_partner_id = self.partner_id
        else:
            self.bank_partner_id = self.company_id.partner_id if self.company_id else False

    def _process_riba_bank(self):
        if self.invoice_payment_term_id.fatturapa_pm_id.code == 'MP12':
            bank_ids = self.partner_id.bank_ids
            self.partner_bank_id = bank_ids and bank_ids[0]
        else:
            bank_ids = self.company_id.partner_id.bank_ids if self.company_id else False
            self.partner_bank_id = bank_ids and bank_ids[0]

    @api.onchange('partner_id')
    def _onchange_partner_id(self):
        res = super(AccountMove, self)._onchange_partner_id()
        if self.move_type == 'out_invoice':
            self._process_riba_partner()
            self._process_riba_bank()
        return res

    @api.onchange('invoice_payment_term_id')
    def _onchange_invoice_payment_term_id(self):
        if self.move_type == 'out_invoice':
            self._process_riba_partner()
            self._process_riba_bank()

    @api.depends('commercial_partner_id', 'move_type')
    def _compute_bank_partner_id(self):
        for move in self:
            if move.is_inbound():
                if move.move_type == 'out_invoice':
                    move._process_riba_partner()
                else:
                    move.bank_partner_id = move.company_id.partner_id
            else:
                move.bank_partner_id = move.commercial_partner_id


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _create_invoices(self, grouped=False, final=False, date=None):
        res = super(SaleOrder, self)._create_invoices(grouped, final, date)
        for invoice in res:
            invoice._process_riba_bank()
        return res