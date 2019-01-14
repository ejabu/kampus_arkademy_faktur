from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class ExampleOrmLine(models.Model):
    _name = 'example.orm.line'

    name = fields.Char('Struk Pembayaran')

    detail = fields.Char('Detail')

    amount = fields.Monetary('Amount')

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        default=lambda self: self.env.user.company_id.currency_id.id)
