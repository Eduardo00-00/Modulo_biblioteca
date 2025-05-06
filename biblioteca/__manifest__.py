{
    'name': 'Biblioteca',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Tu Nombre',
    'category': 'Herramientas',
    'description': 'Gestión de libros en una biblioteca',
    'data': [
        'security/ir.model.access.csv',
        'views/libro_views.xml',
    ],
    'installable': True,
    'application': True,
}
