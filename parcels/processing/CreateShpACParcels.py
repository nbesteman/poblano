#-------------------------------------------------------------------------------
# Name:        CreateUnitParcelShapefiles
# Purpose:     To create county parcel layer in shapefile format.
# Author:      Neil Besteman
# Created:     20170313
# Modified:    20171017
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

arcpy.AddMessage("processing: ACParcels to shapefile")
arcpy.FeatureClassToFeatureClass_conversion(in_features="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_Shapefiles",
                                            out_path="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\intlft",
                                            out_name = "ACParcels_IntlFt.shp",
                                            field_mapping='MAPPING_ID "MAPPING_ID" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,MAPPING_ID,-1,-1;DEED_ACRES "DEED_ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,DEED_ACRES,-1,-1;ACRES "ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,ACRES,-1,-1;COMMENT "COMMENT" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,COMMENT,-1,-1;ERROR "ERROR" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,ERROR,-1,-1;LABEL "LABEL" true true false 15 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,LABEL,-1,-1;CENTERX "CENTERX" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,CENTERX,-1,-1;CENTERY "CENTERY" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,CENTERY,-1,-1;ANGLE "ANGLE" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,ANGLE,-1,-1;OFFSETX "OFFSETX" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,OFFSETX,-1,-1;OFFSETY "OFFSETY" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,OFFSETY,-1,-1;GlobalID "GlobalID" false false false 38 GlobalID 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,GlobalID,-1,-1;Shape_Leng "Shape_Leng" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,Shape_Area,-1,-1', config_keyword="")
arcpy.AddMessage ("finished processing")
