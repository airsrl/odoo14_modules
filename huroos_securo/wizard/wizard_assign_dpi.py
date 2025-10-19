from odoo import fields, models, api


class WizardAssignDpi(models.TransientModel):
    _name = 'wizard.assign.dpi'
    _description = 'Description'
    _rec_name='wizard_name'

    wizard_name=fields.Char()
    name = fields.Many2many('securo.dpi',
                           domain="[('duty_ids','=',duty_ids)]")
    duty_ids = fields.Many2many('securo.employee.duty',
                              string='Mansioni'
                                )
    employee_ids = fields.Many2many('hr.employee',
                                    string='Dipendente',
                                    domain="[('duty_ids','in',duty_ids)]"

                                    )
    date_use = fields.Date('Data assegnazione', default=fields.Date.today())



    def confirm(self):

        for empl in self.employee_ids:
            list_dpi = []
            for dpi in self.name:
                dpi_empl_data={'name':dpi.id,
                               'hr_employee_id':empl.id}
                if self.date_use:
                    dpi_empl_data['date_use'] = self.date_use
                list_dpi.append(dpi_empl_data)
            empl.dpi_ids = [(0,0,data) for data in list_dpi]

    def confirm_print(self):
        self.confirm()
        datas_form = {'assign_date':self.date_use,
                      'employee_ids':[],
                      }


        for empl in self.employee_ids:
            employee = {'empl':empl.name,
                        'dpi_data':[]
                        }
            for dpi in self.name:
                employee['dpi_data'].append({
                                'name':dpi.name,
                                'qty':1,
                            })

            datas_form['employee_ids'].append(employee)
        report_name = "huroos_securo.action_report_print_dpi"

        return self.env.ref(report_name).report_action(self, data=datas_form)



