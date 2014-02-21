# -*- coding: utf-8 -*-

##############################################################################
#    Copyright (C) 2012 SICLIC http://siclic.fr
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#############################################################################

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
