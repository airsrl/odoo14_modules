import json
import logging
import random
from datetime import datetime
import datetime

from odoo import models, fields, api
import queue

#Documentazione
#https://www.datalog.it/valorizzazione-magazzino/#:~:text=Costo%20Medio%20Ponderato%3A%20effettua%20la,magazzino%20ai%20prezzi%20meno%20recenti.
from odoo.tests import Form


class WarehouseValuation(models.Model):
    _name = 'warehouse.valuation'

    name = fields.Char()
    valuation_method = fields.Selection([('cmp', 'CMP'), ('fifo', 'FIFO'), ('lifo', 'LIFO'), ('all', 'Tutti (Categoria Prodotto)')])
    product_ids = fields.Many2many('product.product')
    line_ids = fields.One2many('warehouse.valuation.line', 'valuation_id')

    def compute_valuation(self):
        if not self.product_ids:
            #Carico tutti i Prodotti
            product_ids = self.env['product.product'].search([])
        else:
            #Carico i prodotti selezionati
            product_ids = self.product_ids

        line_values = []
        for product in product_ids:
            print(product.default_code)
            values = {}
            #todo: Prendere valorizzazione da Categoria prodotto
            if self.valuation_method == 'cmp':
                values = self.calculate_cmp(product)
            if self.valuation_method == 'lifo':
                values = self.calculate_lifo(product)
            line_values.append((0, 0, values))

        self.line_ids.detail_lines.unlink()
        self.line_ids.unlink()
        self.line_ids = line_values


    def calculate_lifo(self, product):
        final_qty = 0
        lifo_price_unit = 0
        lifo_total_value = 0
        cost = 0

        #Produzione o Acquisto
        product_type = 'purchase'
        if product.bom_count > 0:
            #Produzione
            product_type = 'production'

        stock_moves = self.get_stock_moves(product)
        lifo_queue = queue.LifoQueue()
        detail_moves = []
        detail_moves_dict = []

        for move in stock_moves:
            detail_vals = {
                'date': move['date'].strftime('%Y-%m-%d %H:%M:%S'), 'move': move['name'],
                'type': '', 'qt': move['qty'], 'price_unit': '',
                'value_unit': '', 'qt_initial': '', 'qt_final': '', 'amount_value': ''
            }
            if move['type'] == 'incoming' or (move['type'] == 'mrp_operation' and move['production_id']):
                detail_vals.update({'type': 'Carico', 'qt_initial': final_qty})
                #Carico Merce (Acquisto o Produzione)
                final_qty += move['qty']
                price_unit = 0

                if product_type == 'purchase':
                    price_unit = self.get_price_unit(move)
                if product_type == 'production':
                    bom = self.env['mrp.bom']._bom_find(product=product)
                    price_unit = self.get_production_price_unit(move, bom)

                if lifo_price_unit == 0:
                    #Primo Movimento
                    lifo_price_unit = price_unit
                    new_value = final_qty * lifo_price_unit
                    lifo_total_value = new_value
                else:
                    #Successivi Movimenti
                    new_value = price_unit * move['qty']
                    lifo_total_value = lifo_total_value + new_value

                cost = lifo_total_value / final_qty
                detail_vals.update({'price_unit': price_unit, 'cost': cost, 'value_unit': new_value, 'qt_final': final_qty, 'amount_value': lifo_total_value})
                #Carico Lifo Queue
                lifo_queue.put({'qt': move['qty'], 'price_unit': price_unit})

            if move['type'] == 'outgoing' or (move['type'] == 'mrp_operation' and not move['production_id']):
                detail_vals.update({'type': 'Scarico', 'qt': -move['qty'], 'qt_initial': final_qty})
                #Scarico Merce (Vendita o Consumo Produzione)
                final_qty -= move['qty']
                qty_move = move['qty']
                partial_value = 0
                qty = 0

                while qty_move > 0:
                    #Calcolo la merce in uscita
                    last_in = lifo_queue.get()
                    qty_move = qty_move - last_in['qt']
                    if qty_move < 0:
                        #Ricarico il Residuo
                        lifo_queue.put({'qt': -(qty_move), 'price_unit': last_in['price_unit']})
                        qty = -qty_move
                    if qty_move >= 0:
                        qty = last_in['qt']


                    new_value = last_in['price_unit'] * (-qty)
                    partial_value += new_value
                    lifo_total_value = lifo_total_value + new_value

                price_unit = -(partial_value / move['qty'])
                cost = lifo_total_value / final_qty
                detail_vals.update({'price_unit': price_unit, 'cost': cost, 'qt_final': final_qty, 'value_unit': partial_value, 'amount_value': lifo_total_value})

            # Carico Dettaglio
            detail_moves_dict.append((0, 0, detail_vals))


        # while not lifo_queue.empty():
        #     print(lifo_queue.get())

        #Aggiorno il costo del Prodotto
        product.standard_price = cost

        return {
            'product_id': product.id,
            'product_type': product_type,
            'final_qty': final_qty,
            'cost': cost,
            'lifo_price_unit': lifo_price_unit,
            'lifo_total_value': lifo_total_value,
            'detail_lines': detail_moves_dict
        }


    def calculate_cmp(self, product):
        final_qty = 0
        cmp_price_unit = 0
        cmp_total_value = 0

        stock_moves = self.get_stock_moves(product)
        for move in stock_moves:
            if move['type'] == 'incoming':
                #Carico Merce
                final_qty += move['qty']
                if cmp_price_unit == 0:
                    #todo: Verificare se prendere da Storico Import
                    #Primo Movimento
                    cmp_price_unit = self.get_price_unit(move)
                    cmp_total_value = round(final_qty * cmp_price_unit, 2)
                else:
                    #Successivi Movimenti
                    new_value = round(self.get_price_unit(move) * move['qty'], 2)
                    cmp_price_unit = round((cmp_total_value + new_value) / final_qty, 2)
                    cmp_total_value = round(cmp_total_value + new_value, 2)

            if move['type'] == 'outgoing':
                #Scarico Merce
                final_qty -= move['qty']
                new_value = round(cmp_price_unit * (-move['qty']), 2)
                cmp_total_value = round(cmp_total_value + new_value, 2)

        return {
            'product_id': product.id,
            'product_type': 'purchase',
            'final_qty': final_qty,
            'cmp_price_unit': cmp_price_unit,
            'cmp_total_value': cmp_total_value,
        }

    def get_production_price_unit(self, move, bom):
        total = 0
        #1. Costo Operazioni di Produzione
        for opt in bom.operation_ids:
            duration_expected = (opt.workcenter_id.time_start + opt.workcenter_id.time_stop + opt.time_cycle)
            total += (duration_expected / 60) * opt.workcenter_id.costs_hour
        #2. Extra Costo
        #3. Costo Componenti
        """
        query per ottenere le stock_move con stesso group_id e raw_material_production_id
        poi cerco il costo del prodotto alla data di produzione (
        """

        return total

    def get_price_unit(self, move):

        purchase_line_id = self.env['purchase.order.line'].browse(move['purchase_line_id'])
        if purchase_line_id:
            #Prezzo da Ordine
            price_unit = purchase_line_id.price_unit
            if purchase_line_id.invoice_lines:
                #Prezzo da Fattura
                for inv_line in purchase_line_id.invoice_lines:
                    if inv_line.move_id.state not in ['cancel', 'draft']:
                        #Solo Fatture Validate
                        if inv_line.move_id.move_type == 'in_invoice':
                            #Fattura Fornitore
                            price_unit = inv_line.price_unit
                        elif inv_line.move_id.move_type == 'in_refund':
                            #Nota Debito Fornitore
                            #todo: Da Gestire
                            print("OK")
        else:
            #Prezzo da Movimento
            price_unit = move['price_unit']

        return price_unit

    def get_stock_moves(self, product):
        query = """
            select 
                date as "date",
                sm.reference as "name",
                product_id as "product",
                price_unit as "price_unit", 
                product_uom_qty as "qty",
                sm.product_uom_qty * sm.price_unit as "value",
                picking_type_id as "picking_type",
                spt.code as "type",
                purchase_line_id as "purchase_line_id",
                production_id as "production_id"
            from stock_move sm
            join stock_picking_type spt on spt.id = sm.picking_type_id 
            where state = 'done' and product_id = %s
            order by sm."date" asc
        """ % (product.id)
        self.env.cr.execute(query)
        moves = self.env.cr.dictfetchall()
        return moves




    def samples(self):

        for x in range(1, 10000):
            code = 'HU00' + str(x)
            p = self.env['product.product'].search([('default_code', '=', code)])
            if not p:
                self.env['product.product'].create({
                    'name': 'HU00' + str(x),
                    'default_code': 'HU00' + str(x),
                    'type': 'product'
                })
                print("Prodotto Creato")
                self.env.cr.commit()

        start_date = datetime.date(2021, 1, 1)
        end_date = datetime.date(2022, 12, 31)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days

        for x in range(1, 1000):
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            order_lines = []
            for y in range(1, random.randrange(1, 200)):
                product_id = self.env['product.product'].search([('default_code', '=', 'HU00' + str(random.randrange(1, 9999)))], limit=1)
                order_lines.append((0, 0, {
                    'product_id': product_id.id,
                    'name': product_id.name,
                    'product_uom': product_id.uom_po_id.id,
                    'product_qty': random.randrange(1, 100),
                    'price_unit': random.uniform(0.5, 10.9)
                }))
            order_vals = {
                'partner_id': 7,
                'date_order': random_date,
                'order_line': order_lines
            }
            order_id = self.env['purchase.order'].create(order_vals)
            self.env.cr.commit()
            order_id.button_confirm()
            self.env.cr.commit()
            receipt = order_id.picking_ids
            wiz = receipt.button_validate()
            if order_id.amount_total > 0:
                wiz = Form(self.env['stock.immediate.transfer'].with_context(wiz['context'])).save().process()
                print("ORDINE ACQUISTO: " + str(x) + ' RIGHE: ' + str(y))

        for x in range(1, 1000):
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + datetime.timedelta(days=random_number_of_days)
            order_lines = []
            for y in range(1, random.randrange(1, 50)):
                product_id = self.env['product.product'].search([('default_code', '=', 'HU00' + str(random.randrange(1, 9999)))], limit=1)
                order_lines.append((0, 0, {
                    'product_id': product_id.id,
                    'name': product_id.name,
                    'product_uom': product_id.uom_po_id.id,
                    'product_uom_qty': random.randrange(1, 5),
                    'price_unit': random.uniform(0.5, 10.9)
                }))
            order_vals = {
                'partner_id': 7,
                'date_order': random_date,
                'order_line': order_lines
            }
            order_id = self.env['sale.order'].create(order_vals)
            self.env.cr.commit()
            order_id.action_confirm()
            self.env.cr.commit()
            receipt = order_id.picking_ids
            try:
                receipt.action_assign()
                res_dict = receipt.button_validate()
                res_dict = Form(self.env['stock.immediate.transfer'].with_context(res_dict['context'])).save().process()
                backorder_wizard = Form(self.env['stock.backorder.confirmation'].with_context(res_dict['context'])).save()
                backorder_wizard.process_cancel_backorder()
                print("ORDINE VENDITA: " + str(x))
            except Exception as e:
                print("NO")
