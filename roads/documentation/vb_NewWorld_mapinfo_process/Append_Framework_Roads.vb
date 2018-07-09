Include "Update_CADmap_Layers.Def"

Sub APPEND_FRAMEWORK_ROADS
'This subroutine works with version 6b

Dim oBoundary as Object

'This next two lines should be moved to a scheduled task update and taken out of this subroutine
'Open Source Framework Roads and clip out 5 county region
'Open Table "J:\Source\Framework\MI Roads.TAB" as MI_Roads Interactive

'Barry = 15
'Kalamazoo = 77
'Kent = 81
'Ottawa = 139
'Van Buren = 159

'Select * from MI_Roads where str$(CountyL) = Any("15","77","81","139","159") or str$(CountyR) = Any("15","77","81","139","159") into Temproads
'Commit Table Temproads As CO_DIRsv+"Co5 Roads.TAB" TYPE NATIVE Charset "WindowsLatin1"
'Close Table MI_Roads

Open Table "J:\Data\00 Allegan Co\Co5 Roads" as Co5roads Interactive
Commit Table Co5roads As "J:\Departments\Dispatch\CADmaps\New Layers\RoadsPlus" TYPE NATIVE Charset "WindowsLatin1"
Close Table Co5roads
Open Table "J:\Departments\Dispatch\CADmaps\New Layers\RoadsPlus" as RoadsPlus Interactive
'Open Table "J:\State\Counties\Counties.tab" as Counties

'Drop unnecessary attributes
'Alter Table "RoadsPlus" ( drop PR,BPT,EPT,LRS_LINK,FNODE_,TNODE_,LENGTH,OID,VER,MGF_HIST) Interactive
Alter Table "RoadsPlus" ( drop PR,BPT,EPT,LRS_LINK,LENGTH,Oid_1,VER,MGF_HIST,Bmp,Emp) Interactive
'Alter Table "RoadsPlus" ( add PRETYPE char(8),VENUE_L char(20),VENUE_R char(20),Roadname2 Char(60),Roadname3 Char(60))
Alter Table "RoadsPlus" ( add PRETYPE char(8),Roadname2 Char(60),Roadname3 Char(60))
Alter Table "RoadsPlus" ( rename Rdname Roadname, NAME FENAME, NAME2 FENAME2, NAME3 FENAME3, LEGALSYST LEGALSYSTEM)
'Alter Table "RoadsPlus" ( order Roadname,Roadname2,Roadname3,PRETYPE,FEDIRP,FENAME,FETYPE,FEDIRS,FEDIRP2,FENAME2,FETYPE2,FEDIRS2,FEDIRP3,FENAME3,FETYPE3,FEDIRS3,FRADDL,TOADDL,FRADDR,TOADDR,ZIPL,ZIPR,LEGALSYSTEM,FCC,FUNCLASS) Interactive
Alter Table "RoadsPlus" ( order Roadname,Roadname2,Roadname3,PRETYPE,FEDIRP,FENAME,FETYPE,FEDIRS,FEDIRP2,FENAME2,FETYPE2,FEDIRS2,FEDIRP3,FENAME3,FETYPE3,FEDIRS3,FRADDL,TOADDL,FRADDR,TOADDR,ZIPL,ZIPR,LEGALSYSTEM,FCC,NFC,Countyl,Countyr) Interactive

Update RoadsPlus Set Roadname2 = LTrim$(RTrim$(FEDIRP2+" "+FENAME2+" "+FETYPE2+" "+FEDIRS2))
Update RoadsPlus Set Roadname3 = LTrim$(RTrim$(FEDIRP3+" "+FENAME3+" "+FETYPE3+" "+FEDIRS3))

Commit Table RoadsPlus

'Select * from Roadsplus where CountyL = 05 or CountyR = 05 into tmpAll
'	Delete from tmpAll
'Select * from Roadsplus where CountyL = 15 into tmp
'	Update tmp set VENUE_L = "Barry Co"
'Select * from Roadsplus where CountyR = 15 into tmp
'	Update tmp set VENUE_R = "Barry Co"
'	Select * from Roadsplus where CountyL = 77 into tmp
'	Update tmp set VENUE_L = "Kalamazoo Co"
'Select * from RoadsPlus where CountyR = 77 into Barry
'	Update tmp set VENUE_R = "Kalamazoo Co"
'	Select * from RoadsPlus where CountyL = 81 into tmp
'	Update tmp set VENUE_L = "Kent Co"
'Select * from RoadsPlus where CountyR = 81 into tmp
'	Update tmp set VENUE_R = "Kent Co"
'Select * from RoadsPlus where CountyL = 139 into tmp
'	Update tmp set VENUE_L = "Ottawa Co"
'Select * from RoadsPlus where CountyR = 139 into tmp
'	Update tmp set VENUE_R = "Ottawa Co"
'Select * from RoadsPlus where CountyL = 159 into tmp
'	Update tmp set VENUE_L = "Van Buren Co"
'Select * from RoadsPlus where CountyR = 159 into tmp
'	Update tmp set VENUE_R = "Van Buren Co"
'Commit Table RoadsPlus

Open Table CO_DIR+"Boundary" as Boundary Interactive
Fetch first from Boundary
oBoundary = Buffer(Boundary.obj,12,2.2,"mi")
Select * from RoadsPlus where obj within oBoundary into TempAddRoads

'delete the roads that are set as within Allegan County
Select * from Roadsplus where CountyL = 05 or CountyR = 05 into tmpAll
	Delete from tmpAll

'Insert Into tmpRoads (VENUE_L,VENUE_R,ROADNAME,ROADNAME2,ROADNAME3,FEDIRP,FENAME,FETYPE,FEDIRS,FEDIRP2,FENAME2,FETYPE2,FEDIRS2,FEDIRP3,FENAME3,FETYPE3,FEDIRS3,FRADDL,TOADDL,FRADDR,TOADDR,ZIPL,ZIPR,LEGALSYSTEM,FCC,FUNCLASS) 
'Select VENUE_L,VENUE_R,ROADNAME,ROADNAME2,ROADNAME3,FEDIRP,FENAME,FETYPE,FEDIRS,FEDIRP2,FENAME2,FETYPE2,FEDIRS2,FEDIRP3,FENAME3,FETYPE3,FEDIRS3,FRADDL,TOADDL,FRADDR,TOADDR,ZIPL,ZIPR,LEGALSYSTEM,FCC,FUNCLASS From TempAddRoads
'20120222 removed FUNCLASS
Insert Into tmpRoads (ROADNAME,ROADNAME1,ROADNAME2,FEDIRP,FENAME,FETYPE,FEDIRS,FEDIRP2,FENAME2,FETYPE2,FEDIRS2,FEDIRP3,FENAME3,FETYPE3,FEDIRS3,FRADDL,TOADDL,FRADDR,TOADDR,ZIPL,ZIPR,LEGALSYSTEM,FCC,COUNTYL,COUNTYR) 
Select ROADNAME,ROADNAME2,ROADNAME3,FEDIRP,FENAME,FETYPE,FEDIRS,FEDIRP2,FENAME2,FETYPE2,FEDIRS2,FEDIRP3,FENAME3,FETYPE3,FEDIRS3,FRADDL,TOADDL,FRADDR,TOADDR,ZIPL,ZIPR,LEGALSYSTEM,FCC,COUNTYL,COUNTYR From TempAddRoads

Commit Table tmpRoads
Drop Table RoadsPlus
Close Table Boundary
End Sub
