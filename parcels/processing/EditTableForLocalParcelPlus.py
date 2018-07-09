#-------------------------------------------------------------------------------
# Name:     edit_table
# Purpose:  Edit table schema for parcelsplus.
# Author:   Neil Besteman
# Created:  20170925
# Modified:
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy

#rename fields
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="MAPPING_ID", new_field_name="PARCELID", new_field_alias="", field_type="TEXT", field_length="20", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="ownername1", new_field_name="owner", new_field_alias="", field_type="TEXT", field_length="35", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="ownerstreetaddr", new_field_name="owner_addr", new_field_alias="", field_type="TEXT", field_length="35", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="ownercity", new_field_name="owner_city", new_field_alias="", field_type="TEXT", field_length="25", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="ownerstate", new_field_name="ownerstate", new_field_alias="", field_type="TEXT", field_length="2", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="ownerzip", new_field_name="owner_zip", new_field_alias="", field_type="TEXT", field_length="10", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="ownercareof", new_field_name="ownercare", new_field_alias="", field_type="TEXT", field_length="35", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="propstreetcombined", new_field_name="propaddrss", new_field_alias="", field_type="TEXT", field_length="62", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="schooldist", new_field_name="schooldist", new_field_alias="", field_type="TEXT", field_length="5", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="zoning", new_field_name="zoning", new_field_alias="", field_type="TEXT", field_length="15", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="propclass", new_field_name="propclass", new_field_alias="", field_type="TEXT", field_length="5", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="genericlistitem", new_field_name="PDR", new_field_alias="", field_type="TEXT", field_length="30", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="ass", new_field_name="assessment", new_field_alias="", field_type="LONG", field_length="4", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="tax", new_field_name="taxable", new_field_alias="", field_type="LONG", field_length="", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="neighborhood", new_field_name="neighborhd", new_field_alias="", field_type="TEXT", field_length="10", field_is_nullable="NULLABLE", clear_field_alias="true")
##xxxxxarcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="homestead", new_field_name="homestead", new_field_alias="", field_type="FLOAT", field_length="", field_is_nullable="NULLABLE", clear_field_alias="true")
##xxxxarcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="MayPRE", new_field_name="MayPRE", new_field_alias="", field_type="FLOAT", field_length="", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="liberpage", new_field_name="liber_page", new_field_alias="", field_type="TEXT", field_length="20", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="taxpayname", new_field_name="tax_name", new_field_alias="", field_type="TEXT", field_length="35", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="taxpaycareof", new_field_name="tax_careof", new_field_alias="", field_type="TEXT", field_length="35", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="taxpaystreetaddr", new_field_name="tax_addres", new_field_alias="", field_type="TEXT", field_length="35", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="taxpaycity", new_field_name="tax_city", new_field_alias="", field_type="TEXT", field_length="25", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="taxpaystate", new_field_name="tax_state", new_field_alias="", field_type="TEXT", field_length="2", field_is_nullable="NULLABLE", clear_field_alias="true")
arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp", field="taxpayzip", new_field_name="tax_zip", new_field_alias="", field_type="TEXT", field_length="10", field_is_nullable="NULLABLE", clear_field_alias="true")

#drop fields
#arcpy.DeleteField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_ParcelsPlus_shp",
#                             drop_field="Rework;"+"Creator;Created;Editor;Edited;Comment;Prop_Addre;CENTER;CENTERY;ANGLE;OFFSETX;OFFSETY;"+
#                                        "Com;ERROR;Status;Changed;ExtraText1;ExtraText2;ExtraDbl1;ExtraDbl2;propaddress;prim_unit;ass_mailzip;"+
#                                        "exemptcode;mapnum;usernum;useCode;overAllStatus;isExempt;propstatus;shortnotes")
