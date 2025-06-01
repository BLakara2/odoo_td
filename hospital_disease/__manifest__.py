{
    'name': 'Hospital Disease',
    'version': '1.0',
    'summary': 'Gestion des maladies dans l\'hôpital',
    'description': 'Module pour gérer les maladies, symptômes, gravité et actions finales.',
    'author': 'Lakara',
    'depends': ['hospital'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_disease_views.xml',
        #'views/menu_views.xml',
        'data/demo_data.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
