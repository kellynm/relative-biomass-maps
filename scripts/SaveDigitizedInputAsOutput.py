# getFeatures.py
# Purpose: Copy the digitized feature set input into a shapefi le
# and send this to the Script Tool as output.
import arcpy, sys
arcpy.env.overwriteOutput = True
fs = sys.argv[1]
outputFeat = 'C:/gispy/scratch/getFeaturesOutput.shp'
arcpy.CopyFeatures_management(fs, outputF