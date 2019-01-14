from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class FakturPajak(models.Model):
    _inherit = 'faktur.pajak'

    reason = fields.Char(string='Kenapa di delete')

    @api.multi
    def cancel_diri_sendiri(self, reason):
        for faktur_doc in self:
            faktur_doc.reason = reason
            faktur_doc.invoice_id.faktur_id = False
            faktur_doc.invoice_id = False
            faktur_doc.date_reserved = False
