odoo.define("fiscal_epos_print.ProductItem", function (require) {
    "use strict";
    var utils = require('web.utils');

    var core = require("web.core");
    var epson_epos_print = require('fiscal_epos_print.epson_epos_print');
    var _t = core._t;
    var eposDriver = epson_epos_print.eposDriver;
    const Registries = require('point_of_sale.Registries');
    const ProductItem = require('point_of_sale.ProductItem');
    var round_pr = utils.round_precision;


    const MyProductItem = ProductItem => class extends ProductItem {

        get price() {

            var formattedUnitPrice = parseFloat(round_pr(this.props.product.get_price(this.pricelist, 1), this.env.pos.currency.rounding));

//            if (this.env.pos.config.iface_tax_included === 'total') {
//                var product = this.props.product;
//                var taxes_ids = product.taxes_id;
//                var taxes =  this.env.pos.taxes;
//                var product_taxes = [];
//
//                _(taxes_ids).each(function(el){
//                    product_taxes.push(_.detect(taxes, function(t){
//                        return t.id === el;
//                    }));
//                });
//                if (!product_taxes[0].price_include && !product_taxes[0].include_base_amount)
//                {
//                    var tax_amount = this._compute_all(product_taxes[0], formattedUnitPrice, 1, !product_taxes[0].price_include);
//                    formattedUnitPrice += tax_amount;
//                }
//            }

            if (this.props.product.to_weight) {
                return `${formattedUnitPrice}/${
                    this.env.pos.units_by_id[this.props.product.uom_id[0]].name
                }`;
            } else {
                formattedUnitPrice = round_pr(formattedUnitPrice, this.env.pos.currency.rounding);
                if (typeof formattedUnitPrice !== 'undefined') {
                    return formattedUnitPrice.toFixed(this.env.pos.currency.rounding.toString().split(".")[1].length);
                }
                else if (typeof formattedUnitPrice === 'undefined') {
                    return;
                }
                else {
                    return this.env.pos.format_currency(formattedUnitPrice,'Product Price');
                }
            }
        }

        _compute_all(tax, base_amount, quantity, price_exclude) {
            base_amount = parseFloat(base_amount);
            if(price_exclude === undefined)
                var price_include = tax.price_include;
            else
                var price_include = !price_exclude;
            if (tax.amount_type === 'fixed') {
                var sign_base_amount = Math.sign(base_amount) || 1;
                // Since base amount has been computed with quantity
                // we take the abs of quantity
                // Same logic as bb72dea98de4dae8f59e397f232a0636411d37ce
                return tax.amount * sign_base_amount * Math.abs(quantity);
            }
            if (tax.amount_type === 'percent' && !price_include){
                return base_amount * tax.amount / 100;
            }
            if (tax.amount_type === 'percent' && price_include){
                return base_amount - (base_amount / (1 + tax.amount / 100));
            }
            if (tax.amount_type === 'division' && !price_include) {
                return base_amount / (1 - tax.amount / 100) - base_amount;
            }
            if (tax.amount_type === 'division' && price_include) {
                return base_amount - (base_amount * (tax.amount / 100));
            }
            return false;
        }
    };
    Registries.Component.extend(ProductItem, MyProductItem);
    return ProductItem;

});

