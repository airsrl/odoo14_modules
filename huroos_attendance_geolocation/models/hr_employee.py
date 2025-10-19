import logging

from odoo import fields, models, api ,exceptions, _
import requests

google_api = "https://maps.googleapis.com/maps/api/geocode/json"
maps_key = "AIzaSyDk2lkidwlijyseSWuFa0e3REvxA3CWDUo"

class HrEmployee(models.Model):

    _inherit = 'hr.employee'

    def get_location(self, coord):
        """
        :param coord: dizionario contenente latitudine e longitudine
        :return: stringa contenente l'indirizzo corrispondente alle coordinate
        """
        lating = ','.join([str(value) for k, value in coord.items()])
        url = google_api
        params = {'latlng': lating, 'key': maps_key}
        try:
            result = requests.get(url, params).json()
        except:
            return " "
        location = str(result['plus_code']['compound_code'])
        if len(result['results']) > 0:
            location = str(result['results'][0]['formatted_address'])
        return location


    def attendance_manual(self, next_action, entered_pin=None, coord=False):
        location = self.get_location(coord)
        res = super(HrEmployee, self.with_context(location=location)).attendance_manual(next_action, entered_pin)
        return res

    def set_break(self):
        employee = self.sudo()
        if employee.user_id:
            modified_attendance = employee.with_user(employee.user_id)._attendance_action_change_break()
        else:
            modified_attendance = employee._attendance_action_change_break()

    def _attendance_action_change(self):
        attendance = super(HrEmployee,self)._attendance_action_change()

        # inserisco la posizione della timbratura
        location = self.env.context.get("location", False)
        if location:
            if self.attendance_state == "checked_in":
                attendance.check_in_location = location
            else:
                attendance.check_out_location = location

        action_date = fields.Datetime.now()
        find_break = self.env['hr.attendance.break'].search([('attendance_id','=',attendance.id),('break_end','=',False)],limit=1)
        if find_break:
            find_break.break_end = action_date
        return attendance

    def _attendance_action_change_break(self):
        """ Check In/Check Out action
            Check In: create a new attendance record
            Check Out: modify check_out field of appropriate attendance record
        """
        self.ensure_one()
        action_date = fields.Datetime.now()

        attendance = self.env['hr.attendance'].search([('employee_id', '=', self.id), ('check_out', '=', False)], limit=1)
        if attendance:
            find_break = self.env['hr.attendance.break'].search([('attendance_id','=',attendance.id),('break_end','=',False)],limit=1)
            if find_break:
                find_break.break_end = action_date
            else:
                vals = {
                    'attendance_id': attendance.id,
                    'break_start': action_date,
                }
                return self.env['hr.attendance.break'].create(vals)

        else:
            raise exceptions.UserError(_('Cannot perform end break on %(empl_name)s, could not find corresponding "start break". '
                'Your attendances have probably been modified manually by human resources.') % {'empl_name': self.sudo().name, })
        return True

class HrEmployeeBase(models.AbstractModel):
    _inherit = "hr.employee.base"

    break_state = fields.Selection(string="Attendance Status", compute='_compute_break_state', selection=[('break_check_out', "End break"), ('break_check_in', "Start break")])

    # @api.depends('last_attendance_id.attendance_break_ids.break_end',  'last_attendance_id')
    def _compute_break_state(self):
        for employee in self:
            att = employee.last_attendance_id.sudo()
            if att and att.attendance_break_ids:
                break_ids = att.mapped('attendance_break_ids')
                break_state_active = break_ids.filtered(lambda x:x.break_end == False)
                employee.break_state = "break_check_in" if break_state_active else "break_check_out"
            else:
                employee.break_state = 'break_check_out'
            logging.info(employee.break_state)
