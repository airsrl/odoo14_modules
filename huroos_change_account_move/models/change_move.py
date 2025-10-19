from odoo import models, fields, api


# Cambio Conti
class CambioContiLine(models.TransientModel):
    _name = 'cambio.conti.line'
    conto_sorgente = fields.Many2one('account.account')
    conto_destinazione = fields.Many2one('account.account')
    id_conto = fields.Many2one('cambio.conti')

# Cambio Imposte Applicate da Imposta Sorgente
class CambioImposteLine(models.TransientModel):
    _name = 'cambio.imposte.line'

    imposta_sorgente = fields.Many2one('account.tax')
    imposta_destinazione = fields.Many2one('account.tax')
    id_conto = fields.Many2one('cambio.conti')

# Cambio Imposte Applicate da Conto Sorgente
class InserimentoImposteLine(models.TransientModel):
    _name = 'inserimento.imposte.line'

    conto_sorgente = fields.Many2one('account.account')
    imposta_destinazione = fields.Many2one('account.tax')
    id_conto = fields.Many2one('cambio.conti')

class CambioCreatoImposteLine(models.TransientModel):
    _name = 'cambio.creato.imposte.line'

    imposta_sorgente = fields.Many2one('account.tax')
    imposta_destinazione = fields.Many2one('account.tax')
    id_conto = fields.Many2one('cambio.conti')

class InserimentoCreatoImposteLine(models.TransientModel):
    _name = 'inserimento.creato.imposte.line'

    conto_sorgente = fields.Many2one('account.account')
    imposta_destinazione = fields.Many2one('account.tax')
    id_conto = fields.Many2one('cambio.conti')

class CambioConti(models.TransientModel):
    _name = 'cambio.conti'

    conti_ids = fields.One2many('cambio.conti.line', 'id_conto')
    imposte_ids = fields.One2many('cambio.imposte.line', 'id_conto')
    ins_imposta_ids = fields.One2many('inserimento.imposte.line', 'id_conto')
    creato_imposte_ids = fields.One2many('cambio.creato.imposte.line', 'id_conto')
    ins_creato_imposta_ids = fields.One2many('inserimento.creato.imposte.line', 'id_conto')
    add_analytic = fields.Boolean()
    account_ids = fields.Many2many('account.account')
    fiscal_position_id = fields.Many2one('account.fiscal.position')
    inverti = fields.Boolean()
    analytic_account_id = fields.Many2one('account.analytic.account')
    conti_doppi_crediti = fields.Boolean()
    merge_account_line = fields.Boolean()


    def applica_regole_conto(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        crediti_v_clienti = self.env['account.account'].search([('name', '=', 'CREDITI V/CLIENTI')], limit=1)

        # Questo per verificare se l'action menu è stato premuto dalle account.move o account.move.line
        origin_active_ids = context.get('active_model', False)

        registrazioni = []
        if origin_active_ids == 'account.move':
            registrazioni = self.env['account.move'].browse(active_ids)
        elif origin_active_ids == 'account.move.line':
            registrazioni = self.env['account.move.line'].browse(active_ids)

        for registrazione in registrazioni:

            line_id = False
            if origin_active_ids == 'account.move.line':
                line_id = registrazione.id
                registrazione = registrazione.move_id

            if self.ins_imposta_ids or self.creato_imposte_ids or self.ins_creato_imposta_ids or self.conti_doppi_crediti or self.analytic_account_id or self.add_analytic or self.merge_account_line:
                # Viene annullata solamente se non bisogna cambiare dei conti, altrimenti sarebbe molto lento
                if registrazione.state == 'posted':
                    # La registrazione è generata, la reimposta in bozza
                    registrazione.button_cancel()


            for line in registrazione.line_ids:

                if (
                        origin_active_ids == 'account.move.line' and line.id == line_id) or origin_active_ids == 'account.move':

                    id_cambio_conto = 0

                    for ins in self.ins_imposta_ids:
                        if line.account_id.id == ins.conto_sorgente.id:
                            # Cambio l'imposta
                            if ins.imposta_destinazione:
                                line.write({'tax_ids': [(5,), (4, ins.imposta_destinazione.id)]})
                            else:
                                line.write({'tax_ids': [(5,)]})

                    for regola in self.conti_ids:
                        if line.account_id.id == regola.conto_sorgente.id:
                            id_cambio_conto = regola.conto_destinazione.id
                    if id_cambio_conto > 0:
                        self.env.cr.execute("update account_move_line set account_id = %s where id = %s", (id_cambio_conto, line.id))


                    if len(line.tax_ids) > 0:
                        id_cambio_imposta = 0
                        for regola in self.imposte_ids:

                            if line.tax_ids[0].id == regola.imposta_sorgente.id:
                                id_cambio_imposta = regola.imposta_destinazione.id
                        if id_cambio_imposta > 0:
                            line.write({'tax_ids': [(6, 0, [id_cambio_imposta])]})

                    if line.tax_line_id:
                        for regola in self.creato_imposte_ids:
                            if line.tax_line_id.id == regola.imposta_sorgente.id:
                                line.write({'tax_line_id': regola.imposta_destinazione.id})

                    if line.account_id:
                        for regola in self.ins_creato_imposta_ids:
                            if line.account_id.id == regola.conto_sorgente.id:
                                line.write({'tax_line_id': regola.imposta_destinazione.id})

                    if self.conti_doppi_crediti:
                        if line.credit != 0:
                            line.account_id = crediti_v_clienti.id

                    if self.analytic_account_id:
                        if line.account_id in self.account_ids:
                            # Per tutte le account.move.line che hanno conto finanziario soggetto e conto analitico mancante
                            line.analytic_account_id = self.analytic_account_id.id

                    if self.add_analytic:
                        if line.account_id in self.account_ids:
                            # Per tutte le account.move.line che hanno conto finanziario soggetto e conto analitico mancante
                            if registrazione.ref:
                                analytic_code = registrazione.ref[:3]
                                if analytic_code:
                                    analytic_account = self.env.cr.execute(
                                        "select id from account_analytic_account where name like '%s%%' and length(name) > 3" % (
                                            analytic_code,))
                                    analytic_account = self.env.cr.fetchall()
                                    if analytic_account:
                                        line.analytic_account_id = analytic_account[0][0]
                                    else:
                                        if 'FATTURE' not in registrazione.journal_id.name:
                                            analytic_code = registrazione.journal_id.name[:3]
                                            if analytic_code:
                                                analytic_account = self.env.cr.execute(
                                                    "select id from account_analytic_account where name like '%s%%' and length(name) > 3" % (
                                                    analytic_code,))
                                                analytic_account = self.env.cr.fetchall()
                                                if analytic_account:
                                                    line.analytic_account_id = analytic_account[0][0]
                                        else:
                                            analytic_code = registrazione.ref[:3]
                                            if analytic_code:
                                                analytic_account = self.env.cr.execute(
                                                    "select id from account_analytic_account where name like '%s%%' and length(name) > 3" % (
                                                        analytic_code,))
                                                analytic_account = self.env.cr.fetchall()
                                                if analytic_account:
                                                    line.analytic_account_id = analytic_account[0][0]

            if self.ins_imposta_ids or self.creato_imposte_ids or self.ins_creato_imposta_ids or self.conti_doppi_crediti or self.analytic_account_id or self.add_analytic or self.merge_account_line:
                if registrazione.state == 'draft':
                    # La registrazione è in bozza, la reimposta in generata
                    registrazione.action_post()