#-------------------------------------------------------------------------------
# Name:     edit_table_GeoAddress2.py
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20180713
# Modified:
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/"
#delete primary address fields
#drop fields
arcpy.DeleteField_management(in_table= "GeoAdd2", drop_field="NUMBER;PREDIR;NAME;SUFFIX;POSTDIR;SUPPLEM")

#rename fields
arcpy.AlterField_management(in_table="GeoAdd2", field="NUMBER1", new_field_name="NUMBER", new_field_alias="", field_type="TEXT", field_length="5", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="GeoAdd2", field="NAME1", new_field_name="NAME", new_field_alias="", field_type="TEXT", field_length="40", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="GeoAdd2", field="PREDIR1", new_field_name="PREDIR", new_field_alias="", field_type="TEXT", field_length="2", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="GeoAdd2", field="SUFFIX1", new_field_name="SUFFIX", new_field_alias="", field_type="TEXT", field_length="4", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="GeoAdd2", field="POSTDIR1", new_field_name="POSTDIR", new_field_alias="", field_type="TEXT", field_length="2", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="GeoAdd2", field="SUPPLEM1", new_field_name="SUPPLEM", new_field_alias="", field_type="TEXT", field_length="30", field_is_nullable="NULLABLE", clear_field_alias="true")
