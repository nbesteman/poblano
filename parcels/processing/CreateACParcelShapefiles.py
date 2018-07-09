#-------------------------------------------------------------------------------
# Name:        CreateUnitParcelShapefiles
# Purpose:     To create individual unit parcels layer in shapefile format.
# Author:      Neil Besteman
# Created:     20170615
# Modified:    20171102
# Input: J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/AC_Parcels_Combined_2_shapefiles
# Output:  J:\Apps\Python\LayerUpdates\parcels\build_ACparcels\AC_Parcels_Combined.shp
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import arcpy,os,shutil

#delete files located in build folder
folder = 'J:\Apps\Python\LayerUpdates\parcels\\build_ACparcels'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #If you also want to remove subdirectories, uncomment the elif statement.
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/"
arcpy.AddMessage("processing: Countywide shapefile conversion of AC_Parcels_Combined")
arcpy.FeatureClassToShapefile_conversion(Input_Features="AC_Parcels_Combined_2_Shapefiles", Output_Folder="J:/Apps/Python/LayerUpdates/parcels/build_ACparcels")
arcpy.AddMessage ("Finished processsing.  Now manually rename and place in data folder.")
