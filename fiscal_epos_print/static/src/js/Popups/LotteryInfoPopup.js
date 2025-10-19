odoo.define('fiscal_epos_print.LotteryInfoPopup', function(require) {
    'use strict';

    const { useState, useRef } = owl.hooks;
    const AbstractAwaitablePopup = require('point_of_sale.AbstractAwaitablePopup');
    const Registries = require('point_of_sale.Registries');

    class LotteryInfoPopup extends AbstractAwaitablePopup {

        constructor() {
            super(...arguments);

            this.state = useState({ inputValue: this.props.startingValue });
            this.inputLotteryCode = useRef('inputLotteryCode');
        }

        mounted() {
            this.inputLotteryCode.el.focus();
        }

        clickConfirmLottery() {
            this.$el = $(this.el);
            var self = this;
            function allValid() {
                return self.$el.find('input').toArray().every(function(element) {
                    return element.value && element.value != ''
                })
            }

            if (allValid()) {
                this.$el.find('#error-message-dialog').hide()

                var order = this.env.pos.get_order();
                order.lottery_code = this.$el.find('#lottery_code').val();

                this.trigger('close-popup');
                if (this.props.update_lottery_info_button && this.props.update_lottery_info_button instanceof Function) {
                    this.props.update_lottery_info_button();
                }
            } else {
                this.$el.find('#error-message-dialog').show();
            }
        }
    }

    LotteryInfoPopup.template = 'LotteryInfoPopup';

    LotteryInfoPopup.defaultProps = {
        confirmText: 'Ok',
        cancelText: 'Cancel',
        body: '',
    };

    Registries.Component.add(LotteryInfoPopup);
    return LotteryInfoPopup;
});
