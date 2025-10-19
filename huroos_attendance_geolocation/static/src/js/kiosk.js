odoo.define('huroos_attendance_geolocation.employee_kanban_view_handler_location', function(require) {
"use strict";

var KanbanRecord = require('web.KanbanRecord');

KanbanRecord.include({
    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @override
     * @private
     */
    _openRecord: function () {
        if (this.modelName === 'hr.employee.public' && this.$el.parents('.o_hr_employee_attendance_kanban').length) {
                                            // needed to diffentiate : check in/out kanban view of employees <-> standard employee kanban view
            var action = {
                type: 'ir.actions.client',
                name: 'Confirm',
                tag: 'hr_attendance_kiosk_confirm',
                employee_id: this.record.id.raw_value,
                employee_name: this.record.name.raw_value,
                employee_state: this.record.attendance_state.raw_value,
                employee_hours_today: this.record.hours_today.raw_value,
                break_state : this.record.break_state.raw_value,
            };
            this.do_action(action);
        } else {
            this._super.apply(this, arguments);
        }
    }
});

});