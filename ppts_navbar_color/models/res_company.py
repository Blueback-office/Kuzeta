from odoo import api, fields, models

class ResCompany(models.Model):
    _inherit = "res.company"

    company_colors = fields.Serialized()
    navbar_color = fields.Char(string="NavBar Color", sparse="company_colors")