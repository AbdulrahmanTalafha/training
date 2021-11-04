from odoo import models, fields, api,exceptions
class school(models.Model):
    _name = 'school'
    name = fields.Char()

