# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<https://www.cybrosys.com>)
#    Author: Vishnu KP(<https://www.cybrosys.com>)
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
    """Used to add new fields to the settings"""
    _inherit = "res.config.settings"

    customer_details = fields.Boolean(string=" Customer Details",
                                      help="By Enabling the customer details"
                                           " in pos receipt",
                                      config_parameter="pos_receipt_extend.customer_details")
    customer_name = fields.Boolean(string=" Customer Name",
                                   help="By Enabling the customer name "
                                        "in pos receipt",
                                   config_parameter="pos_receipt_extend.customer_name")
    customer_address = fields.Boolean(string=" Customer Address",
                                      help="By Enabling the customer Address "
                                           "in pos receipt",
                                      config_parameter="pos_receipt_extend.customer_address")
    customer_mobile = fields.Boolean(string=" Customer Mobile",
                                     help="By Enabling the customer mobile "
                                          "in pos receipt",
                                     config_parameter="pos_receipt_extend.customer_mobile")
    customer_phone = fields.Boolean(string=" Customer Phone",
                                    help="By Enabling the customer phone "
                                         "in pos receipt",
                                    config_parameter="pos_receipt_extend.customer_phone")
    customer_email = fields.Boolean(string=" Customer Email",
                                    help="By Enabling the customer email "
                                         "in pos receipt",
                                    config_parameter="pos_receipt_extend.customer_email")
    customer_vat = fields.Boolean(string=" Customer Vat",
                                  help="By Enabling the customer vat details "
                                       "in pos receipt",
                                  config_parameter="pos_receipt_extend.customer_vat")
    hide_tracking = fields.Boolean(string=" Hide Tracking number",
                                  help="Hide tracking number "
                                       "in pos receipt",
                                  config_parameter="pos_receipt_extend.hide_tracking")
