{
    'name': "Pharmacy",
    'version': '1.0',
    'category': 'Health',
    'summary': "Gestion des pharmacies et médicaments",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/pharmacy_views.xml',
        'views/medication_order_views.xml',
        'views/pharmacy_medicine_views.xml',
        'data/demo_data.xml',
        'data/medication_order_demo.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
