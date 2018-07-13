

arcpy.ExcelToTable_conversion(Input_Excel_File="J:/Apps/Python/LayerUpdates/parcels/source/BSA_ParcelData.xlsx", Output_Table="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/Parcels", Sheet="Parcels")

arcpy.ExcelToTable_conversion(Input_Excel_File="J:/Apps/Python/LayerUpdates/parcels/source/BSA_ParcelData.xlsx", Output_Table="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/ParcelMaster", Sheet="ParcelMaster")

arcpy.ExcelToTable_conversion(Input_Excel_File="J:/Apps/Python/LayerUpdates/parcels/source/BSA_ParcelData.xlsx", Output_Table="J:/Apps/Python/LayerUpdates/parcels/source/Parcels_Combined.gdb/ParcelPreviousYearTotal", Sheet="ParcelPreviousYearTotal")


