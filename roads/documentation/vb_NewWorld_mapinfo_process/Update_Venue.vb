Include "Update_CADmap_Layers.Def"

Sub Update_Venue  ' add venues

'Alter Table "Src" ( add VENUE_L Char(20), VENUE_R Char(20) )
'update Venue left and right
	Open Table "J:\data\00 Allegan Co\ac units.tab" as Unit
	Dim sUnit,sFMCD as String
	Fetch First from Unit
        Do while not EOT(unit)
         sFMCD = Unit.FMCD
         sUnit = Unit.Unit
         Select * from tmpRoads where FMCDL = sFMCD into tmpLeft
          update tmpLeft set VENUE_L = sUnit
          Commit Table tmpRoads
         Select * from tmpRoads where FMCDR = sFMCD into tmpRight
          update tmpRight set VENUE_R = sUnit					
          Commit Table tmpRoads				
         Fetch Next from Unit					
        Loop
Close Table tmpLeft
Close Table tmpRight

Select * from tmpRoads where CountyL = 15 into tmp
	Update tmp set VENUE_L = "Barry Co"
Select * from tmpRoads where CountyR = 15 into tmp
	Update tmp set VENUE_R = "Barry Co"
Select * from tmpRoads where CountyL = 77 into tmp
	Update tmp set VENUE_L = "Kalamazoo Co"
Select * from tmpRoads where CountyR = 77 into tmp
	Update tmp set VENUE_R = "Kalamazoo Co"
Select * from tmpRoads where CountyL = 81 into tmp
	Update tmp set VENUE_L = "Kent Co"
Select * from tmpRoads where CountyR = 81 into tmp
	Update tmp set VENUE_R = "Kent Co"
Select * from tmpRoads where CountyL = 139 into tmp
	Update tmp set VENUE_L = "Ottawa Co"
Select * from tmpRoads where CountyR = 139 into tmp
	Update tmp set VENUE_R = "Ottawa Co"
Select * from tmpRoads where CountyL = 159 into tmp
	Update tmp set VENUE_L = "Van Buren Co"
Select * from tmpRoads where CountyR = 159 into tmp
	Update tmp set VENUE_R = "Van Buren Co"

 Commit Table tmpRoads Interactive
 Alter Table tmpRoads(
     drop COUNTYL,COUNTYR )
Close Table Unit
      Print "venues have been updated"
End Sub 'Update_Venue
