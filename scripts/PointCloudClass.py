import arcpy, sys
arcpy.CheckOutExtension("Spatial")
arcpy.CheckOutExtension("3D")
arcpy.CheckOutExtension("GeoStats")
arcpy.env.workspace = "C:/gispy/Project/data/input"
arcpy.env.overwriteOutput = True

class PointCloud:
    '''LAS point clouds used to create digital surface models.
    Includes bare ground and vegetation canopy point clouds - must indicate type.'''
    def __init__(self, lasFile, resolution, type, date):
        self.lasFile = lasFile
        self.resolution = resolution
        self.type = type
        self.date = date

    def createSurfaceModel(self, fieldBoundary):
        outPoints = "C:/gispy/Project/data/output/" + "tempPoints.shp"
        arcpy.LASToMultipoint_3d(self.lasFile, outPoints, 0.01, '#', '#', '#', "Coordinate Systems"\
                        "/Projected Coordinate Systems/State Plane/NAD 1983 HARN (Meters)/"\
                        "NAD_1983_HARN_StatePlane_North_Carolina_FIPS_3200.prj")
        outRast = "C:/gispy/Project/data/output/" + "tempRast"
        arcpy.RadialBasisFunctions_ga(outPoints, 'Shape.Z', '#', outRast, self.resolution, '#',\
                                     'SPLINE_WITH_TENSION')
        clipRast = "C:/gispy/Project/data/output/" + self.type + self.date
        arcpy.Clip_analysis(outRast, fieldBoundary, clipRast)
        arcpy.Delete_management(outPoints)
        arcpy.Delete_management(outRast)
        return "{0} created.".format(clipRast),

def calcCropHeight(groundDEM, cropDSM):
    cropHeightRast = (arcpy.sa.Raster(cropDSM) - arcpy.sa.Raster(groundDEM))
    cropHeightRast.save('C:/gispy/Project/data/output/cropHeightRast')


BareEarth2015 = PointCloud('BE_lidar_Midpines_2015.las', 0.1, 'DEM', '2015-01-01')
print BareEarth2015.createSurfaceModel('Field_Boundary.shp')