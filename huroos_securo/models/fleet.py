from odoo import fields, models, api
from datetime import date,datetime

def give_years():
    today_year = date.today().year
    start_year = 1985
    stop_year = today_year + 2
    return [((str(r)), (str(r))) for r in range(start_year, stop_year)]

class SecuroWorkEnvironment(models.Model):
    _name='securo.work.environment'
    _description='Ambiente di lavoro'

    name=fields.Char('Ambiente di lavoro')

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)
class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    own_type = fields.Selection(
        [
            ('owner', 'Proprio'),
            ('leasing', 'Leasing'),
            ('finanziamento', 'Finanziamento'),
            # ('rental','Noleggio')
        ], string='Proprietà', default='owner', required=True)
    transport_type= fields.Selection(
        [
            ('cp','Conto Proprio'),
            ('ct','Conto Terzi')
        ],
        string="Tipologia trasporto")

    is_external = fields.Boolean("E' esterno",default=False)

    securo_accident_ids = fields.One2many('securo.accident',
                                          'vehicle_id',
                                          string="Sinistri")
    accident_count = fields.Integer(compute='get_accident_count')

    is_marchio_ce = fields.Boolean('Marchio CE')
    is_libretto = fields.Boolean('Libretto')
    is_conformita = fields.Boolean('Conformità')
    date_purchase = fields.Date('Data acquisto')
    construction_year=fields.Selection(
        selection=give_years(),

        string="Anno costruzione"
    )
    work_environment_id = fields.Many2one('securo.work.environment',
                                          string='Ambiente di lavoro',
                                          domain="[('company_id', '=', company_id)]")
    code = fields.Char('Codice')

    attachment = fields.Many2many('ir.attachment', 'attachment_fleet_rel', 'fleet_doc_id', 'attach_id',
                                  string='Documenti veicolo')

    scadenze_ids = fields.One2many('huroos.fleet.scadenze','fleet_id',string='Scadenze')
    def get_accident_count(self):
        for rec in self:
            rec.accident_count = len(rec.securo_accident_ids)
    def button_show_accident(self):
        context={'default_vehicle_id':self.id}
        domain = [('vehicle_id','=',self.id)]
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "huroos_securo.securo_accident_act_window"
        )
        action['domain']=domain
        action['context']=context
        action['view_id'] = self.env.ref('huroos_securo.securo_accident_tree_button_view').id
        return action

    vehicle_type = fields.Many2one('securo.vehicle.type',related='model_id.vehicle_type')