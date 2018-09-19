#-------------------------------------------------------------------------------
# Name:     AppendGeoAdd2_to_GEoAddresses
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20180810
# Modified:
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/"
#arcpy.env.workspace = "source/AddressData.gdb/"

# remove null and replace with blank
fc = "Addresses_for_NewWorld"
fields = ['PREDIR']
#delete records
with arcpy.da.UpdateCursor(fc,fields) as cursor:
    for row in cursor:
        if row[0] == 'East':
           #row[0] == 'West'
           #cursor.updateRow(row)
           cursor.deleteRow()
arcpy.AddMessage("replace null with blank")
