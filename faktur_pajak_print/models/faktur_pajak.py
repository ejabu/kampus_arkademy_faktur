from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class FakturPajak(models.Model):
    _inherit = 'faktur.pajak'

    name = fields.Char('Name')

    def get_invoices(self):
        # search_query = []
        search_query = [('state', '=', 'open')]
        invoice_docs = self.env['account.invoice'].search(search_query, limit=5)
        self.view_invoice_ids = invoice_docs

    view_invoice_ids = fields.One2many('account.invoice', 'pajak_id', 'View Invoices', compute=get_invoices)


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    pajak_id = fields.Many2one('faktur.pajak', 'Related Pajak')
