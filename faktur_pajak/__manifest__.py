{
    'name': 'Faktur Pajak',
    'version': '11.1.0',
    'author': 'PT Arkana',
    'license': 'OPL-1',
    'category': 'Tailor-Made',
    'website': 'http: //www.arkana.co.id/',
    'summary': 'Custom-built Odoo',
    'description': '''
    ''',
    'depends': [
    ],
    'data': [
        # sSecurity
        'security/access_role.xml',
        'security/ir.model.access.csv',

        'views/faktur_pajak.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}
