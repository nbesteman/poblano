Include "Update_CADmap_Layers.Def"

Type Coordinate
  fX as Float
  fY as Float
End Type

'********************************************
Sub FLIP_LINE_DIRECTION

Dim oActiveLine as Object
Dim iRow as Integer
Dim sFRADDL,sTOADDL,sFRADDR,sTOADDR,sZIPL,sZIPR as String
'Dim sCOUNTYL,sCOUNTYR,sSTATEL,sSTATER,sFMCDL,sFMCDR as String
'Dim sSDL,sSDR,sPCTL,sPCTR,sSDPL,sSDPR,sVPL,sVPR,sCCDL,SCCDR,sSTSL,sSTSR,sSTHL,sSTHR,sUSCL,sUSCR as String

CLS
Set Table tmpRoads FastEdit On Undo Off
iRow = 1
For iRow = 1 to TableInfo(tmpRoads,TAB_INFO_NROWS)
  Select * from tmpRoads where RowID = iRow into TempSelectRoad NoSelect
  If TempSelectRoad.FRADDL+TempSelectRoad.TOADDL+TempSelectRoad.FRADDR+TempSelectRoad.TOADDR>0 Then
	If TempSelectRoad.TOADDL<TempSelectRoad.FRADDL or TempSelectRoad.TOADDR<TempSelectRoad.FRADDR Then
	sFRADDL=TempSelectRoad.TOADDR
	sTOADDL=TempSelectRoad.FRADDR
	sFRADDR=TempSelectRoad.TOADDL
	sTOADDR=TempSelectRoad.FRADDL
	sZIPL=TempSelectRoad.ZIPR
	sZIPR=TempSelectRoad.ZIPL
'	sCOUNTYL = TempSelectRoad.COUNTYR
'	sCOUNTYR = TempSelectRoad.COUNTYL
'	sSTATEL = TempSelectRoad.STATER
'	sSTATER = TempSelectRoad.STATEL
'	sFMCDL=TempSelectRoad.FMCDR
'	sFMCDR=TempSelectRoad.FMCDL
'	sSDL = TempSelectRoad.SDR
'	sSDR = TempSelectRoad.SDL
'	sPCTL=TempSelectRoad.PCTR
'	sPCTR=TempSelectRoad.PCTL
'	sSDPL=TempSelectRoad.SDPR
'	sSDPR=TempSelectRoad.SDPL
'	sVPL=TempSelectRoad.VPR
'	sVPR=TempSelectRoad.VPL
'	sCCDL=TempSelectRoad.CCDR
'	sCCDR=TempSelectRoad.CCDL
'	sSTSL=TempSelectRoad.STSR
'	sSTSR=TempSelectRoad.STSL
'	sSTHL=TempSelectRoad.STHR
'	sSTHR=TempSelectRoad.STHL
'	sUSCL=TempSelectRoad.USCR
'	sUSCR=TempSelectRoad.USCL
	oActiveLine = ConvertToPline(TempSelectRoad.obj)
'	Update Roads Set TOADDL=sTOADDL,TOADDR=sTOADDR,FRADDL=sFRADDL,FRADDR=sFRADDR,ZIPL=sZIPL,ZIPR=sZIPR,
'	  COUNTYL=sCOUNTYR,COUNTYR=sCOUNTYL,FMCDL=sFMCDR,FMCDR=sFMCDL,
'	  SDL=sSDR,SDR=sSDL,PCTL=sPCTR,PCTR=sPCTL,SDPL=sSDPR,SDPR=sSDPL,VPL=sVPR,VPR=sVPL,CCDL=sCCDR,CCDR=sCCDL,
'	  STSL=sSTSR,STSR=sSTSL,STHL=sSTHR,STHR=sSTHL,USCL=sUSCR,USCR=sUSCL,Rdname2="F",obj=FLIPLINE(oActiveLine) 
'	  where RowID = iRow

	Update tmpRoads Set TOADDL=sTOADDL,TOADDR=sTOADDR,FRADDL=sFRADDL,FRADDR=sFRADDR,
   ZIPL=sZIPL,ZIPR=sZIPR,obj=FLIPLINE(oActiveLine) where RowID = iRow
'	Print "Processing: "+iRow
	End If
  End If

Next
Close Table TempSelectRoad
Commit Table tmpRoads

End Sub

'********************************************************************************

Function FLIPLINE(oLine as Object) as Object

Dim faNodeList(0) as Coordinate
Dim iPosition,iNode,iNodeCount as Integer
Dim oNewLine as Object

iNodeCount = ObjectInfo(oLine,OBJ_INFO_NPNTS)
Redim faNodeList(iNodeCount)
iNode = 1

Do While iNode <= iNodeCount 
faNodeList(iNode).fX = ObjectNodeX(oLine,1,iNode)
faNodeList(iNode).fY = ObjectNodeY(oLine,1,iNode)
iNode = iNode+1
Loop

Create Pline into Variable oNewLine 0
iPosition = 1
iNode = iNodeCount
Do While iNode > 0
Alter Object oNewLine Node Add Position 1,iPosition (faNodeList(iNode).fX,faNodeList(iNode).fY)
iPosition = iPosition+1
iNode = iNode-1
Loop

FLIPLINE = oNewLine

End Function
