#-------------------------------------------------------------------------------
# Name:     ReprojectRoads.py
# Purpose:  convert data to projection needed by NewWorld
# Author:   Bryan May
# Created:  20171128
# Modified:
# Input:  J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW
# Output:  J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/tmpRoadsNW_Proj
#-------------------------------------------------------------------------------
import arcpy

ws = "J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/"
arcpy.env.workspace = ws

newFc = "tmpRoadsNW_Proj"
rdFc = "tmpRoadsNW"
tmpTbl = "NW_Alternate_Name"

if arcpy.Exists(newFc):
    arcpy.AddMessage("Deleting old version of Roads_For_NW...")

    arcpy.Delete_management(in_data = newFc, data_type="FeatureClass")

    arcpy.Project_management(in_dataset= rdFc, out_dataset = newFc, out_coor_system="GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", transform_method="", in_coor_system="PROJCS['NAD_1983_StatePlane_Michigan_South_FIPS_2113_Feet_Intl',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',13123359.58005249],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-84.36666666666666],PARAMETER['Standard_Parallel_1',42.1],PARAMETER['Standard_Parallel_2',43.66666666666666],PARAMETER['Latitude_Of_Origin',41.5],UNIT['Foot',0.3048]]", preserve_shape="NO_PRESERVE_SHAPE", max_deviation="", vertical="NO_VERTICAL")
else:
    arcpy.Project_management(in_dataset= rdFc, out_dataset = newFc , out_coor_system="GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]", transform_method="", in_coor_system="PROJCS['NAD_1983_StatePlane_Michigan_South_FIPS_2113_Feet_Intl',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',13123359.58005249],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-84.36666666666666],PARAMETER['Standard_Parallel_1',42.1],PARAMETER['Standard_Parallel_2',43.66666666666666],PARAMETER['Latitude_Of_Origin',41.5],UNIT['Foot',0.3048]]", preserve_shape="NO_PRESERVE_SHAPE", max_deviation="", vertical="NO_VERTICAL")
