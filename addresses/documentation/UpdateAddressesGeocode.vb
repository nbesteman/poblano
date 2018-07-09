'Include "Mapbasic.def"
'Include "Icons.def"
'Include "J:\Apps\MapBasic\Global\Definitions\Directories.Def"
'Include "J:\Apps\MapBasic\Global\Definitions\Printers.Def"
'---
'BUILD_ADDRESS_GEOCODE
'This subroutine builds a point address layer from the AC Addresses that lists
'all addresses and aliases in one column for address matching purposes.
'---
'Define LOG_FILE		1
'Declare Sub MAIN
'Sub MAIN
Include "Main.def"
Sub UpdateAddressesGeocode()
Set ProgressBars Off
'Open Source Table and save into Geocode Table
Open File "J:\apps\MapBasic\lis\LayerUpdates\qaqc\UpdateAddressGeocode.log" For Append As #LOG_FILE
'note "presently pulling from archive folder"
Open Table CO_DIR+"Addresses" as COAddresses
'Open Table "J:\data\00 Allegan Co\archive\AC Addresses20120613.TAB" as COAddresses
Commit Table COAddresses as BuildDir+"AC Addresses Geocode.TAB" TYPE NATIVE Charset "WindowsLatin1"
Close Table COAddresses
'Drop problem rows - empty address, no number
Open Table BuildDir+"AC Addresses Geocode" as Addresses
Alter Table "Addresses" ( drop Flag,Exception,Coll_Mthd,Tax_Pin,Rcl_ID,Sloc_Type,Plc_Type,Loc,Landmark,Seat,Floor,Bldg,MSAGcom,PSAP,ESN,St_Premod,Nhbrhd,Uncorp,MCD_Div,entityID,Latitude,Longitude,Common_Source,Common_Name,Source,Field_Verified,Site_ID,O06,O05,O04,O99,Unoccupied,Hseno_Pre,St_Postmod,Room,Unit ) Interactive
Select * from Addresses where Number="" into Tempselect
Drop Table Tempselect
Select * from Addresses where Not Left$(Address,1) = Any("1","2","3","4","5","6","7","8","9") into Tempselect
Drop Table Tempselect
Pack Table Addresses Data Graphic
'Parse out addresses with aliases and append
Select * from Addresses where Address1<>"" into Address1
Commit Table Address1 As LIS_TEMP+"Address1.TAB" TYPE NATIVE Charset "WindowsLatin1"
Select * from Addresses where Address2<>"" into Address2
Commit Table Address2 As LIS_TEMP+"Address2.TAB" TYPE NATIVE Charset "WindowsLatin1"
Close Table Address1
Close Table Address2
'Open Address1 and Address2 tables and move Alias fields to primaries
Open Table LIS_TEMP+"Address1.TAB" Interactive
Open Table LIS_TEMP+"Address2.TAB" Interactive
Update Address1 Set Address = Address1, PARetired = A1Retired, Number = Number1, NumberSup = NumberSup1, Predirectional = Predirectional1, Street_Name = Street_Name1, Street_Suffix = Street_Suffix1,Postdirectional = Postdirectional1, Supplementary = Supplementary1
Update Address2 Set Address = Address2, PARetired = A2Retired,Number = Number2, NumberSup = NumberSup2, Predirectional = Predirectional2, Street_Name = Street_Name2, Street_Suffix = Street_Suffix2,Postdirectional = Postdirectional2, Supplementary = Supplementary2
'Append Address1 and Address2 to Addresses and delete unnecessary columns 33Columns
Insert Into Addresses (Address,City,Zip,Problem, Notes, PARetired, Number, NumberSup, Predirectional, Street_Name, Street_Suffix, Postdirectional, Supplementary, Muni, County) Select Address,City,Zip,Problem, Notes, PARetired, Number, NumberSup, Predirectional, Street_Name, Street_Suffix, Postdirectional, Supplementary, Muni, County From Address1
Insert Into Addresses (Address,City,Zip,Problem, Notes, PARetired, Number, NumberSup, Predirectional, Street_Name, Street_Suffix, Postdirectional, Supplementary, Muni, County) Select Address,City,Zip,Problem, Notes, PARetired, Number, NumberSup, Predirectional, Street_Name, Street_Suffix, Postdirectional, Supplementary, Muni, County From Address2
Commit Table Addresses Interactive
Alter Table "Addresses" ( drop Address1, A1Retired, Number1, NumberSup1, Predirectional1, Street_Name1, Street_Suffix1, Postdirectional1, Supplementary1 ) Interactive
Alter Table "Addresses" ( drop Address2, A2Retired, Number2, NumberSup2, Predirectional2, Street_Name2, Street_Suffix2, Postdirectional2, Supplementary2 ) Interactive
Alter Table "Addresses" ( add AddressShort Char(40),AddressFull Char(40),StreetFull Char(40) order Address,AddressShort,AddressFull,StreetFull,Problem,Notes,Number,Street_Name,Street_Suffix,NumberSup,Predirectional,Postdirectional,Supplementary,City,Zip,PARetired) Interactive
'Delete Address1 and Address2 Tables
Drop Table Address1
Drop Table Address2
Update Addresses Set Address = RTrim$(Number+" "+NumberSup)+" "+RTrim$(LTrim$(RTrim$(Predirectional+" "+LTrim$(RTrim$(Street_Name+" "+Street_Suffix))+" "+Postdirectional)))
Update Addresses Set AddressShort = RTrim$(Number+" "+NumberSup)+" "+RTrim$(LTrim$(RTrim$(Predirectional+" "+LTrim$(RTrim$(Street_Name))+" "+Postdirectional)))
Update Addresses Set AddressFull = RTrim$(Number+" "+NumberSup)+" "+RTrim$(LTrim$(RTrim$(Predirectional+" "+LTrim$(RTrim$(Street_Name+" "+Street_Suffix))+" "+Postdirectional))+" "+Supplementary)
Update Addresses Set StreetFull = RTrim$(LTrim$(RTrim$(Predirectional+" "+LTrim$(RTrim$(Street_Name+" "+Street_Suffix))+" "+Postdirectional)))
Commit Table Addresses
select * from Addresses where Address = "" into tempSelect
Delete from tempSelect
Commit Table Addresses
Pack Table Addresses Graphic Data
Close All
Set ProgressBars On

Call OpenBuild()
End Sub 'BUILD_ADDRESSES_GEO


'Sub QAQC(sUnit as String)
'Dim iCount,iAcres as Integer
'Dim dToday as Date
'dToday = CurDate()
''  this will be implemented after initial values are generated into qaqc table
'Select Count(*),Sum(MInfo_Acres) from tmpParcels_Comb into NewCount
'Fetch first from NewCount
'iCount = NewCount.Count
'iAcres = NewCount.COL2    'does not like Sum(MInfo_Acres)
'print #LOG_FILE, dToday+","+sUnit+","+iCount+","+iAcres
'End Sub 'QAQC(
