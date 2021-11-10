
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

    #video_url = fields.Char('Video URL', help="URL of a video for showcasing your student.")
    #embed_code = fields.Char(compute="_compute_embed_code")

    #@api.depends('video_url')
    #def _compute_embed_code(self):
     #   for rec in self:
      #      rec.embed_code = get_video_embed_code(rec.video_url)
