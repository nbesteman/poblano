#-------------------------------------------------------------------------------
# Name:     edit_table
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20170703
# Modified: 20170705
# Modified: 20171220 adapted to new schema adding additiona drop fields
#https://gis.stackexchange.com/questions/152481/how-to-delete-selected-rows-using-arcpy
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy,os,shutil

#copy geodatabase and then delete columns
#need to delete geodatabase
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/"
#arcpy.env.workspace = "source/AddressData.gdb/"
fc = "Addresses4CountyShp"
if arcpy.Exists(fc):
    arcpy.AddMessage("deleting old version of Addresses4CountyShp")
    arcpy.Delete_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses4CountyShp", data_type="FeatureClass")
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses4CountyShp", data_type="FeatureClass")
else:
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses4CountyShp", data_type="FeatureClass")
arcpy.AddMessage("created new version of Addresses4CountyShp")
arcpy.DeleteField_management(in_table="Addresses4CountyShp", drop_field="GlobalID;created_user;created_date;last_edited_user;last_edited_date;ENTITYID;ADDRESS1;ADDRESS2;NUMBER1;NUMBERSUP1;PREDIREC0;NAME1;SUFFIX1;POSTDIRE0;SUPPLEME0;NUMBER2;NUMBERSUP2;PREDIREC1;NAME2;SUFFIX2;POSTDIRE1;SUPPLEME1;PARETIRED;A1RETIRED;A2RETIRED;O99;O04;O05;O06;VERIFIED;SOURCE;NAME0;SOURCE0;MCD_DIV;UNCORP;NHBRHD;HSENO_PRE;ST_PREMOD;ST_POSTMOD;ESN;PSAP;MSAGCOM;BLDG;FLOOR;ROOM;UNIT;SEAT;LANDMARK;LOC;PLC_TYPE;SLOC_TYPE;RCL_ID;TAX_PIN;COLL_MTHD;EXCEPTION;FLAG")
arcpy.AddMessage("deleted fields from Addresses4CountyShp")

#delete files located in build folder
folder = 'J:\Apps\Python\LayerUpdates\\addresses\\build'
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        #If you also want to remove subdirectories, uncomment the elif statement.
        #elif os.path.isdir(file_path): shutil.rmtree(file_path)
    except Exception as e:
        print(e)
arcpy.AddMessage("deleted shapefiles in build folder")
arcpy.AddMessage("building shapefiles in build folder")
arcpy.FeatureClassToFeatureClass_conversion(in_features="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses4CountyShp",
                                                out_path="J:/Apps/Python/LayerUpdates/addresses/build",
                                                out_name="Addresses.shp",
                                                where_clause="",
                                                field_mapping='SITE_ID "SITE_ID" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,SITE_ID,-1,-1;ADDRESS "ADDRESS" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,ADDRESS,-1,-1;PROBLEM "PROBLEM" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,PROBLEM,-1,-1;NOTES "NOTES" true true false 250 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,NOTES,-1,-1;PREDIRECTI "PREDIRECTI" true true false 2 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,PREDIRECTI,-1,-1;NUMBER "NUMBER" true true false 5 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,NUMBER,-1,-1;NAME "NAME" true true false 40 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,NAME,-1,-1;SUFFIX "SUFFIX" true true false 4 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,SUFFIX,-1,-1;NUMBERSUP "NUMBERSUP" true true false 4 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,NUMBERSUP,-1,-1;POSTDIRECT "POSTDIRECT" true true false 2 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,POSTDIRECT,-1,-1;SUPPLEMENT "SUPPLEMENT" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,SUPPLEMENT,-1,-1;CITY "CITY" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,CITY,-1,-1;ZIP "ZIP" true true false 5 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,ZIP,-1,-1;UNOCCUPIED "UNOCCUPIED" true true false 2 Short 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,UNOCCUPIED,-1,-1;LATITUDE "LATITUDE" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,LATITUDE,-1,-1;LONGITUDE "LONGITUDE" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,LONGITUDE,-1,-1;COUNTY "COUNTY" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,COUNTY,-1,-1;MUNI "MUNI" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses4CountyShp,MUNI,-1,-1', config_keyword="")

arcpy.AddMessage("finished processing")

#*also was not able to use python to delete features in a geodatabase and then load the data
    #delete Addresses4CountyShapefile
    #arcpy.AddMessage("deleting features in Addresses4CountyShapefile")
    #arcpy.DeleteFeatures_management(in_features="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses4CountyShapefile")
    #arcpy.AddMessage("loading data to Addresses4CountyShapefile")

#---
#this may be handy
    # Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
    # The following inputs are layers or table views: "Addresses4CountyShapefile"
    #arcpy.DeleteField_management(in_table="Addresses4CountyShapefile", drop_field="ADDRESS1;ADDRESS2;NUMBER1;NUMBERSUP1;PREDIREC0;NAME1;SUFFIX1;POSTDIRE0;SUPPLEME0;NUMBER2;NUMBERSUP2;PREDIREC1;NAME2;SUFFIX2;POSTDIRE1;SUPPLEME1;PARETIRED;A1RETIRED;A2RETIRED;O99;O04;O05;O06;VERIFIED;SOURCE;NAME0;SOURCE0;MCD_DIV;UNCORP;NHBRHD;HSENO_PRE;ST_PREMOD;ST_POSTMOD;ESN;PSAP;MSAGCOM;BLDG;FLOOR;ROOM;UNIT;SEAT;LANDMARK;LOC;PLC_TYPE;SLOC_TYPE;RCL_ID;TAX_PIN;COLL_MTHD;EXCEPTION;FLAG")
#---

#this doesn't work either
    #arcpy.FeatureClassToFeatureClass_conversion(in_features="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses", out_path="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb", out_name="Addresses4CountyShapefile", where_clause="", field_mapping='SITE_ID "SITE_ID" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,SITE_ID,-1,-1;ADDRESS "ADDRESS" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,ADDRESS,-1,-1;PROBLEM "PROBLEM" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,PROBLEM,-1,-1;NOTES "NOTES" true true false 250 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,NOTES,-1,-1;PREDIRECTI "PREDIRECTI" true true false 2 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,PREDIRECTI,-1,-1;NUMBER "NUMBER" true true false 5 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,NUMBER,-1,-1;NAME "NAME" true true false 40 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,NAME,-1,-1;SUFFIX "SUFFIX" true true false 4 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,SUFFIX,-1,-1;NUMBERSUP "NUMBERSUP" true true false 4 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,NUMBERSUP,-1,-1;POSTDIRECT "POSTDIRECT" true true false 2 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,POSTDIRECT,-1,-1;SUPPLEMENT "SUPPLEMENT" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,SUPPLEMENT,-1,-1;CITY "CITY" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,CITY,-1,-1;ZIP "ZIP" true true false 5 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,ZIP,-1,-1;ADDRESS1 "ADDRESS1" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,ADDRESS1,-1,-1;UNOCCUPIED "UNOCCUPIED" true true false 2 Short 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,UNOCCUPIED,-1,-1;LATITUDE "LATITUDE" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,LATITUDE,-1,-1;LONGITUDE "LONGITUDE" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,LONGITUDE,-1,-1;ENTITYID "ENTITYID" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,ENTITYID,-1,-1;COUNTY "COUNTY" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,COUNTY,-1,-1;MUNI "MUNI" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,MUNI,-1,-1', config_keyword="")
#for some reson this does not work
    #arcpy.FeatureClassToFeatureClass_conversion(in_features="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses",
    #                                            out_path="J:/Apps/Python/LayerUpdates/addresses/build",
    #                                            out_name="xxxaddresses.shp",
    #                                            where_clause="",
    #                                            field_mapping='SITE_ID "SITE_ID" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,SITE_ID,-1,-1;ADDRESS "ADDRESS" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,ADDRESS,-1,-1;PROBLEM "PROBLEM" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,PROBLEM,-1,-1;NOTES "NOTES" true #true false 250 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,NOTES,-1,-1;PREDIRECTI "PREDIRECTI" true true false 2 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,PREDIRECTI,-1,-1;NUMBER "NUMBER" true true false 5 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,NUMBER,-1,-1;NAME "NAME" true true false 40 Text 0 0 #,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,NAME,-1,-1;SUFFIX "SUFFIX" true true false 4 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,SUFFIX,-1,-1;NUMBERSUP "NUMBERSUP" true true false 4 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,NUMBERSUP,-1,-1;POSTDIRECT "POSTDIRECT" true true false 2 Text 0 0 #,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,POSTDIRECT,-1,-1;SUPPLEMENT "SUPPLEMENT" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,SUPPLEMENT,-1,-1;CITY "CITY" true true false 30 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,CITY,-1,-1;ZIP "ZIP" true true false 5 Text 0 0 #,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,ZIP,-1,-1;UNOCCUPIED "UNOCCUPIED" true true false 2 Short 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,UNOCCUPIED,-1,-1;LATITUDE "LATITUDE" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,LATITUDE,-1,-1;LONGITUDE "LONGITUDE" true true false 8 Double 0 0 #,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,LONGITUDE,-1,-1;ENTITYID "ENTITYID" true true false 8 Double 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,ENTITYID,-1,-1;COUNTY "COUNTY" true true false 20 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,COUNTY,-1,-1;MUNI "MUNI" true true false 50 Text 0 0 #,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,MUNI,-1,-1;ESN "ESN" true true false 50 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,ESN,-1,-1;UNIT "UNIT" true true false 10 Text 0 0 ,First,#,J:\Apps\Python\LayerUpdates\addresses\source\AddressData.gdb\Addresses,UNIT,-1,-1', config_keyword="")
