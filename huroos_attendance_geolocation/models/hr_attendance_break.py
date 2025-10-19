from odoo import fields, models, api, exceptions, _
from odoo.tools import format_datetime
from datetime import date,datetime

class HrAttendanceBreak(models.Model):
    _name = 'hr.attendance.break'


    break_start = fields.Datetime(string="Start Break", default=fields.Datetime.now, required=True)
    break_end = fields.Datetime(string="End Break")
    break_time = fields.Float(string='Break Hours', compute='_compute_break_time', store=True, readonly=True)
    attendance_id = fields.Many2one('hr.attendance', string="Presenza")

    def name_get(self):
        result = []
        for break_time in self:
            if not break_time.break_end:
                result.append((break_time.id, _("Pausa dalle %(break_start)s") % {
                    'break_start': format_datetime(self.env, break_time.break_start, dt_format=False),
                }))
            else:
                result.append((break_time.id, _("Pausa dalle %(break_start)s alle %(break_end)s") % {
                    'break_start': format_datetime(self.env, break_time.break_start, dt_format=False),
                    'break_end': format_datetime(self.env, break_time.break_end, dt_format=False),
                }))
        return result

    @api.depends('break_start', 'break_end')
    def _compute_break_time(self):
        for break_time in self:
            if break_time.break_end and break_time.break_start:
                delta = break_time.break_end - break_time.break_start
                break_time.break_time = delta.total_seconds() / 3600.0
            else:
                break_time.break_time = False

