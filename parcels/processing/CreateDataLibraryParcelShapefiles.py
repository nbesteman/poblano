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
folder = 'J:\Apps\Python\LayerUpdates\parcels\\build_DataLibrary'
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
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/parcels/"
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
    arcpy.FeatureClassToFeatureClass_conversion(in_features="source/Parcels_Combined.gdb/AC_Parcels_Combined_2_DataLibrary",
                                                out_path="build_DataLibrary",
                                                out_name = val + "_Parcels.shp",
                                                where_clause="PARCELID LIKE '"+unitID+"%'",
                                                field_mapping='MAPPING_ID "MAPPING_ID" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,PARCELID,-1,-1;DEED_ACRES "DEED_ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,DEED_ACRES,-1,-1;ACRES "ACRES" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,ACRES,-1,-1;LABEL "LABEL" true true false 15 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,LABEL,-1,-1;CENTERX "CENTERX" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,CENTERX,-1,-1;CENTERY "CENTERY" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,CENTERY,-1,-1;ANGLE "ANGLE" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,ANGLE,-1,-1;OFFSETX "OFFSETX" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,OFFSETX,-1,-1;OFFSETY "OFFSETY" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,OFFSETY,-1,-1;GlobalID "GlobalID" false false false 38 GlobalID 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,GlobalID,-1,-1;neighborho "neighborhood" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,neighborhood,-1,-1;propclass "propclass" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,propclass,-1,-1;schooldist "schooldist" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,schooldist,-1,-1;overAllSta "overAllStatus" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,overAllStatus,-1,-1;isExempt "isExempt" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,isExempt,-1,-1;propstatus "propstatus" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,propstatus,-1,-1;shortnotes "shortnotes" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,shortnotes,-1,-1;MayPRE "MayPRE" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,MayPRE,-1,-1;homestead "homestead" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,homestead,-1,-1;qualag "qualag" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,qualag,-1,-1;owner "ownername1" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,owner,-1,-1;ownaddress "ownerstreetaddr" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,ownaddress,-1,-1;ownercity "ownercity" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,ownercity,-1,-1;ownerstate "ownerstate" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,ownerstate,-1,-1;ownerzip "ownerzip" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,ownerzip,-1,-1;ownercareo "ownercareof" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,ownercareof,-1,-1;propaddres "propstreetcombined" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,propaddress,-1,-1;zoning "zoning" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,zoning,-1,-1;liberpage "liberpage" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,liberpage,-1,-1;taxpayname "taxpayname" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,taxpayname,-1,-1;taxpaycare "taxpaycareof" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,taxpaycareof,-1,-1;taxaddress "taxpaystreetaddr" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,taxaddress,-1,-1;taxpaycity "taxpaycity" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,taxpaycity,-1,-1;taxpaystat "taxpaystate" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,taxpaystate,-1,-1;taxpayzip "taxpayzip" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,taxpayzip,-1,-1;totalacres "totalacres" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,totalacres,-1,-1;propaddrdi "propaddrdirect" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,propaddrdirect,-1,-1;propstreet "propstreetname" true true false 255 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,propstreetname,-1,-1;year "year" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,year,-1,-1;landass "landass" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,landass,-1,-1;assessment "ass" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,assessment,-1,-1;tax "tax" true true false 4 Long 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,tax,-1,-1;Shape_Leng "Shape_Leng" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,Shape_Length,-1,-1;Shape_Area "Shape_Area" false true true 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\FillmoreTwp,Shape_Area,-1,-1', config_keyword="")
arcpy.AddMessage ("finished processing")
