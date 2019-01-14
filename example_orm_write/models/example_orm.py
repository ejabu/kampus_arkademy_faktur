from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ExampleOrm(models.Model):
    _name = 'example.orm'

    name = fields.Char('Name')


    # Perhatian nama recompute sudah digunakan Odoo
    @api.one
    def baca_ulang(self):
        import ipdb; ipdb.set_trace()
        abc = 3
        return
    
