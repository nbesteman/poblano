#-------------------------------------------------------------------------------
# Name:     edit_table
# Purpose:  Edit table schema for export to MapInfo EQ version
# Author:   Neil Besteman
# Created:  20171018
# Modified:  20171025
#Input:J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfoEQ_EQ"
#Output:J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfoEQ_EQ"
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy

#drop fields
arcpy.DeleteField_management(in_table="J:\Apps\Python\LayerUpdates\parcels\source\Parcels_Combined.gdb\AC_Parcels_Combined_2_MapInfoEQ",
                             drop_field="Status;"+
                             "Changed;"+
                             "ExtraText1;"+
                             "ExtraDbl1;"+
                             "ExtraText2;"+
                             "ExtraDbl2;"+
                             "Rework;"+
                             "Creator;"+
                             "Created;"+
                             "Editor;"+
                             "Edited;"+
                             "GlobalID;"
                             )
