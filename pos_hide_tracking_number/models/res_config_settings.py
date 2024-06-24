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
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """
    Inherits res.config.settings to add new fields related to POS receipt customization.
    
    Adds a boolean field to enable or disable details on POS receipts.
    """
    _inherit = "res.config.settings"

    # Field to enable/disable details on POS receipts
    receipt_details = fields.Boolean(
        string="Receipt Details",
        help="""Enable this option to show or hide details on POS receipts.""",
        config_parameter="pos_receipt_extend.receipt_details"
    )
     hide_tracking_number = fields.Boolean(
        string="Hide Order Tracking number",
        help="""Enable this hide the large tracking number on POS receipts.""",
        config_parameter="pos_receipt_extend.hide_tracking_number"
    )