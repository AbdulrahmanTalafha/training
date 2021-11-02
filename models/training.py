from odoo import models, fields, api,exceptions
class training(models.Model):
    _name = 'training'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ("male", "Male"),
        ('female', 'Female'),
        ('other' ,'Other'),
    ], string ="Gender", default="male")
    image = field.Binary(string="image")

