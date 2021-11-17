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
    date_from = fields.Datetime(string="From")
    date_to = fields.Datetime(string="To")
    active = fields.Boolean(string='Active',default=True)
    video_url = fields.Char('Video URL', help="URL of a video for showcasing your student.")
    embed_code = fields.Char(compute="_compute_embed_code")
    

    @api.depends('video_url')
    def _compute_embed_code(self):
        for rec in self:
            rec.embed_code = get_video_embed_code(rec.video_url)
    
    #@api.model
    #def name_get(self):
     #   res = []
      #  for rec in self:
       #     res.append((rec.id, '%s - %s' % (rec.name)))
        #return res

    #@api.model
    #def _name_search(self, name='', args=None, operator='ilike', limit=100):
     #   if args is None:
      #      args = []
       # domain = args + ["|", ('name', operator, name)]
        #return super(training, self).search(domain, limit=limit).name_get()
    
    #@api.model
    #def _namesearch(self, name, args=None, operator = "ilike", limit=100, name_get_uid=None):
     #   args=[]
      #  domain=[]
       # if name:
        #    domain=["|", ("name", operator, name)]
        #return self._search(domain + args, limit=limit, access_right_uid = name_get_uid)