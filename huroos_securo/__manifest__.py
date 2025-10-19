# -*- coding: utf-8 -*-
{
    'name': "Huroos SecurO",
    'summary': "SecurO app.",
     'author': "Huroos srl",
    'web': "www.huroos.com",
    'images': ['static/description/icon.png'],
    'website': 'https://huroos.com',

    'version': '14.0.9',
    'depends': ['base', 'fleet','maintenance','hr','l10n_it_fiscalcode','mail','documents_hr'],
    "qweb": ["static/src/xml/button_tree_assign_dpi.xml"],
    'data': [
        'data/cron_securo_notify.xml',
        'data/email_template.xml',
        'data/securo.vehicle.type.csv',
        'data/hr_fold.xml',

        'report/employee_badge.xml',
        'report/report_consegna_dpi.xml',
        'report/report_dpi.xml',
        'report/report_consegna_badge.xml',

        'views/assets.xml',
        'views/main_menu.xml',
        'views/securo_accident.xml',
        'views/securo_employee_qualification.xml',
        'views/securo_employee_duty.xml',
        'views/hr_employee.xml',
        'views/maintenance.xml',
        'views/hr_employee.xml',
        'views/securo_work_environment.xml',
        'views/securo_dpi.xml',
        'views/securo_course_training.xml',
        'views/securo_dpi_size.xml',
        'views/fleet_vehicle.xml',
        'views/res_partner.xml',
        'views/securo_dpi_employee.xml',
        'views/securo_employee_course.xml',
        'views/occupational_medicine.xml',
        'views/occupational_medicine_periodicity.xml',
        'views/occupational_medicine_employee.xml',
        'views/securo_single_employee_course.xml',
        'views/exam_employee_result.xml',
        'views/res_company.xml',
        'views/securo_notify.xml',
        'views/securo_document_type.xml',
        'views/fleet_vehicle_model.xml',

        'wizard/wizard_assign_course.xml',
        'wizard/wizard_assign_dpi.xml',
        'wizard/wizard_print_dpi_empl.xml',

        'security/ir.model.access.csv',
        'security/securo_security.xml'
    ]

}