#-------------------------------------------------------------------------------
# Name:     ReplaceTextObjectInMXD
# Purpose:  Edit table schema.
# Author:   Neil Besteman
# Created:  20180919
# Modified:
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

import arcpy
from arcpy import env

env.workspace = r"J:\Apps\Python\LayerUpdates\zoning\processing"
for mxdname in arcpy.ListFiles("*.mxd"):
    print mxdname
    mxd = arcpy.mapping.MapDocument(r"J:\Apps\Python\LayerUpdates\zoning\processing\\" + mxdname)
    for elm in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        if elm.text.startswith('As ammended'):
            elm.text = elm.text.replace('As ammended', 'As amended')
            print elm.text
    mxd.save()
del mxd
