
Include "Update_CADmap_Layers.Def"

Sub CREATE_ADDRESS_LAYER
Set ProgressBars Off

'dim iCount as integer

Open Table CO_DIR+"Addresses Geocode.TAB" as GeoAddress
'Open Table "J:\Apps\MapBasic\LIS\LayerUpdates\build\AC Addresses Geocode.TAB" as GeoAddress
Open Table "J:\Departments\Dispatch\Apps\Update_CADmap_Layers\layers\AdditionalGeoAddresses.TAB" as TempGeo
Insert Into GeoAddress (Address, AddressShort,AddressFull,StreetFull,Problem,Notes,Number,Street_Name,Street_Suffix,NumberSup,Predirectional,Postdirectional,Supplementary,City,Zip,PARetired,County,Muni) Select Address, AddressShort,AddressFull,StreetFull,Problem,Notes,Number,Street_Name,Street_Suffix,NumberSup,Predirectional,Postdirectional,Supplementary,City,Zip,PARetired,County,Muni From TempGeo
Commit Table GeoAddress As DISPATCH_DIR+"CADmaps\New Layers\temp\tmpAddresses.TAB" TYPE NATIVE Charset "WindowsLatin1"
Close All
Open Table DISPATCH_DIR+"CADmaps\New Layers\temp\tmpAddresses.TAB" as Addresses
Select * from Addresses where Number = "" into selection
	delete from selection
Commit Table Addresses
Select * from Addresses where Address = "7400 North Shore Dr" and Notes <> "Sleepy Hollow Beach Resort - Main Office, Delicatessen and Crafts Area"
	delete from selection
Commit Table Addresses
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
'Open Table "J:\data\00 Allegan Co\ac units.tab" as Units
'Add Column "Addresses" (Unit Char (20))From Units Set To Unit Where contains
'Commit Table Addresses As DISPATCH_DIR+"CADmaps\New Layers\Addresses.TAB" TYPE NATIVE Charset "WindowsLatin1"
'Close All 'Interactive
'Open Table DISPATCH_DIR+"CADmaps\New Layers\Addresses.TAB" as Addresses
'Set Table Addresses FastEdit On
'Open Table "J:\data\Michigan\county_mi\county_miv11a.TAB" as MiCo
'Add Column "Addresses" (County Char (20))From MiCo Set To Name Where contains
'Commit Table Addresses
'populate VENUE based on out of county
select * from Addresses where county = "Barry" into barry
	update barry set Muni = "Barry Co"
select * from Addresses where county = "Calhoun" into calhoun
	update calhoun set Muni = "Calhoun Co"
select * from Addresses where county = "Kalamazoo" into kzoo
	update kzoo set Muni = "Kalamazoo Co"
select * from Addresses where county = "Kent" into kent
	update kent set Muni = "Kent Co"
select * from Addresses where county = "Ottawa" into ottawa
	update ottawa set Muni = "Ottawa Co"
select * from Addresses where county = "Van Buren" into vb
	update vb set Muni = "Van Buren Co"

'Commit Table Addresses as DISPATCH_DIR+"CADmaps\New Layers\Addresses.TAB"
Commit Table Addresses as DISPATCH_DIR+"Apps\Update_CADmap_Layers\build\Addresses.TAB"

Close All 'Interactive
Open Table DISPATCH_DIR+"Apps\Update_CADmap_Layers\build\Addresses.TAB" as Addresses
Set Table Addresses FastEdit On
'Modify point address table strucutre to match roads
	'drop Address,AddressShort,AddressFull,NumberSup,Supplementary,Problem,Notes,PARetired,Unoccupied,O99,O04,O05,O06,Field_Verified,Common_Name,Common_Source
	'order ROADNAME,PRETYPE,FEDIRP,NUMBER,FENAME,FETYPE,FEDIRS,ZIP,LEGALSYSTEM,SOURCE,VENUE  '''  this line from the order below.... dropped source from it
Alter Table "Addresses" (
	drop Address,AddressShort,AddressFull,NumberSup,Supplementary,Problem,Notes,PARetired,county
	add PRETYPE Char(1),LEGALSYSTEM Char(1)
	rename Muni VENUE,StreetFull ROADNAME,Predirectional FEDIRP,Street_Name FENAME,Street_Suffix FETYPE,Postdirectional FEDIRS
	modify Roadname Char(60),FENAME Char(30)
	order ROADNAME,PRETYPE,FEDIRP,NUMBER,FENAME,FETYPE,FEDIRS,ZIP,LEGALSYSTEM,VENUE
												) Interactive
	drop index Addresses (FENAME)
	drop index Addresses (FETYPE)

'remove spaces from US Highways and Interstates
'I 196, US 31, US 131
Select * from Addresses where instr(1,Roadname,"US 31")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"US 31")-1)+"US31"+mid$(Roadname,instr(1,Roadname,"US 31")+5,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"US 31")-1)+"US31"+mid$(FENAME,instr(1,FENAME,"US 31")+5,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"

Select * from Addresses where instr(1,Roadname,"US 131")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"US 131")-1)+"US131"+mid$(Roadname,instr(1,Roadname,"US 131")+6,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"US 131")-1)+"US131"+mid$(FENAME,instr(1,FENAME,"US 131")+6,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"

Select * from Addresses where instr(1,Roadname,"I 196")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"I 196")-1)+"US196"+mid$(Roadname,instr(1,Roadname,"I 196")+5,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"I 196")-1)+"I196"+mid$(FENAME,instr(1,FENAME,"I 196")+5,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"
'remove dashes (because Chris will get the state to put them in there some day) from US Highways and Interstates
'I 196, US 31, US 131
Select * from Addresses where instr(1,Roadname,"US-31")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"US-31")-1)+"US31"+mid$(Roadname,instr(1,Roadname,"US-31")+5,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"US-31")-1)+"US31"+mid$(FENAME,instr(1,FENAME,"US-31")+5,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"

Select * from Addresses where instr(1,Roadname,"US-131")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"US-131")-1)+"US131"+mid$(Roadname,instr(1,Roadname,"US-131")+6,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"US-131")-1)+"US131"+mid$(FENAME,instr(1,FENAME,"US-131")+6,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"

Select * from Addresses where instr(1,Roadname,"I-196")>0 into Tempselect
Update Tempselect Set Roadname = Left$(Roadname,instr(1,Roadname,"I-196")-1)+"US196"+mid$(Roadname,instr(1,Roadname,"I-196")+5,30)
Update Tempselect Set FENAME = Left$(FENAME,instr(1,FENAME,"I-196")-1)+"I196"+mid$(FENAME,instr(1,FENAME,"I-196")+5,30)
Select * from Tempselect where FETYPE = "" into Tempselect2
Update Tempselect2 Set FETYPE = "Hwy"

'remove spaces from M series roads
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
'remove dashes from M series roads
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
