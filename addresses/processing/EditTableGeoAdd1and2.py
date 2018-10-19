#-------------------------------------------------------------------------------
# Name:     edit_table_GeoAdd1and2.py
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20180713
# Modified: 20180716
# Modifiwed: 20181019 populated source column with primary and secondary addresses
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/"
#edit GeoAdd1
arcpy.DeleteField_management(in_table= "GeoAdd1", drop_field="NUMBER1;PREDIR1;NAME1;SUFFIX1;POSTDIR1;SUPPLEM1;NUMBERSUP1")

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

fc = "GeoAdd2"
fields = ['NUMBER']
with arcpy.da.UpdateCursor(fc,fields) as cursor:
    for row in cursor:
        #delete records with no number assigned
        if row[0] == '':
            cursor.deleteRow()
        if row[0] == ' ':
            cursor.deleteRow()
        if row[0] == None:
            cursor.deleteRow()
arcpy.AddMessage("deleted addresses where null or with no number or a space as a number")

arcpy.CalculateField_management(in_table="GeoAdd1", field="Source", expression='"primary"', expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="GeoAdd2", field="Source", expression='"secondary"', expression_type="PYTHON_9.3", code_block="")

# Replace a layer/table view name with a path to a dataset (which can be a layer file) or create the layer/table view within the script
# The following inputs are layers or table views: "GeoAdd2"
#arcpy.CalculateField_management(in_table="GeoAdd2", field="ROADNAME", expression="!PREDIR! +' '+ !NAME!+ ' ' + !SUFFIX!", expression_type="PYTHON_9.3", code_block="")
arcpy.CalculateField_management(in_table="GeoAdd2", field="ROADNAME", expression="(!PREDIR! +' '+ !NAME!+ ' ' + !SUFFIX!).strip()", expression_type="PYTHON_9.3", code_block="")
