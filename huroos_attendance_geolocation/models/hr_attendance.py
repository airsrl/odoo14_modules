from odoo import fields, models, api ,exceptions, _


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    check_in_location = fields.Char()
    check_out_location = fields.Char()
    attendance_break_ids = fields.One2many('hr.attendance.break',
                                           'attendance_id',
                                           string='Pause')
    attendance_break_html = fields.Html(compute='compute_break_html')

    break_hours = fields.Float(compute='compute_break_hours',store=True)
    net_worked_hours = fields.Float(compute="compute_net_worked_hours",store=True)

    @api.depends('attendance_break_ids.break_time')
    def compute_break_hours(self):
        for rec in self:
            break_ids = rec.mapped('attendance_break_ids')
            break_hours = sum([b.break_time for b in break_ids]) if break_ids else 0
            rec.break_hours = break_hours

    @api.depends('worked_hours','break_hours')
    def compute_net_worked_hours(self):
        for rec in self:
            if rec.worked_hours > 0:
                rec.net_worked_hours = rec.worked_hours - rec.break_hours
            else:
                rec.net_worked_hours = 0

    @api.depends('attendance_break_ids')
    def compute_break_html(self):
        for att in self:

            attendance_break_html = '<table style="min-width: 450px; border: solid 1px #e6e6e6;">'
            for line in att.attendance_break_ids:

                    attendance_break_html += '<tr style="box-shadow: none;">' \
                                 '<td width="5%" style="text-align:center; padding:1px; border: solid 1px#e6e6e6;">'+str(line.display_name)+'</td>' \
                                                                                                                                         '</tr>'
                                                                                                                                                    # '<td width="95%" style="padding:1px; border: solid 1px#e6e6e6;">'+line.product_id.name+'</td>'

            attendance_break_html += '</table>'
            att.attendance_break_html = attendance_break_html



