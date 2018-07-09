Include "Update_CADmap_Layers.Def"

Sub CREATE_TEMPROAD_LAYER
Set Event Processing Off
Set ProgressBars  Off
'Open Source Table and save into New World Table
Open Table "J:\Data\00 Allegan Co\AC Roads.TAB" as AC_Roads 'Interactive
Commit Table AC_Roads As DISPATCH_APPS+"Update_CADmap_Layers\temp\tmpRoads.TAB" TYPE NATIVE Charset "WindowsLatin1"
Close Table AC_Roads
Open Table DISPATCH_APPS+"Update_CADmap_Layers\TEMP\tmpRoads.TAB" Interactive
'Drop unnecessary attributes
'20120222 change data type for zipcode from int to char
Alter Table "tmpRoads" (
                        'drop USCL,USCR,STSL,STSR,STHL,STHR,CCDL,CCDR,SDL,SDR,PCTL,PCTR,SDPL,SDPR,VPL,VPR,Classification,Surface,Restrictions,SnowRemoval,ShoulderWidth 
			'drop USCL,USCR,STSL,STSR,STHL,STHR,CCDL,CCDR,SDL,SDR,PCTL,PCTR,SDPL,SDPR,VPL,VPR,Restrictions,SnowRemoval,ShoulderWidth 
			modify ZIPL Char(5),ZIPR Char(5)
			drop USCL,USCR,STSL,STSR,STHL,STHR,SDL,SDR,Restrictions,SnowRemoval,ShoulderWidth 
                        add VENUE_L char(20), VENUE_R char(20),CITYL char(20),CITYR char(20),JOIN_ID char(10)
                       ) Interactive
Call APPEND_FRAMEWORK_ROADS
Call Update_City
Call FLIP_LINE_DIRECTION	'Flip line direction for arcs whose address range doesn't increase in the direction of the arc
Commit Table tmpRoads
Call Update_Venue

'update Venue left and right
'	Open Table "J:\data\00 Allegan Co\ac units.tab" as Unit
'	Dim sUnit,sFMCD as String
'	Fetch First from Unit
'       Do while not EOT(unit)
'         sFMCD = Unit.FMCD
'         sUnit = Unit.Unit
'         Select * from tmpRoads where FMCDL = sFMCD into tmpLeft
'          update tmpLeft set VENUE_L = sUnit
'          Commit Table tmpRoads
'         Select * from tmpRoads where FMCDR = sFMCD into tmpRight
'          update tmpRight set VENUE_R = sUnit					
'          Commit Table tmpRoads				
'         Fetch Next from Unit					
'        Loop
'Close Table tmpLeft
'Close Table TmpRight	

'Modify FENAME and Roadname listings for M series where space
Select * from tmpRoads where instr(1,Roadname,"M 40")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M 40")-1)+"M40 Hwy"+mid$(Roadname,instr(1,Roadname,"M 40")+4,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M 40")-1)+"M40"+mid$(FENAME,instr(1,FENAME,"M 40")+4,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"
Commit Table tmpRoads
close Table TempSelect
close Table TempSelect2
Select * from tmpRoads where instr(1,Roadname,"M 89")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M 89")-1)+"M89 Hwy"+mid$(Roadname,instr(1,Roadname,"M 89")+4,30)  'changes M 89 to M89 hwy in Roadname
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M 89")-1)+"M89"+mid$(FENAME,instr(1,FENAME,"M 89")+4,30)                'changes M 89 into M89 in FENAME
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"
Commit Table tmpRoads
close Table TempSelect
close Table TempSelect2
Select * from tmpRoads where instr(1,Roadname,"M 222")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M 222")-1)+"M222 Hwy"+mid$(Roadname,instr(1,Roadname,"M 222")+5,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M 222")-1)+"M222"+mid$(FENAME,instr(1,FENAME,"M 222")+5,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"
Commit Table tmpRoads
close Table TempSelect
close Table TempSelect2
Select * from tmpRoads where instr(1,Roadname,"M 179")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M 179")-1)+"M179 Hwy"+mid$(Roadname,instr(1,Roadname,"M 179")+5,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M 179")-1)+"M179"+mid$(FENAME,instr(1,FENAME,"M 179")+5,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"
Commit Table tmpRoads
close Table TempSelect
close Table TempSelect2

'Modify FENAME and Roadname listings for M series where dash
Select * from tmpRoads where instr(1,Roadname,"M-40")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M-40")-1)+"M40 Hwy"+mid$(Roadname,instr(1,Roadname,"M-40")+4,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M-40")-1)+"M40"+mid$(FENAME,instr(1,FENAME,"M-40")+4,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"
Commit Table tmpRoads
Select * from tmpRoads where instr(1,Roadname,"M-89")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M-89")-1)+"M89 Hwy"+mid$(Roadname,instr(1,Roadname,"M-89")+4,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M-89")-1)+"M89"+mid$(FENAME,instr(1,FENAME,"M-89")+4,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"
Commit Table tmpRoads
Select * from tmpRoads where instr(1,Roadname,"M-222")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M-222")-1)+"M222 Hwy"+mid$(Roadname,instr(1,Roadname,"M-222")+5,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M-222")-1)+"M222"+mid$(FENAME,instr(1,FENAME,"M-222")+5,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"
Commit Table tmpRoads
Select * from tmpRoads where instr(1,Roadname,"M-179")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M-179")-1)+"M179 Hwy"+mid$(Roadname,instr(1,Roadname,"M-179")+5,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M-179")-1)+"M179"+mid$(FENAME,instr(1,FENAME,"M-179")+5,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"
Commit Table tmpRoads

'cleanup
Close All
'Set Event Processing On
'Set ProgressBars  On
End Sub
