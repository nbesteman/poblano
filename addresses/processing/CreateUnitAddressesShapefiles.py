#-------------------------------------------------------------------------------
# Name:        CreateUnitAddressesShapefiles
# Purpose:     To create individual unit parcels layer in shapefile format.
# Author:      Neil Besteman
# Created:     20170703
# Modified:    20170705
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import arcpy,os,shutil

#delete files located in build folder
folder = 'J:\Apps\Python\\LayerUpdates\\addresses\\build'
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
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/"
#create a list off of the entered values
unit = {'AlleganTwp': 'Allegan Twp',
        'CascoTwp': 'Casco Twp',
        'CheshireTwp': 'Cheshire Twp',
        'ClydeTwp': 'Clyde Twp',
        'DorrTwp': 'Dorr Twp',
        'FillmoreTwp': 'Fillmore Twp',
        'GangesTwp': 'Ganges Twp',
        'GunPlainTwp': 'Gun Plain Twp',
        'HeathTwp': 'Heath Twp',
        'HopkinsTwp': 'Hopkins Twp',
        'LaketownTwp': 'Laketown Twp',
        'LeeTwp': 'Lee Twp',
        'LeightonTwp': 'Leighton Twp',
        'ManliusTwp': 'Manlius Twp',
        'MartinTwp': 'Martin Twp',
        'MontereyTwp': 'Monterey Twp',
        'OtsegoTwp': 'Otsego Twp',
        'OveriselTwp': 'Overisel Twp',
        'SalemTwp': 'Salem Twp',
        'SaugatuckTwp': 'Saugatuck Twp',
        'TrowbridgeTwp': 'Trowbridge Twp',
        'ValleyTwp': 'Valley Twp',
        'WatsonTwp': 'Watson Twp',
        'WaylandTwp': 'Wayland Twp',
        'MartinVillage': 'Martin Village',
        'HopkinsVillage': 'Hopkins Village',
        'AlleganCity': 'Allegan City',
        'FennvilleCity': 'Fennville City',
        'HollandCity': 'Holland City',
        'OtsegoCity': 'Otsego City',
        'PlainwellCity': 'Plainwell City',
        'WaylandCity': 'Wayland City',
        'SaugatuckCity': 'Saugatuck City',
        'South HavenCity': 'South Haven City',
        'DouglasCity': 'Douglas City'
        }

for val in inputunit:
    print "Value: %s" % unit.get(val)
    unitSpace = str(unit.get(val))
    arcpy.AddMessage("processing: "+val)
    arcpy.FeatureClassToFeatureClass_conversion(in_features="J:/Apps/Python/LayerUpdates/addresses/source//AddressData.gdb/Addresses4LocalShp",
                                                out_path="J:/Apps/Python/LayerUpdates/addresses/build",
                                                out_name = val+".shp",
                                                where_clause="MUNI = '"+unitSpace+"'",
                                                field_mapping='SITE_ID "SITE_ID" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,SITE_ID,-1,-1;ADDRESS "ADDRESS" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,ADDRESS,-1,-1;PREDIR "PREDIR" true true false 2 Text 0 0  ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,PREDIR,-1,-1;NUMBER "NUMBER" true true false 5 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,NUMBER,-1,-1;NAME "NAME" true true false 40 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,NAME,-1,-1;SUFFIX "SUFFIX" true true false 4 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,SUFFIX,-1,-1;NUMBERSUP "NUMBERSUP" true true false 4 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,NUMBERSUP,-1,-1;POSTDIR "POSTDIR" true true false 2 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,POSTDIR,-1,-1;SUPPLEM "SUPPLEM" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,SUPPLEM,-1,-1;CITY "CITY" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,CITY,-1,-1;ZIP "ZIP" true true false 5 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,ZIP,-1,-1;COUNTY "COUNTY" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,COUNTY,-1,-1;MUNI "MUNI" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,MUNI,-1,-1', config_keyword="")


#where_clause="MUNI LIKE "+val+"%",

#arcpy.AddMessage ("finished processing")

#field_mapping='field_mapping='SITE_ID "SITE_ID" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,SITE_ID,-1,-1, config_keyword="")

    #arcpy.FeatureClassToFeatureClass_conversion(in_features="J:/Apps/Python/LayerUpdates/addresses/source//AddressData.gdb/Addresses4LocalShp",out_path="J:/Apps/Python/LayerUpdates/addresses/build",out_name = "test.shp",where_clause="",field_mapping='SITE_ID "SITE_ID" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,SITE_ID,-1,-1;ADDRESS "ADDRESS" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,ADDRESS,-1,-1;PREDIRECTI "PREDIRECTI" true true false 2 Text 0 0  ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,PREDIRECTI,-1,-1;NUMBER "NUMBER" true true false 5 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,NUMBER,-1,-1;NAME "NAME" true true false 40 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,NAME,-1,-1;SUFFIX "SUFFIX" true true false 4 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,SUFFIX,-1,-1;NUMBERSUP "NUMBERSUP" true true false 4 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,NUMBERSUP,-1,-1;POSTDIRECT "POSTDIRECT" true true false 2 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,POSTDIRECT,-1,-1;SUPPLEMENT "SUPPLEMENT" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,SUPPLEMENT,-1,-1;CITY "CITY" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,CITY,-1,-1;ZIP "ZIP" true true false 5 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,ZIP,-1,-1;COUNTY "COUNTY" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,COUNTY,-1,-1;MUNI "MUNI" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4LocalShp,MUNI,-1,-1', config_keyword="")
