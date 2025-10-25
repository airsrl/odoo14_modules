from odoo import fields, models, api
from ast import literal_eval


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    journal_ids = fields.Many2many('account.journal', string='Journals', required=True,
        default=lambda self: self.env['account.journal'].search([('company_id', '=', self.company_id.id)]))
    intervallo = fields.Integer(string='Giorni',
        help="intervallo tra due date in gg, la data di partenza è quella corrente", default=1)

    target_move = fields.Selection([('posted', 'All Posted Entries'),
                                    ('all', 'All Entries'),
                                    ], string='Target Moves', required=True, default='posted')

    destinatari = fields.Text('Destinatari')
    template_registri_id = fields.Many2one('mail.template','Template')
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        icp_sudo = self.env['ir.config_parameter'].sudo()
        icp_sudo.set_param('register_email.journal_ids', self.journal_ids.ids)
        icp_sudo.set_param('register_email.company_id',self.company_id.id)
        icp_sudo.set_param('register_email.target_move',self.target_move)
        icp_sudo.set_param('register_email.intervallo',self.intervallo)
        icp_sudo.set_param('register_email.destinatari', self.destinatari)
        icp_sudo.set_param('register_email.template_registri_id', self.template_registri_id.id)


    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        icp_sudo = self.env['ir.config_parameter'].sudo()
        journal_ids = icp_sudo.get_param('register_email.journal_ids')
        if journal_ids:
            # if len(list(assign_approver_ids)) > 1:
            #     res.update({'assign_approver_ids': [(6, 0, literal_eval(assign_approver_ids))]})
            res.update({'journal_ids': [(6, 0,literal_eval(journal_ids))]})
        else:
            res.update({
                'journal_ids': [(6, 0, [])]
            })
        res.update({
            'company_id':int(icp_sudo.get_param('register_email.company_id')),
            'target_move':icp_sudo.get_param('register_email.target_move'),
            'intervallo':int(icp_sudo.get_param('register_email.intervallo')),
            'destinatari': icp_sudo.get_param('register_email.destinatari'),
            'template_registri_id': int(icp_sudo.get_param('register_email.template_registri_id')),
        })
        return res



