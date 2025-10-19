from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    add_tester=fields.Boolean(compute='get_add_tester',store=True)
    @api.depends('order_line.allowed_tester','order_line.has_tester','order_line.is_tester')
    def get_add_tester(self):
        for rec in self:
            show_button_tester = self.order_line.filtered(
                lambda x: x.allowed_tester is True and (x.has_tester is False and x.is_tester is False))
            if show_button_tester:
                show_button_tester=True
            else:
                show_button_tester = False
            rec.add_tester=show_button_tester
    def get_tester(self):
        lines_for_test=self.order_line.filtered(lambda x:x.allowed_tester is True and not (x.has_tester is True or x.is_tester is True))
        lines_for_test.insert_tester()


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    allowed_tester=fields.Boolean('Richiede tester',related='product_template_id.allowed_tester',store=True)
    has_tester=fields.Boolean('Tester inserito')
    is_tester=fields.Boolean('E\' tester')

    def insert_tester(self):
        for res in self:
            name=f'{res.product_template_id.tester_description} {res.product_id.display_name}'
            default_data={'name':name,'product_uom_qty':1,'price_unit':res.product_template_id.tester_price,'order_id':res.order_id.id,'is_tester':True,'sequence':res.sequence}
            res.copy(default=default_data)
            res.has_tester=True


    def _prepare_procurement_values(self, group_id=False):
        vals = super()._prepare_procurement_values(group_id=group_id)
        vals["is_tester"] = self.is_tester
        return vals


class StockRule(models.Model):
    _inherit='stock.rule'

    def _get_custom_move_fields(self):
        fields = super(StockRule, self)._get_custom_move_fields()
        fields += ['is_tester']
        return fields

class StockMove(models.Model):
    _inherit = "stock.move"
    _rec_name = 'display_name'

    display_name = fields.Char(compute='get_display_name', store=True)
    is_tester=fields.Boolean('E\' tester',related='sale_line_id.is_tester',store=True)

    @api.depends('product_id','is_tester')
    def get_display_name(self):
        for rec in self:
            if not rec.is_tester:
                rec.display_name = rec.product_id.display_name
            else:
                if rec.product_id and rec.product_id.product_tmpl_id:
                    tmpl_id = rec.product_id.product_tmpl_id
                    if tmpl_id.tester_description:
                        name = f"{tmpl_id.tester_description} {rec.display_name}"
                        rec.display_name = name

    def _prepare_procurement_values(self):
        vals = super()._prepare_procurement_values()
        vals["is_tester"] = self.is_tester
        return vals
class StockMoveLine(models.Model):
    _inherit='stock.move.line'

    _rec_name='display_name'
    is_tester = fields.Boolean(related='move_id.is_tester', store=True)
    display_name = fields.Char(compute='get_display_name',store=True)

    @api.depends('product_id', 'is_tester')
    def get_display_name(self):
        for rec in self:
            if not rec.is_tester:
                rec.display_name= rec.product_id.display_name
            else:
                if rec.product_id and rec.product_id.product_tmpl_id:
                    tmpl_id= rec.product_id.product_tmpl_id
                    if tmpl_id.tester_description:
                        name=f"{tmpl_id.tester_description} {rec.product_id.display_name}"
                        rec.display_name = name

