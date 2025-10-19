from odoo import models


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _create_account_move(self):
        """Eredito la creazione della registrazione contabile per assegnarle la data IVA."""

        # Lascio che crei l'account.move
        super(PosSession, self)._create_account_move()

        self.move_id.state = 'draft'
        self.move_id.date_iva = self.move_id.date
        self.move_id.action_post()
