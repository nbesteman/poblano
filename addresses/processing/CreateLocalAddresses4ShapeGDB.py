#-------------------------------------------------------------------------------
#    Name:  CreateLocalAddresses2Shape.py
# Purpose:  Edit table schema for next step of processing into local unit shapefiles.
#  Author:  Neil Besteman
# Created:  20170705
# Modified: 20170705
# Modified: 20171220 adapted to new schema adding additiona drop fields
#    Input: J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses
#   Output: J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses4LocalShp
#    Notes: https://gis.stackexchange.com/questions/152481/how-to-delete-selected-rows-using-arcpy
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy,os,shutil

arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/"
#arcpy.env.workspace = "source/AddressData.gdb/"
fc = "Addresses4LocalShp"
if arcpy.Exists(fc):
    arcpy.AddMessage("deleting old version of Addresses4LocalShp")
    arcpy.Delete_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses4LocalShp", data_type="FeatureClass")
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses4LocalShp", data_type="FeatureClass")
else:
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses4LocalShp", data_type="FeatureClass")
arcpy.AddMessage("created new version of Addresses4LocalShp")
arcpy.DeleteField_management(in_table="Addresses4LocalShp", drop_field="GlobalID;created_user;created_date;last_edited_user;last_edited_date;UNOCCUPIED;PROBLEM;LATITUDE;LONGITUDE;NOTES;ENTITYID;ADDRESS1;ADDRESS2;NUMBER1;NUMBERSUP1;PREDIREC0;NAME1;SUFFIX1;POSTDIRE0;SUPPLEME0;NUMBER2;NUMBERSUP2;PREDIREC1;NAME2;SUFFIX2;POSTDIRE1;SUPPLEME1;PARETIRED;A1RETIRED;A2RETIRED;O99;O04;O05;O06;VERIFIED;SOURCE;NAME0;SOURCE0;MCD_DIV;UNCORP;NHBRHD;HSENO_PRE;ST_PREMOD;ST_POSTMOD;ESN;PSAP;MSAGCOM;BLDG;FLOOR;ROOM;UNIT;SEAT;LANDMARK;LOC;PLC_TYPE;SLOC_TYPE;RCL_ID;TAX_PIN;COLL_MTHD;EXCEPTION;FLAG;PREDIR1;POSTDIR1;SUPPLEM1;PREDIR2;POSTDIR2;SUPPLEM2;BUSNAME;BUSSOURCE;ROADNAME")
arcpy.AddMessage("deleted fields from Addresses4LocalShp")

arcpy.AddMessage("finished processing")
