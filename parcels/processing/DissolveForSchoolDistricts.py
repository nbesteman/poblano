#-------------------------------------------------------------------------------
# Name:     DissolveForSchoolDistricts.py
# Purpose:  Dissolve by School District Field.
# Author:   Neil Besteman
# Created:  20171030
# Modified:
# Input:  J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_SchoolDistrict
# Output:  J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_SchoolDistrict
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/"

fc = "AC_SchoolDistrict"

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "AC_Parcels_Combined_2_SchoolDistrict"
if arcpy.Exists(fc):
    arcpy.AddMessage("Deleting old version of AC_SchoolDistrict...")
    arcpy.Delete_management(in_data="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_SchoolDistrict", data_type="FeatureClass")
    arcpy.Dissolve_management(in_features="AC_Parcels_Combined_2_SchoolDistrict",
    out_feature_class="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_SchoolDistrict",
    dissolve_field="schooldist",
    statistics_fields="",
    multi_part="MULTI_PART",
    unsplit_lines="DISSOLVE_LINES")
    arcpy.AddMessage("   ...and replaced with new AC_SchoolDistrict.")
else:
    arcpy.Dissolve_management(in_features="AC_Parcels_Combined_2_SchoolDistrict",
    out_feature_class="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_SchoolDistrict",
    dissolve_field="schooldist",
    statistics_fields="",
    multi_part="MULTI_PART",
    unsplit_lines="DISSOLVE_LINES")
    arcpy.AddMessage("Created new AC_SchoolDistrict.")
