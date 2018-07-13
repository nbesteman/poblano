#-------------------------------------------------------------------------------
# Name:     edit_table
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20171018
# Modified:
# Input:  J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_2018
# Output:  J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_MapInfoEQ
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/"

fc = "AC_Parcels_Combined_2_MapInfoEQ"
if arcpy.Exists(fc):
    arcpy.AddMessage("Deleting old version of AC_Parcels_Combined_2_MapInfoEQ...")
    arcpy.Delete_management(in_data="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_MapInfoEQ", data_type="FeatureClass")
    arcpy.Merge_management(inputs="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Splits_2019",
    output="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_MapInfoEQ")
    arcpy.AddMessage("   ...and replaced with new AC_Parcels_Combined_2_MapInfoEQ.")
else:
    arcpy.Merge_management(inputs="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined",
    output="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_MapInfoEQ")
    arcpy.AddMessage("Created new AC_Parcels_Combined_2_MapInfoEQ.")
