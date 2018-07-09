
Include "Update_CADmap_Layers.Def"

Sub CREATE_ADDRESS_LAYER
Set ProgressBars Off

'dim iCount as integer

'Open Source Table and save into CADmap Table
Open Table CO_DIR+"Addresses Geocode.TAB" as AC_Addresses  
'Open Table CO_DIR+"geoaddresstest.TAB" as AC_Addresses 
Select * from AC_Addresses where Number = "" into selection
	delete from selection
Commit Table AC_Addresses As DISPATCH_DIR+"CADmaps\New Layers\temp\tmpAddresses.TAB" TYPE NATIVE Charset "WindowsLatin1"
Close All

Open Table DISPATCH_DIR+"CADmaps\New Layers\temp\tmpAddresses.TAB" as Addresses
Set Table Addresses FastEdit On
'check for missing counties
'select * from Addresses where county = "" into countyblank
'icount = tableinfo(countyblank,tab_info_nrows)
'if iCount > 0 Then 
'Call CountyError(iCount)
'End If
'close table countyblank

'populate VENUE based on AC_Units.tab
'Open Table C0_DIR+"Units.tab" as Units
Open Table "J:\data\00 Allegan Co\ac units.tab" as Units
Add Column "Addresses" (Unit Char (20))From Units Set To Unit Where contains
Commit Table Addresses As DISPATCH_DIR+"CADmaps\New Layers\Addresses.TAB" TYPE NATIVE Charset "WindowsLatin1"
Close All 'Interactive
Open Table DISPATCH_DIR+"CADmaps\New Layers\Addresses.TAB" as Addresses
Set Table Addresses FastEdit On
'Open Table "J:\data\Michigan\county_mi\county_miv11a.TAB" as MiCo
'Add Column "Addresses" (County Char (20))From MiCo Set To Name Where contains
'Commit Table Addresses
'populate VENUE based on out of county
select * from Addresses where county = "Barry" into barry
	update barry set Unit = "Barry Co"
select * from Addresses where county = "Calhoun" into calhoun
	update calhoun set Unit = "Calhoun Co"
select * from Addresses where county = "Kalamazoo" into kzoo
	update kzoo set Unit = "Kalamazoo Co"
select * from Addresses where county = "Kent" into kent
	update kent set Unit = "Kent Co"
select * from Addresses where county = "Ottawa" into ottawa
	update ottawa set Unit = "Ottawa Co"
select * from Addresses where county = "Van Buren" into vb
	update vb set Unit = "Van Buren Co"

Commit Table Addresses
Close All 'Interactive
Open Table DISPATCH_DIR+"CADmaps\New Layers\Addresses.TAB" as Addresses
Set Table Addresses FastEdit On
'Modify point address table strucutre to match roads
	'drop Address,AddressShort,AddressFull,NumberSup,Supplementary,Problem,Notes,PARetired,Unoccupied,O99,O04,O05,O06,Field_Verified,Common_Name,Common_Source
	'order ROADNAME,PRETYPE,FEDIRP,NUMBER,FENAME,FETYPE,FEDIRS,ZIP,LEGALSYSTEM,SOURCE,VENUE  '''  this line from the order below.... dropped source from it
Alter Table "Addresses" (
	drop Address,AddressShort,AddressFull,NumberSup,Supplementary,Problem,Notes,PARetired,county
	add PRETYPE Char(1),LEGALSYSTEM Char(1)	
	rename Unit VENUE,StreetFull ROADNAME,Predirectional FEDIRP,Street_Name FENAME,Street_Suffix FETYPE,Postdirectional FEDIRS
	modify Roadname Char(60),FENAME Char(30)
	order ROADNAME,PRETYPE,FEDIRP,NUMBER,FENAME,FETYPE,FEDIRS,ZIP,LEGALSYSTEM,VENUE
												) Interactive
	drop index Addresses (FENAME)
	drop index Addresses (FETYPE)

Select * from Addresses where instr(1,Roadname,"M 40")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M 40")-1)+"M40 Hwy"+mid$(Roadname,instr(1,Roadname,"M 40")+4,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M 40")-1)+"M40"+mid$(FENAME,instr(1,FENAME,"M 40")+4,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"

Select * from Addresses where instr(1,Roadname,"M 89")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M 89")-1)+"M89 Hwy"+mid$(Roadname,instr(1,Roadname,"M 89")+4,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M 89")-1)+"M89"+mid$(FENAME,instr(1,FENAME,"M 89")+4,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"

Select * from Addresses where instr(1,Roadname,"M 222")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M 222")-1)+"M222 Hwy"+mid$(Roadname,instr(1,Roadname,"M 222")+5,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M 222")-1)+"M222"+mid$(FENAME,instr(1,FENAME,"M 222")+5,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"

Select * from Addresses where instr(1,Roadname,"M 179")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M 179")-1)+"M179 Hwy"+mid$(Roadname,instr(1,Roadname,"M 179")+5,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M 179")-1)+"M179"+mid$(FENAME,instr(1,FENAME,"M 179")+5,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"
print "fixed Hwy with spaces"
'update Hwy with dashes
Select * from Addresses where instr(1,Roadname,"M-40")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M-40")-1)+"M40 Hwy"+mid$(Roadname,instr(1,Roadname,"M-40")+4,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M-40")-1)+"M40"+mid$(FENAME,instr(1,FENAME,"M-40")+4,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"

Select * from Addresses where instr(1,Roadname,"M-89")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M-89")-1)+"M89 Hwy"+mid$(Roadname,instr(1,Roadname,"M-89")+4,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M-89")-1)+"M89"+mid$(FENAME,instr(1,FENAME,"M-89")+4,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"

Select * from Addresses where instr(1,Roadname,"M-222")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M-222")-1)+"M222 Hwy"+mid$(Roadname,instr(1,Roadname,"M-222")+5,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M-222")-1)+"M222"+mid$(FENAME,instr(1,FENAME,"M-222")+5,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"

Select * from Addresses where instr(1,Roadname,"M-179")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"M-179")-1)+"M179 Hwy"+mid$(Roadname,instr(1,Roadname,"M-179")+5,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"M-179")-1)+"M179"+mid$(FENAME,instr(1,FENAME,"M-179")+5,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"

print "fixed Hwy with dashes"

Commit Table Addresses Interactive
Pack Table Addresses Graphic Data

Commit Table Addresses As DISPATCH_APPS+"Update_CADmap_Layers\temp\tmpAddresses2.TAB" TYPE NATIVE Charset "WindowsLatin1"
Close All
Open Table DISPATCH_APPS+"Update_CADmap_Layers\temp\tmpAddresses2.TAB" as Addresses2 Interactive
'Alter Table "Addresses2" (drop LEGALSYSTEM,SOURCE)
Alter Table "Addresses2" (drop LEGALSYSTEM)
Commit Table Addresses2 As DISPATCH_DIR+"CADmaps\New Layers\Addresses.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0

'make all UCase$
Update Addresses2 Set ROADNAME = UCase$(ROADNAME)
Update Addresses2 Set PRETYPE = UCase$(PRETYPE)
Update Addresses2 Set FEDIRP = UCase$(FEDIRP)
Update Addresses2 Set FENAME = UCase$(FENAME)
Update Addresses2 Set FETYPE = UCase$(FETYPE)
Update Addresses2 Set FEDIRS = UCase$(FEDIRS)
Update Addresses2 Set CITY = UCase$(CITY)
Commit Table Addresses2 As DISPATCH_DIR+"CADmaps\New Layers\Addresses.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0

Close All

End Sub

'Sub CountyError(iCount as Integer)
'Note "There is missing County data from " + icount + " records."
'End MapInfo
'End Sub


Sub MileMarkers    'not used MileMarkers were added to addresses
'Mile Marker processing
    'select * within buffered region
dim oboundary as object
Open Table CO_DIR+"Mile Markers.TAB" as AC_MileMarker 
Open Table CO_DIR+"Boundary" as Boundary Interactive
Fetch first from Boundary
oBoundary = Buffer(Boundary.obj,12,2.2,"mi")
Select * from AC_MileMarker where obj within oBoundary into MileMarker

Insert into Addresses(FEDIRP,Number, FENAME, FETYPE, obj) Select Direction, MileMarker, Highway, "HWY", obj From MileMarker
'close Boundary
'close AC_MileMarker
End sub 'MileMarkers
