from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import random

class ExampleOrm(models.Model):
    _inherit = 'example.orm'

    records_to_add = fields.Integer('Records to Add', default=2)

    def new_records(self):
        temp_array = []


        # Basic If Conditional
        if self.name:
            temp_name = self.name
        else:
            temp_name = 'Logitech'

        # One Liner
        temp_name = self.name if self.name else 'Logitech'


        for i in range(0, self.records_to_add):
            value = {
                'detail': 'Kelipatan %s by %s' % (self.records_to_add, temp_name),
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
            import ipdb; ipdb.set_trace()
            baris_pertama_doc = self.line_ids[-1]
            self.line_ids.sorted(lambda x: x.amount)
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
        line_obj = self.env['example.orm.line']
        search_query = [
            ('example_id','=',False),
            ]
        nganggur_docs = self.env['example.orm.line'].search(search_query)

        # Alternative 1
        for nganggur_doc in nganggur_docs:
            nganggur_doc.example_id = self.id

        # Alternative 2
        self.line_ids |= nganggur_docs
