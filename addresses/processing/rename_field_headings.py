#-------------------------------------------------------------------------------
# Name:     AppendGeoAdd2_to_GEoAddresses
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20180716
# Modified  20181016 change M-89 to M89, M-40 to M40, etc
#https://gis.stackexchange.com/questions/89362/using-arcpy-update-cursor-to-replace-null-value/89368
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/"
#arcpy.env.workspace = "source/AddressData.gdb/"
#fc = "Addresses_for_NewWorld"

try:
arcpy.AlterField_management(in_table="Addresses_for_NewWorld", field="NAME", new_field_name="FENAME", new_field_alias="", field_type="TEXT", field_length="40", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="Addresses_for_NewWorld", field="PREDIR", new_field_name="FEDIRP", new_field_alias="", field_type="TEXT", field_length="2", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="Addresses_for_NewWorld", field="SUFFIX", new_field_name="FETYPE", new_field_alias="", field_type="TEXT", field_length="4", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="Addresses_for_NewWorld", field="POSTDIR", new_field_name="FEDIRS", new_field_alias="", field_type="TEXT", field_length="2", field_is_nullable="NULLABLE", clear_field_alias="true")
#arcpy.AlterField_management(in_table="GeoAdd2", field="SUPPLEM1", new_field_name="SUPPLEM", new_field_alias="", field_type="TEXT", field_length="30", field_is_nullable="NULLABLE", clear_field_alias="true")
except:
    print arcpy.GetMessages()
