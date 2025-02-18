{
    'name': 'ip_visitor_tracking',
    'version': '1.0',
    'summary': 'Información sobre la geolocalización de los usuarios',
    'description': 'Obtención de información geolocalizada de los visitantes.',
    'author': 'Emilio Neva',
    'category': 'Website',
    'depends': ['base'],
    'data': [
    'security/ir.model.access.csv',
    'views/visitor_tracking_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'icon': '/ip_visitor_tracking/static/description/icon58.png',
}
