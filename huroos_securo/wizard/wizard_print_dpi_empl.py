from odoo import fields, models, api


class WizardPrintDpiEmpl(models.TransientModel):
    _name = 'wizard.print.dpi.empl'
    _description = 'Description'


    name = fields.Char()
    employee_id = fields.Many2one('hr.employee',required=True)
    dpi_ids = fields.Many2many('securo.dpi.employee',
                               domain="[('hr_employee_id','=',employee_id)]",
                              )
    date_assign =  fields.Date('Data assegnazione',required=True, default=fields.Date.today())


    @api.onchange('employee_id')
    def get_dpi_ids(self):
        for empl in self:
            empl.dpi_ids = [(6,0,empl.employee_id.dpi_ids.ids)]


    def print_consegna_dpi(self):
        datas_form = {'assign_date':self.date_assign,
                      'employee_ids':[],
                      }

        employee = {'empl':self.employee_id.name,
                    'dpi_data':[]}
        for dpi in self.dpi_ids:
            employee['dpi_data'].append({
                            'name':dpi.name.name,
                            'qty':1,
                        })

        datas_form['employee_ids'].append(employee)
        report_name = "huroos_securo.action_report_print_dpi"
        return self.env.ref(report_name).report_action(self, data=datas_form)