from odoo import fields, models, api
from odoo.osv import expression

class SelectManuallyDeclarations(models.TransientModel):

    _inherit = "l10n_it_declaration_of_intent.select_declarations"


    def _domain_declaration(self):
        declaration_model = self.env["l10n_it_declaration_of_intent.declaration"]
        invoice_id = self._context.get("active_id", False)
        # if self._context.get("active_line_id", False):
        #     invoice_id = self._context.get("active_line_id")
        active_model = self._context.get("active_model",False)
        if not invoice_id:
            return declaration_model.browse()
        if active_model == 'account.move.line':
            invoice_line_id = self.env["account.move.line"].browse(invoice_id)
            type_short = invoice_line_id.move_id.get_type_short()
            invoice= invoice_line_id.move_id
        elif invoice_id:
            invoice = self.env["account.move"].browse(invoice_id)
            type_short = invoice.get_type_short()

        if not type_short:
            return declaration_model.browse()
        domain = [
            ("partner_id", "=", invoice.partner_id.commercial_partner_id.id),
            ("type", "=", type_short),
        ]
        if invoice.invoice_date:
            date_domain = [
                ("date_start", "<=", invoice.invoice_date),
                ("date_end", ">=", invoice.invoice_date),
            ]
            domain = expression.AND([domain, date_domain])
        return domain
    declaration_of_intent_id = fields.Many2one(
        comodel_name="l10n_it_declaration_of_intent.declaration",
        string="Declaration of Intent",
        domain=_domain_declaration
    )
    def _default_declaration(self):
        declaration_model = self.env["l10n_it_declaration_of_intent.declaration"]
        active_model = self._context.get("active_model",False)
        if active_model and active_model == 'account.move.line':
            return declaration_model.browse()
        invoice_id = self._context.get("active_id", False)
        if not invoice_id:
            return declaration_model.browse()
        invoice = self.env["account.move"].browse(invoice_id)
        type_short = invoice.get_type_short()
        if not type_short:
            return declaration_model.browse()
        domain = [
            ("partner_id", "=", invoice.partner_id.commercial_partner_id.id),
            ("type", "=", type_short),
        ]
        if invoice.invoice_date:
            date_domain = [
                ("date_start", "<=", invoice.invoice_date),
                ("date_end", ">=", invoice.invoice_date),
            ]
            domain = expression.AND([domain, date_domain])
        return declaration_model.search(domain)

    declaration_ids = fields.Many2many(
        comodel_name="l10n_it_declaration_of_intent.declaration",
        relation="declaration_select_manually_rel",
        string="Declarations of Intent",
        default=_default_declaration,
    )
    def confirm_line(self):
        self.ensure_one()
        res = True
        # Link declaration to invoice
        invoice_id = self._context.get("active_id", False)
        if self._context.get("active_line_id", False):
            invoice_id = self._context.get("active_line_id", False)
        active_model = self._context.get("active_model",False)
        if not invoice_id:
            return res
        if active_model == 'account.move.line':
            invoice_line = self.env["account.move.line"].browse(invoice_id)

            invoice_line.force_declaration_of_intent_id = self.declaration_of_intent_id.id
            return
        elif invoice_id:
            invoice = self.env["account.move"].browse(invoice_id)

            for line in invoice.invoice_line_ids:
                if line.product_id:
                    line.force_declaration_of_intent_id = self.declaration_of_intent_id.id
        return True
    
    


            