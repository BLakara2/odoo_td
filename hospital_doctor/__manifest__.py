{
    'name': 'Hospital Doctor',
    'version': '1.0',
    'summary': 'Manage doctors in the hospital',
    'description': 'Module to manage doctors in the hospital system',
    'category': 'Hospital',
    'depends': ['base','hospital'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_doctor_views.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'auto_install': False,
}
