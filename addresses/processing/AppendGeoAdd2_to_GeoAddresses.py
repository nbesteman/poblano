#-------------------------------------------------------------------------------
# Name:     AppendGeoAdd2_to_GEoAddresses
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20180716
# Modified:
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/"


arcpy.Append_management(inputs="GeoAdd2", target="GeoAddAddresses", schema_type="TEST", field_mapping="", subtype="")
