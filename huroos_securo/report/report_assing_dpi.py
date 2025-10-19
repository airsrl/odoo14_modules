
from odoo import api, models
from datetime import datetime


class ReportConsegnaDpi(models.AbstractModel):
    _name = "report.huroos_securo.report_consegna_dpi"
    _description = "Report consegna dpi"

    @api.model
    def _get_report_values(self, docids, data=None):
        # docids required by caller but not used
        docargs = {
            "doc_ids": [],
            "doc_model": [],
            "employee_ids": data["employee_ids"],

            "assign_date": datetime.strptime(data['assign_date'], '%Y-%m-%d').date().strftime("%A %d %B %Y"),
            "company" :self.env.company,
            "env": self.env,

        }
        return docargs
