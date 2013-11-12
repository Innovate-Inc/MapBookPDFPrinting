import arcpy
import os
from arcpy import env

#####Old Method
#If set as a parameter in the tool, %ScratchWorkSpace% gets resolved into a path
#arcpy.env.scratchWorkspace = arcpy.GetParameterAsText(6) #contains a "\" at the end and is a Derived type parameter
#arcpy.env.scratchWorkspace = arcpy.env.scratchFolder
#environment = arcpy.env.scratchWorkspace #does not contain a "\" at end of the path
#####

#DS- Testing this setting for establishing the scratch folder.  Due to the new process at 10.1
# for deploying GP Services, this changed was needed.  No longer need the output parameter within the toolbox
environment = arcpy.env.scratchFolder
arcpy.env.overwriteOutput = True

arcpy.AddMessage("Output Directory Setting: " + environment)

mxdName = arcpy.GetParameterAsText(0)
mbName = arcpy.GetParameterAsText(1) #The name of the outfile
pageRangeType = arcpy.GetParameterAsText(2) #Values:  ALL or RANGE
pageRange = arcpy.GetParameterAsText(3) #Values: 1, 3, 5-12
outputDPI = arcpy.GetParameter(4) #Values: 50-300
outputQuality = arcpy.GetParameterAsText(5)
outputPDF = environment + "\\" #Extra path separators needed here.  See note above

#local Test
mxd = arcpy.mapping.MapDocument("C:\\Data\\GISData\\r9\\MapBook\\MapBookGISDev\\" + mxdName + ".mxd")

#EPA Orator-s
#mxd = arcpy.mapping.MapDocument("D:\\Public\\Data\\R9app\\data\\PrintTiles\\" + mxdName + ".mxd")

arcpy.AddMessage("Creating Map Book...")
mxd.dataDrivenPages.exportToPDF(mbName,pageRangeType,pageRange,"PDF_SINGLE_FILE",outputDPI,outputQuality,"RGB","TRUE","ADAPTIVE","RASTERIZE_BITMAP","FALSE","TRUE","LAYERS_ONLY","TRUE",80,"FALSE") #10.1

#mxd.dataDrivenPages.exportToPDF(mbName,pageRangeType,pageRange,"PDF_SINGLE_FILE",outputDPI,outputQuality,"RGB","TRUE","ADAPTIVE","RASTERIZE_BITMAP","FALSE","TRUE","LAYERS_ONLY","TRUE",80) # 10.0

arcpy.AddMessage("Map Book Created:" + mbName)
del mxd

#####Old Method Below######

##mapBookPath = "C:\\zInnovate\\Projects\\R9\\TestPython\\myBook.pdf"
##mapBookPath = outputPDF + mxdName + ".pdf"
#mapBookPath = mbName
##arcpy.AddMessage(mxd)
##arcpy.AddMessage(mapBookPath)

#Create the file and Append pages
#pdfMapBook = arcpy.mapping.PDFDocumentCreate(mapBookPath)
#for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
  #mxd.dataDrivenPages.currentPageID = pageNum
  ##create individual pages and then append to mapbook
  ##arcpy.mapping.ExportToPDF(mxd, r"C:\zInnovate\Projects\R9\TestPython\junk" + str(pageNum) + ".pdf")
  ##pdfMapBook.appendPages(r"C:\zInnovate\Projects\R9\TestPython\junk" + str(pageNum) + ".pdf")
  #arcpy.mapping.ExportToPDF(mxd, outputPDF + mxdName + "_" + str(pageNum) + ".pdf","PAGE_LAYOUT",640,480,outputDPI,outputQuality,"RGB","TRUE","ADAPTIVE","RASTERIZE_BITMAP","FALSE","TRUE","LAYERS_ONLY","TRUE",80)
  #pdfMapBook.appendPages(outputPDF + mxdName + "_" + str(pageNum) + ".pdf")
  #arcpy.AddMessage("Temp PDF: " +outputPDF + mxdName + "_" + str(pageNum) + ".pdf")

#pdfMapBook.saveAndClose()

#####Parameter Requirements######

#####10.0
#arcpy.mapping.ExportToPDF (map_document, out_pdf, {data_frame}, {df_export_width}, {df_export_height}, {resolution}, {image_quality}, {colorspace},
#             {compress_vectors}, {image_compression}, {picture_symbol}, {convert_markers}, {embed_fonts}, {layers_attributes},
#             {georef_info}, {jpeg_compression_quality})

######10.1
#mxd.dataDrivenPages.exportToPDF (out_pdf, {page_range_type}, {page_range_string}, {multiple_files}, {resolution}, {image_quality}, {colorspace},
#             {compress_vectors}, {image_compression}, {picture_symbol}, {convert_markers}, {embed_fonts}, {layers_attributes},
#             {georef_info}, {jpeg_compression_quality}, {show_selection_symbology})

#mxd.dataDrivenPages.exportToPDF(mbName,pageRangeType,pageRange,"PDF_SINGLE_FILE",outputDPI,outputQuality,"RGB","TRUE","ADAPTIVE","RASTERIZE_BITMAP","FALSE","TRUE","LAYERS_ONLY","TRUE",80,"FALSE")
#arcpy.mapping.ExportToPDF(mxd, outputPDF + mxdName + "_" + str(pageNum) + ".pdf","PAGE_LAYOUT",640,480,outputDPI,outputQuality,"RGB","TRUE","ADAPTIVE","RASTERIZE_BITMAP","FALSE","TRUE","LAYERS_ONLY","TRUE",80)

#arcpy.AddMessage("Final Mapbook: " + mapBookPath)
#del mxd

