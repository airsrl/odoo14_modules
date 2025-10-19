from odoo import fields, models, api
from datetime import date, datetime

def give_years():
    today_year = date.today().year
    start_year = 1985
    stop_year = today_year + 2
    return [((str(r)), (str(r))) for r in range(start_year, stop_year)]


class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'
    _description = 'Description'


    is_rental = fields.Boolean(string='Noleggio')

    own_type = fields.Selection(
        [
            ('owner','Proprio'),
            ('leasing','Leasing'),
            ('finanziamento','Finanziamento'),
            #('rental','Noleggio')
        ],string='Proprietà',default='owner',required=True)

    transport_type = fields.Selection(
        [
            ('cp', 'Conto Proprio'),
            ('ct', 'Conto Terzi')
        ],
        string="Tipologia trasporto")
    attachment = fields.Many2many('ir.attachment', 'attachment_gen_rel', 'equip_id', 'attach_id', string='Documenti attrezzatura')
    #rental
    attachment_rental = fields.Many2many('ir.attachment','attachment_rental_rel','rental_id','attach_id', string='Documenti noleggio')
    start_rental = fields.Date(string='Dal')
    end_rental = fields.Date(string='Al')

    # #leasing
    attachment_leasing = fields.Many2many('ir.attachment', 'attachment_leasing_rel', 'leasing_id', 'attach_id', string='Documenti leasing')
    start_leasing = fields.Date(string='Dal')
    end_leasing = fields.Date(string='Al')

    # #finanziamento
    attachment_finanziamento = fields.Many2many('ir.attachment', 'attachment_finanziamento_rel', 'finanziamento_id', 'attach_id', string='Documenti finanziamento')
    start_finanziamento = fields.Date(string='Dal')
    end_finanziamento= fields.Date(string='Al')



    is_marchio_ce = fields.Boolean('Marchio CE')
    is_libretto = fields.Boolean('Libretto')
    is_conformita = fields.Boolean('Conformità')
    date_purchase = fields.Date('Data acquisto')
    construction_year=fields.Selection(
        selection=give_years(),

        string="Anno costruzione"
    )
    work_environment_id = fields.Many2one('securo.work.environment',
                                          string='Ambiente di lavoro')
                                         # domain="[('company_id', '=', company_id)]")
    num_telaio = fields.Char('Numero telaio')
    code = fields.Char('Codice')
    scadenze_ids = fields.One2many('huroos.fleet.scadenze', 'equipment_id', string='Scadenze')