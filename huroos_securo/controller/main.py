from odoo import http
from odoo.http import request
from werkzeug.urls import url_encode
import zipfile,base64
from io import BytesIO
import werkzeug


class DownloadZipFile(http.Controller):
    @http.route("/download_attachments/", type="http", auth="user", website=True)
    def download_attachments_product_routes(self, **data):
        if data.get('res_model',False) and data.get('res_model') == 'hr.employee':
            employee_id = request.env['hr.employee'].sudo().search([('id', '=', data.get('res_id'))])
            general_attachment = employee_id.attachment
            in_memory = BytesIO()
            zip_archive = zipfile.ZipFile(in_memory, "w")
            for gen_att in general_attachment:
                zip_archive.writestr( f"FILE GENERALI/{gen_att.name}",
                                  base64.b64decode(gen_att.datas))
            formazione_attachment_ids = employee_id.employee_course_ids.mapped('attestato')
            for form_att in formazione_attachment_ids:
                zip_archive.writestr(f"Corsi e formazione/{form_att.name}",
                                     base64.b64decode(form_att.datas))
            visit_attachment_ids = employee_id.employee_medical_ids.mapped('document_ids')
            for visit_att in visit_attachment_ids:
                zip_archive.writestr(f"Visite mediche/{visit_att.name}",
                                     base64.b64decode(visit_att.datas))
            exam_attachment_ids = employee_id.employee_medical_ids.exam_ids.mapped('document_ids')
            for exam_att in exam_attachment_ids:
                zip_archive.writestr(f"Esami/{exam_att.name}",
                                     base64.b64decode(exam_att.datas))
            zip_archive.close()
            res = http.send_file(in_memory, filename=f"Doc_{employee_id.name}.zip", as_attachment=True)
            return res



