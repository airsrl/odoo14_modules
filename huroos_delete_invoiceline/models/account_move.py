from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    def recompute_lines(self):

        self._recompute_dynamic_lines(recompute_all_taxes=True)
    def delete_row_invoice(self):
        self.ensure_one()
        line_account_move = [line.id for line in self.invoice_line_ids]
        # needed for avoiding errors after grouping in assets
        wiz = self.env['wizard.deleteline'].create({'name':'test',
                                                    'account_line_ids':[(6,0,line_account_move)],
                                                    'move_id':self.id
                                                    })
        return {
            "name": "Elimina righe",
            "view_mode": "form",
            "res_model": "wizard.deleteline",
            "view_id": False,
            "type": "ir.actions.act_window",
            "target": "new",
            'res_id':wiz.id

        }
class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    def unlink(self):
        res=super(AccountMoveLine, self).unlink()
        return res

