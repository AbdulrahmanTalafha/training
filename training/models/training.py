from odoo import models, fields, api,exceptions
class training(models.Model):
    _name = 'training'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Training'
    
    name = fields.Char(string = "Name", required = True)
    age = fields.Integer(string="Age" , required = True)
    gender = fields.Selection([
        ("male", "Male"),
        ('female', 'Female'),
        ('other' ,'Other'),
    ], string ="Gender", default = "male")
    image = fields.Binary(string = "image")
    active = fields.Boolean(string='Active',default=True)

