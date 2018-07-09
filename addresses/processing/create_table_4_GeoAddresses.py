#-------------------------------------------------------------------------------
# Name:     edit_table
# Purpose:  Edit table schema for NewWorld version of Addresses
# Author:   Neil Besteman
# Created:  20170703
# Modified: 20170707
# Modified: 20171220
#https://gis.stackexchange.com/questions/152481/how-to-delete-selected-rows-using-arcpy
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/"
#arcpy.env.workspace = "source/AddressData.gdb/"
fc = "GeoAddresses"
if arcpy.Exists(fc):
    arcpy.AddMessage("deleting old version of GeoAddresses")
    arcpy.Delete_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAddresses", data_type="FeatureClass")
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAddresses", data_type="FeatureClass")
else:
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAddresses", data_type="FeatureClass")
arcpy.AddMessage("created new version of GeoAddresses")
arcpy.DeleteField_management(in_table="GeoAddresses",
                            drop_field="GlobalID;created_user;created_date;last_edited_user;last_edited_date;COLL_MTHD;EXCEPTION;FLAG;Coll_Mthd;Tax_Pin;Rcl_ID;Sloc_Type;Plc_Type;Loc;"+
                            "Landmark;Seat;Floor;Bldg;MSAGcom;PSAP;ESN;St_Premod;Nhbrhd;Uncorp;MCD_Div;entityID;"+
                            "Latitude;Longitude;Common_Source;Common_Name;Source;Field_Verified;Site_ID;O06;O05;O04;O99;"+
                            "Unoccupied;Hseno_Pre;St_Postmod;Room;Unit;SOURCE0;NAME0;VERIFIED;A2RETIRED;PARETIRED;"+
                            "SUPPLEME1;POSTDIRE1;SUFFIX2;NAME2;PREDIREC1;NUMBERSUP2;NUMBER2;SUPPLEME0;POSTDIRE0;"+
                            "SUFFIX1;NAME1;PREDIREC0;NUMBERSUP1;NUMBER1;")
arcpy.AddMessage("deleted fields from GeoAddresses")

fields = ['NUMBER']
iSpace = 1

#delete addresses with no Number
with arcpy.da.UpdateCursor(fc,fields) as cursor:
    for row in cursor:
        #sObjectID = row[1]
        if row[0] == '':  # and row[4] == 'Sleepy Hollow Beach Resort - Main Office, Delicatessen and Crafts Area':
            cursor.deleteRow()
            arcpy.AddMessage("deleted address with blank number")
        if row[0] == ' ':
            cursor.deleteRow()
            arcpy.AddMessage("deleted address with space")
            #if left(1,row[0]) == any("1","2","3","4","5","6","7","8","9"):
#        if row[0][0] <> any(x):
#            cursor.deleteRow()
#            arcpy.AddMessage(str(sObjectID) + " " + row[0][0])
arcpy.AddMessage("deleted addresses with no number or a space")

#need to append secondary addresses

arcpy.AddMessage("finished processing")

# The following inputs are layers or table views: "Addresses_2_Geodatabase"
#arcpy.CalculateField_management(in_table="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAddresses", field="NUMBER", expression="''", expression_type="PYTHON_9.3", code_block="")
# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "Addresses_2_Geodatabase"
#arcpy.DeleteFeatures_management(in_features="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAddresses")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "GeoAddresses"
#arcpy.DeleteField_management(in_table="GeoAddresses", drop_field="TAX_PIN;COLL_MTHD;EXCEPTION;FLAG")
