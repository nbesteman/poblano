#-------------------------------------------------------------------------------
# Name:     ReplicateForNewRoads
# Purpose:  Replicate table to create roads layer for use with NewWorld
#           (in tmpRoadsNW)add JOIN_ID and Calculate value = OID
# Author:   Neil Besteman
# Created:  20171106
# Modified:  20171128
# Input:  J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/AC_Roads
# Output:  J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW
#-------------------------------------------------------------------------------
import arcpy

arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/"

fc = "tmpRoadsNW"
if arcpy.Exists(fc):
    arcpy.AddMessage("Deleting old version of tmpRoadsNW...")
    arcpy.Delete_management(in_data="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", data_type="FeatureClass")
    # Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
    arcpy.FeatureClassToFeatureClass_conversion(in_features="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/AC_Roads",
    out_path="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb", out_name="tmpRoadsNW", where_clause="",
    field_mapping='ROADNAME "ROADNAME" true true false 60 Text 0 0 ,First,#,AC_Roads,ROADNAME,-1,-1; \
    ROADNAME1 "ROADNAME1" true true false 60 Text 0 0 ,First,#,AC_Roads,ROADNAME1,-1,-1; \
    ROADNAME2 "ROADNAME2" true true false 60 Text 0 0 ,First,#,AC_Roads,ROADNAME2,-1,-1; \
    FEDIRP "FEDIRP" true true false 2 Text 0 0 ,First,#,AC_Roads,FEDIRP,-1,-1; \
    FENAME "FENAME" true true false 40 Text 0 0 ,First,#,AC_Roads,FENAME,-1,-1; \
    FETYPE "FETYPE" true true false 4 Text 0 0 ,First,#,AC_Roads,FETYPE,-1,-1; \
    FEDIRS "FEDIRS" true true false 2 Text 0 0 ,First,#,AC_Roads,FEDIRS,-1,-1; \
    FEDIRP2 "FEDIRP2" true true false 2 Text 0 0 ,First,#,AC_Roads,FEDIRP2,-1,-1; \
    FENAME2 "FENAME2" true true false 40 Text 0 0 ,First,#,AC_Roads,FENAME2,-1,-1; \
    FETYPE2 "FETYPE2" true true false 4 Text 0 0 ,First,#,AC_Roads,FETYPE2,-1,-1; \
    FEDIRS2 "FEDIRS2" true true false 2 Text 0 0 ,First,#,AC_Roads,FEDIRS2,-1,-1; \
    FEDIRP3 "FEDIRP3" true true false 2 Text 0 0 ,First,#,AC_Roads,FEDIRP3,-1,-1; \
    FENAME3 "FENAME3" true true false 40 Text 0 0 ,First,#,AC_Roads,FENAME3,-1,-1; \
    FETYPE3 "FETYPE3" true true false 4 Text 0 0 ,First,#,AC_Roads,FETYPE3,-1,-1; \
    FEDIRS3 "FEDIRS3" true true false 2 Text 0 0 ,First,#,AC_Roads,FEDIRS3,-1,-1; \
    FRADDL "FRADDL" true true false 8 Double 0 0 ,First,#,AC_Roads,FRADDL,-1,-1; \
    TOADDL "TOADDL" true true false 8 Double 0 0 ,First,#,AC_Roads,TOADDL,-1,-1; \
    FRADDR "FRADDR" true true false 8 Double 0 0 ,First,#,AC_Roads,FRADDR,-1,-1; \
    TOADDR "TOADDR" true true false 8 Double 0 0 ,First,#,AC_Roads,TOADDR,-1,-1; \
    ZIPL "ZIPL" true true false 8 Double 0 0 ,First,#,AC_Roads,ZIPL,-1,-1; \
    ZIPR "ZIPR" true true false 8 Double 0 0 ,First,#,AC_Roads,ZIPR,-1,-1; \
    FMCDL "FMCDL" true true false 5 Text 0 0 ,First,#,AC_Roads,FMCDL,-1,-1; \
    FMCDR "FMCDR" true true false 5 Text 0 0 ,First,#,AC_Roads,FMCDR,-1,-1; \
    FCC "FCC" true true false 3 Text 0 0 ,First,#,AC_Roads,FCC,-1,-1; \
    LEGALSYSTE "LEGALSYSTE" true true false 8 Double 0 0 ,First,#,AC_Roads,LEGALSYSTEM,-1,-1; \
    CITYL "CITYL" true true false 20 Text 0 0 ,First,#,AC_Roads,CITYL,-1,-1; \
    CITYR "CITYR" true true false 20 Text 0 0 ,First,#,AC_Roads,CITYR,-1,-1; \
    VENUE_L "VENUE_L" true true false 50 Text 0 0 ,First,#,AC_Roads,VENUE_L,-1,-1; \
    VENUE_R "VENUE_R" true true false 50 Text 0 0 ,First,#,AC_Roads,VENUE_R,-1,-1; \
    MAINTENANC "MAINTENANC" true true false 25 Text 0 0,First,#,AC_Roads,MAINTENANCE,-1,-1', config_keyword="")
    arcpy.AddMessage("   ...and replaced with AC_Roads.")
else:
    arcpy.FeatureClassToFeatureClass_conversion(in_features="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/AC_Roads",
    out_path="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb", out_name="tmpRoadsNW", where_clause="",
    field_mapping='ROADNAME "ROADNAME" true true false 60 Text 0 0 ,First,#,AC_Roads,ROADNAME,-1,-1; \
    ROADNAME1 "ROADNAME1" true true false 60 Text 0 0 ,First,#,AC_Roads,ROADNAME1,-1,-1; \
    ROADNAME2 "ROADNAME2" true true false 60 Text 0 0 ,First,#,AC_Roads,ROADNAME2,-1,-1; \
    FEDIRP "FEDIRP" true true false 2 Text 0 0 ,First,#,AC_Roads,FEDIRP,-1,-1; \
    FENAME "FENAME" true true false 40 Text 0 0 ,First,#,AC_Roads,FENAME,-1,-1; \
    FETYPE "FETYPE" true true false 4 Text 0 0 ,First,#,AC_Roads,FETYPE,-1,-1; \
    FEDIRS "FEDIRS" true true false 2 Text 0 0 ,First,#,AC_Roads,FEDIRS,-1,-1; \
    FEDIRP2 "FEDIRP2" true true false 2 Text 0 0 ,First,#,AC_Roads,FEDIRP2,-1,-1; \
    FENAME2 "FENAME2" true true false 40 Text 0 0 ,First,#,AC_Roads,FENAME2,-1,-1; \
    FETYPE2 "FETYPE2" true true false 4 Text 0 0 ,First,#,AC_Roads,FETYPE2,-1,-1; \
    FEDIRS2 "FEDIRS2" true true false 2 Text 0 0 ,First,#,AC_Roads,FEDIRS2,-1,-1; \
    FEDIRP3 "FEDIRP3" true true false 2 Text 0 0 ,First,#,AC_Roads,FEDIRP3,-1,-1; \
    FENAME3 "FENAME3" true true false 40 Text 0 0 ,First,#,AC_Roads,FENAME3,-1,-1; \
    FETYPE3 "FETYPE3" true true false 4 Text 0 0 ,First,#,AC_Roads,FETYPE3,-1,-1; \
    FEDIRS3 "FEDIRS3" true true false 2 Text 0 0 ,First,#,AC_Roads,FEDIRS3,-1,-1; \
    FRADDL "FRADDL" true true false 8 Double 0 0 ,First,#,AC_Roads,FRADDL,-1,-1; \
    TOADDL "TOADDL" true true false 8 Double 0 0 ,First,#,AC_Roads,TOADDL,-1,-1; \
    FRADDR "FRADDR" true true false 8 Double 0 0 ,First,#,AC_Roads,FRADDR,-1,-1; \
    TOADDR "TOADDR" true true false 8 Double 0 0 ,First,#,AC_Roads,TOADDR,-1,-1; \
    ZIPL "ZIPL" true true false 8 Double 0 0 ,First,#,AC_Roads,ZIPL,-1,-1; \
    ZIPR "ZIPR" true true false 8 Double 0 0 ,First,#,AC_Roads,ZIPR,-1,-1; \
    FMCDL "FMCDL" true true false 5 Text 0 0 ,First,#,AC_Roads,FMCDL,-1,-1; \
    FMCDR "FMCDR" true true false 5 Text 0 0 ,First,#,AC_Roads,FMCDR,-1,-1; \
    FCC "FCC" true true false 3 Text 0 0 ,First,#,AC_Roads,FCC,-1,-1; \
    LEGALSYSTEM "LEGALSYSTEM" true true false 8 Double 0 0 ,First,#,AC_Roads,LEGALSYSTEM,-1,-1; \
    CITYL "CITYL" true true false 20 Text 0 0 ,First,#,AC_Roads,CITYL,-1,-1; \
    CITYR "CITYR" true true false 20 Text 0 0 ,First,#,AC_Roads,CITYR,-1,-1; \
    VENUE_L "VENUE_L" true true false 50 Text 0 0 ,First,#,AC_Roads,VENUE_L,-1,-1; \
    VENUE_R "VENUE_R" true true false 50 Text 0 0 ,First,#,AC_Roads,VENUE_R,-1,-1; \
    MAINTENANC "MAINTENANC" true true false 25 Text 0 0,First,#,AC_Roads,MAINTENANCE,-1,-1', config_keyword="")
    arcpy.AddMessage("   ...and replaced with AC_Roads.")

arcpy.AddField_management("J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", "JOIN_ID", "LONG")
#update the join id after appending the county 5 data
#arcpy.CalculateField_management("J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW","JOIN_ID", "[OBJECTID]")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "tmpRoadsNW"
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="ROADNAME", expression="!ROADNAME!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="ROADNAME1", expression="!ROADNAME1!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="ROADNAME2", expression="!ROADNAME2!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="FEDIRP", expression="!FEDIRP!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="FENAME", expression="!FENAME!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="FETYPE", expression="!FETYPE!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="FEDIRS", expression="!FEDIRS!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="FEDIRP2", expression="!FEDIRP2!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="FENAME2", expression="!FENAME2!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="FETYPE2", expression="!FETYPE2!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="FEDIRS2", expression="!FEDIRS2!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="FEDIRP3", expression="!FEDIRP3!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="FENAME3", expression="!FENAME3!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="FETYPE3", expression="!FETYPE3!.upper()", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW", field="FEDIRS3", expression="!FEDIRS3!.upper()", expression_type="PYTHON_9.3", code_block="")
    #CITYL "CITYL" true true false 20 Text 0 0 ,First,#,AC_Roads,CITYL,-1,-1;
    #CITYR "CITYR" true true false 20 Text 0 0 ,First,#,AC_Roads,CITYR,-1,-1;
    #VENUE_L "VENUE_L" true true false 50 Text 0 0 ,First,#,AC_Roads,VENUE_L,-1,-1;
    #VENUE_R "VENUE_R" true true false 50 Text 0 0 ,First,#,AC_Roads,VENUE_R,-1,-1;
