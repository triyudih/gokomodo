{
    'name': 'Gokomodo Test',
    'version': '14.0',
    'author': 'TYH',
    'license': 'OPL-1',
    'category': 'Tailor-Made',
    'website': '',
    'summary': 'Custom-built Odoo',
    'description': '''
    ''',
    'depends': ['sale','account'
    ],
    'data': [
       'views/sale_order_view.xml',
       'security/ir.model.access.csv',
       'data/tax_data.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}