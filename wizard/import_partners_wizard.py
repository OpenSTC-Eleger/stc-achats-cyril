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

from osv import fields, osv
import base64
import csv
import StringIO

class openstc_import_partners_wizard(osv.osv_memory):
    _name = 'openstc.import.partners.wizard'
    _columns = {
        'csv_file':fields.binary('CSV file', required=True),
        'output_msg':fields.text('Informations', readonly=True),
        'csv_separator':fields.char('Separator', size=1, required=True),
        'csv_text_separator':fields.char('Text separator', size=1),
        'is_exhaustive':fields.boolean('is exhaustive', help="If set, Partners not found in the csv file will be deactivated (further imports can reactive them)"),
        'state':fields.selection([('wait','Wait'),('done','Done')], 'State', required=True),
        }
    _defaults = {
        'csv_separator':',',
        'csv_text_separator':'"',
        'is_exhaustive': lambda *a: False,
        'state':'wait',
        }
    
    """
    @note: launched by OpenERP button action on wizard
        perform update of res.partner table using supplied .csv file.
        Use partner.code_tiers as "External id" to synchronize data with following rules:
        - if code_tiers is found both on csv and db, update record (set 'name' and force 'active' to True)
        - elif code_tiers found in csv but not found in db, create record
        - elif code_tiers found in db but not found in csv file, deactivate record ('active' set to False) 
    """
    def import_partners(self, cr, uid, ids, context=None):
        partner_obj = self.pool.get('res.partner')
        for wizard in self.browse(cr, uid, ids, context=context):
            cpt_updated = 0
            cpt_created = 0
            cpt_removed = 0
            #retrieve all partners with a known code_tiers, store results in a dict, with code_tiers in a dict
            partner_ids = partner_obj.search(cr, uid, ['|',('code_tiers_ciril','!=',False),'&',('code_tiers_ciril','!=',False),('active','=',False)],context=context)
            #map_code_tiers_id store all actual code_tiers in db, 
            #if some keys stay in this dict after iterating csv file, means that remaining records must be deactivated
            map_code_tiers_id = {}
            for partner in partner_obj.read(cr, uid, partner_ids, ['code_tiers_ciril'],context=context):
                map_code_tiers_id.update({partner['code_tiers_ciril']:partner['id']})
            
            #Note: perhaps avoid to store data on variable, in case file is larger than max storage authorized by python console 
            csv_file = StringIO.StringIO(base64.decodestring(wizard.csv_file))
            #Note: I use str() to retrieve ascii code instead of unicode, csv library does not support unicode for its params
            read = csv.DictReader(csv_file, 
                          fieldnames=['code_tiers','name'],
                          delimiter=str(wizard.csv_separator), 
                          quotechar=str(wizard.csv_text_separator) and str(wizard.csv_text_separator) or '')
            read.next()
            #for each line, update database (create or update records)
            #if name is not present in file, write False by default to raise an openerp error (displayed to user by its own)
            for line in read:
                if line.get('code_tiers','') in map_code_tiers_id.keys():
                    #partner found, update him and remove code_tiers key from map_code_tiers_id
                    partner_obj.write(cr, uid, [map_code_tiers_id.pop(line.get('code_tiers'))], 
                                      {'name':line.get('name', False),'active':True},context=context) 
                    cpt_updated += 1
                else:
                    partner_obj.create(cr, uid, {'name':line.get('name',False),
                                                 'code_tiers_ciril':line.get('code_tiers')}, context=context)
                    cpt_created += 1
            #deactivate partner where ids remains on map_coe_tiers_id
            if map_code_tiers_id and wizard.is_exhaustive:
                cpt_removed = len(map_code_tiers_id.values()) 
                partner_obj.write(cr, uid, map_code_tiers_id.values(), {'active':False}, context=context)
            self.write(cr, uid, ids, 
                       {'state':'done', 'output_msg': 'updated: %s\ncreated: %s\ndeactivated: %s'% (str(cpt_updated),
                                                                                             str(cpt_created),
                                                                                             str(cpt_removed))}, context=context)
        return True
    
openstc_import_partners_wizard()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
