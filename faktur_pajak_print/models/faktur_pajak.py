from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import random

class FakturPajak(models.Model):
    _inherit = 'faktur.pajak'

    name = fields.Char('Name')

    def compute_invoices(self):
        for doc in self:
            # search_query = []
            search_query = [('state', '=', 'open')]
            invoice_docs = self.env['account.invoice'].search(search_query, limit=5)
            doc.view_invoice_ids = invoice_docs

    view_invoice_ids = fields.One2many('account.invoice', 'pajak_id', 'View Invoices', compute=compute_invoices)

    def get_array(self):
        temp_array = []
        search_query = [('state', '=', 'open')]
        random_offset = random.randint(1, 6)
        invoice_docs = self.env['account.invoice'].search(search_query, limit=5, offset=random_offset)
        for invoice_doc in invoice_docs:
            value = {
                'name': invoice_doc.number,
                'amount': invoice_doc.amount_total,
            }
            temp_array.append(value)
        return temp_array

    def get_invoices(self):
        temp_array = []
        search_query = [('state', '=', 'open')]
        random_offset = random.randint(1, 6)
        invoice_docs = self.env['account.invoice'].search(search_query, limit=5, offset=random_offset)
        return invoice_docs


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    pajak_id = fields.Many2one('faktur.pajak', 'Related Pajak')
