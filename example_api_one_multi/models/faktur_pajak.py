from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class FakturPajak(models.Model):
    _inherit = 'faktur.pajak'

    @api.one
    def clear_filter(self):
        import ipdb; ipdb.set_trace()
        self.filter_invoice = False

    @api.one
    def clear_filter_all(self):
        import ipdb; ipdb.set_trace()
        search_query = []
        faktur_docs = self.search(search_query, limit=2)
        faktur_docs.clear_filter()
        # faktur_docs.clear_filter_multi()

    # ------------------------------

    @api.multi
    def clear_filter_multi(self):
        import ipdb; ipdb.set_trace()
        for faktur_doc in self:
            faktur_doc.filter_invoice = False