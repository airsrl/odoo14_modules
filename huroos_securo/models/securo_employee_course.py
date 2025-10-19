from odoo import fields, models, api
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


class SecuroEmployeeCourse(models.Model):
    _name = "securo.employee.course"

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)
    name = fields.Many2one('securo.course.training',
                           string="Corso / formazione")
    description = fields.Text('Descrizione/Normativa', related="name.description")
    duty_id = fields.Many2one('securo.employee.duty',
                              string='Mansione', required=1)
    administrator = fields.Char('Organizzatore / Responsabile')
    teacher = fields.Char('Docente')
    course_deadline = fields.Date('Scadenza',
                                  compute="compute_deadline",
                                  inverse="set_deadline",
                                  store=True)
    course_date = fields.Datetime('Data corso', )
    course_hour = fields.Float('Durata /H')
    attachment = fields.Many2many('ir.attachment',
                                  'attachment_course_rel',
                                  'course_id',
                                  'attach_id',
                                  string='Documenti')
    course_stop = fields.Datetime("Fine corso", compute='get_stop_course', store=True)
    employee_result_ids = fields.One2many('securo.single.employee.course',
                                          'course_id',
                                          string="Risultato impiegati")
    count_empl_res = fields.Integer(compute='compute_count_empl_res', store=True)

    status = fields.Selection([
        ('draft', 'Bozze'),
        ('assign', 'Assegnato'),
        ('done', 'Completato')],
        default='draft',
        copy=False)

    def name_get(self):
        result = []
        for rec in self:
            name = (f"{rec.name.name} {rec.course_date.strftime('%d-%m-%Y') if rec.course_date else ''} {rec.teacher}")
            result.append((rec.id, name))
        return result

    @api.depends('course_date')
    def compute_deadline(self):
        for rec in self:
            if rec.name.periodicity_id:
                expire = rec.name.periodicity_id
                if expire.type == 'day':
                    rec.course_deadline = rec.course_date + relativedelta(days=expire.duration)
                elif expire.type == 'month':
                    rec.course_deadline = rec.course_date + relativedelta(months=expire.duration)
                elif expire.type == 'year':
                    rec.course_deadline = rec.course_date + relativedelta(years=expire.duration)

    def set_deadline(self):
        pass

    def show_employee_course(self):
        view_tree_id = self.env.ref('huroos_securo.securo_single_employee_course_tree_view').id,
        return {
            'name': 'Partecipanti',
            'type': 'ir.actions.act_window',
            'res_model': 'securo.single.employee.course',
            'view_mode': 'tree,form',
            'views': [(view_tree_id, 'tree'), (False, 'form')],
            'domain': [('course_id', '=', self.id)],
            'context': {'default_course_id': self.id}

        }

    def delete(self):
        self.employee_result_ids.unlink()
        self.unlink()
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "huroos_securo.securo_employee_course_act_window"
        )
        action['target'] = 'main'
        return action

    def complete(self):
        self.status = 'done'

    def assign(self):
        if self.duty_id:
            context = {'default_duty_id': self.duty_id.id,
                       'default_course_empl_id': self.id}
            view_id = self.env.ref('huroos_securo.wizard_assign_course_form_view').id

            return {
                'name': 'Assegna dipendenti',
                'type': 'ir.actions.act_window',
                'res_model': 'wizard.assign.course',
                'view_id': view_id,
                'view_mode': 'form',
                'target': 'new',
                'flags': {'initial_mode': 'edit'},
                'context': context

            }

    @api.depends('employee_result_ids')
    def compute_count_empl_res(self):
        for rec in self:
            rec.count_empl_res = len(rec.employee_result_ids)

    @api.onchange('name')
    def onchange_dates(self):
        if self.name:
            values = {

                'course_hour': self.name.course_hour,
                'attachment': [(6, 0, self.name.attachment.ids)]
            }
            self.update(values)

    @api.depends('course_date', 'course_hour')
    def get_stop_course(self):
        for rec in self:
            if rec.course_date and rec.course_hour:
                rec.course_stop = rec.course_date + timedelta(hours=rec.course_hour)


class SecuroSingleEmployeeCourse(models.Model):
    _name = 'securo.single.employee.course'

    name = fields.Char('Nome')
    esito = fields.Boolean()
    hr_employee_id = fields.Many2one('hr.employee', string='Dipendente', required=1)
    single_course_id = fields.Many2one('securo.course.training',
                                       string="Corso / formazione", required=1)
    course_id = fields.Many2one('securo.employee.course',
                                'Corso Organizzato')
    course_date = fields.Datetime('Data corso')
    course_hour = fields.Float(compute='compute_course_hour',readonly=True,store=True,string="Durata/H")

    @api.depends('course_id','single_course_id')
    def compute_course_hour(self):
        for rec in self:
            if rec.course_id:
                rec.course_hour = rec.course_id.course_hour
            elif rec.single_course_id:
                rec.course_hour = rec.single_course_id.course_hour
            else:
                rec.course_hour = 0


    course_deadline = fields.Date('Scadenza')
    attestato = fields.Many2many('ir.attachment',
                                 'attachment_single_course_rel',
                                 'attestato_id',
                                 'attach_id',
                                 string='Attestato')
    has_notify = fields.Boolean()

    # def write(self, vals):
    #     res = super(SecuroSingleEmployeeCourse, self).write(vals)
    #     if 'attestato' in vals and vals['attestato']:
    #         self.create_document()
    #     return res
    @api.onchange('attestato')
    def create_document(self):
        if self.hr_employee_id:
            if self.mapped('attestato'):
                return self.hr_employee_id.create_document_attachment({'attestato':self.mapped('attestato')})

    def name_get(self):
        result = []
        for rec in self:
            name = (f"{rec.single_course_id.name}  {rec.hr_employee_id.name}")
            result.append((rec.id, name))
        return result

    @api.onchange('visit_deadline')
    def onchange_deadline(self):
        if self.course_deadline > date.today():
            self.has_notify = False

    def get_course_deadline(self):
        deadline = False
        if self.single_course_id.periodicity_id and self.course_date:
            expire = self.single_course_id.periodicity_id

            if expire.type == 'day':
                deadline = self.course_date + relativedelta(days=expire.duration)
            elif expire.type == 'month':
                deadline = self.course_date + relativedelta(months=expire.duration)
            elif expire.type == 'year':
                deadline = self.course_date + relativedelta(years=expire.duration)
        return deadline

    @api.onchange('single_course_id','course_date')
    def onchange_single_course_id(self):
        if self.single_course_id:
            self.course_deadline = self.get_course_deadline()

    @api.onchange('course_id')
    def onchange_course_id(self):
        if self.course_id:
            self.course_date = self.course_id.course_date
            self.course_deadline = self.course_id.course_deadline
            self.single_course_id = self.course_id.name
