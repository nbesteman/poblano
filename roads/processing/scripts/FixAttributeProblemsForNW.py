#-------------------------------------------------------------------------------
# Name:        FixAttributeProblemsForNW.py
# Purpose:     Fix attribute issues for NewWorld
# Author:      Neil Besteman
# Created:     20171109
# Modified:    20171127
# Input:    J:/Apps/Python/LayerUpdates/roads/source/Parcels_Combined.gdb/tmpRoadsNW.FENAME
# Output:   J:/Apps/Python/LayerUpdates/roads/source/Parcels_Combined.gdb/tmpRoadsNW.ROADNAME
#-------------------------------------------------------------------------------
import arcpy, time, sys, os

arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/roads/source/Roads.gdb/"
fc = "tmpRoadsNW"
xVal = ''

fields = ['ROADNAME','FENAME','FETYPE']
sHwy = ['FENAME = \'M 40\'','FENAME = \'M 89\'','FENAME = \'M 179\'', 'FENAME = \'M 222\'']
dict = {'M 40':'M40 HWY','M 89':'M89 HWY','M 179':'M179 HWY','M 222':'M222 HWY'}

#passes 'FENAME = \'M 40\''
def roadName(where):
    # Create update cursor for feature class
    counter = 0
    arcpy.AddMessage('processing ' + where)
    with arcpy.da.UpdateCursor(fc, fields, where) as cursor:
        for row in cursor:
            Hwy = row[1]
            #cursor.updateRow(row)
            xVal = (dict.get(Hwy))
            #arcpy.AddMessage('Hwy = '+ Hwy)
            #arcpy.AddMessage('xVal = '+ xVal)
            Hwy = Hwy.replace(" ","")
            row[0] = xVal
            #row[1] = Hwy
            row[2] = 'HWY'
            cursor.updateRow(row)
        counter +=1

for value in sHwy:
    roadName(value)
    time.sleep(3)
