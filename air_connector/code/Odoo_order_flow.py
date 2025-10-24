from odoo import models
import logging, json


class sale_order_api(models.Model):
    _inherit = 'sale.order'

    def action_invoice_api(self):
        fatt = self._create_invoices()
        return f"order_id: {self.id} - Creata fattura in bozza id {fatt.id} per l'ordine {self.name}"


class sale_order_api(models.Model):
    _inherit = 'account.move'

    def action_confirm_invoice_api(self):
        self.action_post()
        return f"invoice_id: {self.id} - Fattura confermata  {self.state}"

    # def action_register_payment_api(self):
    #     # Dati accesso wordpress da Configurazione Odoo
    #     account_payment = self.env['account.payment']
    #
    #     payment_env = self.env['account.payment'].with_context(default_invoice_ids=[(4, self.id, False)])
    #     payment = payment_env.create({
    #         'payment_date': self.date,
    #         'payment_method_id': 1,
    #         'payment_type': 'inbound',
    #         'partner_type': 'customer',
    #         'communication': self.name,
    #         'partner_id': self.partner_id.id,
    #         'amount': self.amount_total,
    #         # 'journal_id': default_journal_id.id,
    #         # 'company_id': SaleInvoice.company_id.id,
    #         'currency_id': self.env.company and self.env.company.currency_id and self.env.company.currency_id.id,
    #         'payment_difference_handling': 'reconcile',
    #         # 'writeoff_account_id': self.diff_income_account.id,
    #     })
    #     payment.post()
    #     return f"invoice_id: {self.id} - Creato pagamento atteso: {payment}"
