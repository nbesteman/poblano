#-------------------------------------------------------------------------------
# Name:        CreateUnitParcelPlusShapefiles.py
# Purpose:     To create individual unit parcelsplus layer in shapefile format.
# Author:      Neil Besteman
# Created:     20171010
#-------------------------------------------------------------------------------
import arcpy,os,shutil

#delete files located in build folder
folder = 'J:\Apps\Python\LayerUpdates\parcels\\build_ParcelsPlus'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)

    except Exception as e:
        print(e)

inputunittmp = arcpy.GetParameterAsText(0) # list of values such as AlleganTwp,CascoTwp
arcpy.AddMessage(inputunittmp)
inputunit = inputunittmp.split(";")
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/parcels/source/"

#create a list off of the entered values
unit = {
        'AlleganTwp': '01',
        'CascoTwp': '02',
        'CheshireTwp': '03',
        'ClydeTwp': '04',
        'DorrTwp': '05',
        'FillmoreTwp': '06',
        'GangesTwp': '07',
        'GunPlainTwp': '08',
        'HeathTwp': '09',
        'HopkinsTwp': '10',
        'LaketownTwp': '11',
        'LeeTwp': '12',
        'LeightonTwp': '13',
        'ManliusTwp': '14',
        'MartinTwp': '15',
        'MontereyTwp': '16',
        'OtsegoTwp': '17',
        'OveriselTwp': '18',
        'SalemTwp': '19',
        'SaugatuckTwp': '20',
        'TrowbridgeTwp': '21',
        'ValleyTwp': '22',
        'WatsonTwp': '23',
        'WaylandTwp': '24',
        'MartinVillage': '42',
        'HopkinsVillage': '44',
        'AlleganCity': '51',
        'FennvilleCity': '52',
        'HollandCity': '53',
        'OtsegoCity': '54',
        'PlainwellCity': '55',
        'WaylandCity': '56',
        'SaugatuckCity': '57',
        'SouthHavenCity': '58',
        'DouglasCity': '59',
        }

for val in inputunit:
    print val
    unitID = str(unit.get(val))
    wClause = "Unit_ID = "+"'"+unitID+"'"
    outClause = unitID + val
    parcelClause = unitID + "parcels"
    arcpy.AddMessage("processing: "+ unitID + val)
    arcpy.MakeFeatureLayer_management("J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\UnitClip", outClause, wClause)
    arcpy.MakeFeatureLayer_management("J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles", parcelClause)
    arcpy.SelectLayerByLocation_management(parcelClause ,"INTERSECT",outClause)

#create shapefiles ParcelsPlus from the selection.
    arcpy.FeatureClassToFeatureClass_conversion(in_features=parcelClause,
                                                out_path="J:/Apps/Python/LayerUpdates/parcels/build_ParcelsPlus",
                                                out_name = val + ".shp",
                                                field_mapping='PARCELID "PARCELID" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,PARCELID,-1,-1;ACRES "ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,ACRES,-1,-1;owner "owner" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,owner,-1,-1;owner_addr "owner_addr" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,owner_addr,-1,-1;owner_city "owner_city" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,owner_city,-1,-1;ownerstate "ownerstate" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,ownerstate,-1,-1;owner_zip "owner_zip" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,owner_zip,-1,-1;ownercare "ownercare" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,ownercare,-1,-1;propaddrss "propaddrss" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,propaddrss,-1,-1;zoning "zoning" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,zoning,-1,-1;liber_page "liber_page" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,liber_page,-1,-1;tax_name "tax_name" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,tax_name,-1,-1;tax_careof "tax_careof" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,tax_careof,-1,-1;tax_addres "tax_addres" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,tax_addres,-1,-1;tax_city "tax_city" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,tax_city,-1,-1;tax_state "tax_state" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,tax_state,-1,-1;tax_zip "tax_zip" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,tax_zip,-1,-1;totalacres "totalacres" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,totalacres,-1,-1;PDR "PDR" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,PDR,-1,-1;neighborhd "neighborhd" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,neighborhd,-1,-1;propclass "propclass" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,propclass,-1,-1;schooldist "schooldist" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,schooldist,-1,-1;MayPRE "MayPRE" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,MayPRE,-1,-1;homestead "homestead" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,homestead,-1,-1;qualag "qualag" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,qualag,-1,-1;year "year" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,year,-1,-1;assessment "assessment" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,assessment,-1,-1;taxable "taxable" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,taxable,-1,-1;DEED_ACRES "DEED_ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,DEED_ACRES,-1,-1;GlobalID "GlobalID" false false true 38 GlobalID 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,GlobalID,-1,-1;Shape_Leng "Shape_Leng" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_Shapefiles,Shape_Area,-1,-1', config_keyword="")

arcpy.AddMessage ("finished processing")
