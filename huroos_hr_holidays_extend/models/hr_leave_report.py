from odoo import api, fields, models, tools, exceptions, _
from odoo.osv import expression


class LeaveReport(models.Model):
    _inherit = "hr.leave.report"

    number_of_hours = fields.Float('Number of hours', readonly=True)

    def init(self):
        tools.drop_view_if_exists(self._cr, 'hr_leave_report')

        self._cr.execute("""
            CREATE or REPLACE view hr_leave_report as (
                SELECT row_number() over(ORDER BY leaves.employee_id) as id,
                leaves.employee_id as employee_id, leaves.name as name,
                leaves.number_of_days as number_of_days,leaves.number_of_hours as number_of_hours,
                 leaves.leave_type as leave_type,
                leaves.category_id as category_id, leaves.department_id as department_id,
                leaves.holiday_status_id as holiday_status_id, leaves.state as state,
                leaves.holiday_type as holiday_type, leaves.date_from as date_from,
                leaves.date_to as date_to, leaves.payslip_status as payslip_status
                from (select
                    allocation.employee_id as employee_id,
                    allocation.private_name as name,
                    allocation.number_of_days as number_of_days,
                    allocation.number_of_hours as number_of_hours,
                    allocation.category_id as category_id,
                    allocation.department_id as department_id,
                    allocation.holiday_status_id as holiday_status_id,
                    allocation.state as state,
                    allocation.holiday_type,
                    null as date_from,
                    null as date_to,
                    FALSE as payslip_status,
                    'allocation' as leave_type
                from hr_leave_allocation as allocation
                union all select
                    request.employee_id as employee_id,
                    request.private_name as name,
                    (request.number_of_days * -1) as number_of_days,
                    (request.number_of_hours * -1) as number_of_hours,
                    request.category_id as category_id,
                    request.department_id as department_id,
                    request.holiday_status_id as holiday_status_id,
                    request.state as state,
                    request.holiday_type,
                    request.date_from as date_from,
                    request.date_to as date_to,
                    request.payslip_status as payslip_status,
                    'request' as leave_type
                from hr_leave as request) leaves
            );
        """)

