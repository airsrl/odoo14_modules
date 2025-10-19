from odoo import fields, models, api
from odoo.tools.misc import formatLang


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    payment_date = fields.Date(
        string='Ultimo pagamento',
        store=True,
        compute='_compute_payment_date',
    )
    payment_info = fields.Html(
        string="Tabella pagamenti",
        compute="_compute_payment_info",
        help="Colonne tabella: Data pagamento, ammontare, fascia di giorni in ritardo/anticipo"
    )
    payment_info_ids = fields.Many2many(
        comodel_name="account.payment.info",
        string="Info pagamenti",
        compute="_compute_payment_info_ids"
    )

    @api.depends('matching_number', 'move_id.date', 'move_id', 'payment_id.date')
    def _compute_payment_info_ids(self):
        for line in self:
            payment_info_ids = [(5, )]
            if line.move_id.state == 'posted' and line.move_id.is_invoice(include_receipts=True):
                for partial, amount, counterpart_line in line.move_id._get_reconciled_invoices_partials():
                    if counterpart_line == partial.credit_move_id and line != partial.debit_move_id:
                        continue
                    elif counterpart_line == partial.debit_move_id and line != partial.credit_move_id:
                        continue

                    difference = counterpart_line.date - line.date_maturity
                    payment_info_ids.append((0, 0, {
                        'due_date': line.date_maturity,
                        'date': counterpart_line.date,
                        'amount': amount,
                        'difference': difference.days
                    }))

            line.payment_info_ids = payment_info_ids or False

    @api.depends('matching_number', 'move_id.date', 'move_id', 'payment_id.date')
    def _compute_payment_info(self):
        for line in self:

            payment_vals_list = list()
            if line.move_id.state == 'posted' and line.move_id.is_invoice(include_receipts=True):
                for partial, amount, counterpart_line in line.move_id._get_reconciled_invoices_partials():
                    if counterpart_line == partial.credit_move_id and line != partial.debit_move_id:
                        continue
                    elif counterpart_line == partial.debit_move_id and line != partial.credit_move_id:
                        continue

                    difference = counterpart_line.date - line.date_maturity

                    payment_vals_list.append({
                        'date': counterpart_line.date.strftime("%d/%m/%Y") if counterpart_line.date else "",
                        'amount': formatLang(self.env, amount, currency_obj=line.currency_id),
                        'difference': difference.days
                    })

            if payment_vals_list:
                table = "<table style='min-width: 250px; border: solid 1px #e6e6e6;' class='o_editable_list'>"
                table += "<tbody>"
                for val in payment_vals_list:
                    table += "<tr style='box-shadow: none;'>"
                    table += f"<td style='width:30%;padding:3px; border: solid 1px#e6e6e6;'>{val['date']}</td>"
                    table += f"<td style='width:30%;padding:3px; border: solid 1px#e6e6e6;'>{val['amount']}</td>"
                    table += f"<td style='width:40%;padding:3px; border: solid 1px#e6e6e6;'>{val['difference']}</td>"
                    table += "</tr>"
                table += "</tbody>"
                table += "</table>"
                line.payment_info = table
            else:
                line.payment_info = False

    @api.depends('matching_number', 'move_id.date', 'move_id', 'payment_id.date')
    def _compute_payment_date(self):

        for move_line in self:
            move = move_line.move_id
            payment_list_date = []

            if move.state == 'posted' and move.is_invoice(include_receipts=True):
                for partial, amount, counterpart_line in move._get_reconciled_invoices_partials():
                    payment_list_date.append(counterpart_line.date)
            if payment_list_date:
                move_line.payment_date = max(payment_list_date)
            else:
                move_line.payment_date = False


class AccountPaymentInfo(models.Model):
    _name = "account.payment.info"
    _description = "Informazioni di pagamento di una riga contabile"

    date = fields.Date(string="Data pagamento", required=True)
    amount = fields.Float(string="Valore pagamento", required=True)
    due_date = fields.Date(string="Scadenza", required=True)
    difference = fields.Integer(string="Differenza")

    @api.model
    def name_get(self):
        result = list()
        for info in self:
            name = f'{info.date.strftime("%d/%m/%Y")};{formatLang(self.env, info.amount)}€;{info.difference}'
            result.append((info.id, name))
        return result
