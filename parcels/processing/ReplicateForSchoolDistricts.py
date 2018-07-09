#-------------------------------------------------------------------------------
# Name:     ReplicateForSchoolDistricts.py
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20171030
# Modified:
# Input:  J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined
# Output:  J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_SchoolDistrict
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/"

fc = "AC_Parcels_Combined_2_SchoolDistrict"
if arcpy.Exists(fc):
    arcpy.AddMessage("Deleting old version of AC_Parcels_Combined_2_SchoolDistrict...")
    arcpy.Delete_management(in_data="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_SchoolDistrict", data_type="FeatureClass")
    arcpy.Merge_management(inputs="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined",
    output="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_SchoolDistrict",
    field_mappings='schooldist "schooldist" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,schooldist,-1,-1')
    arcpy.AddMessage("   ...and replaced with new AC_Parcels_Combined_2_SchoolDistrict.")
else:
    arcpy.Merge_management(inputs="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined",
    output="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_SchoolDistrict",
    field_mappings='schooldist "schooldist" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,schooldist,-1,-1')
    arcpy.AddMessage("Created new AC_Parcels_Combined_2_SchoolDistrict.")
