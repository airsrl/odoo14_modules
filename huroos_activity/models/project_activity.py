# -*- coding: utf-8 -*-
# Powered by Federico Ranieri.
# Part of Huroos. See LICENSE file for full copyright and licensing details.
# © 2022 Huroos Srl. (<https://www.huroos.com>).

import datetime

from odoo import models, fields, api


class ProjectActivity(models.Model):
    _name = 'project.activity'

    user_id = fields.Many2one('res.users', default=lambda self: self.env.user.id)
    date = fields.Date(default=lambda self: datetime.datetime.now().date())
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    task_id = fields.Many2one('project.task')
    project_id = fields.Many2one('project.project', related='task_id.project_id')
    project_color = fields.Integer('Project color', related='project_id.color')
    description = fields.Text(required=True)
    hour = fields.Float()
    manual = fields.Boolean()

    def name_get(self):
        result = []
        for record in self:
            name = record.description[:50]
            if record.project_id:
                name = record.project_id.name + ": " + name
            result.append((record.id, name))
        return result



