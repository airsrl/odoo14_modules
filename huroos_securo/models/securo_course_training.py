from odoo import fields, models, api

class SecuroCourseTraining(models.Model):
    _name = 'securo.course.training'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Configurazione corso e formazione'



    name = fields.Char('Corso/Formazione')
    course_hour = fields.Float('Ore corso')
    periodicity_id = fields.Many2one('course.visit.periodicity',
                              string='Periodicità')
    def _default_company(self):
        return self.env.company
    company_id = fields.Many2one("res.company", required=True, default=_default_company)

    description = fields.Text('Descrizione/Normativa')



    attachment = fields.Many2many('ir.attachment',
                                  'attachment_course_tr_rel',
                                  'course_training_id',
                                  'attach_id',
                                  string='Materiale didattico')




