
from odoo import models,fields,api,exceptions

class school(models.Model):
    _name = 'school'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    namee = fields.Char(string='Name')
    agee = fields.Integer(string='Age')
    genderr = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default="Male")
    imagee = fields.Binary(string='Image')
