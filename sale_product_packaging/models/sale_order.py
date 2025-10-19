from odoo import fields, models, api
import pandas as pd

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def add_additional_product(self):
        for record in self:
            # Pickings in SO
            for picking in record.picking_ids:
                if picking.state in ['done', 'cancel']:
                    continue
                additional_products_ids = []
                # Lines in move lines
                for line in picking.move_lines:
                    if line.product_id.categ_id and line.product_id.categ_id.additional_products_in_picking and not line.is_tester: #modifica Kevin originale
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
    def action_confirm(self):
        """ Setting product code generatig it frome the category sequence """
        res = super(SaleOrder, self).action_confirm()
        self.add_product_packaging()


        return res

    def add_product_packaging(self):
        for record in self:
            # Pickings in SO
            for picking in record.picking_ids:
                if picking.state in ['done', 'cancel']:
                    continue
                additional_box_standard = []
                # Lines in move lines

                for line in picking.move_lines:
                    prd = False
                    if line.product_id.box_standard_id and not line.is_tester:
                        prd=line.product_id.box_standard_id
                    elif line.product_id.box_tester_id and line.is_tester:
                        prd = line.product_id.box_tester_id
                    if prd:
                        existing_line = next(
                            (item for item in additional_box_standard if item["product_id"] == prd.id and item['is_tester'] == line.is_tester ) , False)
                        if existing_line:
                            # Incrementing qty
                            existing_line["product_uom_qty"] = float(
                                existing_line["product_uom_qty"]) + line.product_qty / (prd.qty_contained or 1)
                        else:
                            # New move.line
                            additional_box_standard.append(
                                {
                                    "product_id": prd.id,
                                    "name": f"+ {prd.name}",
                                    "description_picking": f"+ {prd.name}",
                                    "product_uom": prd.uom_id.id,
                                    "location_id": line.location_id.id,
                                    "location_dest_id": line.location_dest_id.id,
                                    "product_uom_qty": line.product_qty / (prd.qty_contained or 1),
                                    "picking_id": picking.id,
                                    "date": line.date,
                                    "date_deadline": line.date_deadline,
                                    'is_tester':line.is_tester
                                }
                            )

            # Adding the additional_products_ids lines

                for val in additional_box_standard:
                    val['product_uom_qty'] = round(val['product_uom_qty'],2)
                move = self.env["stock.move"].create(additional_box_standard)

