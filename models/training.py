from odoo import models, fields, api,exceptions
class training(models.Model):
    _name = 'training'
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ("male", "female")
        ('female', 'male')
        ('other' ,'Other')
    ], string ="Gender", default="male")

