#-------------------------------------------------------------------------------
#     Name: Append_Co5_Roads
#  Purpose: Append Co5_Roads to tmpRoadsNW layer for use with NewWorld
#   Author: Neil Besteman
#  Created: 20171108
# Modified: 20171122
#    Input: J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW
#   Output: J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/"

fc = "tmpRoadsNW"
if arcpy.Exists(fc):
    arcpy.Append_management()
    arcpy.Append_management(inputs="County5_RoadsforNW", target="tmpRoadsNW", schema_type="NO_TEST", \
    field_mapping='ROADNAME "ROADNAME" true true false 60 Text 0 0 ,First,#,County5_RoadsforNW,Roadname,-1,-1; \
    ROADNAME1 "ROADNAME1" true true false 60 Text 0 0 ,First,#; \
    ROADNAME2 "ROADNAME2" true true false 60 Text 0 0 ,First,#,County5_RoadsforNW,Roadname2,-1,-1; \
    FEDIRP "FEDIRP" true true false 2 Text 0 0 ,First,#,County5_RoadsforNW,FEDIRP,-1,-1; \
    FENAME "FENAME" true true false 40 Text 0 0 ,First,#,County5_RoadsforNW,FENAME,-1,-1; \
    FETYPE "FETYPE" true true false 4 Text 0 0 ,First,#,County5_RoadsforNW,FETYPE,-1,-1; \
    FEDIRS "FEDIRS" true true false 2 Text 0 0 ,First,#,County5_RoadsforNW,FEDIRS,-1,-1; \
    FEDIRP2 "FEDIRP2" true true false 2 Text 0 0 ,First,#,County5_RoadsforNW,FEDIRP2,-1,-1; \
    FENAME2 "FENAME2" true true false 40 Text 0 0 ,First,#,County5_RoadsforNW,FENAME2,-1,-1; \
    FETYPE2 "FETYPE2" true true false 4 Text 0 0 ,First,#,County5_RoadsforNW,FETYPE2,-1,-1; \
    FEDIRS2 "FEDIRS2" true true false 2 Text 0 0 ,First,#,County5_RoadsforNW,FEDIRS2,-1,-1; \
    FEDIRP3 "FEDIRP3" true true false 2 Text 0 0 ,First,#,County5_RoadsforNW,FEDIRP3,-1,-1; \
    FENAME3 "FENAME3" true true false 40 Text 0 0 ,First,#,County5_RoadsforNW,FENAME3,-1,-1; \
    FETYPE3 "FETYPE3" true true false 4 Text 0 0 ,First,#,County5_RoadsforNW,FETYPE3,-1,-1; \
    FEDIRS3 "FEDIRS3" true true false 2 Text 0 0 ,First,#,County5_RoadsforNW,FEDIRS3,-1,-1; \
    FRADDL "FRADDL" true true false 8 Double 0 0 ,First,#,County5_RoadsforNW,FRADDL,-1,-1; \
    TOADDL "TOADDL" true true false 8 Double 0 0 ,First,#,County5_RoadsforNW,TOADDL,-1,-1; \
    FRADDR "FRADDR" true true false 8 Double 0 0 ,First,#,County5_RoadsforNW,FRADDR,-1,-1; \
    TOADDR "TOADDR" true true false 8 Double 0 0 ,First,#,County5_RoadsforNW,TOADDR,-1,-1; \
    ZIPL "ZIPL" true true false 8 Double 0 0 ,First,#,County5_RoadsforNW,ZIPL,-1,-1; \
    ZIPR "ZIPR" true true false 8 Double 0 0 ,First,#,County5_RoadsforNW,ZIPR,-1,-1; \
    FMCDL "FMCDL" true true false 5 Text 0 0 ,First,#; \
    FMCDR "FMCDR" true true false 5 Text 0 0 ,First,#; \
    FCC "FCC" true true false 3 Text 0 0 ,First,#,County5_RoadsforNW,FCC,-1,-1; \
    LEGALSYSTEM "LEGALSYSTEM" true true false 8 Double 0 0 ,First,#; \
    VENUE_L "VENUE_L" true true false 50 Text 0 0 ,First,#; \
    VENUE_R "VENUE_R" true true false 50 Text 0 0 ,First,#; \
    COUNTYL "COUNTYL" true true false 8 Double 0 0 ,First,#,County5_RoadsforNW,COUNTYL,-1,-1; \
    COUNTYR "COUNTYR" true true false 8 Double 0 0 ,First,#,County5_RoadsforNW,COUNTYR,-1,-1; \
    SYM "SYM" true true false 8 Double 0 0 ,First,#; \
    Shape_Length "Shape_Length" false true true 8 Double 0 0 ,First,#,County5_RoadsforNW,Shape_Length,-1,-1', subtype="")
else:
    arcpy.AddMessage("Created tmpRoadsNW not located.")
