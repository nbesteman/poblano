#-------------------------------------------------------------------------------
# Name:     AppendGeoAdd2_to_GEoAddresses
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20180716
# Modified: 20180809
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/"
#arcpy.env.workspace = "source/AddressData.gdb/"
fc1 = "Addresses_for_NewWorld"
if arcpy.Exists(fc1):
    arcpy.AddMessage("deleting old version of Addresses_for_NewWorld")
    arcpy.Delete_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses_for_NewWorld", data_type="FeatureClass")
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAdd1", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses_for_NewWorld", data_type="FeatureClass")
else:
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAdd1", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses_for_NewWorld", data_type="FeatureClass")
arcpy.AddMessage("created new version of loadthis_to_NewWorld")

arcpy.Append_management(inputs="GeoAdd2", target="Addresses_for_NewWorld", schema_type="TEST", field_mapping="", subtype="")


# remove null and replace with blank
fields = ['POSTDIR']
#delete records
with arcpy.da.UpdateCursor(fc1,fields) as cursor:
    for row in cursor:
        if row[0] == None:
           row[0] = ''
arcpy.AddMessage("replace null with blank")
