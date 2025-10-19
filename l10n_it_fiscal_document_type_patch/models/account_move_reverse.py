from odoo import fields, models, api


class AccountMoveReversal(models.TransientModel):

    _inherit = 'account.move.reversal'


    def reverse_moves(self):
        res = super(AccountMoveReversal, self).reverse_moves()
        if isinstance(res, dict):
            if self.refund_method == 'modify':
                invoice_ids_domain = ('id', 'in', [res['res_id']])
            else:
                invoice_ids_domain = res['domain'][-1] if 'domain' in res else ('id', 'in', [res['res_id']])
            invoices = self.env['account.move'].search([invoice_ids_domain])
            for invoice in invoices:
                if invoice.move_type == 'out_refund':
                    document_type = invoice._get_document_fiscal_type(invoice.move_type,
                                                                    invoice.partner_id,
                                                                    invoice.fiscal_position_id,
                                                                    invoice.journal_id,)
                    if document_type:
                        invoice.fiscal_document_type_id = document_type[0]

                    td_refund = self.env['fiscal.document.type'].search([('out_refund','=',True)],limit=1)
                    invoice.fiscal_document_type_id  = td_refund
                    
        return res

class FiscalDocumentType(models.Model):
    _inherit = 'fiscal.document.type'
    refund_fiscal_document_type_id = fields.Many2one(
        "fiscal.document.type",
        string="Refund Fiscal Document Type",
        readonly=False,
    )
class AccountMove(models.Model):
    _inherit = "account.move"



    def _get_document_fiscal_type(
        self, move_type=None, partner=None, fiscal_position=None, journal=None
    ):
        dt = []
        doc_id = False
        if not move_type:
            move_type = "out_invoice"

        # Partner
        if partner:
            if move_type in ("out_invoice"):
                doc_id = partner.out_fiscal_document_type.id or False
            elif move_type in ("in_invoice"):
                doc_id = partner.in_fiscal_document_type.id or False
        # Fiscal Position
        if not doc_id and fiscal_position:
            doc_id = fiscal_position.fiscal_document_type_id.id or False
        # Journal
        if not doc_id and journal:
            dt = (
                self.env["fiscal.document.type"]
                .search([("journal_ids", "in", [journal.id])])
                .ids
            )
        if (
            not doc_id
            and not dt
            and move_type in ["out_invoice", "out_refund", "in_invoice", "in_refund"]
        ):
            dt = self.env["fiscal.document.type"].search([(move_type, "=", True)]).ids

        # Refund Document type
        if (dt or doc_id) and ("out_refund" or 'in_refund') in move_type:
            fdt = self.env["fiscal.document.type"].browse(doc_id or dt[0])
            if (
                fdt
                and not fdt.out_refund
                and not fdt.in_refund
                and fdt.refund_fiscal_document_type_id
            ):
                if dt:
                    dt[0] = fdt.refund_fiscal_document_type_id.id
                else:
                    dt.append(fdt.refund_fiscal_document_type_id.id)

        if doc_id:
            dt.append(doc_id)
        return dt