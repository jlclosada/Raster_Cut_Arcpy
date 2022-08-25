#AUTOMATIC RASTER TRIMMER FOR ARCGIS WITH PYTHON

--Warnings--

This script is only available for ArcMap (ArcGIS). 
ArcMap is currently running the specific Python version 2.7. If you don't have Python 2.7 installed separately on your machine, 
you can still run this script in the ArcMap Python console (just copy/paste the code to the console).

--Description--

This script is responsible for reading one by one all the rasters found in a given folder. That folder is defined in the code with the variable "work_path". 
ArcMap will automatically detect that this is the working folder and will be able to read and execute functions directly there.

In this tool, all the rasters will be cut from the same mask (a shapefile that must be previously created). For example, if you have a time series of 50 
very heavy rasters, but you are only interested in a small area of ​​that raster, you may want to crop the images by focusing on the AOI (the shapefile).

We must also specify the path where the shapefile is located using the "mask_path" variable.

Finally, we will select the path where we want our new clipped rasters to be generated.

You will only need to change the paths in this script, and of course generate your AOI with the shapefile. You will also need to change the file names 
for the outputs.


A very simple script, but very practical for the Geographic Information Systems sector.
