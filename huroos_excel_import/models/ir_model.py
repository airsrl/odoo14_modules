from odoo import api, models


class IrModel(models.Model):
    _inherit = "ir.model"

    def name_get(self):
        result = list()
        for record in self:
            result.append((record.id, f"{record.model}, {record.name}"))
        return result


class IrModelFields(models.Model):
    _inherit = "ir.model.fields"

    def name_get(self):
        result = list()
        for record in self:
            result.append((record.id, f"{record.name}, {record.field_description}"))
        return result

    # TODO: to fix. It returns duplicated records
    # @api.model
    # def name_search(self, name='', args=None, operator='ilike', limit=100):
    #     recs = self.search([('name', operator, name)])
    #     ids = [rec.id for rec in recs]
    #     return self.browse(ids).sudo().name_get()
