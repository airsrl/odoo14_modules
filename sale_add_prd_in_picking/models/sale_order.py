from odoo import fields, models, api


class sale_order(models.Model):
    _inherit = 'sale.order'

    # @api.multi
    def action_confirm(self):
        """ Setting product code generatig it frome the category sequence """
        res = super(sale_order, self).action_confirm()
        self.add_additional_product()

        return res

    def add_additional_product(self):
        for record in self:
            # Pickings in SO
            for picking in record.picking_ids:
                if picking.state in ['done', 'cancel']:
                    continue
                additional_products_ids = []
                # Lines in move lines
                for line in picking.move_lines:
                    if line.product_id.categ_id and line.product_id.categ_id.additional_products_in_picking:
                        # Products in additional products in Category
                        for prd in line.product_id.categ_id.additional_products_in_picking:

                            # Checking if a line with the same product already exists in additional_products_ids
                            existing_line = next((item for item in additional_products_ids if item["product_id"] == prd.id), False)
                            if existing_line:
                                # Incrementing qty
                                existing_line["product_uom_qty"] = float(existing_line["product_uom_qty"]) + line.product_qty
                            else:
                                # New move.line
                                additional_products_ids.append(
                                    {
                                        "product_id": prd.id,
                                        "name": f"+ {prd.name}",
                                        "description_picking": f"+ {prd.name}",
                                        "product_uom": prd.uom_id.id,
                                        "location_id": line.location_id.id,
                                        "location_dest_id": line.location_dest_id.id,
                                        "product_uom_qty": line.product_qty,
                                        "picking_id": picking.id,
                                        "date": line.date,
                                        "date_deadline": line.date_deadline
                                    }
                                )

                # Adding the additional_products_ids lines
                move = self.env["stock.move"].create(additional_products_ids)
