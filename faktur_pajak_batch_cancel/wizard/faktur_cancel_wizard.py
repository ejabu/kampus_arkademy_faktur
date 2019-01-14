from datetime import datetime, date
from odoo import fields, models, api, _

class FakturCancelWizard(models.TransientModel):

    _name = 'faktur.cancel.wizard'

    name = fields.Char('Name')

    def process_wizard(self):
        ids_to_change = self._context.get('active_ids')
        active_model = self._context.get('active_model')
        doc_ids = self.env[active_model].browse(ids_to_change)
        reason = self.name
        doc_ids.cancel_diri_sendiri(reason)
