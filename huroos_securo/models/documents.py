from odoo import fields, models, api


class DocumentsFolder(models.Model):
    _inherit = 'documents.folder'


    employee_id = fields.Many2one('hr.employee', string='Dipendente')
