#-------------------------------------------------------------------------------
# Name:        CreateUnitParcelShapefiles
# Purpose:     To create a AC parcels comb in shapefile format for use with MapInfo
# Author:      Neil Besteman
# Created:     20170623
# Modified:    20170623
# Input        J:\Apps\Python\LayerUpdates\parcels\processing\shapes\intlft\AC_ParcelsComb_IntlFt.shp
# Output       J:/Apps/Python/LayerUpdates/parcels/processing/shapes/meters/AC_ParcelsComb_meters.shp
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy,os,shutil

#delete files located in build folder
folder = 'J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #If you also want to remove subdirectories, uncomment the elif statement.
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)

arcpy.AddMessage("processing: reprojecting to meters")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "AC_ParcelsComb_IntlFt"
arcpy.Project_management(in_dataset="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\intlft\AC_ParcelsComb_IntlFt.shp", out_dataset="J:/Apps/Python/LayerUpdates/parcels/processing/shapes/meters/AC_ParcelsComb_meters.shp", out_coor_system="PROJCS['NAD_1983_StatePlane_Michigan_South_FIPS_2113',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',4000000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-84.36666666666666],PARAMETER['Standard_Parallel_1',42.1],PARAMETER['Standard_Parallel_2',43.66666666666666],PARAMETER['Latitude_Of_Origin',41.5],UNIT['Meter',1.0]]", transform_method="", in_coor_system="PROJCS['NAD_1983_StatePlane_Michigan_South_FIPS_2113_Feet_Intl',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',13123359.58005249],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-84.36666666666666],PARAMETER['Standard_Parallel_1',42.1],PARAMETER['Standard_Parallel_2',43.66666666666666],PARAMETER['Latitude_Of_Origin',41.5],UNIT['Foot',0.3048]]", preserve_shape="NO_PRESERVE_SHAPE", max_deviation="", vertical="NO_VERTICAL")
arcpy.AddMessage("processing: reprojected to meters")
