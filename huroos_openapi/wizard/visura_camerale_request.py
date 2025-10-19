from odoo import fields, models
from odoo.exceptions import UserError


class VisuraCameraleRequest(models.TransientModel):
    _name = "visura.camerale.request"
    _description = "Wizard di richiesta visura camerale"

    code = fields.Char(
        string="C.F./P.IVA"
    )

    def confirm_request(self):
        return self.request_visura(force=True)

    def request_visura(self, force=False):
        # Prima di fare la richiesta controllo se è già stata effettuata una visura su questa P.IVA/C.F.
        if not force and self.env['res.partner.visura.camerale'].search([('cf_piva_id', '=', self.code)]):
            return {
                "type": "ir.actions.act_window",
                "view_mode": "form",
                "view_id": self.env.ref('huroos_openapi.view_visura_camerale_confirm_request').id,
                "res_model": "visura.camerale.request",
                "target": "new",
                "res_id": self.id
            }

        openapi_engine = self.env.ref('huroos_openapi.openapi_engine_main')
        data = openapi_engine.endpoint("/ordinaria-societa-capitale").call(
            payload={"cf_piva_id": self.code}
        )
        if data and data.get('data') and data.get('success'):
            self.env['res.partner.visura.camerale'].sudo().create({
                'name': data['data']['id'],
                'type': data['data']['tipo'],
                'state': data['data']['stato_richiesta'],
                'cf_piva_id': data['data']['cf_piva_id']
            })
            action = self.env['ir.actions.act_window']._for_xml_id('huroos_openapi.action_visure_camerali')
            action['target'] = "main"
            return action
        else:
            raise UserError(data.get('message', "Qualcosa è andato storto durante la richiesta della visura camerale."))

