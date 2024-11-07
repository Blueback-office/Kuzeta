# -*- coding: utf-8 -*-
from odoo import models
from odoo.http import request
from odoo import http

class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()
        cids = request.httprequest.cookies.get('cids')
        company_ids = list(map(int, cids.split(',')))
        first_company_id = company_ids[0]
        company_id = self.env['res.company'].sudo().search([('id', '=', first_company_id)])
        result['user_companies']['color'] = company_id.navbar_color
        return result