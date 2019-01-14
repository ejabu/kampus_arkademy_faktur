from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class FakturPajak(models.Model):
    _inherit = 'faktur.pajak'

    # @api.multi
    # def cancel_diri_sendiri(self):
        # import ipdb; ipdb.set_trace()
        # for faktur_doc in self:
        #     faktur_doc.invoice_id.faktur_id = False
        #     faktur_doc.invoice_id = False
        #     faktur_doc.date_reserved = False

    @api.multi
    def cancel_diri_sendiri(self):
        self.invoice_id.faktur_id = False
        self.invoice_id = False
        self.date_reserved = False
