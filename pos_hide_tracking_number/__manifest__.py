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
{
    'name': 'Remove Order Tracking Number',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Custom module to modify POS receipt header',
    'description': 'This module removes the tracking number from the POS receipt header.',
    'author': 'Caribbean Data Challengers',
    'depends': ['point_of_sale'],
    'data': [
        'views/assets.xml',
        'views/receipt_header.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
