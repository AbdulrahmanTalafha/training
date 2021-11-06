from typing_extensions import Required
from odoo import models,fields,api,exception

class school(models.Model):
    _name = 'school'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'School'

    name = fields.Char(string='Name')
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male')
        ('female', 'Female')
        ('other', 'Other')
    ], string='Gender', default="Male")
    image = fields.Binary(string='Image')
