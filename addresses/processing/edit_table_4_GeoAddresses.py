#-------------------------------------------------------------------------------
# Name:     edit_table
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20170703
# Modified: 20170707
# Modified: 20180716 deleted ADDRESS2;PREDIR2;POSTDIR2;SUPPLEM2
#https://gis.stackexchange.com/questions/152481/how-to-delete-selected-rows-using-arcpy
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/"
#arcpy.env.workspace = "source/AddressData.gdb/"
fc = "GeoAddresses"

fields = ['NUMBER']
#delete records
with arcpy.da.UpdateCursor(fc,fields) as cursor:
    for row in cursor:
        #delete records with no number assigned
        if row[0] == '':  # and row[4] == 'Sleepy Hollow Beach Resort - Main Office, Delicatessen and Crafts Area':
            cursor.deleteRow()
        if row[0] == ' ':
            cursor.deleteRow()
        if row[0] == None:
            cursor.deleteRow()
arcpy.AddMessage("deleted addresses with no number or a space as a number")

fields = ['ADDRESS']
with arcpy.da.UpdateCursor(fc,fields) as cursor:
    for row in cursor:
        #delete specific addresses that cause problems for NewWorld system and Dispatch
        #if row[0] == '7400 North Shore Dr':
        if row[0] == 'Sleepy Hollow Beach Resort - Main Office, Delicatessen and Crafts Area':
            cursor.deleteRow()
            arcpy.AddMessage("deleted Sleepy Hollow Main office") #requested by Dispatch

fields = ['COUNTY','MUNI']
#create update cursor for County names
with arcpy.da.UpdateCursor(fc,fields) as cursor:
    for row in cursor:
        if row[0] == 'BARRY':
            row[1] = 'Barry Co'
        elif row[0] == 'CALHOUN':
            row[1] = 'Calhoun Co'
        elif row[0] == 'KALAMAZOO':
            row[1] = 'Kalamazoo Co'
        elif row[0] == 'KENT':
            row[1] = 'Kent Co'
        elif row[0] == 'OTTAWA':
            row[1] = 'Ottawa Co'
        elif row[0] == 'VAN BUREN':
            row[1] = 'Van Buren Co'
        cursor.updateRow(row)
    arcpy.AddMessage("updated surrounding counties in MUNI field")
arcpy.AddMessage("finished updateing surrounding counties")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "GeoAddresses"
arcpy.DeleteField_management(in_table="GeoAddresses", drop_field="ADDRESS;ADDRESS1;PROBLEM;NOTES;NUMBERSUP;NUMBERSUP1;SUPPLEMENT;COUNTY;BUSNAME;BUSSOURCE;A1RETIRED;ADDRESS2;PREDIR2;POSTDIR2;SUPPLEM2")
arcpy.AlterField_management(in_table="GeoAdd1", field="PREDIR", clear_field_alias="true")
arcpy.AlterField_management(in_table="GeoAdd1", field="NAME", clear_field_alias="true")
arcpy.AlterField_management(in_table="GeoAdd1", field="SUFFIX", clear_field_alias="true")
arcpy.AlterField_management(in_table="GeoAdd1", field="POSTDIR", clear_field_alias="true")
arcpy.AlterField_management(in_table="GeoAdd1", field="SUPPLEM", clear_field_alias="true")
arcpy.AlterField_management(in_table="GeoAdd1", field="MUNI", clear_field_alias="true")
arcpy.AlterField_management(in_table="GeoAdd1", field="CITY", clear_field_alias="true")
arcpy.AlterField_management(in_table="GeoAdd1", field="ZIP", clear_field_alias="true")
