odoo.define('fiscal_epos_print.models', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    var core = require("web.core");
    var utils = require('web.utils');
    var _t = core._t;
    var round_pr = utils.round_precision;
    var OrderSuper = models.Order;

    const { Gui } = require('point_of_sale.Gui');

    models.load_fields("pos.payment.method",
        ["fiscalprinter_payment_type", "fiscalprinter_payment_index"]);
//
//    function round_dec(value, exp) {
//        if (value) {
//            value = parseFloat(value.toString().replace(",", "."));
//            exp = parseFloat(exp.toString().replace(",", "."));
//            exp = exp.toString().split('.')[1].length;
//            if (typeof exp === 'undefined' || +exp === 0)
//              return Math.round(value);
//
//            value = +value;
//            exp = +exp;
//
//            if (isNaN(value) || !(typeof exp === 'number' && exp % 1 === 0))
//              return NaN;
//
//            // Shift
//            value = value.toString().split('e');
//            value = Math.round(+(value[0] + 'e' + (value[1] ? (+value[1] + exp) : exp)));
//
//            // Shift back
//            value = value.toString().split('e');
//            return +(value[0] + 'e' + (value[1] ? (+value[1] - exp) : -exp));
//        }
//    }

    models.Order = models.Order.extend({
        initialize: function(attributes, options){
            OrderSuper.prototype.initialize.call(this, attributes, options);
            this.lottery_code = null;
            this.refund_report = null;
            this.refund_date = null;
            this.refund_doc_num = null;
            this.refund_cash_fiscal_serial = null;
            this.has_refund = false;
            this.fiscal_receipt_number = null;
            this.fiscal_receipt_amount = null;
            this.fiscal_receipt_date = null;
            this.fiscal_z_rep_number = null;
            this.fiscal_printer_serial = this.pos.config.fiscal_printer_serial || null;
            this.fiscal_printer_debug_info = null;
        },

        // Manages the case in which after printing an invoice
        // you pass a barcode in the mask of the registered invoice
        add_product: function(product, options) {
            if(this._printed || this.finalized === true) {
                this.destroy();
                return this.pos.get_order().add_product(product, options);
            }
            OrderSuper.prototype.add_product.apply(this, arguments);
        },

        check_order_has_refund: function() {
            var order = this.pos.get_order();
            if (order) {
                var lines = order.orderlines;
                order.has_refund = lines.find(function(line){ return line.quantity < 0.0;}) !== undefined;
            }
        },

        init_from_JSON: function (json) {
            OrderSuper.prototype.init_from_JSON.apply(this, arguments);
            this.lottery_code = json.lottery_code;
            this.refund_report = json.refund_report;
            this.refund_date = json.refund_date;
            this.refund_doc_num = json.refund_doc_num;
            this.refund_cash_fiscal_serial = json.refund_cash_fiscal_serial;
            this.check_order_has_refund();
            this.fiscal_receipt_number = json.fiscal_receipt_number;
            this.fiscal_receipt_amount = json.fiscal_receipt_amount;
            this.fiscal_receipt_date = json.fiscal_receipt_date;
            this.fiscal_z_rep_number = json.fiscal_z_rep_number;
            this.fiscal_printer_serial = json.fiscal_printer_serial;
            this.fiscal_printer_debug_info = json.fiscal_printer_debug_info;
        },

        export_as_JSON: function() {
            var result = OrderSuper.prototype.export_as_JSON.call(this);
            result.lottery_code = this.lottery_code;
            result.refund_report = this.refund_report;
            result.refund_date = this.refund_date;
            result.refund_doc_num = this.refund_doc_num;
            result.refund_cash_fiscal_serial = this.refund_cash_fiscal_serial;
            result.fiscal_receipt_number = this.fiscal_receipt_number;
            result.fiscal_receipt_amount = this.fiscal_receipt_amount;
            result.fiscal_receipt_date = this.fiscal_receipt_date; // parsed by backend
            result.fiscal_z_rep_number = this.fiscal_z_rep_number;
            result.fiscal_printer_serial = this.fiscal_printer_serial || null;
            result.fiscal_printer_debug_info = this.fiscal_printer_debug_info;
            return result;
        },

        export_for_printing: function(){
            var receipt = OrderSuper.prototype.export_for_printing.call(this);

            receipt.lottery_code = this.lottery_code;
            receipt.refund_date = this.refund_date;
            receipt.refund_report = this.refund_report;
            receipt.refund_doc_num = this.refund_doc_num;
            receipt.refund_cash_fiscal_serial = this.refund_cash_fiscal_serial;
            receipt.fiscal_receipt_number = this.fiscal_receipt_number;
            receipt.fiscal_receipt_amount = this.fiscal_receipt_amount;
            receipt.fiscal_receipt_date = this.fiscal_receipt_date;
            receipt.fiscal_z_rep_number = this.fiscal_z_rep_number;
            receipt.fiscal_printer_serial = this.fiscal_printer_serial;
            receipt.fiscal_printer_debug_info = this.fiscal_printer_debug_info;

            return receipt
        },

        getPrinterOptions: function (){
            var protocol = ((this.pos.config.use_https) ? 'https://' : 'http://');
            var printer_url = protocol + this.pos.config.printer_ip + '/cgi-bin/fpmate.cgi';
            return {url: printer_url};
        },

            /* ---- Payment Status --- */
        get_subtotal: function(){
            var ret = this.orderlines.reduce((function(sum, orderLine){
                return sum + orderLine.get_display_price();
            }), 0);
            if (ret) {
                return round_pr(ret, this.pos.currency.rounding);
            }
            else {return ret;}
        },
        get_total_with_tax: function() {
            var ret = this.orderlines.reduce((function(sum, orderLine){
                return sum + orderLine.get_display_price();
            }), 0);
            if (ret) {
//                return round_dec(ret, this.pos.config.decimal_rounding)?.toFixed(this.pos.config.decimal_rounding);
                return round_pr(ret, this.pos.currency.rounding)?.toFixed(this.pos.currency.rounding.toString().split(".")[1].length);
            }
            else {return ret;}
        },
        get_total_without_tax: function() {
            var ret = this.orderlines.reduce((function(sum, orderLine) {
                return sum + orderLine.get_price_without_tax();
            }), 0);
            if (ret) {
//                return round_dec(ret, this.pos.config.decimal_rounding)?.toFixed(this.pos.config.decimal_rounding);
                return round_pr(ret, this.pos.currency.rounding).toFixed(this.pos.currency.rounding.toString().split(".")[1].length);
            }
            else {return ret;}
        },
        get_total_discount: function() {
            var rounding_dec= this.pos.currency.rounding;
            var ret = this.orderlines.reduce((function(sum, orderLine) {
                var unit_price = orderLine.get_unit_price();
                var line_disc= orderLine.get_discount();
                sum += (unit_price * (line_disc/100) * orderLine.get_quantity());
                if (orderLine.display_discount_policy() === 'without_discount'){
//                    var lst_price= round_dec(orderLine.get_lst_price(), decimal_rounding)?.toFixed(decimal_rounding);
//                    var unit_price1= round_dec(orderLine.get_unit_price(), decimal_rounding)?.toFixed(decimal_rounding);
//                    sum += ((lst_price - unit_price1) * orderLine.get_quantity());

                    sum += ((orderLine.get_lst_price() - orderLine.get_unit_price()) * orderLine.get_quantity());
                }
                return sum;
            }), 0);

            if (ret) {
                return round_pr(ret, rounding_dec);
            }
            else {return ret;}
        },
        get_total_tax: function() {
            if (this.pos.company.tax_calculation_rounding_method === "round_globally") {
                // As always, we need:
                // 1. For each tax, sum their amount across all order lines
                // 2. Round that result
                // 3. Sum all those rounded amounts
                var groupTaxes = {};
                this.orderlines.each(function (line) {
                    var taxDetails = line.get_tax_details();
                    var taxIds = Object.keys(taxDetails);
                    for (var t = 0; t<taxIds.length; t++) {
                        var taxId = taxIds[t];
                        if (!(taxId in groupTaxes)) {
                            groupTaxes[taxId] = 0;
                        }
                        groupTaxes[taxId] += taxDetails[taxId];
                    }
                });

                var sum = 0;
                var taxIds = Object.keys(groupTaxes);
                for (var j = 0; j<taxIds.length; j++) {
                    var taxAmount = groupTaxes[taxIds[j]];
                    sum += taxAmount;
                }
                if (sum) {
//                    return round_dec(sum, this.pos.config.decimal_rounding)?.toFixed(this.pos.config.decimal_rounding);
                    return round_pr(sum, this.pos.currency.rounding)?.toFixed(this.pos.currency.rounding.toString().split(".")[1].length);
                }
                else {return sum;}
            } else {
                var ret = this.orderlines.reduce((function(sum, orderLine) {
                    return sum + orderLine.get_tax();
                }), 0);
                if (ret) {
//                    return round_dec(ret, this.pos.config.decimal_rounding)?.toFixed(this.pos.config.decimal_rounding);
                    return round_pr(ret, this.pos.currency.rounding).toFixed(this.pos.currency.rounding.toString().split(".")[1].length);
                }
                else {return ret;}
            }
        },

        get_total_paid: function() {
            var ret = this.paymentlines.reduce((function(sum, paymentLine) {
                if (paymentLine.is_done()) {
                    sum += paymentLine.get_amount();
                }
                return sum;
            }), 0);
            if (ret) {
//                return round_dec(ret, this.pos.config.decimal_rounding)?.toFixed(this.pos.config.decimal_rounding);
                return round_pr(ret, this.pos.currency.rounding).toFixed(this.pos.currency.rounding.toString().split(".")[1].length);
            }
            else {return ret;}
        },
    });

    var _product_super = models.Product.prototype;
    models.Product = models.Product.extend({

        get_price: function(pricelist, quantity, price_extra){
            var self = this;
            var date = moment().startOf('day');

            // In case of nested pricelists, it is necessary that all pricelists are made available in
            // the POS. Display a basic alert to the user in this case.
            if (pricelist === undefined) {
                alert(_t(
                    'An error occurred when loading product prices. ' +
                    'Make sure all pricelists are available in the POS.'
                ));
            }

            var category_ids = [];
            var category = this.categ;
            while (category) {
                category_ids.push(category.id);
                category = category.parent;
            }

            var pricelist_items = _.filter(pricelist.items, function (item) {
                return (! item.product_tmpl_id || item.product_tmpl_id[0] === self.product_tmpl_id) &&
                       (! item.product_id || item.product_id[0] === self.id) &&
                       (! item.categ_id || _.contains(category_ids, item.categ_id[0])) &&
                       (! item.date_start || moment(item.date_start).isSameOrBefore(date)) &&
                       (! item.date_end || moment(item.date_end).isSameOrAfter(date));
            });

            var price = self.lst_price;
            if (price_extra){
                price += price_extra;
            }
            _.find(pricelist_items, function (rule) {
                if (rule.min_quantity && quantity < rule.min_quantity) {
                    return false;
                }

                if (rule.base === 'pricelist') {
                    price = self.get_price(rule.base_pricelist, quantity);
                } else if (rule.base === 'standard_price') {
                    price = self.standard_price;
                }

                if (rule.compute_price === 'fixed') {
                    price = rule.fixed_price;
                    return true;
                } else if (rule.compute_price === 'percentage') {
                    price = price - (price * (rule.percent_price / 100));
                    return true;
                } else {
                    var price_limit = price;
                    price = price - (price * (rule.price_discount / 100));
                    if (rule.price_round) {
                        price = round_pr(price, rule.price_round);
                    }
                    if (rule.price_surcharge) {
                        price += rule.price_surcharge;
                    }
                    if (rule.price_min_margin) {
                        price = Math.max(price, price_limit + rule.price_min_margin);
                    }
                    if (rule.price_max_margin) {
                        price = Math.min(price, price_limit + rule.price_max_margin);
                    }
                    return true;
                }

                return false;
            });

            // Rewrited whit the new method round_dec()but be carefull whit pricelist price computed
            /* Original comment*/
            //This return value has to be rounded with round_di before
            // being used further. Note that this cannot happen here,
            // because it would cause inconsistencies with the backend for
            // pricelist that have base == 'pricelist'.
//            price = round_dec(price, this.pos.config.decimal_rounding);
//            price = price?.toFixed(this.pos.config.decimal_rounding); //round_pr
            return price;
        },
    });

    var _orderline_super = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        export_for_printing: function () {
            var res = _orderline_super.export_for_printing.call(this, arguments);
            res.tax_department = this.get_tax_details_r();
            if (!res.tax_department) {
                Gui.showPopup("ErrorPopup", {
                    title: _t("Network error"),
                    body: _t("Manca iva su prodotto"),
                });
            }
            if (res.tax_department.included_in_price === true) {
                res.full_price = this.price;
            } else {
                res.full_price = this.price * (1 + res.tax_department.tax_amount / 100);
            }
            return res;
        },
        get_tax_details_r: function(){
            var detail =  this.get_all_prices().taxDetails;
            for (var i in detail){
                return {
                    code: this.pos.taxes_by_id[i].fpdeptax,
                    taxname: this.pos.taxes_by_id[i].name,
                    included_in_price: this.pos.taxes_by_id[i].price_include,
                    tax_amount: this.pos.taxes_by_id[i].amount,
                }
            }
            // TODO is this correct?
            Gui.showPopup('ErrorPopup', {
                'title': _t('Error'),
                'body': _t('No taxes found'),
            });
        },
        set_quantity: function (quantity, keep_price) {
            var qty = quantity;
            if (qty === "0") {
                // Epson FP doesn't allow lines with quantity 0
                qty = "remove";
            }
            return _orderline_super.set_quantity.call(this, qty, keep_price);
        },

        fix_tax_included_price: function(line){
            var lnprice = line.price;
            var lncomprice = line.compute_fixed_price(lnprice);

            line.set_unit_price(line.compute_fixed_price(line.price));
        },
//        set_unit_price: function(price){
//            this.order.assert_editable();
//            var parsed_price = !isNaN(price) ?
//                price :
//                isNaN(parseFloat(price)) ? 0 : field_utils.parse.float('' + price)
//            this.price = round_dec(parsed_price || 0, this.pos.config.decimal_rounding)?.toFixed(this.pos.config.decimal_rounding);
//            this.trigger('change',this);
//        },
//        get_unit_price: function(){
//            var digits = this.pos.config.decimal_rounding;
////            round_dec(total_included, self.pos.config.decimal_rounding)?.toFixed(this.pos.config.decimal_rounding)
//            // round_dec and truncate to mimic _symbol_set behavior
//            var priceRounded= parseFloat(round_dec(this.price || 0, digits)?.toFixed(this.pos.config.decimal_rounding));
//            return priceRounded;
//        },
//        get_unit_display_price: function(){
//            if (this.pos.config.iface_tax_included === 'total') {
//                var quantity = this.quantity;
//                this.quantity = 1.0;
//                var price = round_dec(this.get_all_prices().priceWithTax, this.pos.config.decimal_rounding)?.toFixed(this.pos.config.decimal_rounding);
////                var price = this.get_all_prices().priceWithTax;
//                this.quantity = quantity;
//                return price;
//            } else {
//                return this.get_unit_price();
//            }
//        },
//        get_base_price:    function(){
////            var rounding = this.pos.currency.rounding;
////            return round_pr(this.get_unit_price() * this.get_quantity() * (1 - this.get_discount()/100), rounding);
//            var priceround = round_dec(this.get_unit_price() * this.get_quantity() * (1 - this.get_discount()/100), this.pos.config.decimal_rounding)?.toFixed(this.pos.config.decimal_rounding)
//            return priceround;
//        },
//        get_display_price_one: function(){
//            var rounding = this.pos.currency.rounding;
//            var price_unit = this.get_unit_price();
//            if (this.pos.config.iface_tax_included !== 'total') {
//                return round_pr(price_unit * (1.0 - (this.get_discount() / 100.0)), rounding);
//            } else {
//                var product =  this.get_product();
//                var taxes_ids = product.taxes_id;
//                var taxes =  this.pos.taxes;
//                var product_taxes = [];
//
//                _(taxes_ids).each(function(el){
//                    product_taxes.push(_.detect(taxes, function(t){
//                        return t.id === el;
//                    }));
//                });
//
//                var all_taxes = this.compute_all(product_taxes, price_unit, 1, this.pos.currency.rounding);
//
////                return round_pr(all_taxes.total_included * (1 - this.get_discount()/100), rounding);
//                var priceRounded= round_dec(all_taxes.total_included * (1 - this.get_discount()/100), this.pos.config.decimal_rounding)?.toFixed(this.pos.config.decimal_rounding);
//                return priceRounded;
//            }
//        },

        // TODO CONTROLLARE SE SERVE
//        compute_all: function(taxes, price_unit, quantity, currency_rounding, no_map_tax) {
//            var res = _orderline_super.compute_all.call(this, taxes, price_unit, quantity, currency_rounding, no_map_tax);
//            var self = this;
//
//            var total_excluded = round_pr(price_unit * quantity, currency_rounding);
//            var total_included = total_excluded;
//            var base = total_excluded;
//            var list_taxes = res.taxes;
//            // amount_type 'group' not handled (used only for purchases, in Italy)
//            //_(taxes).each(function(tax) {
//            _(taxes).each(function(tax,index) {
//                if (!no_map_tax){
//                    tax = self._map_tax_fiscal_position(tax);
//                }
//                if (!tax){
//                    return;
//                }
//                var tax_amount = self._compute_all(tax[0], base, quantity);
//                tax_amount = round_pr(tax_amount, currency_rounding);
//                if (!tax_amount){
//                    // Intervene here: also add taxes with 0 amount
//                    if (tax[0].price_include) {
//                        total_excluded -= tax_amount;
//                        base -= tax_amount;
//                    }
//                    else {
//                        total_included += tax_amount;
//                    }
//                    if (tax[0].include_base_amount) {
//                        base += tax_amount;
//                    }
//                    var data = {
//                        id: tax[0].id,
//                        amount: tax_amount,
//                        name: tax[0].name,
//                    };
//                    list_taxes.push(data);
//                }
//                total_included = total_included ? round_dec(total_included, self.pos.config.decimal_rounding)?.toFixed(this.pos.config.decimal_rounding) : total_included;
//            });
//            res.taxes = list_taxes;

//            return res;
//        },

        compute_all: function(taxes, price_unit, quantity, currency_rounding, handle_price_include=true) {
            var self = this;

            // 1) Flatten the taxes.

            var _collect_taxes = function(taxes, all_taxes){
                taxes.sort(function (tax1, tax2) {
                    return tax1.sequence - tax2.sequence;
                });
                _(taxes).each(function(tax){
                    if(tax.amount_type === 'group')
                        all_taxes = _collect_taxes(tax.children_tax_ids, all_taxes);
                    else
                        all_taxes.push(tax);
                });
                return all_taxes;
            }
            var collect_taxes = function(taxes){
                return _collect_taxes(taxes, []);
            }

            taxes = collect_taxes(taxes);

            // 2) Deal with the rounding methods

            var round_tax = this.pos.company.tax_calculation_rounding_method !== 'round_globally';

            var initial_currency_rounding = currency_rounding;
            if(!round_tax)
                currency_rounding = currency_rounding * 0.00001;

            // 3) Iterate the taxes in the reversed sequence order to retrieve the initial base of the computation.
            var recompute_base = function(base_amount, fixed_amount, percent_amount, division_amount){
                 return (base_amount - fixed_amount) / (1.0 + percent_amount / 100.0) * (100 - division_amount) / 100;
            }

//            var base = round_pr(price_unit * quantity, initial_currency_rounding);
//            var base = round_pr(price_unit, initial_currency_rounding);
            var base = price_unit;

            var sign = 1;
            if(base < 0){
                base = -base;
                sign = -1;
            }

            var total_included_checkpoints = {};
            var i = taxes.length - 1;
            var store_included_tax_total = true;

            var incl_fixed_amount = 0.0;
            var incl_percent_amount = 0.0;
            var incl_division_amount = 0.0;

            var cached_tax_amounts = {};
            if (handle_price_include){
                _(taxes.reverse()).each(function(tax){
                    if(tax.include_base_amount){
                        base = recompute_base(base, incl_fixed_amount, incl_percent_amount, incl_division_amount);
                        incl_fixed_amount = 0.0;
                        incl_percent_amount = 0.0;
                        incl_division_amount = 0.0;
                        store_included_tax_total = true;
                    }
                    if(tax.price_include){
                        if(tax.amount_type === 'percent')
                            incl_percent_amount += tax.amount;
                        else if(tax.amount_type === 'division')
                            incl_division_amount += tax.amount;
                        else if(tax.amount_type === 'fixed')
                            incl_fixed_amount += quantity * tax.amount
                        else{
                            var tax_amount = self._compute_all(tax, base, quantity);
                            incl_fixed_amount += tax_amount;
                            cached_tax_amounts[i] = tax_amount;
                        }
                        if(store_included_tax_total){
                            total_included_checkpoints[i] = base;
                            store_included_tax_total = false;
                        }
                    }
                    i -= 1;
                });
            }

//            var total_excluded = round_pr(recompute_base(base, incl_fixed_amount, incl_percent_amount, incl_division_amount) , initial_currency_rounding);
            var total_excluded = recompute_base(base, incl_fixed_amount, incl_percent_amount, incl_division_amount);
            var total_included = total_excluded;

            // 4) Iterate the taxes in the sequence order to fill missing base/amount values.

            base = total_excluded;

            var skip_checkpoint = false;

            var taxes_vals = [];
            i = 0;
            var cumulated_tax_included_amount = 0;
            _(taxes.reverse()).each(function(tax){
                if(!skip_checkpoint && tax.price_include && total_included_checkpoints[i] !== undefined){
                    var tax_amount = total_included_checkpoints[i] - (base + cumulated_tax_included_amount);
                    cumulated_tax_included_amount = 0;
                }else
                    var tax_amount = self._compute_all(tax, base, quantity, true);

                tax_amount = tax_amount * quantity;

                if(tax.price_include && total_included_checkpoints[i] === undefined)
                    cumulated_tax_included_amount += tax_amount;

                taxes_vals.push({
                    'id': tax.id,
                    'name': tax.name,
                    'amount': sign * round_pr(tax_amount, self.pos.currency.rounding),
                    'base': sign * round_pr(base, self.pos.currency.rounding),
                });

                if(tax.include_base_amount){
                    base += tax_amount / quantity;
                    if(!tax.price_include)
                        skip_checkpoint = true;
                }

                total_included += tax_amount / quantity;
                i += 1;
            });
            total_excluded = total_excluded * quantity;
//            total_included = round_dec(total_included, self.pos.config.decimal_rounding)?.toFixed(this.pos.config.decimal_rounding) * quantity;
            total_included = round_pr(total_included, this.pos.currency.rounding)?.toFixed(this.pos.currency.rounding.toString().split(".")[1].length) * quantity;
             if (isNaN(total_excluded))
                total_excluded = 0;
            if (isNaN(total_included))
                total_included = 0;
            return {
                'taxes': taxes_vals,
                'total_excluded': sign * round_pr(total_excluded, this.pos.currency.rounding),
                'total_included': sign * round_pr(total_included, this.pos.currency.rounding),
            }
        },

        get_all_prices: function(){
            var self = this;

            var price_unit = this.get_unit_price() * (1.0 - (this.get_discount() / 100.0));
            var taxtotal = 0;

            var product =  this.get_product();
            var taxes =  this.pos.taxes;
            var taxes_ids = _.filter(product.taxes_id, t => t in this.pos.taxes_by_id);
            var taxdetail = {};
            var product_taxes = [];

            _(taxes_ids).each(function(el){
                var tax = _.detect(taxes, function(t){
                    return t.id === el;
                });
                product_taxes.push.apply(product_taxes, self._map_tax_fiscal_position(tax));
            });
            product_taxes = _.uniq(product_taxes, function(tax) { return tax.id; });

            var all_taxes = this.compute_all(product_taxes, price_unit, this.get_quantity(), this.pos.currency.rounding);
            var all_taxes_before_discount = this.compute_all(product_taxes, this.get_unit_price(), this.get_quantity(), this.pos.currency.rounding);
            _(all_taxes.taxes).each(function(tax) {
                if (!isNaN(tax.amount)){
                    taxtotal += tax.amount;
                    taxdetail[tax.id] = tax.amount;
                }
                else {
                    tax.amount = 0
                    taxtotal += tax.amount;
                    taxdetail[tax.id] = tax.amount;
                }
            });

            var txsinc = round_pr(all_taxes.total_included, this.pos.currency.rounding)?.toFixed(this.pos.currency.rounding.toString().split(".")[1].length);
            var txsexc = round_pr(all_taxes.total_excluded, this.pos.currency.rounding)?.toFixed(this.pos.currency.rounding.toString().split(".")[1].length);
            if (typeof txsinc !== 'undefined' && typeof txsexc !== 'undefined'){
                taxtotal = txsinc-txsexc;
            }
            else if(typeof txsinc === 'undefined' || typeof txsexc === 'undefined'){
                txsinc = 0;
                txsexc = 0;
                taxtotal = txsinc-txsexc;
            }
            return {
                "priceWithTax": parseFloat(txsinc),
                "priceWithoutTax": parseFloat(txsexc),
                "priceSumTaxVoid":  (all_taxes.total_void) ? round_pr(all_taxes.total_included, this.pos.currency.rounding)?.toFixed(this.pos.currency.rounding.toString().split(".")[1].length) : all_taxes.total_void,
                "priceWithTaxBeforeDiscount": all_taxes_before_discount.total_included,
                "tax": round_pr(taxtotal, this.pos.currency.rounding),
                "taxDetails": taxdetail,
            };
        },

//        get_fixed_lst_price: function(){
//            return round_dec(this.compute_fixed_price(this.get_lst_price())).toFixed(this.pos.config.decimal_rounding);
//        },
//        get_lst_price: function(){
//            return round_dec(this.product.lst_price).toFixed(this.pos.config.decimal_rounding);
//        },
//round_dec(ret, this.pos.config.decimal_rounding).toFixed(this.pos.config.decimal_rounding);
        set_lst_price: function(price){
            this.order.assert_editable();
            this.product.lst_price = round_pr(parseFloat(price) || 0, this.pos.currency.rounding)?.toFixed(this.pos.currency.rounding.toString().split(".")[1].length);
            this.trigger('change',this);
        },
    });

    /*
    Overwrite Paymentline.export_for_printing() in order
    to make it export the payment type that must be passed
    to the fiscal printer.
    */
    var original = models.Paymentline.prototype.export_for_printing;
    models.Paymentline = models.Paymentline.extend({
        export_for_printing: function() {
            var res = original.apply(this, arguments);
            res.type = this.payment_method.fiscalprinter_payment_type;
            res.type_index = this.payment_method.fiscalprinter_payment_index;
            return res;
        }
    });

    var _super_posmodel = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({
        initialize: function (session, attributes) {
            var tax_model = _.find(this.models, function(model){ return model.model === 'account.tax'; });
            tax_model.fields.push('fpdeptax');
            return _super_posmodel.initialize.call(this, session, attributes);
        },
    });

});
