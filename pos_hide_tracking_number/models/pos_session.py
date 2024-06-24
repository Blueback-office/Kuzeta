# -*- coding: utf-8 -*-
#############################################################################
#
#    Caribbean Data Challengers
#
#    Copyright (C) 2024-TODAY Caribbean Data Challengers(<https://www.cdc.aw>)
#    Author: Toon van der Ploeg
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
from odoo import models

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        # Extends the list of models to be loaded in the POS UI
        result = super()._pos_ui_models_to_load()
        result.append('res.config.settings')
        return result

    def _loader_params_res_config_settings(self):
        # Specifies fields from res.config.settings to be loaded in the POS UI
        return {
            'search_params': {
                'fields': [
                    'hide_tracking_number',
                    'receipt_details'
                ],
            },
        }

    def _get_pos_ui_res_config_settings(self, params):
        # Fetches configuration settings based on specified parameters
        return self.env['res.config.settings'].sudo().search_read(
            **params['search_params'])