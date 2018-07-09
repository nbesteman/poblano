#-------------------------------------------------------------------------------
# Name:        CreateUnitParcelShapefiles
# Purpose:     To create and load zipfiles for individual unit parcels layer in shapefile format.
# Author:      Neil Besteman
# Created:     20170620
# Modified:    20170620
# Input:    J:\Apps\Python\LayerUpdates\parcels\build_DataLibrary\AlleganTwp_Parcels.shp
# Output:   J:\Apps\Python\LayerUpdates\parcels\build_DataLibrary\AlleganTwp_Parcels.zip
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy,os,shutil,zipfile

#folder = 'J:\Apps\Python\LayerUpdates\parcels\\build_DataLibrary'

dir_name = "J:/Apps/Python/LayerUpdates/parcels/build_DataLibrary/"
os.chdir(dir_name)
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
    zipname = val + "_Parcels.zip"
    arcpy.AddMessage(zipname)
    arcpy.AddMessage(dir_name)

    zf = zipfile.ZipFile(zipname, mode = 'w')
    try:
        print 'adding files'
        zf.write(val+'_Parcels.dbf')
        zf.write(val+'_Parcels.prj')
        zf.write(val+'_Parcels.shp')
        zf.write(val+'_Parcels.shx')
    finally:
        print 'closing'
        zf.close()

    #shutil.make_archive(zipname,"zip",)

arcpy.AddMessage ("finished processing")
