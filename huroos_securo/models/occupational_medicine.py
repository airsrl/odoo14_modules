from odoo import fields, models, api
from datetime import date,datetime,timedelta
from dateutil.relativedelta import relativedelta


class MedicalVisitExam(models.Model):
    _name="medical.visit.exam"

    """ 
        Tabella contenente i singoli esami configurabili all'interno di una visita medica
        ex Visita Medica generale > -esame del sangue
                                    -controllo pressione
                                    - ec...
    """
    name=fields.Char('Nome esame')
    visit_id = fields.Many2one('occupational.medicine')

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)

class Examresult(models.Model):
    _name="exam.result"

    name=fields.Char('Esito')

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)

class  CourseVisitPeriodicity(models.Model):
    _name='course.visit.periodicity'

    name= fields.Char('Periodicità')
    duration = fields.Integer(default=1)
    type = fields.Selection([('day','Giorni'),('month','Mesi'),('year','Anni')],default="year",string='Periodo di tempo')
    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)
class OccupationalMedicine(models.Model):
    _name = 'occupational.medicine'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'Medicina del lavoro'

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)
    name = fields.Char('Protocollo Sanitario')
    description = fields.Text('Note')
    period_id = fields.Many2one('course.visit.periodicity',
                              string='Periodicità')

    doctor = fields.Char('Medico')

    category = fields.Selection([('esame','Esame'),('visita','Visita')],string='Categoria')
    cost = fields.Float('Costo')

    exam_ids= fields.One2many('medical.visit.exam','visit_id',string='Esami')
    attachment = fields.Many2many('ir.attachment',
                                  'attachment_occupational_rel',
                                  'occupational_id',
                                  'attach_id',
                                  string='Materiale informativo')

class OccupationalMedicineEmployee(models.Model):
    _name="occupational.medicine.employee"
    """ in caso di migrazione valutare effettivamente l'utilità di questa tabella"""
    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)

    name=fields.Many2one('occupational.medicine',
                         string="Visita medica")

    employee_id = fields.Many2one('hr.employee',
                                  string='Dipendente')
                                  #domain="[('company_id', '=', company_id)]")
    visit_date = fields.Date('Data visita')
    visit_deadline = fields.Date('Scadenza',
                                  compute='compute_deadline',
                           inverse='set_deadline',
                           store=True)
    doctor = fields.Char('Medico')
    description = fields.Text('Note')


    employee_result_ids = fields.One2many('exam.employee.result',
                                          'medical_visit_id',
                                          string="Risultato")
    count_empl_res = fields.Integer(compute='compute_count_empl_res',store=True)

    status = fields.Selection([
        ('draft', 'Bozze'),
        ('assign', 'Assegnato'),
        ('done', 'Completato')],
        default ='draft',
        copy=False)
    duty_id = fields.Many2one('securo.employee.duty',
                              string='Mansione',required=1)

    attachment = fields.Many2many('ir.attachment',
                                  'attachment_empl_occupational_rel',
                                  'occupational_empl_id',
                                  'attach_id',
                                  string='Materiale informativo')

    @api.depends('visit_date')
    def compute_deadline(self):
        for rec in self:
            if rec.name.period_id:
                expire=rec.name.period_id
                if rec.visit_deadline:
                    if expire.type == 'day':
                        rec.visit_deadline = rec.visit_date + relativedelta(days=expire.duration)
                    elif expire.type == 'month':
                        rec.visit_deadline = rec.visit_date + relativedelta(months=expire.duration)
                    elif expire.type == 'year':
                        rec.visit_deadline = rec.visit_date + relativedelta(years=expire.duration)

    def set_deadline(self):
        pass

    @api.depends('employee_result_ids')
    def compute_count_empl_res(self):
        for rec in self:
            rec.count_empl_res = len(rec.employee_result_ids)

    def show_employee_visit(self):

            return {
                'name': 'Partecipanti',
                'type': 'ir.actions.act_window',
                'res_model': 'exam.employee.result',
                'view_mode': 'tree,form',
                 'domain':[('medical_visit_id','=',self.id)],
                'context':{'default_medical_visit_id':self.id}


            }
    def delete(self):
        self.employee_result_ids.unlink()
        self.unlink()
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "huroos_securo.occupational_medicine_employee_act_window"
        )
        action['target'] = 'main'
        return action
    def complete(self):
        self.status= 'done'
    def assign(self):
        if self.duty_id:
            context={'default_duty_id':self.duty_id.id,
                     'default_medical_visit_id':self.id}
            view_id=self.env.ref('huroos_securo.wizard_assign_course_form_view').id


            return {
                'name': 'Assegna dipendenti',
                'type': 'ir.actions.act_window',
                'res_model': 'wizard.assign.course',
                'view_id': view_id,
                'view_mode': 'form',
                'target': 'new',
                'flags': {'initial_mode': 'edit'},
                 'context':context

            }
    @api.onchange('name')
    def onchange_dates(self):
        if self.name:
            values = {
              'doctor':self.name.doctor,
                'attachment':[(6,0,self.name.attachment.ids)]
            }
            self.update(values)

class ExamEmployeeResult(models.Model):
    _name='exam.employee.result'

    name = fields.Char('Nome')
    esito = fields.Many2one('exam.result',
                            string='Esito')
    hr_employee_id = fields.Many2one('hr.employee',string='Dipendente',required=1)
    employee_active = fields.Boolean(related='hr_employee_id.active', store=True)
    medical_visit_id = fields.Many2one('occupational.medicine.employee','Visita Organizzata')
    visit_id = fields.Many2one('occupational.medicine',
                         string="Visita medica",required=True)
    visit_date = fields.Date('Data')
    visit_deadline = fields.Date('Scadenza')
    document_ids = fields.Many2many('ir.attachment',
                                  'attachment_exam_result_rel',
                                  'exam_res_id',
                                  'attach_id',
                                  string='Documentazione')
    has_notify = fields.Boolean()
    exam_ids = fields.One2many('securo.exam.result','employee_result_id',string='Esami')

    def write(self, vals):
        res= super(ExamEmployeeResult, self).write(vals)
        if 'document_ids' in vals and vals['document_ids']:
            self.create_document(vals)
        return res


    def create_document(self,vals):
        if self.hr_employee_id:
            return self.hr_employee_id.create_document_attachment({'visita':self.mapped('document_ids')})

    @api.onchange('medical_visit_id',)
    def onchange_medical_visit(self):
        if self.medical_visit_id:
            self.visit_date = self.medical_visit_id.visit_date
            self.visit_deadline = self.medical_visit_id.visit_deadline
            self.visit_id = self.medical_visit_id.name.id

    @api.onchange('medical_id','visit_date' )
    def onchange_visit_date(self):
        if not self.medical_visit_id and (self.visit_id and self.visit_date):
            self.visit_deadline = self.find_date_deadline()


    @api.onchange('visit_deadline')
    def onchange_deadline(self):
        if self.visit_deadline:
            if self.visit_deadline > date.today():
                self.has_notify = False
    def _default_company(self):
        return self.env.company

    def find_date_deadline(self):
        visit_deadline = None
        if self.visit_date and self.visit_id:
            expire=self.visit_id.period_id
            if expire.type == 'day':
               visit_deadline = self.visit_date + relativedelta(days=expire.duration)
            elif expire.type == 'month':
                visit_deadline = self.visit_date + relativedelta(months=expire.duration)
            elif expire.type == 'year':
                visit_deadline = self.visit_date + relativedelta(years=expire.duration)
        return visit_deadline

    company_id = fields.Many2one("res.company", required=True, default=_default_company)

    def view_open_exams(self):
        return {
            'name': 'Esami',
            'type': 'ir.actions.act_window',
            'res_model': 'exam.employee.result',
            'view_mode': 'form',
            'res_id':self.id,
            'view_id': self.env.ref('huroos_securo.view_exam_employee_result_form').id,
            'flags': {'initial_mode': 'edit'},
            'target':'new',
            'context': {'create': False, 'delete': False}

        }
class SecuroExamResult(models.Model):
    _name="securo.exam.result"

    """Esami per ogni visita medica"""

    name=fields.Many2one('medical.visit.exam','Esame')
    esito=fields.Many2one('exam.result','Esito')
    employee_result_id = fields.Many2one('exam.employee.result')
    visit_id = fields.Many2one('occupational.medicine',related='employee_result_id.visit_id',store=True)
    description= fields.Char('Descrizione')
    result_date = fields.Date('Data Esame')
    next_date = fields.Date('Scadenza')
    document_ids = fields.Many2many('ir.attachment',
                                    'attachment_securo_exam_result_rel',
                                    'sec_exam_res_id',
                                    'attach_id',
                                    string='Documentazione')

    has_notify = fields.Boolean()
    @api.onchange('visit_id','visit_id.exam_ids')

    def onchange_exam(self):
        if self.visit_id and self.visit_id.exam_ids:
            return {
                'domain': {
                    'name': [('id', 'in', self.visit_id.exam_ids.ids)]
                }
            }
        else:
            return {
                'domain': {
                    'name': [('id', 'in', [])]
                }
            }

    def write(self, vals):
        res= super(SecuroExamResult, self).write(vals)
        if 'document_ids' in vals and vals['document_ids']:
            self.create_document()
        return res


    def create_document(self):
        if self.employee_result_id and self.employee_result_id.hr_employee_id:
            return self.employee_result_id.hr_employee_id.create_document_attachment({'esame':self.mapped('document_ids')})


    def _default_company(self):
        return self.env.company
    company_id = fields.Many2one("res.company", required=True, default=_default_company)