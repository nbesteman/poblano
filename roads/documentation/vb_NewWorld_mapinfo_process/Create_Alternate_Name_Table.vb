Include "Update_CADmap_Layers.Def"

Sub CREATE_ALTERNATE_NAME_TABLE
Set Event Processing Off
	'Open Table DISPATCH_DIR+"CADmaps\New Layers\Roads.TAB"
         Open Table DISPATCH_APPS+"Update_CADmap_Layers\build\Roads.TAB"
	 Update Roads Set JOIN_ID = RowID
         'need to use character due to oddity in the upload process whith NewWorld
	 Commit Table "Roads"
	Select * from "Roads" where Fename2 <> "" into tmpSelect
  Commit Table tmpSelect As DISPATCH_APPS+"Update_CADmap_Layers\temp\tmpAlternate_Name.TAB" TYPE NATIVE Charset "WindowsLatin1"
  Close Table "Roads"
  Open Table DISPATCH_APPS+"Update_CADmap_Layers\temp\tmpAlternate_Name.TAB" as tmpAlt 
       Alter Table "tmpAlt" ( 
         add PRETYPE Char(4)
         drop Roadname,Roadname1,Roadname2,FEDIRP,FENAME,FETYPE,FEDIRS,FEDIRP3,FENAME3,FETYPE3,FEDIRS3,FRADDL,FRADDR,TOADDL,TOADDR,ZIPL,ZIPR,FMCDL,FMCDR,LEGALSYSTEM,VENUE_L,VENUE_R,CITYL,CITYR,FCC
         rename FEDIRP2 PREDIR,FENAME2 ALTSTNAME,FETYPE2 STREETYPE,FEDIRS2 SUFDIR
         order JOIN_ID,PREDIR,PRETYPE,ALTSTNAME,STREETYPE,SUFDIR )'Interactive    'note - keep column names under 11 characters due to shapefile restrictions
	Commit Table tmpAlt As "J:\Departments\Dispatch\apps\Update_CADmap_Layers\build\Alternate_Name.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0 
	Close All
Set Event Processing On
Set ProgressBars  On
End Sub

