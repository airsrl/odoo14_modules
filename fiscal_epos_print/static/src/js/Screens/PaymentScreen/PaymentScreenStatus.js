odoo.define("fiscal_epos_print.PaymentScreenStatus", function (require) {
    "use strict";

    const Registries = require('point_of_sale.Registries');
    const PaymentScreenStatus = require('point_of_sale.PaymentScreenStatus');

    const MyPaymentScreenStatus = PaymentScreenStatus => class extends PaymentScreenStatus {
         get totalDueText() {
            var total1 = parseFloat(this.currentOrder.get_total_with_tax())
            var rounding1 = parseFloat(this.currentOrder.get_rounding_applied())
            return this.env.pos.format_currency(total1+rounding1);
        }
    };

    Registries.Component.extend(PaymentScreenStatus, MyPaymentScreenStatus);

    return PaymentScreenStatus;
});

