from odoo import models,fields,api
from odoo.exceptions import UserError


class AccountConfigSettingsInh(models.TransientModel):
    _inherit = 'res.config.settings'

    competence_iva = fields.Boolean(help="Attivare per abilitare la competenza IVA sulle fatture di acquisto, "
                                         "ad esempio spsotare la competenza nel mese precedente se entro il giorno 16 del mese successivo.")

    def set_values(self):
        super(AccountConfigSettingsInh, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('huroos_data_iva.account_competence_iva',self.competence_iva)
        print(self.competence_iva)

    @api.model
    def get_values(self):
        res = super(AccountConfigSettingsInh, self).get_values()
        res.update(competence_iva=self.env['ir.config_parameter'].sudo().get_param('huroos_data_iva.account_competence_iva'))
        return res


    def compute_competence_iva(self):
        """
        Calcola Pregresso Abilitazione Competenza IVA:
        """
        #Solo le righe con valorizzato creato dall'imposta o imposta applicata
        if self.competence_iva:
            move_line_ids = self.env['account.move.line'].search(['|', ('tax_ids', '!=', False), ('tax_line_id', '!=', False)])
            for move in move_line_ids:
                if not move.date_iva:
                    move.date_iva = move.date
                    move.move_id.date_iva = move.date
                    print("Calcolato pregresso IVA")
        else:
            raise UserError("Devi abilitare la competenza per iva per calcolare il pregresso")