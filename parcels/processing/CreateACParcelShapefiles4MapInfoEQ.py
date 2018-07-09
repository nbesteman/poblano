#-------------------------------------------------------------------------------
# Name:        CreateUnitParcelShapefiles for MapinfoEQ
# Purpose:     To create a AC parcels comb in shapefile format for use with MapInfo
# Author:      Neil Besteman
# Created:     20171023
# Modified:    20171025 changed out path
# Input:       J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_MapInfoEQ
# Output:      J:/Apps/Python/LayerUpdates/parcels/processing/shapes/intlft/EQ/AC_ParcelsEQ_IntlFt.shp
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import arcpy,os,shutil

#delete files located in build folder
folder = 'J:\Apps\Python\LayerUpdates\parcels\processing\shapes\intlft\EQ'
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

arcpy.AddMessage("processing: AC_Parcels_Combined_2_MapInfoEQ to shapefile for MapInfo conversion")
os.system('explorer "J:\Apps\Python\LayerUpdates\parcels\processing\shapes\intlft\EQ"')
arcpy.FeatureClassToShapefile_conversion(Input_Features="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_MapInfoEQ",
Output_Folder="J:/Apps/Python/LayerUpdates/parcels/processing/shapes/intlft/EQ")

arcpy.AddMessage("processing: reprojection to meters")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
