{
    'name': 'Faktur Pajak Batch Cancel',
    'version': '11.1.0',
    'author': 'PT Arkana',
    'license': 'OPL-1',
    'category': 'Tailor-Made',
    'website': 'http: //www.arkana.co.id/',
    'summary': 'Custom-built Odoo',
    'description': '''
        Next : Faktur Pajak di Cancel, ngelepas nomor Invoice.
        Dan Faktur ID di Invoice tersebut jg di cancel.
        
    ''',
    'depends': [
        'faktur_pajak_invoice',
    ],
    'data': [
        'wizard/faktur_cancel_wizard.xml',
    ],
    'qweb': [
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}