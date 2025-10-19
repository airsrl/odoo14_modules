

from odoo import _, fields, models

from odoo.addons.l10n_it_delivery_note.models.stock_delivery_note import DATE_FORMAT


class AccountInvoice(models.Model):
    _inherit = "account.move"


    note_dn = fields.Boolean(string="Note DN")





    def group_lines_by_ddt(self,group_by):
        for invoice in self.filtered(lambda i: i.delivery_note_ids):
            invoice.invoice_line_ids.filtered(lambda r: r.display_type).unlink()
            dn_list_grouped, residual_list = invoice.grouped_lines_by_ddt(group_by)
            #invoice.line_ids.unlink()

            line_number = 0
            invoice_line_vals_list = [(5,)]
            for dn in dn_list_grouped:
                # prepare nota dn
                delivery_note_id = self.env["stock.delivery.note"].browse(dn)
                nota_dn_vals = {
                    "sequence": line_number,
                    "name": _("""Delivery Note "{}" of {}""").format(
                        delivery_note_id.name,
                        delivery_note_id.date.strftime(DATE_FORMAT),
                    ),
                    "display_type": "line_section",
                    "note_dn": True,
                    "move_id": invoice.id,
                }
                #invoice.write({"invoice_line_ids": [(0, 0, nota_dn_vals)]})
                invoice_line_vals_list.append((0, 0, nota_dn_vals))
                line_number += 1


                for line in dn_list_grouped[dn]:
                    invoice_line_vals = {
                        "sequence": line_number,
                        "delivery_note_id": line["delivery_note_id"],
                        "sale_line_ids": line["sale_line_ids"],
                        "product_id": line["product_id"],
                        "name": line["name"],
                        "quantity": line["quantity"],
                        "product_uom_id": line["product_uom_id"],
                        "discount": line["discount"],
                        "price_unit": line["price_unit"],
                        "account_id": line["account_id"],
                        "tax_ids": line["tax_ids"],
                        "analytic_account_id": line["analytic_account_id"],
                        "analytic_tag_ids": line["analytic_tag_ids"],
                        "move_id": invoice.id,
                    }

                    #invoice.write({"invoice_line_ids": [(0,0, invoice_line_vals)] })
                    invoice_line_vals_list.append((0, 0, invoice_line_vals))
                    line_number += 1


            invoice.write({"invoice_line_ids": invoice_line_vals_list})


            for line in residual_list:
                invoice_line_vals = {
                    "sequence": line_number,
                    "delivery_note_id": line["delivery_note_id"],
                    "sale_line_ids": line["sale_line_ids"],
                    "product_id": line["product_id"],
                    "name": line["name"],
                    "quantity": line["quantity"],
                    "product_uom_id": line["product_uom_id"],
                    "discount": line["discount"],
                    "price_unit": line["price_unit"],
                    "account_id": line["account_id"],
                    "tax_ids": line["tax_ids"],
                    "analytic_account_id": line["analytic_account_id"],
                    "analytic_tag_ids": line["analytic_tag_ids"],
                    "move_id": invoice.id,
                }
                invoice.write({"invoice_line_ids": [(0, 0, invoice_line_vals)]})
                line_number += 1

    def grouped_lines_by_ddt(self, group_by='ddt_date'):
        """
        Returns invoice lines from a specified invoice grouped by ddt
        """
        dn_list = []
        residual_list = []

        # do not consider Sections and Notes: they will be overwritten
        for invoice_line in self.invoice_line_ids.filtered(
            lambda l: not l.display_type
        ):
            note_line_qty = 0
            for sale_line in invoice_line.sale_line_ids:
                delivery_note_line_ids = (
                    self.delivery_note_ids.mapped("line_ids")
                    & sale_line.delivery_note_line_ids
                )
                for note_line in delivery_note_line_ids:
                    note_line_qty += note_line.product_qty
                    dn_list.append(
                        {
                            "delivery_note_id": note_line.delivery_note_id.id,
                            "date": note_line.delivery_note_id.date,
                            "sale_line_ids": [(6, 0, [sale_line.id])],
                            "product_id": invoice_line.product_id.id,
                            "name": invoice_line.name,
                            "quantity": note_line.product_qty,
                            "product_uom_id": note_line.product_uom_id.id,
                            "discount": invoice_line.discount,
                            "price_unit": invoice_line.price_unit,
                            "account_id": invoice_line.account_id.id,
                            "tax_ids": [(6, 0, invoice_line.tax_ids.ids)],
                            "analytic_account_id": invoice_line.analytic_account_id.id,
                            "analytic_tag_ids": [
                                (6, 0, invoice_line.analytic_tag_ids.ids)
                            ],
                        }
                    )
            if invoice_line.quantity != note_line_qty:
                residual_list.append(
                    {
                        "delivery_note_id": False,
                        "date": False,
                        "sale_line_ids": [(6, 0, invoice_line.sale_line_ids.ids)],
                        "product_id": invoice_line.product_id.id,
                        "name": invoice_line.name,
                        "quantity": invoice_line.quantity - note_line_qty,
                        "product_uom_id": invoice_line.product_uom_id.id,
                        "discount": invoice_line.discount,
                        "price_unit": invoice_line.price_unit,
                        "account_id": invoice_line.account_id.id,
                        "tax_ids": invoice_line.tax_ids.ids,
                        "analytic_account_id": invoice_line.analytic_account_id.id,
                        "analytic_tag_ids": [(6, 0, invoice_line.analytic_tag_ids.ids)],
                    }
                )
        # group by dn
        if group_by == 'ddt_number':
            dn_list.sort(key=lambda x: x.get("delivery_note_id"))
        else:
            dn_list.sort(key=lambda x: x.get("date"),reverse=True)
        dn_list_grouped = {}
        for item in dn_list:
            dn_list_grouped.setdefault(item["delivery_note_id"], []).append(item)
        return dn_list_grouped, residual_list





class AccountInvoiceLine(models.Model):
    _inherit = "account.move.line"



    note_dn = fields.Boolean(string="Note DN")
