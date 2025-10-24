from odoo import fields, models, api


class ReportFornitoriData(models.Model):
    _name = 'report.fornitori.data'
    _rec_name='product_id'
    _order = 'invoice_date desc'
    name=fields.Char()
    invoice_date = fields.Date()
    bom_date=fields.Date()
    bom_name=fields.Char()
    mrp_id=fields.Many2one('mrp.production')
    move_type=fields.Selection([('invoice','Fattura'),('bom','Ordine di prod')],default='invoice')
    move_id = fields.Many2one('account.move')
    move_line =fields.Many2one('account.move.line')
    product_id = fields.Many2one('product.product')
    marchio_id=fields.Many2one('ak_connettore.marchio', related='product_id.marchio_id')
    partner_id = fields.Many2one('res.partner')
    quantity = fields.Float('Qty')
    product_type = fields.Selection([('direct','Scarico in prod.'),('comp','Componente')],default='comp',required=True)
    stock_move=fields.Many2one('stock.move')
    stock_move_line = fields.Many2one('stock.move.line')
    pos_order_id=fields.Many2one('pos.order')
    bom_id = fields.Many2one('mrp.bom')
    pos_order_line=fields.Many2one('pos.order.line',string='Pos order line')


    def maintenance_record(self):
        #Invoice
        invoices = self.search([('move_id','!=',False)])
        invoices_canceled= invoices.filtered(lambda inv:inv.move_id.state in ['cancel'])
        if invoices_canceled:
            invoices_canceled.unlink()
        #pos_order
        pos_orders = self.search([('pos_order_id', '!=', False),('move_id','=',False)])
        pos_orders_canceled = pos_orders.filtered(lambda pos: pos.pos_order_id.state in ['cancel'] or pos.pos_order_id.lines == False)
        if pos_orders_canceled:
            pos_orders_canceled.unlink()
        account_move = pos_orders.filtered(lambda pos: pos.pos_order_id.state in ['invoiced'] and pos.pos_order_id.account_move != False)
        invoice_to_delete = [p.pos_order_id.account_move.id for p in account_move]
        search_invoice_to_delete = self.search([('move_id','in',invoice_to_delete)])
        if search_invoice_to_delete:
            search_invoice_to_delete.unlink()
        #Move line
        stock_move_lines = self.search([('stock_move_line', '!=', False)])
        lines_canceled = stock_move_lines.filtered(lambda stock: stock.stock_move_line.state in ['cancel'])
        if lines_canceled:
            lines_canceled.unlink()

    def delete_all(self):
        qry='delete from report_fornitori_data'
        self.env.cr.execute(qry)
        self.env.cr.commit()
    def create_records(self):
        esistenti_inv = self.search([('move_id','!=',False)])
        esistenti_inv =[rec.move_id.id for rec in esistenti_inv]
        invoices =self.env['account.move'].search([('id','not in',esistenti_inv),('state','in',['posted'])])
        for inv in invoices:
            if inv.move_type in ['out_invoice']:
                self.create_report_fornitori_data(inv)
            elif inv.move_type in ['out_refund']:
                self.create_report_fornitori_data(inv, refund=True)
        self.create_pos_order_line()
    def create_pos_order_line(self):
        existing_pos = self.search([('pos_order_id','!=',False)])
        existing_pos_list= [ex_p.pos_order_id.id for ex_p in existing_pos ]
        search_pos=self.env['pos.order'].search([('state','in',['done','invoiced']),('lines','!=',False),('id','not in',existing_pos_list)])
        for pos in search_pos:
            if pos.account_move:
                exist_invoice = self.search([('move_id', '=', pos.account_move.id)])
                if exist_invoice:
                    exist_invoice.unlink()
            move_lines=pos.picking_ids.mapped('move_line_ids')
            for line in move_lines:


                line_dict = {'pos_order_id': pos.id,
                             'move_type': 'invoice',
                             'stock_move': line.move_id.id,
                             'product_id': line.product_id.id,
                             'quantity': line.qty_done if line.qty_done else line.product_uom_qty,
                             'product_type': 'comp',
                             'partner_id': pos.partner_id.id,
                             'stock_move_line': line.id,
                             'invoice_date': pos.fiscal_receipt_date}



                self.create(line_dict)
    def create_records_bom(self):
        esistenti_bom = self.search([('mrp_id', '!=', False)])
        esistenti_bom = [rec.mrp_id.id for rec in esistenti_bom]
        mrp_ids=self.env['mrp.production'].search([('id', 'not in', esistenti_bom),('state','=','done')])

        for mrp in mrp_ids:

            line_dict = {'mrp_id': mrp.id,'move_type':'bom','bom_date':mrp.date_finished,'invoice_date':mrp.date_finished,'name':mrp.name}
            for mrp_line in mrp.move_raw_ids:
                if mrp_line.quantity_done > 0:
                    line_dict['bom_id']=mrp.bom_id.id
                    line_dict['product_id'] = mrp_line.product_id.id
                    line_dict['quantity'] = mrp_line.quantity_done
                    line_dict['product_type'] = 'direct'
                    line_dict['stock_move'] = mrp_line.move_line_ids[0].move_id.id if mrp_line.move_line_ids else False
                    self.create(line_dict)
    def create_report_fornitori_data(self,invoice,refund=False,pos_order=False):

        for line in invoice.invoice_line_ids:
            line_dict = {'move_id': invoice.id,'move_type':'invoice'}

            if not line.product_id.bom_ids:
                line_dict['product_id'] = line.product_id.id
                line_dict['quantity'] = line.quantity if not refund else (line.quantity * -1)
                line_dict['product_type'] = 'comp'
            line_dict['move_line'] = line.id
            line_dict['partner_id'] = line.partner_id.id
            if pos_order:
                line_dict['pos_order_id']=pos_order
            line_dict['invoice_date'] = invoice.invoice_date

            self.create(line_dict)

            #todo fix forse non serve ###########


