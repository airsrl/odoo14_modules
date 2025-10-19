# -*- coding: utf-8 -*-
from odoo import models, fields
import datetime


class hr_applicant(models.Model):
    _inherit = 'hr.applicant'

    is_last_update_max_stage_red_warning = fields.Boolean(
        compute="_compute_is_last_update_max_stage_red_warning"
    )
    is_last_update_max_stage_yellow_warning = fields.Boolean(
        compute="_compute_is_last_update_max_stage_yellow_warning"
    )
    created_cron_activity_type_ids = fields.One2many(
        comodel_name="mail.activity.type",
        inverse_name="created_cron_hr_applicant_ids"
    )

    def write(self, vals):
        if 'stage_id' in vals:
            vals['created_cron_activity_type_ids'] = [(5, 0, 0)]
        res = super(hr_applicant, self).write(vals)
        return res

    def _compute_is_last_update_max_stage_red_warning(self):
        for rec in self:
            rec.is_last_update_max_stage_red_warning = rec.stage_id.last_update_max_stage_red_warning and \
                                                       rec.date_last_stage_update < fields.datetime.utcnow() + datetime.timedelta(hours=rec.stage_id.last_update_max_stage_red_warning * -1)

    def _compute_is_last_update_max_stage_yellow_warning(self):
        for rec in self:
            rec.is_last_update_max_stage_yellow_warning = rec.stage_id.last_update_max_stage_yellow_warning \
                                                          and not rec.is_last_update_max_stage_red_warning \
                                                          and rec.date_last_stage_update < fields.datetime.utcnow() + datetime.timedelta(hours=rec.stage_id.last_update_max_stage_yellow_warning * -1)


class MailActivityType(models.Model):
    _inherit = 'mail.activity.type'

    created_cron_hr_applicant_ids = fields.Many2one(
        comodel_name="hr.applicant",
        inverse_name="created_cron_activity_type_ids"
    )
