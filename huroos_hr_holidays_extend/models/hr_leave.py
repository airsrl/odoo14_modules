from odoo import fields, models, api


class HrLeave(models.Model):
    _inherit = 'hr.leave'

    number_of_hours = fields.Float(
        'Duration (Hours)',
        compute='_compute_number_of_hours',
        store=True,
        help='Number of days of the time off request. Used in the calculation. To manually correct the duration, use this field.')

    @api.depends('date_from', 'date_to', 'employee_id')
    def _compute_number_of_hours(self):
        for holiday in self:
            if holiday.date_from and holiday.date_to:
                holiday.number_of_hours = holiday.number_of_hours_display#_get_number_of_days(holiday.date_from, holiday.date_to, holiday.employee_id.id)['hours']
            else:
                holiday.number_of_hours = 0
