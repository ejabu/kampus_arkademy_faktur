from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import random

class ExampleOrm(models.Model):
    _inherit = 'example.orm'

    records_to_add = fields.Integer('Records to Add', default=2)

    def new_records(self):
        temp_array = []
        for i in range(0, self.records_to_add):
            value = {
                'detail': 'Kelipatan %s by %s' % (self.records_to_add, self.name),
                'amount': random.randint(1, 6) * 1000,
            }
            temp_array.append((0, 0, value))

        self.write({
            'line_ids' : temp_array
        })

    def break_one_record(self):
        line_docs = self.line_ids
        if line_docs:
            baris_pertama_doc = line_docs[0]
            baris_pertama_doc.example_id = False

    def delete_one_record(self):
        line_docs = self.line_ids
        if line_docs:
            baris_pertama_doc = self.line_ids[0]
            self.write({
                'line_ids': [
                    (3, baris_pertama_doc.id)
                    ],
            })

    def break_all_record(self):
        line_docs = self.line_ids
        for line_doc in line_docs:
            line_doc.example_id = False

    def link_one_record(self):
        search_query = [('example_id', '=', False)]
        line_doc = self.env['example.orm.line'].search(search_query, limit=1)
        if not line_doc:
            raise UserError('Line sudah ke link semua')
        self.write({
            'line_ids': [(4, line_doc.id)]
        })

    
    def link_all__nganggur_record(self):
        import ipdb; ipdb.set_trace()
        # It's your job to do it!

    