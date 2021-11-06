from odoo import models, fields, api,exceptions
class trainingg(models.Model):
    _name = 'training'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Training'
    
    name = fields.Char(string = "Name", required = True)
    agee = fields.Integer(string="Age")
    gender = fields.Selection([
        ("male", "Male"),
        ('female', 'Female'),
        ('other' ,'Other'),
    ], string ="Gender", default = "male")
    image = fields.Binary(string = "image")

