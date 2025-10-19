from odoo import api, fields, models
import json


class ResPartner(models.Model):
    _inherit = "res.partner"

    openapi_data = fields.Text(
        string="Dati ottenuti da chiamate OpenAPI",
        readonly=True,
        help="È una stringa contenente un dizionario con i dati di questo contatto prelevati da OpenAPI"
    )
    openapi_last_fetch_date = fields.Datetime(
        string="Dati aggiornati al",
        readonly=True
    )
    openapi_id = fields.Char(
        string="ID OpenAPI",
        compute="_compute_openapi_id"
    )
    visure_camerali_ids = fields.One2many(
        comodel_name="res.partner.visura.camerale",
        inverse_name="partner_id",
        string="Visure camerali"
    )
    visure_camerali_count = fields.Integer(
        string="N° visure camerali",
        compute="_compute_visure_camerali_count"
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if 'openapi_data' in vals:
                vals['openapi_last_fetch_date'] = fields.datetime.now()

        return super(ResPartner, self).create(vals_list)

    def write(self, vals):
        if 'openapi_data' in vals:
            # Ogni volta che tocco il campo openapi_data faccio in modo di aggiornare il dizionario e non di
            # sovrascriverlo ogni volta, oltre che tenere aggiornata la data di ultima sincronizzazione
            vals['openapi_last_fetch_date'] = fields.datetime.now()
            if self.openapi_data:
                try:
                    new_openapi_data = json.loads(vals['openapi_data'])
                    old_openapi_data = json.loads(self.openapi_data)
                    old_openapi_data.update(new_openapi_data)
                    vals['openapi_data'] = json.dumps(old_openapi_data, indent=4)
                except:
                    pass

        return super(ResPartner, self).write(vals)

    @api.depends('openapi_data')
    def _compute_openapi_id(self):
        for partner in self:
            partner.openapi_id = False
            if partner.openapi_data:
                openapi_data = json.loads(partner.openapi_data)
                partner.openapi_id = openapi_data.get("id", "")

    @api.depends('visure_camerali_ids')
    def _compute_visure_camerali_count(self):
        for partner in self:
            partner.visure_camerali_count = len(partner.visure_camerali_ids)

    def view_partner_visure_camerali(self):
        self.ensure_one()
        action = self.env['ir.actions.act_window']._for_xml_id('huroos_openapi.action_visure_camerali')
        action['domain'] = [('partner_id', '=', self.id)]
        return action
