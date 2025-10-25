from odoo import fields, models, api
from datetime import datetime,date,timedelta
import base64
from odoo.exceptions import UserError

class AccountCommonReport(models.TransientModel):
    _inherit = 'account.common.report'


    def automatic_check_report(self):
        vals={}
        config_sudo = self.env['res.config.settings'].sudo()

        intervallo = config_sudo.get_values()['intervallo']
        intervallo = int(intervallo) if intervallo else 0

        date_to = date.today()
        date_from = date_to - timedelta(days=intervallo)
        company_id =config_sudo.get_values()['company_id']
        company_id = int(company_id) if company_id else self.env.company.id
        journal_ids =config_sudo.get_values()['journal_ids']

        target_move = config_sudo.get_values()['target_move']
        target_move = target_move if target_move else 'posted'
        vals['date_from'] = date_from
        vals['date_to'] = date_to
        vals['journal_ids'] = journal_ids
        vals['company_id'] = company_id
        vals['target_move'] = target_move
        #vals['amount_currency']= False
        vals['sort_selection']= 'move_name'

        new= self.env['account.print.journal'].create(vals)
        pdf =new.check_report()
        pdf_down = self.env.ref('account.action_report_journal').with_context(landscape=True).sudo()._render_qweb_pdf(new.ids,data=pdf['data'])
        b64_pdf = base64.encodestring(pdf_down[0])
        template = int(config_sudo.get_values()['template_registri_id']) or False
        destinatari = config_sudo.get_values()['destinatari'] or ''
        # save pdf as attachment
        name = pdf['name']
        attch= self.env['ir.attachment'].create({
            'name': name + '.pdf',
            'type': 'binary',
            'datas': b64_pdf,
            'store_fname': name,
            'mimetype': 'application/x-pdf'
        })
        allegato = attch.ids
        return self.invio_email(template=template,res_id=new.id,destinatari=destinatari,allegato=allegato)


    def invio_email(self, template, res_id, destinatari,allegato=False):
        if not template:
            raise UserError('Impostare un template')


        template = self.env['mail.template'].browse(int(template))
        smtp = template.mail_server_id
        fields={}
        fields['mail_server_id'] = smtp.id
        fields['email_from'] = smtp.smtp_user

        fields['email_to'] = destinatari
        create_values = template.generate_email(res_id,fields)


        mail = self.env['mail.mail'].create(create_values)
        mail.subject = template.subject
        mail.body_html= template.body_html
        mail.email_to = destinatari
        if not mail.attachment_ids:
            for att in allegato:
                mail.attachment_ids = [(4, att)]

        mail.send()