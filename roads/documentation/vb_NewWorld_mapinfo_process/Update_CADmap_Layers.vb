Include "Update_CADmap_Layers.Def"

Sub MAIN
Dim lDebug as Logical
Dim iCol1,iCol2 as Integer
Dim iRow1,iRow2,iRow3,iRow4,iRow5,iRow6,iRow7,iRow8,iRow9,iRow10,iRow11,iRow12 as Integer
Dim lCommon,lAddresses,lRoads,lESNs,lMutualAid,lWreckers,lUnits,lHwyExits,lMileMarkers,lRail,lRivers,lLakes,lVenues as Logical
Dim sType as String
lDebug = TRUE

Set Event Processing Off

'Create a dialog with a checkbox list of layers to process
'Standard Update Layers: default check on - process as one
	'Addresses
	'Roads
'Occasional Update Dispatch Layers: default check off
	'ESNs
	'Mutual Aid
	'Venues
	'Wreckers
'Occasional Update Base Layers: default checked off
	'Rivers
	'Units
	'Lakes
	'Rail
'Fixed Layers: default check off
	'Mile Markers
	'Hwy Exits
'Fixed Layers: not listed
	'Aerial

'Dialog Spacing
iCol1 = 10
iCol2 = iCol1+30
iRow1 = 10
iRow2 = iRow1+12			
iRow3 = iRow2+12	
iRow4 = iRow3+12	
iRow5 = iRow4+12
iRow6 = iRow5+12			
iRow7 = iRow6+12	
iRow8 = iRow7+12	
iRow9 = iRow8+12
iRow10 = iRow9+12
iRow11 = iRow10+12
iRow12 = iRow11+12

Dialog 
  Title "Check Layers to Update:"

	Control CheckBox							
		Position iCol1,iRow1
		Title "Addresses"
		Value FALSE
		Into lAddresses
	Control CheckBox							
		Position iCol1,iRow2
		Title "ESNs"
		Value FALSE
		Into lESNs
	Control CheckBox							
		Position iCol1,iRow3
		Title "Mutual Aid"
		Value FALSE
		Into lMutualAid
	Control CheckBox							
		Position iCol1,iRow4
		Title "Wreckers"
		Value FALSE
		Into lWreckers
		'disable 
	Control CheckBox							
		Position iCol1,iRow5
		Title "Units"
		Value False
		Into lUnits
	Control CheckBox							
		Position iCol1,iRow6
		Title "Highway Exits"
		Value FALSE
		Into lHwyExits
	Control CheckBox							
		Position iCol1,iRow7
		Title "Mile Markers"
		Value FALSE
		Into lMileMarkers
	Control CheckBox							
		Position iCol1,iRow8
		Title "Rail"
		Value FALSE
		Into lRail
	Control CheckBox							
		Position iCol1,iRow9
		Title "Lakes"
		Value FALSE
		Into lLakes
	Control CheckBox							
		Position iCol1,iRow10
		Title "Rivers"
		Value False
		Into lRivers
	Control CheckBox							
		Position iCol1,iRow11
		Title "Roads"
		Value FALSE
		Into lRoads
	Control CheckBox							
		Position iCol1,iRow12
		Title "Common Names"
		Value FALSE
		Into lCommon
		Disable
	
	Control OKButton
	  Title "&Update"
	Control CancelButton
	  Title "&Cancel"

If CommandInfo(CMD_INFO_DLG_OK)= TRUE Then 'Process layers as needed into new folder
Print "Processing New Layers..."
'Common Name
If lCommon = TRUE Then	'Create a Common Names layer
	Call CREATE_CommonName_Layer
	Print "Common Names Layer Created..."
Else
	Print "Common Names Layer Skipped..."
End If
'ADDRESSES
If lAddresses = TRUE Then	'Create a address layer
	Call CREATE_ADDRESS_LAYER
	Print "ADDRESS Layer Created..."
Else
	Print "ADDRESS Layer Skipped..."
End If
'CENTERLINES,ROAD,ADDRESSES
If lRoads = TRUE Then	'Create a roads and alternate name layer
	Call CREATE_TEMPROAD_LAYER
	Call CREATE_ROAD_LAYER
	Call CREATE_ALTERNATE_NAME_TABLE
	Print "ROAD Layer Created..."
Else
	Print "ROAD Layer Skipped..."
End If
'ESNs
'ERROR - need to select and process ESN polygons only, do not include polylines that reside in this layer
If lESNs = TRUE Then	'Create an ESN layer
	Open Table DISPATCH_LAYERS+"ESN Districts.TAB" as ESNs Interactive
	Select * from ESNs where Str$(ObjectInfo(obj,OBJ_Info_Type)) = "7" into Tempselect
	'Commit Table Tempselect As DISPATCH_DIR+"CADmaps\New Layers\ESNs.TAB" TYPE NATIVE Charset "WindowsLatin1"
	Commit Table Tempselect As DISPATCH_DIR+"CADmaps\New Layers\ESNs.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0
	Close Table ESNs
 	Print "ESN Layer Created..."
Else
	Print "ESN Layer Skipped..."
End If 
'MUTUAL AID
If lMutualAid = True Then	'Create Mutual Aid Layer
	Open Table DISPATCH_LAYERS+"Mutual Aid Boundaries.TAB" as Mutual_Aid Interactive
	Commit Table Mutual_Aid As DISPATCH_DIR+"CADmaps\New Layers\Mutual Aid.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0    'TYPE NATIVE Charset "WindowsLatin1"
	Close Table Mutual_Aid
 	Print "MUTUAL AID Layer Created..."
Else
	Print "MUTUAL AID Layer Skipped..."
End If 
'WRECKER DISTRICTS
If lWreckers = True Then
	Open Table DISPATCH_LAYERS+"Wrecker Districts.TAB" Interactive
	Commit Table Wrecker_Districts As "J:\Departments\Dispatch\CADmaps\New Layers\Wreckers.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0 'TYPE NATIVE Charset "WindowsLatin1"
	Close Table Wrecker_Districts
 	Print "WRECKER DISTRICT Layer Created..."
Else
	Print "WRECKER DISTRICT Layer Skipped..."
End If 
'HWY EXITS
If lHwyExits = True Then	'Create Hwy Exits Layer
	Open Table CO_DIR+"Road Hwy Exits.TAB" As Hwy_Exits Interactive
	Commit Table Hwy_Exits As DISPATCH_DIR+"CADmaps\New Layers\Hwy Exits.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0 'TYPE NATIVE Charset "WindowsLatin1"
	Close Table Hwy_Exits
 	Print "HWY EXIT Layer Created..."
Else
	Print "HWY EXIT Layer Skipped..."
End If
'LAKES      may change based on AC Hydro layer
If lLakes = True Then
	'Open Table CO_DIR+"Lakes 2+ Acres.TAB" As Lakes2Acre Interactive
	Open Table CO_DIR+"lakes.tab" Interactive As Lakes
	select Township,Lakename,Acres from Lakes where Acres >= 2 into Lakes2Acre
	Commit Table Lakes2Acre As DISPATCH_DIR+"CADmaps\New Layers\Lakes.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0  'TYPE NATIVE Charset "WindowsLatin1"
	Close Table Lakes2Acre
	Close Table Lakes
 	Print "LAKES Layer Created..."
Else
	Print "LAKES Layer Skipped..."
End If 
'RAIL
If lRail = True Then
	Open Table CO_DIR+"Railroads.TAB" as Rail Interactive
	select * from Rail where FCC = Any("B01","B02") into Tempselect
	Delete from Tempselect
	Commit Table Rail As DISPATCH_DIR+"CADmaps\New Layers\Rail.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0 'TYPE NATIVE Charset "WindowsLatin1"
	Rollback Table Rail
	Close Table Rail
 	Print "RAIL Layer Created..."
Else
	Print "RAIL Layer Skipped..."
End If 
'RIVERS *** leave the rivers layer as is until AC Hydro layer is established and import as appropriate
If lRivers = True Then	'Create River Layer
Open Table CO_DIR+"Rivers.TAB" As Rivers Interactive
	Commit Table Rivers As DISPATCH_DIR+"CADmaps\New Layers\Rivers.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0 'TYPE NATIVE Charset "WindowsLatin1"
	Close Table Rivers
 	Print "RIVER Layer Created..."
Else
	Print "RIVER Layer Skipped..."
End If 
'UNITS
If lUnits = True Then	'Create Units Layer
	Open Table CO_DIR+"Units.TAB" As Units Interactive
	Commit Table Units As DISPATCH_DIR+"CADmaps\New Layers\Units.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0 'TYPE NATIVE Charset "WindowsLatin1"
	Close Table Units
 	Print "UNITS Layer Created..."
Else
	Print "UNITS Layer Skipped..."
End If
'MILE MARKERS
If lMileMarkers = True Then 'Create Mile Marker Layer
	Open Table CO_DIR+"Mile Markers.TAB" as Mile_Markers Interactive
	Commit Table Mile_Markers As DISPATCH_DIR+"CADmaps\New Layers\Mile Markers.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0 'TYPE NATIVE Charset "WindowsLatin1"
	Close Table Mile_Markers Interactive
	Open Table DISPATCH_DIR+"CADmaps\New Layers\Mile Markers.TAB" As Mile_Markers
		Select * from Mile_Markers where Highway = "US 131" and MileMarker < 44 into MM131a
			Delete from MM131a
		Commit Table Mile_Markers
		Select * from Mile_Markers where Highway = "US 131" and MileMarker > 73 into MM131b
			Delete from MM131b
		Commit Table Mile_Markers
		Select * from Mile_Markers where Highway = "US 196" and MileMarker < 19 into US196a
			Delete from US196a
		Commit Table Mile_Markers
		Select * from Mile_Markers where Highway = "US 196" and MileMarker > 54 into US196b
			Delete from US196b				
		Commit Table Mile_Markers
	Close Table Mile_Markers
 	Print "MILE MARKER Layer Created..."
Else
	Print "MILE MARKER Layer Skipped..."
End If
' Convert all new layers into shapefiles	'If lDebug = TRUE Then Print "OK to 4" End If
End If
Print "Completed All Layer Processing"
End Sub
