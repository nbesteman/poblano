#-------------------------------------------------------------------------------
# Name:        CreateUnitParcelShapefiles
# Purpose:     To create individual unit parcels layer in shapefile format.
# Author:      Neil Besteman
# Created:     20171109
# Modified:
# Input:    J:/Apps/Python/LayerUpdates/roads/source/Parcels_Combined.gdb/Co5_RoadsforNW
# Output:   J:/Apps/Python/LayerUpdates/roads/source/Parcels_Combined.gdb/Co5_RoadsforNW
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/"
fc = "County5_RoadsforNW"
fieldsL = ['COUNTYL', 'VENUE_L']
fieldsR = ['COUNTYR', 'VENUE_R']

# Create update cursor for feature class
with arcpy.da.UpdateCursor(fc, fieldsL) as cursor:
    # For each row, evaluate the COUNTYL value (index position
    # of 0), and update VENUE_L (index position of 1)
    for row in cursor:
        if (row[0] == 15):
            row[1] = 'Barry Co'
        elif (row[0] == 77):
            row[1] = 'Kalamazoo Co'
        elif (row[0] == 81):
            row[1] = 'Kent Co'
        elif (row[0] == 139):
            row[1] = 'Ottawa Co'
        elif (row[0] == 159):
            row[1] = 'Van Buren Co'
        # Update the cursor with the updated list
        cursor.updateRow(row)

with arcpy.da.UpdateCursor(fc, fieldsR) as cursor:
    # For each row, evaluate the COUNTYR value (index position
    # of 0), and update VENUE_R (index position of 1)
    for row in cursor:
        if (row[0] == 15):
            row[1] = 'Barry Co'
        elif (row[0] == 77):
            row[1] = 'Kalamazoo Co'
        elif (row[0] == 81):
            row[1] = 'Kent Co'
        elif (row[0] == 139):
            row[1] = 'Ottawa Co'
        elif (row[0] == 159):
            row[1] = 'Van Buren Co'
        # Update the cursor with the updated list
        cursor.updateRow(row)
