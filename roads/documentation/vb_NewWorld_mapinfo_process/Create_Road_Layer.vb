Include "Update_CADmap_Layers.Def"

Sub CREATE_ROAD_LAYER

Open Table DISPATCH_APPS+"Update_CADmap_Layers\temp\tmpRoads.TAB" As Road 
	Alter Table Road (
         drop GST,GSF,LngthCalcFt,TRAFALIGN,SpeedLimit,SYM,Classification,Surface,LENGTH
         order Roadname,Roadname1,Roadname2,FEDIRP,FENAME,FETYPE,FEDIRS,
                                            FEDIRP2,FENAME2,FETYPE2,FEDIRS2,
                                            FEDIRP3,FENAME3,FETYPE3,FEDIRS3,
                                            FRADDL,TOADDL,FRADDR,TOADDR,ZIPL,ZIPR,
                                            FMCDL,FMCDR,FCC,LEGALSYSTEM,
                                            CITYL,CITYR,VENUE_L,VENUE_R
                         )
'make all UCase$
Update Road Set ROADNAME = UCase$(ROADNAME)
Update Road Set ROADNAME1 = UCase$(ROADNAME1)
Update Road Set ROADNAME2 = UCase$(ROADNAME2)
Update Road Set FETYPE = UCase$(FETYPE)
Update Road Set FETYPE2 = UCase$(FETYPE2)
Update Road Set FETYPE3 = UCase$(FETYPE3)
Update Road Set FEDIRP = UCase$(FEDIRP)
Update Road Set FEDIRP2 = UCase$(FEDIRP2)
Update Road Set FEDIRP3 = UCase$(FEDIRP3)
Update Road Set FENAME = UCase$(FENAME)
Update Road Set FENAME2 = UCase$(FENAME2)
Update Road Set FENAME3 = UCase$(FENAME3)
Update Road Set FETYPE = UCase$(FETYPE)
Update Road Set FETYPE2 = UCase$(FETYPE2)
Update Road Set FETYPE3 = UCase$(FETYPE3)
Update Road Set FEDIRS = UCase$(FEDIRS)
Update Road Set FEDIRS2 = UCase$(FEDIRS2)
Update Road Set FEDIRS3 = UCase$(FEDIRS3)
Commit Table Road As DISPATCH_DIR+"Apps\Update_CADmap_Layers\build\Roads.TAB" TYPE NATIVE Charset "WindowsLatin1" CoordSys Earth Projection 1, 0
Close All 'Interactive

End Sub
