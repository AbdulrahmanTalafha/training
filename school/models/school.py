
from odoo import models,fields,api,exceptions

class school(models.Model):
    _name = 'school'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default="Male")
    imagee = fields.Binary(string='Image')
