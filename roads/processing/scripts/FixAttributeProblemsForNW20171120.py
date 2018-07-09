#-------------------------------------------------------------------------------
# Name:        FixAttributeProblemsForNW.py
# Purpose:     Fix attribute issues for NewWorld
# Author:      Neil Besteman
# Created:     20171109
# Modified:    20171117
# Input:    J:/Apps/Python/LayerUpdates/roads/source/Parcels_Combined.gdb/Co5_RoadsforNW
# Output:   J:/Apps/Python/LayerUpdates/roads/source/Parcels_Combined.gdb/Co5_RoadsforNW
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/"
fc = "tmpRoadsNW"
counter = 0
counter40 = 0
counter89 = 0
counter179 = 0
counter222 = 0

#where = 'where instr(1,Roadname,"M 40")>0'
fields = ['Roadname']

#where = 'CountyL = 139'
where40 = 'FENAME = \'M 40\''
where89 = 'FENAME = \'M 89\''
where179 = 'FENAME = \'M 179\''
where222 = 'FENAME = \'M 222\''
#where = 'instr(1,[Roadname],"M 40")>0'
arcpy.AddMessage(counter)
# Create update cursor for feature class
with arcpy.da.UpdateCursor(fc, fields, where) as cursor:
    #problem with using where like this
#with arcpy.da.UpdateCursor(fc, fields) as cursor:
    # For each row, evaluate the COUNTYL value (index position
    # of 0), and update VENUE_L (index position of 1)
    for row in cursor:
        counter +=1
        if (where40):
            row[0] = 'M40 Hwy'
            cursor.updateRow(row)
            arcpy.AddMessage('M40'+str(counter40))
            counter40 +=1
        elif (where89):
            row[0] = 'M89 Hwy'
            cursor.updateRow(row)
            arcpy.AddMessage('M89'+str(counter89))
            counter89 +=1
        elif (where179):
            row[0] = 'M179 Hwy'
            cursor.updateRow(row)
            arcpy.AddMessage('M179'+str(counter179))
            counte179r +=1
        elif (where222):
            row[0] = 'M222 Hwy'
            cursor.updateRow(row)
            arcpy.AddMessage('M222'+str(counter222))
            counter222 +=1

#this worked:
#with arcpy.da.UpdateCursor(fc, fields, where) as cursor:
#    for row in cursor:
#        counter +=1
#        if (where):
#            arcpy.AddMessage(counter)
