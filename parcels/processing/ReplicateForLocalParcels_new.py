#-------------------------------------------------------------------------------
# Name:     edit_table
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20170626
# Modified: 20170818 added copy for parcelsplus
# Modified: 20170925 fixed parcelsplus portions
# Modified: 20171213 cleaned up the readability
# Input:  J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined
# Output:  J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_Shapefiles
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/"

fc = "AC_Parcels_Combined_2_Shapefiles"
if arcpy.Exists(fc):
    arcpy.AddMessage("Deleting old version of AC_Parcels_Combined_2_Shapefiles...")
    arcpy.Delete_management(in_data="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_Shapefiles", data_type="FeatureClass")
    arcpy.Merge_management(inputs="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined",
    output="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_Shapefiles",
    field_mappings='MAPPING_ID "MAPPING_ID" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,MAPPING_ID,-1,-1; \
    ACRES "ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ACRES,-1,-1; \
    ownername1 "ownername1" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ownername1,-1,-1; \
    ownerstreetaddr "ownerstreetaddr" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ownerstreetaddr,-1,-1; \
    ownercity "ownercity" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ownercity,-1,-1; \
    ownerstate "ownerstate" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ownerstate,-1,-1; \
    ownerzip "ownerzip" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ownerzip,-1,-1; \
    ownercareof "ownercareof" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ownercareof,-1,-1; \propstreetcombined "propstreetcombined" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,propstreetcombined,-1,-1; \zoning "zoning" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,zoning,-1,-1; \
    liberpage "liberpage" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,liberpage,-1,-1; \
    taxpayname "taxpayname" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,taxpayname,-1,-1; \
    taxpaycareof "taxpaycareof" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,taxpaycareof,-1,-1; \
    taxpaystreetaddr "taxpaystreetaddr" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,taxpaystreetaddr,-1,-1; \taxpaycity "taxpaycity" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,taxpaycity,-1,-1; \taxpaystate "taxpaystate" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,taxpaystate,-1,-1; \
    taxpayzip "taxpayzip" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,taxpayzip,-1,-1; \
    totalacres "totalacres" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,totalacres,-1,-1; \
    genericlistitem "genericlistitem" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,genericlistitem,-1,-1; \
    neighborhood "neighborhood" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,neighborhood,-1,-1; \
    propclass "propclass" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,propclass,-1,-1; \
    schooldist "schooldist" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,schooldist,-1,-1; \
    MayPRE "MayPRE" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,MayPRE,-1,-1; \
    homestead "homestead" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,homestead,-1,-1; \
    qualag "qualag" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,qualag,-1,-1; \
    year "year" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,year,-1,-1; \
    ass "ass" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ass,-1,-1; \
    tax "tax" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,tax,-1,-1; \
    DEED_ACRES "DEED_ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,DEED_ACRES,-1,-1; \
    Shape_Length "Shape_Length" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,Shape_Length,-1,-1; \
    Shape_Area "Shape_Area" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,Shape_Area,-1,-1; \
    GlobalID "GlobalID" false false false 38 GlobalID 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,GlobalID,-1,-1')
    arcpy.AddMessage("   ...and replaced with new AC_Parcels_Combined_2_Shapefiles.")
else:
    arcpy.Merge_management(inputs="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined",
    output="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_Shapefiles",
    field_mappings='MAPPING_ID "MAPPING_ID" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,MAPPING_ID,-1,-1; \
    ACRES "ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ACRES,-1,-1; \
    ownername1 "ownername1" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ownername1,-1,-1; \
    ownerstreetaddr "ownerstreetaddr" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ownerstreetaddr,-1,-1; \
    ownercity "ownercity" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ownercity,-1,-1; \
    ownerstate "ownerstate" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ownerstate,-1,-1; \
    ownerzip "ownerzip" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ownerzip,-1,-1; \
    ownercareof "ownercareof" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ownercareof,-1,-1; \
    propstreetcombined "propstreetcombined" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,propstreetcombined,-1,-1; \
    zoning "zoning" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,zoning,-1,-1; \
    liberpage "liberpage" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,liberpage,-1,-1; \
    taxpayname "taxpayname" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,taxpayname,-1,-1; \
    taxpaycareof "taxpaycareof" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,taxpaycareof,-1,-1; \
    taxpaystreetaddr "taxpaystreetaddr" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,taxpaystreetaddr,-1,-1; \
    taxpaycity "taxpaycity" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,taxpaycity,-1,-1; \
    taxpaystate "taxpaystate" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,taxpaystate,-1,-1; \taxpayzip "taxpayzip" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,taxpayzip,-1,-1; \totalacres "totalacres" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,totalacres,-1,-1; \genericlistitem "genericlistitem" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,genericlistitem,-1,-1; \
    neighborhood "neighborhood" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,neighborhood,-1,-1; \
    propclass "propclass" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,propclass,-1,-1; \
    schooldist "schooldist" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,schooldist,-1,-1; \
    MayPRE "MayPRE" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,MayPRE,-1,-1; \
    homestead "homestead" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,homestead,-1,-1; \
    qualag "qualag" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,qualag,-1,-1; \
    year "year" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,year,-1,-1; \
    ass "ass" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,ass,-1,-1; \
    tax "tax" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,tax,-1,-1; \
    DEED_ACRES "DEED_ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,DEED_ACRES,-1,-1; \
    Shape_Length "Shape_Length" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,Shape_Length,-1,-1; \
    Shape_Area "Shape_Area" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,Shape_Area,-1,-1; \
    GlobalID "GlobalID" false false false 38 GlobalID 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined,GlobalID,-1,-1')
    arcpy.AddMessage("Created new AC_Parcels_Combined_2_Shapefiles.")
