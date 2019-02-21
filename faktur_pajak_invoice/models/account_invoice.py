from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    faktur_id = fields.Many2one('faktur.pajak', 'Faktur Terkait')

    def get_faktur_pajak(self):
        search_query = [('invoice_id', '=', False)]

        faktur_doc = self.env['faktur.pajak'].search(search_query, limit=1)

        self.faktur_id = faktur_doc.id
        faktur_doc.invoice_id = self.id

        # self.write({
        #     'faktur_id': faktur_doc.id,
        # })

        current_time = fields.Datetime.now()

        faktur_doc.write({
            'invoice_id': self.id,
            'date_reserved': current_time,
        })

    @api.multi
    def action_invoice_open(self):
        result = super(AccountInvoice, self).action_invoice_open()
        for invoice_doc in self:
            invoice_doc.get_faktur_pajak()
        return result

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        recs = self.browse()
        if name:
            recs = self.search([('number', 'ilike', name)] + args, limit=limit)
        if not recs:
            recs = self.search([] + args, limit=limit)
        return recs.name_get()
