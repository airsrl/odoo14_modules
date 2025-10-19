import datetime
import logging

from odoo import models, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def force_delete_invoice_and_related_payment(self):
        types = self.mapped('move_type')
        if not self._context.get('force_delete'):
            raise UserError(_("You cannot delete an invoice. something went wrong force delete delete context"))
        count = len(self)
        progr = 0

        for invoice in self:
            progr += 1

            relatedpayments_list = self and invoice._get_reconciled_info_JSON_values() or []
            relatedpayments_ids = relatedpayments_list and map(lambda x: x['account_payment_id'],
                                                               relatedpayments_list) or False
            relatedpayments_ids = relatedpayments_ids and self.env['account.payment'].browse(
                list(relatedpayments_ids)) or self.env['account.payment']
            if relatedpayments_ids:
                relatedpayments_ids.action_draft()
                for payment in relatedpayments_ids:
                    payment.write({'name': False})
                    # BUG FIX calling payment.unlink()  will delete even the account.move linked to the payment
                    payment.unlink()
                logging.info("Fattura Rimossa: " + str(progr) + '/' + str(count))
        # I have to add .exists()  in order to get rid of the error "Record does not exist or has been deleted"
        invoice_posted_cancel = self.filtered(lambda x: x.exists() and x.state in ['posted', 'cancel', 'draft']) or \
                                self.env['account.move']
        if invoice_posted_cancel:
            for inv in invoice_posted_cancel:
                inv.button_draft()
                inv.with_context(force_delete=True).unlink()

        return {
            'name': _('Invoices'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'account.move',
            'views': [(self.env.ref('account.view_invoice_tree').id, 'tree'),
                      (self.env.ref('account.view_move_form').id, 'form')],
            'domain': [('move_type', 'in', types)],
        }
