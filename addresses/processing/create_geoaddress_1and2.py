#-------------------------------------------------------------------------------
# Name:     create geoaddress 1 and 2
# Purpose:  create two geoaddress tables to make into one
# Author:   Neil Besteman
# Created:  20190713
# Modified:
#https://gis.stackexchange.com/questions/152481/how-to-delete-selected-rows-using-arcpy
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/"
#arcpy.env.workspace = "source/AddressData.gdb/"
fc1 = "GeoAdd1"
if arcpy.Exists(fc1):
    arcpy.AddMessage("deleting old version of GeoAdd1")
    arcpy.Delete_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAdd1", data_type="FeatureClass")
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAddresses", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAdd1", data_type="FeatureClass")
else:
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAddresses", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAdd1", data_type="FeatureClass")
arcpy.AddMessage("created new version of GeoAdd1")

fc2 = "GeoAdd2"
if arcpy.Exists(fc2):
    arcpy.AddMessage("deleting old version of GeoAdd2")
    arcpy.Delete_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAdd2", data_type="FeatureClass")
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAddresses", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAdd2", data_type="FeatureClass")
else:
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAddresses", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAdd2", data_type="FeatureClass")
arcpy.AddMessage("created new version of GeoAdd2")

arcpy.AddMessage("finished processing")