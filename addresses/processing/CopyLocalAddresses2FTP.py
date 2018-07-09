#-------------------------------------------------------------------------------
# Name:     CopyLocalParcel2FTP
# Purpose:  To copy local parcels to the FTP site for distribution.
# Author:   Neil Besteman
# Created:  20170706
# Modified: 20170706
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import arcpy,os,shutil

inputunittmp = arcpy.GetParameterAsText(0) # list of values such as AlleganTwp,CascoTwp
#inputlayertmp = arcpy.GetParameterAsText(1) # list of values such as Addresses,Parcels
#inputunit = ["AlleganTwp","CascoTwp"]

srcDir = ''
trgtDir = ''
unitdict = {}
layerlist = []
unitlist = []

inputunit = inputunittmp.split(";")
#inputlayer = inputlayertmp.split(";")
#layerlist = inputlayer
unitlist = inputunit
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/parcels/"
srcPath = 'J:/data/Shapefiles/'
trgtPath = 'S:/Secure/Units/'

unitdict = {
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

filetype =  ['.shp',
            '.dbf',
            '.sbn',
            '.sbx',
            '.cpg',
            '.shx',
            '.prj'
            ]

for unit in inputunit:
    unitID = str(unitdict.get(unit))
    srcFolder = unitID+unit
    trgtFolder = trgtPath+unit+'/LIS/'
    arcpy.AddMessage('processing: '+unitID + ' '+unit)
    #for layer in inputlayer:
    #    layer = layer
    for ext in filetype:
        srcFile = srcPath+srcFolder+'/Addresses'+ext
        trgtFile = trgtFolder+'Addresses'+ext
        arcpy.AddMessage('source file: '+srcFile)
        arcpy.AddMessage('target file: '+trgtFile)
        #manual format:  shutil.copyfile('J:/data/Shapefiles/01AlleganTwp/Parcels.shp','J:/data/Shapefiles/01AlleganTwp/archive/Parcels.shp')
        shutil.copyfile(srcFile,trgtFile)
