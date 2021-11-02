from odoo import models, fields, api,exceptions
class school(models.Model):
    _name = 'school'
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ("male", "Male"),
        ('female', 'Female'),
        ('other' ,'Other'),
    ], string ="Gender", default="male")

