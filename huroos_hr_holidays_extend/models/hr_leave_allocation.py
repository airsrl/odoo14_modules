from odoo import fields, models, api


class HolidaysAllocation(models.Model):
    """ Allocation Requests Access specifications: similar to leave requests """
    _inherit = "hr.leave.allocation"

    number_of_hours = fields.Float(
        'Duration (hours)', compute='_compute_from_holiday_status_id',
        store=True,
        help="If Accrual Allocation: Number of hours allocated in addition to the ones you will get via the accrual' system.")


    @api.depends('holiday_status_id', 'allocation_type', 'number_of_hours_display', 'number_of_days_display')
    def _compute_from_holiday_status_id(self):
        for allocation in self:
            allocation.number_of_hours = allocation.number_of_hours_display
        return super()._compute_from_holiday_status_id()
