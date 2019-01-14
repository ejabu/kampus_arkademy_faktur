from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import random

class ExampleOrm(models.Model):
    _inherit = 'example.orm'

    records_to_add = fields.Integer('Name', default=2)

    @api.one
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
        return
