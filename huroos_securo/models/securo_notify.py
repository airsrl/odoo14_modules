from odoo import fields, models, api
from datetime import date, datetime, timedelta


class SecuroNotify(models.Model):
    _name = 'securo.notify'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'notifiche securo'

    name = fields.Char()
    mail_destinatari = fields.Many2many('res.partner', string='Email destinatari')
    active = fields.Boolean('Attivo')
    # scadenze corsi
    course_days = fields.Integer('giorni dalla scadenza')
    course_mail = fields.Boolean('Abilita invio email')

    # scadenza visite
    visit_days = fields.Integer('giorni dalla scadenza')
    visit_mail = fields.Boolean('Abilita invio email')

    # scadenza Autoveicoli
    veichle_days = fields.Integer('giorni dalla scadenza')
    veichle_mail = fields.Boolean('Abilita invio email')

    # scadenza Attrezzature
    tool_days = fields.Integer('giorni dalla scadenza')
    tool_mail = fields.Boolean('Abilita invio email')

    _sql_constraints = [
        ('company_uniq', 'unique(company_id)', 'Configurazioni singole per azienda!'),
    ]

    def _default_company(self):
        return self.env.company

    company_id = fields.Many2one("res.company", required=True, default=_default_company)

    def name_get(self):
        result = []
        for rec in self:
            name = rec.company_id.name + ' ' + ''.join(rec.mail_destinatari.mapped('name'))
            result.append((rec.id, name))
        return result

    def cron_mail_deadline(self):
        records = self.search([('active', '=', True)])
        for rec in records:
            rec.send_email_scadenze(exclude_old_note=True)

    def send_email_scadenze(self, exclude_old_note=False):
        # template_id = self.env.ref('huroos_securo.email_template_deadline').id
        # mail_template_id = self.env['mail.template'].browse(template_id)
        data_inizio = date.today()

        html_visit = ""
        html_exam = ""
        if self.visit_mail:
            data_fine_visite = data_inizio + timedelta(days=self.visit_days)
            domain = [('visit_deadline', '>=', data_inizio), ('visit_deadline', '<=', data_fine_visite)]
            if exclude_old_note:
                domain.append(('has_notify', '=', False))

            deadline_visit = self.env['exam.employee.result'].search(domain, order='visit_deadline asc')
            if deadline_visit:
                html_visit += '<p>Le seguenti visite mediche sono in scadenza:</p>'
                html_visit += '<table width="900px;">'
                html_visit += '<thead><tr>'
                html_visit += '<th style="text-align: left; border-bottom: 1px solid black;">Dipendente</th>'
                html_visit += '<th style="text-align: left;padding-left:3px; border-bottom: 1px solid black;">Visita</th>'
                html_visit += '<th style="text-align: right; border-bottom: 1px solid black;">Esito</th>'
                html_visit += '<th style="text-align: right; border-bottom: 1px solid black;">Scadenza</th>'
                html_visit += '</tr></thead>' \
                              '<tbody>'
                for visit in deadline_visit:
                    html_visit += f"""
                            <tr>
                                <td style="text-align: left; border-bottom: 1px solid lightgray;"><span>{visit.hr_employee_id.name}</span></td>
                                <td style="text-align: left;padding-left:3px; border-bottom: 1px solid lightgray;"><span>{visit.visit_id.display_name}</span></td>
                               
                                <td style="text-align: right;padding-left:3px; border-bottom: 1px solid lightgray;"><span>{visit.esito.name if visit.esito else ''}</span></td>
                                <td style="text-align: right; border-bottom: 1px solid lightgray;"><span>{visit.visit_deadline.strftime('%d/%m/%Y')}</span></td>
                            </tr>"""
                html_visit += '</tbody></table>'
                if exclude_old_note:
                    deadline_visit.write({'has_notify': True})

            domain = [('next_date', '>=', data_inizio), ('next_date', '<=', data_fine_visite)]
            if exclude_old_note:
                domain.append(('has_notify', '=', False))
            deadline_exam = self.env['securo.exam.result'].search(domain, order='next_date asc')

            if deadline_exam:
                html_exam += '<br/><p>I seguenti esami sono in scadenza:</p>'
                html_exam += '<table width="900px;">'
                html_exam += '<thead><tr>'
                html_exam += '<th style="text-align: left; border-bottom: 1px solid black;">Dipendente</th>'
                html_exam += '<th style="text-align: left;padding-left:3px; border-bottom: 1px solid black;">Esame</th>'
                html_exam += '<th style="text-align: left; border-bottom: 1px solid black;">Descrizione</th>'
                html_exam += '<th style="text-align: right; border-bottom: 1px solid black;">Esito</th>'
                html_exam += '<th style="text-align: right; border-bottom: 1px solid black;">Scadenza</th>'
                html_exam += '</tr></thead>' \
                             '<tbody>'
                for exam in deadline_exam:
                    html_exam += f"""
                            <tr>
                                <td style="text-align: left; border-bottom: 1px solid lightgray;"><span>{exam.employee_result_id.hr_employee_id.name}</span></td>
                                 <td style="text-align: left;padding-left:3px; border-bottom: 1px solid lightgray;"><span>{exam.name.name}</span></td>
                                  <td style="text-align: left;padding-left:3px; border-bottom: 1px solid lightgray;"><span>{exam.description if exam.description else ''}</span></td>
                                <td style="text-align: right;padding-left:3px; border-bottom: 1px solid lightgray;"><span>{exam.esito.name if exam.esito else ''}</span></td>
                                <td style="text-align: right; border-bottom: 1px solid lightgray;"><span>{exam.next_date.strftime('%d/%m/%Y')}</span></td>
                            </tr>"""

                html_exam += '</tbody></table><br/>'
                if exclude_old_note:
                    deadline_exam.write({'has_notify': True})
        html_course = ""
        if self.course_mail:

            data_fine_corsi = data_inizio + timedelta(days=self.course_days)
            domain = [('course_deadline', '>=', data_inizio),
                      ('course_deadline', '<=', data_fine_corsi)]
            if exclude_old_note:
                domain.append(('has_notify', '=', False))
            deadline_course = self.env['securo.single.employee.course'].search(domain, order='course_deadline asc')

            if deadline_course:
                html_course += '<p>I seguenti corsi sono in scadenza:</p>'
                html_course += '<table width="900px">'
                html_course += '<thead>' \
                               '<tr>'
                html_course += '<th style="text-align: left; border-bottom: 1px solid black;">Dipendente</th>'
                html_course += '<th style="text-align: left; padding-left:3px; border-bottom: 1px solid black;">Corso</th>'
                html_course += '<th style="text-align: right; border-bottom: 1px solid black;">Scadenza</th>'
                html_course += '</tr></thead> ' \
                               '<tbody>'
                for course in deadline_course:
                    html_course += f"""
                    
                                        <tr>
                                            <td style="text-align: left; border-bottom: 1px solid lightgray;"><span>{course.hr_employee_id.name}</span></td>
                                            <td style="text-align:padding-left:3px; left; border-bottom: 1px solid lightgray;"><span>{course.course_id.name if course.course_id else course.single_course_id.name}</span></td>
                                            <td style="text-align: right; border-bottom: 1px solid lightgray;"><span>{course.course_deadline.strftime('%d/%m/%Y')}</span></td>
                                        </tr>"""
                html_course += '</tbody></table><br/>'
                if exclude_old_note:
                    deadline_course.write({'has_notify': True})
        html_veichle = ""
        if self.veichle_mail:
            data_fine = data_inizio + timedelta(days=self.veichle_days)
            domain = [('due_date', '>=', data_inizio), ('due_date', '<=', data_fine), ('fleet_id', '!=', False)]
            if exclude_old_note:
                domain.append(('has_notify', '=', False))

            deadline_veichle = self.env['huroos.fleet.scadenze'].search(domain, order='due_date asc')
            if deadline_veichle:
                html_veichle += '<p>I seguenti doc. autoveicolo sono in scadenza:</p>'
                html_veichle += '<table width="900px;">'
                html_veichle += '<thead><tr>'
                html_veichle += '<th style="text-align: left; border-bottom: 1px solid black;">Autoveicolo</th>'
                html_veichle += '<th style="text-align: left;padding-left:3px; border-bottom: 1px solid black;">Tipo Documento</th>'
                html_veichle += '<th style="text-align: left;padding-left:3px; border-bottom: 1px solid black;">Desc. Documento</th>'
                html_veichle += '<th style="text-align: right; border-bottom: 1px solid black;">Scadenza</th>'
                html_veichle += '</tr></thead>' \
                                '<tbody>'
                for vec in deadline_veichle:
                    html_veichle += f"""
                            <tr>
                                <td style="text-align: left; border-bottom: 1px solid lightgray;"><span>{vec.fleet_id.name}</span></td>
                                <td style="text-align: left;padding-left:3px; border-bottom: 1px solid lightgray;"><span>{vec.name.name if vec.name else ""}</span></td>
                                <td style="text-align: left;padding-left:3px; border-bottom: 1px solid lightgray;"><span>{vec.description}</span></td>
                                <td style="text-align: right; border-bottom: 1px solid lightgray;"><span>{vec.due_date.strftime('%d/%m/%Y')}</span></td>
                            </tr>"""
                html_veichle += '</tbody></table><br/>'
                if exclude_old_note:
                    deadline_veichle.write({'has_notify': True})
        html_equipment = ""
        if self.tool_mail:
            data_fine = data_inizio + timedelta(days=self.tool_days)
            domain = [('due_date', '>=', data_inizio), ('due_date', '<=', data_fine), ('equipment_id', '!=', False)]
            if exclude_old_note:
                domain.append(('has_notify', '=', False))

            deadline_equipment = self.env['huroos.fleet.scadenze'].search(domain, order='due_date asc')
            if deadline_equipment:
                html_equipment += '<p>I seguenti doc. automezzi sono in scadenza:</p>'
                html_equipment += '<table width="900px;">'
                html_equipment += '<thead><tr>'
                html_equipment += '<th style="text-align: left; border-bottom: 1px solid black;">Automezzo/Attrezzatura</th>'
                html_equipment += '<th style="text-align: left;padding-left:3px; border-bottom: 1px solid black;">Tipo Documento</th>'
                html_equipment += '<th style="text-align: left;padding-left:3px; border-bottom: 1px solid black;">Desc. Documento</th>'
                html_equipment += '<th style="text-align: right; border-bottom: 1px solid black;">Scadenza</th>'
                html_equipment += '</tr></thead>' \
                                  '<tbody>'
                for eq in deadline_equipment:
                    html_equipment += f"""
                                    <tr>
                                        <td style="text-align: left; border-bottom: 1px solid lightgray;"><span>{eq.equipment_id.name}</span></td>
                                        <td style="text-align: left;padding-left:3px; border-bottom: 1px solid lightgray;"><span>{eq.name.name if eq.name else ''}</span></td>
                                        <td style="text-align: left;padding-left:3px; border-bottom: 1px solid lightgray;"><span>{eq.description}</span></td>
                                        <td style="text-align: right; border-bottom: 1px solid lightgray;"><span>{eq.due_date.strftime('%d/%m/%Y')}</span></td>
                                    </tr>"""
                html_equipment += '</tbody></table><br/>'
                if exclude_old_note:
                    deadline_equipment.write({'has_notify': True})

        if html_course or html_visit or html_veichle or html_equipment:
            body = """
                            <div style="margin: 0px; padding: 0px;">
                                <p>Buongiorno, 
                                prego prendere visione delle seguenti informazioni .</p>
                                %s
                                <br/>
                                %s
                                <br/>
                                %s
                                <br/>
                                %s
                                <br/>
                                %s
                                <p>Grazie <br/></p>
                                <p>Cordiali saluti,<br/>
                                ${object.company_id.display_name}</p>
                            </div>
                    """ % (html_visit, html_exam, html_course, html_veichle, html_equipment)

            email_destinatari = self.mail_destinatari.ids

            self.message_post(author_id=self.env.ref('base.partner_root').id, body=body, message_type="email",
                              subtype_xmlid="huroos_securo.email_template_deadline", partner_ids=email_destinatari)

    def open_notify_config(self):

        if len(self.env.companies) > 1:

            return {
                'name': 'Configurazione notifiche',
                'type': 'ir.actions.act_window',
                'res_model': 'securo.notify',
                'domain': [('id', 'in', self.env.companies.ids)],
                'views': [(False, 'tree'), (False, 'form')],
                'view_mode': 'tree,form',
                'target': 'current',
                'context': {'create': True, 'delete': False}

            }
        else:
            exist = self.env['securo.notify'].search([('company_id', '=', self.env.company.id)])
            if exist:
                return {
                    'name': 'Configurazione notifiche',
                    'type': 'ir.actions.act_window',
                    'res_model': 'securo.notify',
                    'view_mode': 'form',
                    'target': 'current',
                    'res_id': exist.id,

                }
            else:
                return {
                    'name': 'Configurazione notifiche',
                    'type': 'ir.actions.act_window',
                    'res_model': 'securo.notify',
                    'view_mode': 'form',
                    'target': 'current',
                    'context': {},

                }
