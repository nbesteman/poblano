#-------------------------------------------------------------------------------
# Name:     CreateAlternateNameTable.py
# Purpose:  Create the Alternate Name Table table for use with NewWorld
# Author:   Bryan May
# Created:  20171128
# Modified:
# Input:  J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/AC_Roads
# Output:  J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/AlternatenameTable
#-------------------------------------------------------------------------------
import arcpy

rdFc = "tmpRoadsNW"
tmpTbl = "NW_Alternate_Name"

ws = "J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/"
arcpy.env.workspace = ws

if arcpy.Exists(tmpTbl):
    arcpy.AddMessage("Deleting old version of "+ tmpTbl + "...")

    arcpy.Delete_management(in_data = tmpTbl)

    arcpy.MakeFeatureLayer_management( rdFc, "rdLyr1" )

    arcpy.SelectLayerByAttribute_management("rdLyr1", "NEW_SELECTION","(FENAME2) <> ' ' ")

    arcpy.TableToTable_conversion("rdLyr1", ws ,tmpTbl, where_clause="",
    field_mapping='FEDIRP2 "FEDIRP2" true true false 2 Text 0 0 ,First,#,J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW,FEDIRP2,-1,-1; \
    FENAME2 "FENAME2" true true false 40 Text 0 0 ,First,#,J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW,FENAME2,-1,-1; \
    FETYPE2 "FETYPE2" true true false 4 Text 0 0 ,First,#,J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW,FETYPE2,-1,-1; \
    FEDIRS2 "FEDIRS2" true true false 2 Text 0 0 ,First,#,J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW,FEDIRS2,-1,-1; \
    JOIN_ID "JOIN_ID" true true false 4 Long 0 0 ,First,#,J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW,JOIN_ID,-1,-1', config_keyword="")

    arcpy.AddField_management( tmpTbl , "PRETYPE", "TEXT","","", "4","","true")

    arcpy.AlterField_management( tmpTbl , "FEDIRP2" , "PREFIX_DIRECTION","","","","","true")

    arcpy.AlterField_management( tmpTbl , "FENAME2" , "ALTERNATE_STREET_NAME","","","","","true")

    arcpy.AlterField_management( tmpTbl , "FETYPE2" , "STREET_TYPE","","","","","true")

    arcpy.AlterField_management( tmpTbl , "FEDIRS2" , "SUFFIX_DIRECTION","","","","","true")

else:
    arcpy.MakeFeatureLayer_management( rdFc, "rdLyr1" )

    arcpy.SelectLayerByAttribute_management("rdLyr1", "NEW_SELECTION","(FENAME2) <> ' ' ")

    arcpy.TableToTable_conversion("rdLyr1", ws ,tmpTbl, where_clause="",
    field_mapping='FEDIRP2 "FEDIRP2" true true false 2 Text 0 0 ,First,#,J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW,FEDIRP2,-1,-1; \
    FENAME2 "FENAME2" true true false 40 Text 0 0 ,First,#,J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW,FENAME2,-1,-1; \
    FETYPE2 "FETYPE2" true true false 4 Text 0 0 ,First,#,J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW,FETYPE2,-1,-1; \
    FEDIRS2 "FEDIRS2" true true false 2 Text 0 0 ,First,#,J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW,FEDIRS2,-1,-1; \
    JOIN_ID "JOIN_ID" true true false 4 Long 0 0 ,First,#,J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW,JOIN_ID,-1,-1', config_keyword="")

    arcpy.AddField_management( tmpTbl , "PRETYPE", "TEXT","","", "4","","true")

    arcpy.AlterField_management( tmpTbl , "FEDIRP2" , "PREFIX_DIRECTION","","","","","true")

    arcpy.AlterField_management( tmpTbl , "FENAME2" , "ALTERNATE_STREET_NAME","","","","","true")

    arcpy.AlterField_management( tmpTbl , "FETYPE2" , "STREET_TYPE","","","","","true")

    arcpy.AlterField_management( tmpTbl , "FEDIRS2" , "SUFFIX_DIRECTION","","","","","true")
