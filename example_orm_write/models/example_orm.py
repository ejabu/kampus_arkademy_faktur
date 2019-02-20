from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ExampleOrm(models.Model):
    _name = 'example.orm'
    # _rec_name = 'records_to_add'

    name = fields.Char('Header Title')
