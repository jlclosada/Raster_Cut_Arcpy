
#-------------------------------------------------------------------------------------------
#Name:      raster_cut_wMask.py
#Purpose:   This script retrieves a series of rasters from a defined path and clips them from a mask (a previously defined shp file).
#Autor:     jcaceres
#Version:   1.0.0
#Created:   08/08/2022
#Copyright: (c) jcaceres 2022
#License:   <your license>
#--------------------------------------------------------------------------------------------


import arcpy, os
from arcpy import env
from arcpy.sa import *

work_path = "\\\\imgwebserver\\IDIS\\DEMETER\\DATOS\\MODELO_BIOMASA_AGUA\\CALCULO_ET_MINARET\\2019\\Salidas\\KC\\"
mascara_path = "\\\\imgwebserver\\IDIS\\DEMETER\\DATOS\\GRAFICAS\\shp_auxiliares\\parcelas_estudio.shp"
ouput_path = "\\\\imgwebserver\\IDIS\\DEMETER\\DATOS\\MODELO_BIOMASA_AGUA\\CALCULO_ET_MINARET\\2019\\Salidas\\KC\\output"

arcpy.env.workspace = work_path

raster_list = arcpy.ListRasters('*.img')
for raster in raster_list:
    print('Cutting...: ' + raster)
    arcpy.env.snapRaster = raster
    fecha = str(raster.split('_')[1])
    out_path_file = ouput_path + '\\' + 'kcminaret_' + fecha + '_NDVI_BOA_rec.tif'

    recorte = ExtractByMask(raster, mascara_path)
    recorte.save(out_path_file)
    print("File has been exported: " + 'kcminaret_' + fecha + '_NDVI_BOA_rec.tif')

print("Done!")
print("Output path:  ", ouput_path)

