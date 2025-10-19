from odoo import fields, models, api,_
from odoo.exceptions import UserError
from odoo.tools.misc import format_date
class AccountMove(models.Model):
    _inherit = 'account.move'

    def update_declarations(self, declarations, grouped_lines):
        """
        Update the declarations adding a new line representing this invoice.

        Also add a comment in this invoice stating which declaration is into.
        """
        self.ensure_one()
        is_sale_document = self.is_sale_document()
        for force_declaration in grouped_lines.keys():
            for tax, lines in grouped_lines[force_declaration].items():
                # Create a detail in declaration for every tax group
                amount = sum(line.balance for line in lines)
                if is_sale_document:
                    amount *= -1
                # Select right declaration(s)
                if force_declaration:
                    declarations = [force_declaration]
                else:
                    declarations = declarations

                for declaration in declarations:
                    if tax not in declaration.taxes_ids:
                        continue
                    # avoid creating line with same invoice_id
                    declaration.line_ids.filtered(
                        lambda line: line.invoice_id == self
                    ).unlink()
                    declaration.line_ids = [
                        (0, 0, self._prepare_declaration_line(amount, lines, tax)),
                    ]
                    # Link declaration to invoice
                    self.declaration_of_intent_ids = [(4, declaration.id)]
                    if is_sale_document:

                        if not self.narration:
                            self.narration = ""

                        declaration_text = _(
                            "\n\nVostra dichiarazione d'intento nr %s del %s, "
                            "nostro protocollo nr %s del %s, "
                            "protocollo telematico nr %s."
                            % (
                                declaration.partner_document_number,
                                format_date(
                                    self.env, declaration.partner_document_date
                                ),
                                declaration.number,
                                format_date(self.env, declaration.date),
                                declaration.telematic_protocol,
                            )
                        )
                        #   FIX corretta doppia dicitura dichiarazione
                        if declaration_text not in self.narration:
                            self.narration += declaration_text
    def select_manually_declaration_for_alline(self):
        self.ensure_one()
        action = self.env.ref(
            "huroos_declaration_fix.select_manually_declarations_action_line"
        ).with_context(active_id=self.id).read()[0]
        return action
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'


    def select_manually_declarations_line(self):
        self.ensure_one()
        context=dict(self.env.context)
        context['active_line_id']=self.id
        if self.move_id:
            context['active_id']=self.move_id.id
        else:
            context['active_id']=False
        action = self.env.ref(
            "huroos_declaration_fix.select_manually_declarations_action_line"
        ).with_context(context).read()[0]
        return action
