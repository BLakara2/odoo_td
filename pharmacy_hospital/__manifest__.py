{
    'name': "Pharmacy Hospital",
    'version': '1.0',
    'category': 'Health',
    'summary': "Extension pour intégrer pharmacie & hôpital",
    'depends': ['hospital', 'hospital_doctor', 'pharmacy'],
    'data': [
        'security/ir.model.access.csv',
        'views/prescription_views.xml',
        'views/patient_inherit.xml',
        'data/demo_data.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
