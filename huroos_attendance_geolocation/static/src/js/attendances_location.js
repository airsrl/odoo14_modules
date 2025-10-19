odoo.define('huroos_attendance_geolocation.attendances_location', function (require) {
"use strict";

var MyAttendances = require('hr_attendance.my_attendances');
var core = require('web.core');
var field_utils = require('web.field_utils');
var rpc = require('web.rpc');

MyAttendances.include({
    events: _.extend({}, MyAttendances.prototype.events, {'click .o_hr_attendance_break_icon': function () {this.update_break()},

    }),

    update_attendance: function () {
        var self = this;
        if (navigator.geolocation) {
            // getcurrentposition restituisce le coordinate attuali e prende 3 parametri:
            // funzione da eseguire in caso di successo
            // funzione da eseguire in caso di errore
            // dizionario/oggetto di opzioni
            navigator.geolocation.getCurrentPosition(
                self.setAttendanceLocation.bind(self),
                self.manageLocationError.bind(self),
                {enableHighAccuracy: true}
            );
        }
    },
    setAttendanceLocation: function (position) {
        var self = this;
        var coords = _.pick(position.coords, ['latitude', 'longitude']);

        // chiamo la funzione base aggiungendo le coordinate
        this._rpc({
            model: "hr.employee",
            method: "attendance_manual",
            args: [[self.employee.id],
                "hr_attendance.hr_attendance_action_my_attendances", null, coords],
        }).then(function (result) {
            if (result.action) {
                self.do_action(result.action);
            } else if (result.warning) {
                self.do_warn(result.warning);
            }
        });
    },
    manageLocationError: function (error) {
        // gestisco errore di navigator get positzion
        alert("ERROR(" + error.code + "): " + error.message);
        const position = {
            coords: {
                latitude: 0.0,
                longitude: 0.0,
            },
        };
        this.setAttendanceLocation(position);
    },

    update_break: function () {
        var self=this;
        this._rpc({
                model: 'hr.employee',
                method: 'set_break',
                args: [[self.employee.id]],
            }).then(function() {
                window.location.reload();
            });
    },


    willStart: function () {
        var self = this;

        var def = this._rpc({
                model: 'hr.employee',
                method: 'search_read',
                args: [[['user_id', '=', this.getSession().uid]], ['attendance_state', 'name', 'hours_today','break_state']],
            })
            .then(function (res) {
                self.employee = res.length && res[0];
                if (res.length) {
                    self.hours_today = field_utils.format.float_time(self.employee.hours_today);
                }
            });
        var coords = false;
        var def1 = navigator.geolocation.getCurrentPosition(function(position) {
            coords = _.pick(position.coords, ['latitude', 'longitude']);
            return self._rpc({
                model: 'hr.employee',
                method: 'get_location',
                args: [['user_id', '=', self.getSession().uid], coords],
            }).then(function (res) {
                document.getElementById("location_placeholder").innerHTML = res;
            });

        })

        return Promise.all([def,def1, this._super.apply(this, arguments)]);
    },




   });

});


