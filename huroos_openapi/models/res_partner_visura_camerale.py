from odoo import fields, models
from odoo.exceptions import UserError


class ResPartnerVisuraCamerale(models.Model):
    _name = "res.partner.visura.camerale"
    _description = "Visura camerale partner"

    active = fields.Boolean(
        # Per gestire archiviazione delle visure richieste, dato che non è possibile eliminarle
        default=True
    )
    name = fields.Char(
        string="ID richiesta",
        readonly=True
    )
    state = fields.Char(
        string="Stato",
        required=True,
        readonly=True
    )
    type = fields.Char(
        string="Tipologia",
        required=True,
        readonly=True
    )
    cf_piva_id = fields.Char(
        string="C.F./P.IVA",
        readonly=True
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Contatto"
    )
    file = fields.Binary(
        string="File",
        readonly=True
    )

    _sql_constraints = [('request_name', 'UNIQUE(name)', "'L'ID della richiesta deve essere univoco!'")]

    def obtain_file(self):
        self.ensure_one()
        openapi_engine = self.env.ref('huroos_openapi.openapi_engine_main')
        data = openapi_engine.endpoint("/ordinaria-societa-capitale").call(
            request_id=self.name,
            get_attachment=True
        )
        if data and data.get('data') and data.get('success'):
            file = data['data']['file'].encode("utf-8")
            self.sudo().file = file
        else:
            raise UserError(data.get('message', "Qualcosa è andato storto durante l'ottenimento del file della visura."))
