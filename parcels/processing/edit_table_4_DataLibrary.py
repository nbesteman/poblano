#-------------------------------------------------------------------------------
# Name:     edit_table
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20170620
# Modified: 20171023
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
#rename fields
#end result of parcels in parcel data is PARCELID, PROPADDRSS,SCHOOLDIST,PROPCLASS


arcpy.AlterField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_DataLibrary", field="MAPPING_ID", new_field_name="PARCELID", new_field_alias="", field_type="TEXT", field_length="20", field_is_nullable="NULLABLE", clear_field_alias="true")
#drop fields
arcpy.DeleteField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_DataLibrary", drop_field="DEED_ACRES;ACRES;COMMENT;ERROR;LABEL;CENTERX;CENTERY;ANGLE;OFFSETX;OFFSETY;Status;Changed;Extra1;ExtraText1;ExtraDbl1;Rework;Creator;Created;Editor;Edited;ownername1;ownerstreetaddr;ownercity;ownerstate;ownerzip;ownercareof;zoning;liberpage;taxpayname;taxpaycareof;taxpaycity;taxpaystate;taxpayzip;totalacres;prim_unit;ass_mailzip;propaddrdirect;propstreetname;propstreetcombined;taxpaystreetaddr;usernum;isExempt;genericlistitem;neighborhood;exemptcode;mapnum;useCode;overAllStatus;isExcept;propstatus;shortnotes;MayPRE;homestead;qualag;year;landass;ass;tax")
