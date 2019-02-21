from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class FakturPajak(models.Model):
    _inherit = 'faktur.pajak'

    filter_invoice = fields.Text('Filter Invoice',)
    is_valid = fields.Boolean('Is Valid')

    @api.onchange('filter_invoice')
    def validate_form(self):
        filter_invoice = self.filter_invoice

        ## A. Validasi Karakter
        if '*' in filter_invoice:
            self.is_valid = False
            self.invoice_id = False
            return {
                'warning': {
                    'title': 'Karakter Error',
                    'message': 'Tidak boleh ada *',
                }
            }
        elif '/' in filter_invoice:
            self.is_valid = False
            self.invoice_id = False
            return {
                'warning': {
                    'title': 'Karakter Error',
                    'message': 'Tidak boleh ada /'
                }
            }

        ## B. Jika benar, apply Domain pada Invoice
        self.is_valid = True
        return {
            'domain': {
                'invoice_id': [('number', 'like', filter_invoice)],
            }
        }
