from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class FakturPajak(models.Model):
    _inherit = 'faktur.pajak'

    invoice_id = fields.Many2one('account.invoice', 'Invoice Terkait')
    date_reserved = fields.Datetime(string='Date Reserved')
