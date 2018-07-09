#-------------------------------------------------------------------------------
# Name:        FlipLineDirection.py
# Purpose:     Flip address ranges to line direction(maybe)
# Author:      Neil Besteman
# Created:     20171128
# Modified:    20171130
# Input:    J:/Apps/Python/LayerUpdates/roads/source/Parcels_Combined.gdb/tmpRoadsNW_Proj
# Output:   J:/Apps/Python/LayerUpdates/roads/source/Parcels_Combined.gdb/tmpRoadsNW_Proj (*flipped)
#-------------------------------------------------------------------------------
import arcpy, time, sys, os

arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/"


fc = "tmpRoadsNW_Proj"
fields = ['FRADDL', 'TOADDL', 'FRADDR', 'TOADDR', 'ZIPL', 'ZIPR']

def flipRanges():
    # Create update cursor for feature class
    counter = 0
    arcpy.AddMessage('processing')
    with arcpy.da.UpdateCursor(fc, fields) as cursor:
        for row in cursor:
            iFRADDL = row[0]
            iTOADDL = row[1]
            iFRADDR = row[2]
            iTOADDR = row[3]
            iZIPL = row[4]
            iZIPR = row[5]
            iTotal = row[0]+row[1]+row[2]+row[3]
            if iTotal > 0 :
                arcpy.AddMessage(str(iTotal) +" is Greater than zero\n")
                #if (row[1] < row[0]) or (row[3] < row[2]):
                if (iTOADDL < iFRADDL) or (iTOADDR < iFRADDR):
                    arcpy.AddMessage( str(iTOADDL) +" < " + str(iFRADDL) + "or " + str(iTOADDR) + " < " + str(iFRADDR) +"\n")
                    nTOADDR = iFRADDL
                    nFRADDR = iTOADDL
                    nTOADDL = iFRADDR
                    nFRADDL = iTOADDR
                    nZIPL = iZIPR
                    nZIPR = iZIPL
                    row[0] = nFRADDL
                    row[1] = nTOADDL
                    row[2] = nFRADDR
                    row[3] = nTOADDR
                    row[4] = nZIPL
                    row[5] = nZIPR
                    cursor.updateRow(row)
        counter +=1

flipRanges()
time.sleep(25)
