{
    'name': "Huroos attendance geolocation",
    'summary': "Adds geolocation in attendance apps.",
     'author': "Huroos srl",
    'web': "www.huroos.com",
    'images': ['static/description/icon.png'],
    'website': 'https://huroos.com',

    'version': '14.0.2.0',
    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_attendance'],

    # always loaded
    'data': [
        'views/assets.xml',
        'views/hr_attendance.xml',
        'security/ir.model.access.csv'
    ],
    'qweb': [
        "static/src/xml/attendance.xml",
    ]

}