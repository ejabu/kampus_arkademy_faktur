{
    'name': 'Faktur Pajak Print',
    'version': '11.1.0',
    'author': 'PT Arkana',
    'license': 'OPL-1',
    'category': 'Tailor-Made',
    'website': 'http: //www.arkana.co.id/',
    'summary': 'Custom-built Odoo',
    'description': '''
    ''',
    'depends': [
        'account',
        'faktur_pajak_invoice',
    ],
    'data': [
        'print/faktur_pajak_print.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}