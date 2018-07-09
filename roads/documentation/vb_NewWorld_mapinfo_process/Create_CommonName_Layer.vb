'append milemarkers to end   needs some work
Include "Update_CADmap_Layers.Def"

Sub CREATE_CommonName_LAYER
'sub main
		Set ProgressBars Off
		Open Table CO_DIR+"Addresses Geocode.TAB" as Src   
		Select * from Src where Common_Name <> "" into tmpSelect
		Commit table tmpSelect As DISPATCH_DIR+"CADmaps\New Layers\temp\tmpCommon.TAB" TYPE NATIVE Charset "WindowsLatin1"
		Close All
		Open Table DISPATCH_DIR+"CADmaps\New Layers\temp\tmpCommon.TAB" as Src 'Interactive
																''populate VENUE
																'Open Table "J:\data\00 Allegan Co\ac units.tab" as Units 'Interactive
																'Add Column "Common" (Unit Char (20))From Units Set To Unit Where contains 
	'	Commit Table Src As DISPATCH_DIR+"CADmaps\New Layers\temp\tmpCommon_Names.TAB" TYPE NATIVE Charset "WindowsLatin1"
	'	Close All 'Interactive
		Open Table DISPATCH_DIR+"CADmaps\New Layers\temp\tmpCommon.TAB" as Src 'Interactive
			Set Table Src FastEdit On
		Alter Table "Src" (
			drop Address,AddressShort,AddressFull,NumberSup,Supplementary,City,Zip,Problem,Notes,PARetired,Unoccupied,O99,O04,O05,O06,Field_Verified,Source,Common_Source
			add PREFIX_TYPE Char(1)
			'rename Unit VENUE,StreetFull ROADNAME,Predirectional FEDIRP,Street_Name FENAME,Street_Suffix FETYPE,Postdirectional FEDIRS
			rename Predirectional PREFIX_DIRECTION,Number HOUSE_NUMBER,Street_Suffix STREET_TYPE,Postdirectional SUFFIX_DIRECTION
			modify StreetFull Char(60),STREET_NAME Char(30)
			order COMMON_NAME,StreetFull,HOUSE_NUMBER,PREFIX_DIRECTION,PREFIX_TYPE,STREET_NAME,STREET_TYPE,SUFFIX_DIRECTION
														) Interactive
		
			drop index Src (Street_Name)
			drop index Src (STREET_TYPE)
		
		
		Select * from Src where instr(1,StreetFull,"M 40")>0 into Tempselect
		Update Tempselect Set StreetFull = Left$(StreetFull,instr(1,StreetFull,"M 40")-1)+"M40 Hwy"+mid$(StreetFull,instr(1,StreetFull,"M 40")+4,30)
		Update Tempselect Set Street_Name = Left$(Street_Name,instr(1,Street_Name,"M 40")-1)+"M40"+mid$(Street_Name,instr(1,Street_Name,"M 40")+4,30)
		Select * from Tempselect where STREET_TYPE = "" into Tempselect2
		'drop HWY on request from dispatch
		'Update Tempselect2 Set STREET_TYPE = "Hwy"
		
		Select * from Src where instr(1,StreetFull,"M 89")>0 into Tempselect
		Update Tempselect Set StreetFull = Left$(StreetFull,instr(1,StreetFull,"M 89")-1)+"M89 Hwy"+mid$(StreetFull,instr(1,StreetFull,"M 89")+4,30)
		Update Tempselect Set Street_Name = Left$(Street_Name,instr(1,Street_Name,"M 89")-1)+"M89"+mid$(Street_Name,instr(1,Street_Name,"M 89")+4,30)
		Select * from Tempselect where STREET_TYPE = "" into Tempselect2
		'drop HWY on request from dispatch
		'Update Tempselect2 Set STREET_TYPE = "Hwy"
		
		Select * from Src where instr(1,StreetFull,"M 222")>0 into Tempselect
		Update Tempselect Set StreetFull = Left$(StreetFull,instr(1,StreetFull,"M 222")-1)+"M222 Hwy"+mid$(StreetFull,instr(1,StreetFull,"M 222")+5,30)
		Update Tempselect Set Street_Name = Left$(Street_Name,instr(1,Street_Name,"M 222")-1)+"M222"+mid$(Street_Name,instr(1,Street_Name,"M 222")+5,30)
		Select * from Tempselect where STREET_TYPE = "" into Tempselect2
		'drop HWY on request from dispatch
		'Update Tempselect2 Set STREET_TYPE = "Hwy"
		
		Select * from Src where instr(1,StreetFull,"M 179")>0 into Tempselect
		Update Tempselect Set StreetFull = Left$(StreetFull,instr(1,StreetFull,"M 179")-1)+"M179 Hwy"+mid$(StreetFull,instr(1,StreetFull,"M 179")+5,30)
		Update Tempselect Set Street_Name = Left$(Street_Name,instr(1,Street_Name,"M 179")-1)+"M179"+mid$(Street_Name,instr(1,Street_Name,"M 179")+5,30)
		Select * from Tempselect where STREET_TYPE = "" into Tempselect2
		'drop HWY on request from dispatch
		'Update Tempselect2 Set STREET_TYPE = "Hwy"
		Commit Table Src
		Alter Table "Src" (drop StreetFull)
		Commit Table Src 'Interactive
		Pack Table Src Graphic Data
		'*****************************************************************************************
		'Mile Marker processing
		  			Open Table "J:\Departments\Dispatch\Layers\Mile Markers.TAB" As Markers
		
		 				Insert into Src (Common_Name,obj) Select LTrim$(Prefix + " " + Highway + " " + MileMarker+"MM"),obj from Markers
		
		
		'Commit Table Addresses As DISPATCH_APPS+"Update CADmap Layers\temp\tmpAddresses.TAB" TYPE NATIVE Charset "WindowsLatin1"
		
		Commit Table Src As DISPATCH_APPS+"Update CADmap Layers\temp\tmpCommon2.TAB" TYPE NATIVE Charset "WindowsLatin1"
		Close All
		Open Table DISPATCH_APPS+"Update CADmap Layers\temp\tmpCommon2.TAB" as Src2 Interactive
		'Alter Table "Common2" (drop LEGALSYSTEM,SOURCE)
		'Commit Table Common2 'As DISPATCH_DIR+"CADmaps\New Layers\Common.TAB"
		
		'
		''make all UCase$
		Update Src2 Set COMMON_NAME = UCase$(COMMON_NAME)
		'Update Src2 Set StreetFull = UCase$(StreetFull)
		Update Src2 Set PREFIX_TYPE = UCase$(PREFIX_TYPE)
		Update Src2 Set PREFIX_DIRECTION = UCase$(PREFIX_DIRECTION)
		Update Src2 Set STREET_NAME = UCase$(STREET_NAME)
		Update Src2 Set STREET_TYPE = UCase$(STREET_TYPE)
		Update Src2 Set SUFFIX_DIRECTION = UCase$(SUFFIX_DIRECTION)
		'Update Src2 Set VENUE = UCase$(VENUE)
		Commit Table Src2 As DISPATCH_DIR+"CADmaps\New Layers\temp\tmpCommonNames.TAB"
			Close Table Src2
		Open Table "J:\Departments\Dispatch\CADmaps\New Layers\temp\tmpCommonNames.TAB" As Src3
		Alter Table Src3 ( add ROADNAME Char(80),VENUE Char(20) rename Common_Name NAME,PREFIX_TYPE PRETYPE,PREFIX_DIRECTION FEDIRP,HOUSE_NUMBER NUMBER,STREET_NAME FENAME,STREET_TYPE FETYPE,SUFFIX_DIRECTION FEDIRS order NAME,ROADNAME,PRETYPE,FEDIRP,NUMBER,FENAME,FETYPE,FEDIRS,VENUE) Interactive
		'Alter Table Src3 ( modify ZIP Char(5) ) Interactive
	Update Src3 Set ROADNAME = ltrim$(rtrim$(fedirp+" "+fename+" "+fetype))	
	
		Commit Table Src3 Interactive
	'update zipcods
'	Open Table "J:\data\00 Allegan Co\ac zip codes.tab" Interactive	
'	Add Column "CommonNames" (ZIP )From ac_zip_codes Set To ZIP Where contains

Open Table "J:\data\00 Allegan Co\ac units.tab" Interactive
	Add Column "Src3" (VENUE )From ac_units Set To Unit Where contains
	Update Src3 Set VENUE = UCase$(Venue)	
		'Commit Table Src3 As DISPATCH_DIR+"CADmaps\New Layers\CommonNames.TAB"
		Commit Table Src3 As DISPATCH_DIR+"CADmaps\New Layers\CommonNames.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0

		Close All

End Sub
