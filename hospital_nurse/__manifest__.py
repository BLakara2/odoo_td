{
    'name': 'Hospital Nurse',
    'version': '1.0',
    'summary': 'Gestion des infirmières et des rondes',
    'description': 'Module pour gérer les infirmières, rondes et suivi des patients hospitalisés',
    'author': 'Lakara',
    'depends': ['base', 'web', 'hospital'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_nurse_views.xml',
        'views/hospital_nurse_report.xml',
        'data/demo_data.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
