from odoo import fields, models, api


class AccessWizard(models.TransientModel):
    _name = 'access.wizard'

    name = fields.Char()
    access_right=fields.Selection(
        [('_read','Read'),('_write','Write'),('_unlink','Delete'),('_create','Create')]
    )
    res_group_id=fields.Many2one(
        'res.groups'
    )
    text=fields.Char()

    remove=fields.Boolean()
    remove_all =fields.Boolean()
    def button_confirm(self):
        for rec in self:
            if rec.remove_all:
                rec.res_group_id.remove_rights_all()
            else:
                perm=f'perm{rec.access_right}'
                rec.res_group_id.give_rights_all(perm,rec.remove)
