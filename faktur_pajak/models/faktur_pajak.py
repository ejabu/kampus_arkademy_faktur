from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class FakturPajak(models.Model):
    _name = 'faktur.pajak'

    name = fields.Char('Nomor')

    _sql_constraints = [
        ('nomor_faktur_harus_unique', 'unique(name)', 'Nomor Harus Unique !'),
    ]
