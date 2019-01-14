{
    'name': 'Faktur Pajak Invoice',
    'version': '11.1.0',
    'author': 'PT Arkana',
    'license': 'OPL-1',
    'category': 'Tailor-Made',
    'website': 'http: //www.arkana.co.id/',
    'summary': 'Custom-built Odoo',
    'description': '''
    ''',
    'depends': [
        'account', # python
        'faktur_pajak', # python
    ],
    'data': [
        'views/faktur_pajak.xml',
        'views/account_invoice.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}