#-------------------------------------------------------------------------------
# Name:     edit_table
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20170703
# Modified: 20170707
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
#delete addresses with no Number
with arcpy.da.UpdateCursor(fc,fields) as cursor:
    for row in cursor:
        if row[0] == '':  # and row[4] == 'Sleepy Hollow Beach Resort - Main Office, Delicatessen and Crafts Area':
            cursor.deleteRow()
        #arcpy.AddMessage("deleted addresses with blank number")
        if row[0] == ' ':
            cursor.deleteRow()
arcpy.AddMessage("deleted addresses with no number or a space as a number")

fields = ['ADDRESS']
#delete specific addresses that cause problems for NewWorld system and Dispatch
with arcpy.da.UpdateCursor(fc,fields) as cursor:
    for row in cursor:
        if row[0] == '7400 North Shore Dr':  # and row[4] == 'Sleepy Hollow Beach Resort - Main Office, Delicatessen and Crafts Area':
            cursor.deleteRow()
            arcpy.AddMessage("deleted 7400 North Shore Dr") #requested by Dispatch

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
arcpy.DeleteField_management(in_table="GeoAddresses", drop_field="ADDRESS;PROBLEM;NOTES;NUMBERSUP;SUPPLEMENT;COUNTY")
