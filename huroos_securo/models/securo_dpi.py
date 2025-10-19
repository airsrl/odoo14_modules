from odoo import fields, models, api
from odoo.exceptions import UserError
class DpiEmployee(models.Model):
    _name="securo.dpi.employee"

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)

    name=fields.Many2one('securo.dpi',
                         string='DPI')
    type_id=fields.Many2one(related='name.type_id')
    category_id=fields.Many2one(related='name.category_id',
                                store=True)
    size_id = fields.Many2one('securo.dpi.size',
                              string='Taglia')
    hr_employee_id = fields.Many2one('hr.employee',
                                     string='Dipendente')
    duration_id = fields.Many2one(related='name.duration_id',
                                  store=True,
                                  string='Durata')
    date_use = fields.Date('Data assegnazione',required=True, default=fields.Date.today())
    date_expire = fields.Date(compute='compute_date_expire',store=True,string='Scadenza')
    duty_ids = fields.Many2many('securo.employee.duty',
                              string='Mansione',
                              related='hr_employee_id.duty_ids',
                              )


    @api.depends('date_use','duration_id')
    def compute_date_expire(self):
        for rec in self:
            if rec.duration_id.has_expiration:
                expire=rec.duration_id
                if expire.type == 'day':
                    rec.date_expire = rec.date_use + relativedelta(days=expire.num_type)
                elif expire.type == 'month':
                    rec.date_expire = rec.date_use + relativedelta(months=expire.num_type)
                elif expire.type == 'year':
                    rec.date_expire = rec.date_use + relativedelta(years=expire.num_type)

    def _print_consegna_dpi(self):
        datas_form = {'assign_date':min(self.mapped('date_use')),
                      'employee_ids':[],
                      }
        employee_ids =list(dict(self.mapped('hr_employee_id'))) if len(self.mapped('hr_employee_id').ids) > 1 else self.mapped('hr_employee_id')
        if len(employee_ids) > 1:
            raise UserError("Non puoi selezionare dpi di dipendenti diversi")
        employee = {'empl':employee_ids.name,
                    'dpi_data':[]}
        for dpi in self:
            employee['dpi_data'].append({
                            'name':dpi.name.name,
                            'qty':1,
                        })

        datas_form['employee_ids'].append(employee)
        report_name = "huroos_securo.action_report_print_dpi"

        return self.env.ref(report_name).report_action(self, data=datas_form)

class SecuroDpiSize(models.Model):
    _name = 'securo.dpi.size'

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)
    name=fields.Char('Taglia')

class SecuroDpiType(models.Model):
    _name = 'securo.dpi.type'

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)
    name=fields.Char('Tipo')
    dpi_ids = fields.One2many('securo.dpi','type_id',string='DPI')
class SecuroDpiCategory(models.Model):
    _name='securo.dpi.category'

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)
    name=fields.Char('Categoria')
    attachment = fields.Many2many('ir.attachment',
                                  'attachment_dpi_categ_rel',
                                  'dpi_categ_id',
                                  'attach_id',
                                  string='Strumenti')
    dpi_ids = fields.One2many('securo.dpi','category_id',string='DPI')
class SecuroDpiDuraton(models.Model):
    _name='securo.dpi.duration'

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)
    name=fields.Char('Durata')
    dpi_ids = fields.One2many('securo.dpi','duration_id',string='DPI')
    has_expiration = fields.Boolean('Ha scadenza?')
    type = fields.Selection([('day','Giorni'),('month','Mesi'),('year','Anni')],string='Scade')
    num_type = fields.Integer('Dopo')
class SecuroDpi(models.Model):
    _name = 'securo.dpi'
    _description = 'Dpi'

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)
    name = fields.Char('Descrizione')
    type_id = fields.Many2one('securo.dpi.type',
                              string='Tipo',
                             )
    category_id = fields.Many2one('securo.dpi.category',string='Categoria',
                             )
    duration_id = fields.Many2one('securo.dpi.duration',string='Durata')
    duty_ids = fields.Many2many('securo.employee.duty',
                              string='Mansioni')

