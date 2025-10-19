# -*- coding: utf-8 -*-
{
    'name': "Huroos HR stage auto activities",
    'summary': """Huroos HR stage auto activities""",
    'description': """Huroos HR stage auto activities""",
    'author': "Huroos SC - www.huroos.com",
    'website': "www.huroos.com",
    'category': 'Tools',
    'version': '14.0.1.0',
    'depends': ['base', 'hr_recruitment', 'mail'],
    'data': [
        'data/ir_cron.xml',

        'security/ir.model.access.csv',

        'views/hr_applicant.xml',
        'views/hr_recruitment_stage.xml'
    ]
}
