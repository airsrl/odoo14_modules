from odoo import fields, models, api

class HuroosScadenzeType(models.Model):
    _name="securo.document.type"

    name=fields.Char('Tipo documento')
class HuroosFleetScadenze(models.Model):
    _name='huroos.fleet.scadenze'

    name=fields.Many2one('securo.document.type',
                         'Tipo documento')
    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)

    description = fields.Text('Note')
    fleet_id = fields.Many2one('fleet.vehicle')
    equipment_id = fields.Many2one('maintenance.equipment')
    doc_date = fields.Date('Data')
    due_date = fields.Date('Data scadenza')
    attachment = fields.Many2many('ir.attachment',
                                  'attachment_scadenze_rel',
                                  'scadenze_id',
                                  'attach_id',
                                  string='Allegati')
    has_notify = fields.Boolean()