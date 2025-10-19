from odoo import fields, models, api


class ResGroups(models.Model):
    _inherit = 'res.groups'

    perm_read=fields.Boolean('Read access')
    perm_create = fields.Boolean('Create access')
    perm_write=fields.Boolean('Write access')
    perm_unlink =fields.Boolean('Delete access')


    def remove_all_rights(self):

        context={'default_res_group_id':self.id,'default_remove_all':True,'default_text':'Confirm remove all the access rights ?'}

        return {
            "name": "Remove all rights",
            "view_mode": "form",
            "res_model": "access.wizard",
            "type": "ir.actions.act_window",
            "context": context,
            'target':'new'
            }
    def open_wizard_read(self):
        context={}
        if not  self.perm_read:
            context={'default_res_group_id':self.id,'default_access_right':'_read','default_text':'Confirm give Read access all?'}
        else:
            context={'default_res_group_id':self.id,'default_access_right':'_read','default_text':'Confirm remove Read access all?','default_remove':True}

        return {
            "name": "Access Rights",
            "view_mode": "form",
            "res_model": "access.wizard",
            "type": "ir.actions.act_window",
            "context": context,
            'target':'new'
            }
    def open_wizard_write(self):
        if not self.perm_write:
            context={'default_res_group_id':self.id,'default_access_right':'_write','default_text':'Confirm give Write access all?'}
        else:
            context={'default_res_group_id':self.id,'default_access_right':'_write','default_text':'Confirm remove Write access all?','default_remove':True}

        return {
            "name": "Assign Access Rights",
            "view_mode": "form",
            "res_model": "access.wizard",
            "type": "ir.actions.act_window",
            "context": context,
            'target': 'new'
        }
    def open_wizard_create(self):
        if not self.perm_create:
            context={'default_res_group_id':self.id,'default_access_right':'_create','default_text':'Confirm give Create access  all ?'}
        else:
            context={'default_res_group_id':self.id,'default_access_right':'_create','default_text':'Confirm remove Create access all?','default_remove':True}

        return {
            "name": "Assign Access Rights",
            "view_mode": "form",
            "res_model": "access.wizard",
            "type": "ir.actions.act_window",
            "context": context,
            'target': 'new'
        }
    def open_wizard_delete(self):
        if not self.perm_unlink:
            context={'default_res_group_id':self.id,'default_access_right':'_unlink','default_text':'Confirm give Delete access  all?'}
        else:
            context={'default_res_group_id':self.id,'default_access_right':'_unlink','default_text':'Confirm remove Delete access all?','default_remove':True}

        return {
            "name": "Assign Access Rights",
            "view_mode": "form",
            "res_model": "access.wizard",
            "type": "ir.actions.act_window",
            "context": context,
            'target': 'new'
        }
    def give_rights_all(self,perm,remove=False):
        for rec in self:
            if rec.model_access:
                if not remove:
                    rec.model_access.write({perm:True})
                    rec.write({perm:True})
                else:
                    rec.model_access.write({perm: False})
                    rec.write({perm: False})

    def remove_rights_all(self):
        for rec in self:
            if rec.model_access:
                rec.model_access.write({'perm_read': False,'perm_write':False,'perm_create':False,'perm_unlink':False})
            rec.write({'perm_read': False,'perm_write':False,'perm_create':False,'perm_unlink':False})