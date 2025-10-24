from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    cg_url = fields.Char(string='URL API Computer Gross')
    cg_user = fields.Char(string='User API Computer Gross')
    cg_password = fields.Char(string='Password API Computer Gross')

    an_url = fields.Char(string='URL FTP AllNet')
    an_user = fields.Char(string='User FTP AllNet')
    an_password = fields.Char(string='Password FTP AllNet')

    td_url = fields.Char(string='URL FTP Techdata')
    td_user = fields.Char(string='User FTP Techdata')
    td_password = fields.Char(string='Password FTP Techdata')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        icp_sudo = self.env['ir.config_parameter'].sudo()

        icp_sudo.set_param('ambient7_custom.cg_url', self.cg_url)
        icp_sudo.set_param('ambient7_custom.cg_user', self.cg_user)
        icp_sudo.set_param('ambient7_custom.cg_password', self.cg_password)

        icp_sudo.set_param('ambient7_custom.an_url', self.an_url)
        icp_sudo.set_param('ambient7_custom.an_user', self.an_user)
        icp_sudo.set_param('ambient7_custom.an_password', self.an_password)

        icp_sudo.set_param('ambient7_custom.td_url', self.td_url)
        icp_sudo.set_param('ambient7_custom.td_user', self.td_user)
        icp_sudo.set_param('ambient7_custom.td_password', self.td_password)

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        icp_sudo = self.env['ir.config_parameter'].sudo()
        res.update({
            'cg_url': icp_sudo.get_param('ambient7_custom.cg_url'),
            'cg_user': icp_sudo.get_param('ambient7_custom.cg_user'),
            'cg_password': icp_sudo.get_param('ambient7_custom.cg_password'),

            'an_url': icp_sudo.get_param('ambient7_custom.an_url'),
            'an_user': icp_sudo.get_param('ambient7_custom.an_user'),
            'an_password': icp_sudo.get_param('ambient7_custom.an_password'),

            'td_url': icp_sudo.get_param('ambient7_custom.td_url'),
            'td_user': icp_sudo.get_param('ambient7_custom.td_user'),
            'td_password': icp_sudo.get_param('ambient7_custom.td_password')
        })
        return res
