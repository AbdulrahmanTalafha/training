from odoo import models, fields, api,exceptions
class training(models.Model):
    _name = 'training'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Training'
    
    name = fields.Char(string="Name", required=True)
    age = fields.Selection([
        ("tt", "22"),
        ('ee', '33'),
        ('rr' ,'44'),
    ], string ="Age", default="tt")
    gender = fields.Selection([
        ("male", "Male"),
        ('female', 'Female'),
        ('other' ,'Other'),
    ], string ="Gender", default="male")
    image = fields.Binary(string="image")

