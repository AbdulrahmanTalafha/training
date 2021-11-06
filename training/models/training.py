from odoo import models, fields, api,exceptions
from odoo.addons.website.tools import get_video_embed_code

class training(models.Model):
    _name = 'training'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Training'
    
    name = fields.Char(string = "Name", required = True)
    age = fields.Integer(string = "Age")
    gender = fields.Selection([
        ("male", "Male"),
        ('female', 'Female'),
        ('other' ,'Other'),
    ], string = "Gender", default = "male")
    image = fields.Binary(string = "image")
    active = fields.Boolean(string='Active',default=True)
    video_url = fields.Char('Video URL', help="URL of a video")
    embed_code = fields.Char(compute="_compute_embed_code")

    @api.depends('video_url')
    def _compute_embed_code(self):
        for rec in self:
            rec.embed_code = get_video_embed_code(rec.video_url)
