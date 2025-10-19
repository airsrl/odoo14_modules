# -*- coding: utf-8 -*-
from odoo import models, fields
import datetime
import logging

_logger = logging.getLogger(__name__)


class HrRecruitmentStage(models.Model):
    _inherit = 'hr.recruitment.stage'

    cron_activities_ids = fields.One2many(
        comodel_name='hr.recruitment.stage.cron.activities',
        inverse_name="stage_id"
    )
    last_update_max_stage_yellow_warning = fields.Integer(
        "Max hours yellow color"
    )
    last_update_max_stage_red_warning = fields.Integer(
        "Max hours red color"
    )

    def cron_create_activities(self):
        try:
            hr_applicant_list = self.env['hr.applicant'].search([('kanban_state', '!=', 'blocked')])
            res_model_id = self.env['ir.model'].search([('model', '=', 'hr.applicant')]).id

            activity_data = []
            for applicant in hr_applicant_list:

                for cron_activity in applicant.stage_id.cron_activities_ids:
                    activity_type_id = cron_activity.activity_type_id

                    if applicant.date_last_stage_update > fields.datetime.utcnow() + datetime.timedelta(hours=cron_activity.cron_hours_trigger * -1):
                        continue

                    # check if the activity already exists
                    activity = self.env['mail.activity'].search(
                        [
                            ('res_model_id', '=', res_model_id),
                            ('res_id', '=', applicant.id),
                            ('activity_type_id', '=', activity_type_id.id),
                            ('user_id', '=', applicant.user_id.id)
                        ]
                    )

                    # if the activity does not exist
                    if not activity and activity_type_id.id not in applicant.created_cron_activity_type_ids.mapped('id'):
                        activity_data.append(
                            {
                                'summary': activity_type_id.summary,
                                'note': activity_type_id.default_description,
                                'res_id': applicant.id,
                                'user_id': applicant.user_id.id,
                                'date_deadline': fields.datetime.utcnow(),
                                'res_model_id': res_model_id,
                                'activity_type_id': activity_type_id.id
                            }
                        )
                        applicant.write({'created_cron_activity_type_ids': [(4, activity_type_id.id, 0)]})

            _logger.info(f'Creating {len(activity_data)} activities.')
            self.env['mail.activity'].create(activity_data)

        except Exception as ex:
            _logger.exception(ex)
            pass


class HrRecruitmentStageCronActivities(models.Model):
    _name = 'hr.recruitment.stage.cron.activities'
    _description = 'HR Recruitment stage cron activities'

    stage_id = fields.Many2one(
        comodel_name='hr.recruitment.stage',
        required=True
    )
    activity_type_id = fields.Many2one(
        comodel_name='mail.activity.type',
        required=True
    )
    cron_hours_trigger = fields.Integer(
        string="Hours",
        required=True
    )
