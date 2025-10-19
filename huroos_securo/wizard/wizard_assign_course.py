from odoo import fields, models, api


class WizardAssignCourse(models.TransientModel):
    _name = 'wizard.assign.course'

    name = fields.Char()
    medical_visit_id = fields.Many2one('occupational.medicine.employee', 'Visita')
    course_empl_id = fields.Many2one('securo.employee.course')
    duty_id = fields.Many2one('securo.employee.duty',
                              string='Mansione',
                              required=True)
    employee_ids = fields.Many2many('hr.employee',
                                    string='Dipendenti',
                                    domain="[('duty_ids','in',duty_id)]")

    def check_course(self):
        to_delete = self.env['securo.single.employee.course'].search(
            [('course_id', '=', self.course_empl_id.id), ('hr_employee_id', 'not in', self.employee_ids.ids),
             ('course_date', '=', self.course_empl_id.course_date)])
        if to_delete:
            to_delete.unlink()

    def check_medical_visit(self):
        to_delete = self.env['exam.employee.result'].search(
            [('medical_visit_id', '=', self.medical_visit_id.id),
             ('hr_employee_id', 'not in', self.employee_ids.ids),
             ('visit_date', '=', self.medical_visit_id.visit_date)])
        if to_delete:
            to_delete.unlink()

    def confirm(self):
        if self.course_empl_id:
            sec_empl_env = self.env['securo.single.employee.course']
            if self.employee_ids:
                self.check_course()
                for empl in self.employee_ids:
                    data = {'course_id': self.course_empl_id.id,
                            'hr_employee_id': empl.id,
                            'name': f"{empl.display_name}",
                            'course_date': self.course_empl_id.course_date,
                            'course_deadline': self.course_empl_id.course_deadline}
                    sec_empl_env.create(data)
            self.course_empl_id.status = 'assign'
        elif self.medical_visit_id:
            exam_empl_env = self.env['exam.employee.result']
            if self.employee_ids:
                self.check_medical_visit()
                for empl in self.employee_ids:
                    data = {'medical_visit_id': self.medical_visit_id.id,
                            'hr_employee_id': empl.id,
                            'name': f"{empl.display_name}",
                            'visit_date': self.medical_visit_id.visit_date,
                            'visit_deadline': self.medical_visit_id.visit_deadline}

                    exam_empl_env.create(data)
                    self.medical_visit_id.status = 'assign'
