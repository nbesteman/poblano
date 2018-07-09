#-------------------------------------------------------------------------------
# Name:        CreateUnitParcelShapefiles
# Purpose:     To create individual unit parcels layer in shapefile format.
# Author:      Neil Besteman
# Created:     20170313
# Modified:    20170324
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

inputunittmp = arcpy.GetParameterAsText(0) # list of values such as AlleganTwp,CascoTwp
#inputunit = ["AlleganTwp","CascoTwp"]
arcpy.AddMessage(inputunittmp)
inputunit = inputunittmp.split(";")
#arcpy.AddMessage('processing: '+inputunit)
#arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/parcels/"
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
    #print "Value: %s" % unit.get(val)
    #print "Value: " + unit.get(val)
    unitID = str(unit.get(val))
    arcpy.AddMessage("processing: "+unitID+val)
    arcpy.FeatureClassToFeatureClass_conversion(in_features="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_2_MI",
                                                out_path="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\intlft",
                                                out_name = val + ".shp",
                                                where_clause="MAPPING_ID LIKE '"+unitID+"%'",
                                                field_mapping='MAPPING_ID "MAPPING_ID" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,MAPPING_ID,-1,-1;DEED_ACRES "DEED_ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,DEED_ACRES,-1,-1;ACRES "ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,ACRES,-1,-1;COMMENT "COMMENT" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,COMMENT,-1,-1;ERROR "ERROR" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,ERROR,-1,-1;LABEL "LABEL" true true false 15 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,LABEL,-1,-1;CENTERX "CENTERX" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,CENTERX,-1,-1;CENTERY "CENTERY" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,CENTERY,-1,-1;ANGLE "ANGLE" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,ANGLE,-1,-1;OFFSETX "OFFSETX" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,OFFSETX,-1,-1;OFFSETY "OFFSETY" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,OFFSETY,-1,-1;GlobalID "GlobalID" false false false 38 GlobalID 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,GlobalID,-1,-1;Shape_Leng "Shape_Leng" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_2_MI,Shape_Area,-1,-1', config_keyword="")
arcpy.AddMessage ("finished processing")





