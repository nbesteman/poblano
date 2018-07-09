#-------------------------------------------------------------------------------
#     Name: Append_Co5_Roads
#  Purpose: Append Co5_Roads to tmpRoadsNW layer for use with NewWorld
#   Author: Neil Besteman
#  Created: 20171108
# Modified: 20171127
#    Input: J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW
#   Output: J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW (*Appended)

#Reference: https://community.esri.com/thread/185431-append-tool-and-field-mapping-help-examples
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/"

appendthis = "County5_RoadsforNW"
targetFc = "tmpRoadsNW"

if arcpy.Exists(targetFc):
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "tmpRoadsNW"
    fieldmapping = arcpy.FieldMappings()
    fieldmapping.addTable(appendthis)

    arcpy.Append_management(appendthis, targetFc, "NO_TEST", fieldmapping)
    #arcpy.Append_management(inputs="County5_RoadsforNW", target= fc, schema_type="NO_TEST",field_mapping = fieldmapping, subtype="")
else:
    arcpy.AddMessage("Created tmpRoadsNW not located.")

arcpy.CalculateField_management("J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW","JOIN_ID", "[OBJECTID]")
