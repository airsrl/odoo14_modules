# -*- coding: utf-8 -*-
{
    'name': "Huroos holidays extend",
    'summary': "Adds feature in time-off apps.",
     'author': "Huroos srl",
    'web': "www.huroos.com",
    'images': ['static/description/icon.png'],
    'website': 'https://huroos.com',

    'version': '14.0.1.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_holidays'],
    # always loaded
    'data': [
        'views/hr_leave_report.xml'
    ]

}