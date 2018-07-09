Include "Update_CADmap_Layers.Def"

Sub Update_City  ' add CITYL and CITYR based on zipl and zipr fields
Open Table "J:\data\00 Allegan Co\AC ZIP Codes.TAB" as Zippy
Dim sZip,sCity as String
fetch first from Zippy
Do while not EOT(Zippy)
	sZip = Zippy.Zip
	sCity = Zippy.City
          Select * from tmpRoads where ZIPL = sZip into tmpZipL
          update tmpZipL set CITYL = sCity
          Commit Table tmpRoads
          Select * from tmpRoads where ZIPR = sZip into tmpZipR
          update tmpZipR set CITYR = sCity
          Commit Table tmpRoads								
         Fetch Next from Zippy					
        Loop
'Add Column "tmpRoads" (CITYL )From Zippy Set To City Where ZIPL = ZIP
'Add Column "tmpRoads" (CITYR )From Zippy Set To City Where ZIPR = ZIP
	Commit Table tmpRoads Interactive
Close Table Zippy
Close Table tmpZipL
Close Table tmpZipR
      Print "zip codes have been updated"
End Sub 'Update_City
