{
    'name': 'Example Api One Multi',
    'version': '11.1.0',
    'author': 'PT Arkana',
    'license': 'OPL-1',
    'category': 'Tailor-Made',
    'website': 'http: //www.arkana.co.id/',
    'summary': 'Custom-built Odoo',
    'description': '''
    ''',
    'depends': [
        'faktur_pajak',
        'faktur_pajak_filter',
    ],
    'data': [
        'views/faktur_pajak.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}