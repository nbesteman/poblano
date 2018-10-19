#-------------------------------------------------------------------------------
# Name:     AppendGeoAdd2_to_GEoAddresses
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20180716
# Modified  20181016 change M-89 to M89, M-40 to M40, etc
#https://gis.stackexchange.com/questions/89362/using-arcpy-update-cursor-to-replace-null-value/89368
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
arcpy.env.workspace = "J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/"
#arcpy.env.workspace = "source/AddressData.gdb/"
fc1 = "Addresses_for_NewWorld"
if arcpy.Exists(fc1):
    arcpy.AddMessage("deleting old version of Addresses_for_NewWorld")
    arcpy.Delete_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses_for_NewWorld", data_type="FeatureClass")
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAdd1", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses_for_NewWorld", data_type="FeatureClass")
else:
    arcpy.Copy_management(in_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/GeoAdd1", out_data="J:/Apps/Python/LayerUpdates/addresses/source/AddressData.gdb/Addresses_for_NewWorld", data_type="FeatureClass")
arcpy.AddMessage("created new version of Addresses_for_NewWorld")

arcpy.Append_management(inputs="GeoAdd2", target="Addresses_for_NewWorld", schema_type="TEST", field_mapping="", subtype="")

# remove null and replace with blank

fieldlist = ['PREDIR','POSTDIR','SUPPLEM','SUFFIX']
#delete records
for field in fieldlist:
    try:
        with arcpy.da.UpdateCursor(fc1,field) as cursor:
            for row in cursor:
                if row[0] == None:
                   row[0] = ''
                   cursor.updateRow(row)
        arcpy.AddMessage("replace null with blank")
        del row
    except:
        print arcpy.GetMessages()
#edit streetnames such as M-89, M-40 to M89, M40
fieldlist2 = ['NAME','SUFFIX','ROADNAME']
#delete records
try:
    with arcpy.da.UpdateCursor(fc1,fieldlist2) as cursor:
        for row in cursor:
#  Michigan Hwy's
            if row[0] == 'M-89':
                row[0] = 'M89'
                row[1] = 'Hwy'
                row[2] = 'M89 Hwy'
            elif row[0] == 'M-40':
                row[0] = 'M40'
                row[1] = 'Hwy'
                row[2] = 'M40 Hwy'
            elif row[0] == 'M 89':
                row[0] = 'M89'
                row[1] = 'Hwy'
                row[2] = 'M89 Hwy'
            elif row[0] == 'M 40':
                row[0] = 'M40'
                row[1] = 'Hwy'
                row[2] = 'M40 Hwy'
            elif row[0] == 'M 222':
                row[0] = 'M222'
                row[1] = 'Hwy'
                row[2] = 'M222 Hwy'
            elif row[0] == 'M-222':
                row[0] = 'M222'
                row[1] = 'Hwy'
                row[2] = 'M222 Hwy'
            elif row[0] == 'M 179':
                row[0] = 'M179'
                row[1] = 'Hwy'
                row[2] = 'M179 Hwy'
            elif row[0] == 'M-179':
                row[0] = 'M179'
                row[1] = 'Hwy'
                row[2] = 'M179 Hwy'
# Freeways
            elif row[2] == 'US 131 HWY':
                row[0] = 'US131'
                row[1] = 'Hwy'
                row[2] = 'US131 HWY'
            elif row[2] == 'NB US 131 HWY':
                row[0] = 'US131'
                row[1] = 'Hwy'
                row[2] = 'NB US131 HWY'
            elif row[2] == 'SB US 131 HWY':
                row[0] = 'US131'
                row[2] = 'SB US131 HWY'
            elif row[2] == 'I 196 HWY':
                row[0] = 'I196'
                row[1] = 'Hwy'
                row[2] = 'I196 HWY'
            elif row[2] == 'NB I 196 HWY':
                row[0] = 'I196'
                row[1] = 'Hwy'
                row[2] = 'NB I196 HWY'
            elif row[2] == 'SB I 196 HWY':
                row[0] = 'I196'
                #row[1] = 'Hwy'
                row[2] = 'SB I196 HWY'
# Freeway exits have no space in the raw data.   fieldlist2 = ['NAME','SUFFIX','ROADNAME']
            elif row[0] == 'Exit I196':
                row[0] = 'Exit I196'
                row[1] = 'Hwy'
                row[2] = 'Exit I196 HWY'
            elif row[0] == 'Exit NB I196':
                row[0] = 'Exit NB I196'
                row[1] = 'Hwy'
                row[2] = 'Exit NB I196 HWY'
            elif row[0] == 'Exit SB I196':
                row[0] = 'Exit SB I196'
                row[1] = 'Hwy'
                row[2] = 'Exit SB I196 HWY'
            elif row[0] == 'Exit EB I196':
                row[0] = 'Exit EB I196'
                row[1] = 'Hwy'
                row[2] = 'Exit EB I196 HWY'
            elif row[0] == 'Exit WB I196':
                row[0] = 'Exit WB I196'
                row[1] = 'Hwy'
                row[2] = 'Exit WB I196 HWY'
            cursor.updateRow(row)
        arcpy.AddMessage("M-89 to M89, M-40 to M40, etc")
        del row
except:
    print arcpy.GetMessages()
