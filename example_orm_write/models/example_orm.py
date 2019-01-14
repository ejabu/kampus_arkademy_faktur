from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ExampleOrm(models.Model):
    _name = 'example.orm'

    name = fields.Char('Header Title')
