#-------------------------------------------------------------------------------
# Name:     MoveParcelPlus2Local.py
# Purpose:  To move the unit parcelplus shapefiles to the local unit folders.
# Author:   Bryan May
# Created:  20171010
# Modified:
#-------------------------------------------------------------------------------
import os,shutil

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

#srcDir = '../build'
srcDir = 'J:/Apps/Python/LayerUpdates/parcels//build_ParcelsPlus'
trgtPath = 'J:/data/Shapefiles/'
#arcpy.AddMessage(srcDir + 'test')
for fname in os.listdir(srcDir):
    arcpy.AddMessage(fname)
    #delete the .xml files (metadata) this may be changed at some point but for now
    #it interferes with the file format
    unitname = (os.path.splitext(fname)[0])
    extension = (os.path.splitext(fname)[1])
    if extension == '.xml':
        print extension
        print srcDir+'/'+fname
        os.remove(srcDir+'/'+fname)
#populate a second time because removed the .xml
for fname in os.listdir(srcDir):
    unitname = (os.path.splitext(fname)[0])
    extension = (os.path.splitext(fname)[1])
    unitID = str(unit.get(unitname))
    #print 'moving:  '  +unitID + " " +fname
    trgtDir = unitID+unitname
    trgt = trgtPath+trgtDir+'/ParcelsPlus'+extension
    shutil.move(os.path.join(srcDir, fname), trgt)
##if fname.startswith(prefix):
##                if not os.path.isdir(os.path.join(targetDir, prefix)):
##                    os.mkdir(os.path.join(targetDir, prefix))
##                shutil.move(os.path.join(srcDir, fnmae), targetDir)
