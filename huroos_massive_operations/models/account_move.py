from odoo import models, fields, api,_
from odoo.exceptions import UserError,ValidationError
from odoo.addons.sale.models.account_move import AccountMove as AMove

class AccountMove(models.Model):
    _inherit = 'account.move'

    am_account_id = fields.Many2one('account.account')
    row_description = fields.Char()
    am_analytic_account = fields.Many2one('account.analytic.account')
    am_analytic_tag = fields.Many2many('account.analytic.tag')
    am_tax_id = fields.Many2one('account.tax')
    am_rda = fields.Many2one('withholding.tax')
    am_rc = fields.Boolean()
    am_from_date = fields.Date()
    am_to_date = fields.Date()
    am_remove_vat = fields.Boolean()
    select_all_rows = fields.Boolean(default=False)
    am_sale_order_line_id = fields.Many2one('sale.order.line','Riga ordine di vendita')
    am_remove_sale_order_line = fields.Boolean()
    am_sale_id  = fields.Many2one('sale.order','Ordine di vendita')


    def action_post(self):
        #inherit of the function from account.move to validate a new tax and the priceunit of a downpayment
        res = super(AMove,self).action_post()
        line_ids = self.mapped('line_ids').filtered(lambda line: line.sale_line_ids.filtered(lambda p: p.is_downpayment))
        for line in line_ids:
            try:
                line.sale_line_ids.tax_id = line.tax_ids
                if all(line.tax_ids.mapped('price_include')):
                    line.sale_line_ids.price_unit = line.price_unit
                else:
                    #To keep positive amount on the sale order and to have the right price for the invoice
                    #We need the - before our untaxed_amount_to_invoice
                    line.sale_line_ids.price_unit = -line.sale_line_ids.untaxed_amount_to_invoice
            except UserError:
                # a UserError here means the SO was locked, which prevents changing the taxes
                # just ignore the error - this is a nice to have feature and should not be blocking
                pass
        return res

    @api.constrains("am_sale_order_line_id", "am_sale_id","am_remove_sale_order_line")
    def _check_massive_order(self):
        if self.am_sale_order_line_id and self.am_sale_id:
            raise ValidationError(
                _("Errore! Non è possibile associare una singola riga d'ordine se il campo \"Ordine di vendita\" ha un valore selezionato.")
            )
        elif (self.am_sale_order_line_id or self.am_sale_id) and self.am_remove_sale_order_line:
            raise ValidationError(
                _("Errore! Non è possibile collegare una riga d'ordine se il campo \"Rimuovi righe d'ordine\" è attivo.")
            )
    def button_select_all_rows(self):
        value = False
        if not self.select_all_rows:
            value = True
        for line in self.invoice_line_ids.filtered(lambda line:line.price_unit != 0):
            line.write({'selected_row': value})
        self.select_all_rows = value



    def apply_partner_account(self):
        if self.state != 'draft':
            raise UserError("Per modificare la fattura riportarla in stato BOZZA")

        if self.partner_id:
            self.flush()
            for l in self.invoice_line_ids:
                if l.selected_row:
                    if self.am_account_id:
                        l.account_id = self.am_account_id.id
                    if self.am_analytic_account:
                        l.analytic_account_id = self.am_analytic_account.id
                    if self.am_analytic_tag:
                        l.analytic_tag_ids = self.am_analytic_tag.ids
                    if self.am_tax_id:
                        l.tax_ids = [(5, 0), (4, self.am_tax_id.id)]
                    if self.am_rda:
                        l.invoice_line_tax_wt_ids = [(5, 0), (4, self.am_rda.id)]
                    if 'rc' in self.env[self._name]._fields :
                        if self.am_rc != l.rc:
                            l.rc = self.am_rc
                    if self.am_remove_vat:
                        l.tax_ids = [(5,)]
                    if self.am_from_date and self.am_to_date:
                        l.write({
                            'start_date': self.am_from_date,
                            'end_date': self.am_to_date
                        })
                    if self.am_sale_order_line_id:
                        l.sale_line_ids = [(5, 0),(4, self.am_sale_order_line_id.id)]
                    elif self.am_sale_id:
                        l.add_order_invoice_line(self.am_sale_id)
                    if self.am_remove_sale_order_line:
                        l.sale_line_ids = [(5,)]

                l.selected_row = False
            self.select_all_rows = False
            return {'type': 'ir.actions.client', 'tag': 'reload'}


class AccountMoveLines(models.Model):
    _inherit = "account.move.line"

    selected_row = fields.Boolean()
    selected = fields.Boolean(store=True) #todo-fix da eliminare
    def set_selected_row(self):
        self.selected_row = True if not self.selected_row else False



    def add_order_invoice_line(self, order_id):
        order_lines = order_id.order_line
        for l in self:
            is_compatible, order_line = l.check_order_line_compatibility(order_lines)
            if is_compatible:
                l.sale_line_ids = [(6, 0, order_line.ids)]
            else:
                raise ValidationError(
                    f"Non è possibile associare una riga d'ordine alla riga fattura {l.name},\n controllare le unità di misura."
                )

    def check_order_line_compatibility(self,lines):
        is_compatible = False
        product_uom = self.product_uom_id
        if not self.product_uom_id and self.product_id:
            product_uom = self.product_id.uom_id
        compatible_lines =  lines.filtered(lambda line:line.product_uom == product_uom and line.is_downpayment == False)
        if compatible_lines:
            is_compatible = True
        return is_compatible, compatible_lines


