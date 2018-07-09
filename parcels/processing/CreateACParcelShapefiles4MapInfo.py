#-------------------------------------------------------------------------------
# Name:        CreateUnitParcelShapefiles
# Purpose:     To create a AC parcels comb in shapefile format for use with MapInfo
# Author:      Neil Besteman
# Created:     20170623
# Modified:    20171018
# Input:       J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_MapInfo
# Output:      J:/Apps/Python/LayerUpdates/parcels/processing/shapes/intlft/AC_ParcelsComb_IntlFt.shp
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import arcpy,os,shutil

#delete files located in build folder
folder = 'J:\Apps\Python\LayerUpdates\parcels\processing\shapes\intlft'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #If you also want to remove subdirectories, uncomment the elif statement.
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/parcels/"

arcpy.AddMessage("processing: AC_Parcels_Combined_2_MapInfo to shapefile for MapInfo conversion")
arcpy.FeatureClassToFeatureClass_conversion(in_features="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_MapInfo",
out_path="J:/Apps/Python/LayerUpdates/parcels/processing/shapes/intlft",
out_name="AC_ParcelsComb_IntlFt.shp",
where_clause="",
field_mapping=
'PARCEL_ID "PARCEL_ID" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,PARCEL_ID,-1,-1;'+
'DEED_ACRES "DEED_ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,DEED_ACRES,-1,-1;'+
'ACRES "ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,ACRES,-1,-1;'+
'GlobalID "GlobalID" false false false 38 GlobalID 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,GlobalID,-1,-1;'+
'owner "owner" true true false 35 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,owner,-1,-1;'+
'owner_addr "owner_addr" true true false 35 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,owner_addr,-1,-1;'+
'owner_city "owner_city" true true false 25 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,owner_city,-1,-1;'+
'ownerstate "ownerstate" true true false 2 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,ownerstate,-1,-1;'+
'owner_zip "owner_zip" true true false 10 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,owner_zip,-1,-1;'+
'ownercare "ownercare" true true false 35 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,ownercare,-1,-1;'+
'propaddrss "propaddrss" true true false 62 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,propaddrss,-1,-1;'+
'zoning "zoning" true true false 15 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,zoning,-1,-1;'+
'liber_page "liber_page" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,liber_page,-1,-1;'+
'tax_name "tax_name" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,tax_name,-1,-1;'+
'tax_careof "tax_careof" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,tax_careof,-1,-1;'+
'tax_addres "tax_addres" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,tax_addres,-1,-1;'+
'tax_city "tax_city" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,tax_city,-1,-1;'+
'tax_state "tax_state" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,tax_state,-1,-1;'+
'tax_zip "tax_zip" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,tax_zip,-1,-1;'+
'PDR "PDR" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,PDR,-1,-1;'+
'propclass "propclass" true true false 5 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,propclass,-1,-1;'+
'schooldist "schooldist" true true false 5 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,schooldist,-1,-1;'+
'MayPRE "MayPRE" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,MayPRE,-1,-1;'+
'homestead "homestead" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,homestead,-1,-1;'+
'assessment "assessment" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,assessment,-1,-1;'+
'taxable "taxable" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,taxable,-1,-1;'+
'Shape_Leng "Shape_Leng" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,Shape_Length,-1,-1;'+
'Shape_Area "Shape_Area" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfo,Shape_Area,-1,-1', config_keyword="")
arcpy.AddMessage ("finished processing too shapefile")
arcpy.AddMessage("processing: reprojection to meters")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
