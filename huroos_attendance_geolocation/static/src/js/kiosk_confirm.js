odoo.define('huroos_attendance_geolocation.kiosk_confirm_location', function (require) {
"use strict";

var KioskConfirm = require('hr_attendance.kiosk_confirm');

KioskConfirm.include({

    events: _.extend(KioskConfirm.prototype.events, {
        "click .o_hr_attendance_sign_in_out_icon": _.debounce(function () {
            this.update_attendance();
        }, 200, true),
        "click .o_hr_attendance_pin_pad_button_ok": _.debounce(function () {
            this.pin_pad = true;
            this.update_attendance();
        }, 200, true),
    }),

    init: function (parent, action) {
        this._super.apply(this, arguments);
        this.pin_pad = false;
        this.break_state = action.break_state;
    },

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
        var pinCode = null;
        var coords = _.pick(position.coords, ['latitude', 'longitude']);

        if (this.pin_pad) {
            this.$(".o_hr_attendance_pin_pad_button_ok").attr("disabled","disabled");
            pinCode = this.$(".o_hr_attendance_PINbox").val();
        }

        this._rpc({
            model: "hr.employee",
            method: "attendance_manual",
            args: [[this.employee_id], this.next_action, pinCode, coords],
        }).then(function (result) {
            if (result.action) {
                self.do_action(result.action);
            } else if (result.warning) {
                self.do_warn(result.warning);
                if (self.pin_pad) {
                    self.$(".o_hr_attendance_PINbox").val("");
                    setTimeout(function () {
                        self.$(".o_hr_attendance_pin_pad_button_ok").removeAttr("disabled");
                    }, 500);
                }
                self.pin_pad = false;
            }
        });
    },

    manageLocationError: function (error) {
        // gestisco errore di navigator get position
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
                args: [[this.employee_id]],
            }).then(function() {
                self.do_action(self.next_action);
            });
        },
    });

});

