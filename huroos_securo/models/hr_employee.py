from odoo import fields, models, api
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta


class SecuroEmployeeDuty(models.Model):
    _name = 'securo.employee.duty'
    _description = 'Mansione dipendenti'

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)
    name = fields.Char('Mansione')
    employee_ids = fields.Many2many('hr.employee', 'employee_duty_rel', 'empl_id', 'duty_id', string='Dipendenti')


class SecuroEmployeeQualification(models.Model):
    _name = 'securo.employee.qualification'
    _description = 'Qualifica dipendenti'

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)
    name = fields.Char('Qualifica')
    employee_ids = fields.One2many('hr.employee',
                                   'qualification_id',
                                   string='Dipendenti')


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    dpi_ids = fields.One2many('securo.dpi.employee',
                              'hr_employee_id',
                              string='Dpi')

    employee_course_ids = fields.One2many('securo.single.employee.course', 'hr_employee_id',
                                          string='Corsi e formazione')
    qualification_id = fields.Many2one('securo.employee.qualification',
                                       string='Qualifica')
    # domain="[('company_id', '=', company_id)]")
    duty_ids = fields.Many2many('securo.employee.duty', 'employee_duty_rel', 'duty_id', 'empl_id',
                                string='Mansione')
    size_casco = fields.Many2one('securo.dpi.size',
                                 string='Taglia casco'
                                 )
    size_scarpe = fields.Many2one('securo.dpi.size',
                                  string='Taglia Scarpa'
                                  )
    size_abbigliamento = fields.Many2one('securo.dpi.size',
                                         string='Taglia abbigliamento'
                                         )
    size_pantaloni = fields.Many2one('securo.dpi.size',
                                     string='Taglia pantaloni'
                                     )
    size_guanti = fields.Many2one('securo.dpi.size',
                                  string='Taglia guanti'
                                  )
    hire_date = fields.Date('Data assunzione')

    employee_medical_ids = fields.One2many('exam.employee.result',
                                           'hr_employee_id',
                                           string='Protocollo sanitario')

    attachment = fields.Many2many('ir.attachment',
                                  'attachment_hr_empl_rel',
                                  'hr_empl_id',
                                  'attach_id',
                                  string='Documenti generici',
                                  )
    contract_level = fields.Char('Livello contrattuale')

    def write(self, vals):
        res = super(HrEmployee, self).write(vals)
        if 'attachment' in vals and vals['attachment']:
            self.create_document_attachment({'general': self.mapped('attachment')})
        return res

    def general_create_document_attachment(self):
        for rec in self:
            attachments_list = {'general': rec.mapped('attachment'),
                                'attestato': rec.mapped('employee_course_ids.attestato'),
                                'visita': rec.mapped('employee_medical_ids.document_ids'),
                                'esame': rec.mapped('employee_medical_ids.exam_ids.document_ids')}
            rec.sudo().create_document_attachment(attachments_list)

    def create_document_attachment(self, attachments_list):
        for key, atts in attachments_list.items():
            for att in atts:
                value = {'attachment_id': att._origin.id,
                         'name': att._origin.name or self.display_name,
                         'folder_id': self.get_employee_document_folder().id,
                         'owner_id': self._get_document_owner().id,
                         'partner_id': self.user_partner_id.id,
                         'tag_ids': [(6, 0, self._get_document_employee_tags(key).ids)]}
                exist_att_id = self.env['documents.document'].search(
                    [('attachment_id', '=', att._origin.id)],limit=1)
                try:
                    if not exist_att_id:

                        self.env['documents.document'].create(value)

                    else:

                        exist_att_id.write(value)
                except Exception as e:
                    print(e)
                    continue

    def get_employee_document_folder(self):
        parent = self.env.ref('huroos_securo.documents_hr_folder_personal')
        fold_id = self.env['documents.folder'].search(
            [('parent_folder_id', '=', parent.id), ('employee_id', '=', self._origin.id)], limit=1)
        if not fold_id:
            fold_id = self.env['documents.folder'].sudo().create(
                {'name': f"{self.name}", 'parent_folder_id': parent.id, 'employee_id': self._origin.id})
            self.env.cr.commit()
        return fold_id

    def _get_document_employee_tags(self, use=False):
        if use == 'visita':
            return self.env.ref('huroos_securo.visit_employee_document')
        elif use == 'attestato':
            return self.env.ref('huroos_securo.course_employee_document')
        elif use == 'esame':
            return self.env.ref('huroos_securo.exam_employee_document')
        else:
            return self.env.ref('huroos_securo.general_employee_document')

    def employee_print_dpi(self):

        return {
            'name': 'Stampa consegna DPI',
            'type': 'ir.actions.act_window',
            'res_model': 'wizard.print.dpi.empl',
            'view_mode': 'form',
            'target': 'new',

            'context': {'default_employee_id': self.id}

        }

    def open_responsible_config(self):
        if len(self.env.companies) > 1:
            view_form_id = self.env.ref('huroos_securo.hr_company_form_securo').id
            return {
                'name': 'Responsabile securO',
                'type': 'ir.actions.act_window',
                'res_model': 'res.company',
                'domain': [('id', 'in', self.env.companies.ids)],
                'views': [(False, 'tree'), (view_form_id, 'form')],
                'view_mode': 'tree,form',
                'target': 'current',
                'context': {'create': False, 'delete': False}

            }
        else:
            return {
                'name': 'Responsabile securO',
                'type': 'ir.actions.act_window',
                'res_model': 'res.company',
                'view_mode': 'form',
                'target': 'current',
                'res_id': self.env.company.id,
                'view_id': self.env.ref('huroos_securo.hr_company_form_securo').id

            }

    def download_employee_attachments(self):

        return {"type": "ir.actions.act_url",
                "url": "/download_attachments?res_id={}&res_model={}".format(self.id, self._name)
                }
