# -*- coding: utf-8 -*-
##############################################################################
#
#    Openstc Achat Ciril module for OpenERP, Description
#    Copyright (C) 200X Company (<http://website>) author
#
#    This file is a part of Openstc Achat Ciril
#
#    Openstc Achat Ciril is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Openstc Achat Ciril is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "openstc_achat_stock",
    "version": "0.1",
    "depends": ["openstc_achat_stock"],
    "author": "SICLIC",
    "category": "SICLIC",
    "description": """
    This module is used to be able to synchronize with Civil-Net-Finances (created by CIRIL).
    Update Partners according to CIRIL exported csv file
    Push .txt files to a remote server of CIRIL to create engages on Civil-Net-Finances
    """,
    "data": [
             "wizard/import_partners_wizard_view.xml"
             ],
    "init_xml":[],
    "demo": [],
    "test": [],
    "installable": True,
    "active": False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
