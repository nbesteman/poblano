#-------------------------------------------------------------------------------
# Name:     edit_table
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20170623
# Modified: 20170623
# Input:    J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp
# Output:   J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
#rename fields
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="MAPPING_ID", new_field_name="PARCEL_ID", new_field_alias="", field_type="TEXT", field_length="20", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="ownername1", new_field_name="owner", new_field_alias="", field_type="TEXT", field_length="35", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="ownerstreetaddr", new_field_name="owner_addr", new_field_alias="", field_type="TEXT", field_length="35", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="ownercity", new_field_name="owner_city", new_field_alias="", field_type="TEXT", field_length="25", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="ownerstate", new_field_name="ownerstate", new_field_alias="", field_type="TEXT", field_length="2", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="ownerzip", new_field_name="owner_zip", new_field_alias="", field_type="TEXT", field_length="10", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="ownercareof", new_field_name="ownercare", new_field_alias="", field_type="TEXT", field_length="35", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="propstreetcombined", new_field_name="propaddrss", new_field_alias="", field_type="TEXT", field_length="62", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="schooldist", new_field_name="schooldist", new_field_alias="", field_type="TEXT", field_length="5", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="zoning", new_field_name="zoning", new_field_alias="", field_type="TEXT", field_length="15", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="propclass", new_field_name="propclass", new_field_alias="", field_type="TEXT", field_length="5", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="genericlistitem", new_field_name="PDR", new_field_alias="", field_type="TEXT", field_length="30", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="ass", new_field_name="assessment", new_field_alias="", field_type="LONG", field_length="4", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="tax", new_field_name="taxable", new_field_alias="", field_type="LONG", field_length="", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="homestead", new_field_name="homestead", new_field_alias="", field_type="DOUBLE", field_length="", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="MayPRE", new_field_name="MayPRE", new_field_alias="", field_type="LONG", field_length="", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="liberpage", new_field_name="liber_page", new_field_alias="", field_type="TEXT", field_length="20", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="taxpayname", new_field_name="tax_name", new_field_alias="", field_type="TEXT", field_length="35", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="taxpaycareof", new_field_name="tax_careof", new_field_alias="", field_type="TEXT", field_length="35", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="taxpaystreetaddr", new_field_name="tax_addres", new_field_alias="", field_type="TEXT", field_length="35", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="taxpaycity", new_field_name="tax_city", new_field_alias="", field_type="TEXT", field_length="25", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="taxpaystate", new_field_name="tax_state", new_field_alias="", field_type="TEXT", field_length="2", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\processing\shapes\meters\AC_ParcelsComb_meters.shp", field="taxpayzip", new_field_name="tax_zip", new_field_alias="", field_type="TEXT", field_length="10", field_is_nullable="NULLABLE", clear_field_alias="true")
