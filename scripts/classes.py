class CropField:
    '''Crop field of interest.
    Properties:
        crop type
        field boundaries to limit biomass calculation
        plant density - number of plants per square meter
        height to weight ratio to convert plant heights in meters to approximate weight in lbs
        date crop was planted
        date crop was or is expected to be harvested'''
    def __init__(self, name, crop, fieldBounds, density, h2wRatio, plantDate, harvestDate):

    def calcBiomass(self, density, h2wRatio, cropHeightRast):
        raster calc
        ZonalStatisticsasTable
        Read table
        return biomass
    
    def calcArea(self)
        Use boundaries drawn by user to caclulate polygon area
        return area in acres


class LidarPointCloud:
    '''Point cloud dataset (.las) to be used to create DEM of bare earth.'''
    def __init__(self, lasFile, resolution):

    def createDEM(self, fieldBounds):
        return DEM


class UASPointCloud:
    '''Point cloud dataset (.las) to be used to create DSM of crop growth.
    Properies:
        lasFile - location of .las file
        resolution - desired resolution of DEM or DSM, default is 0.1m
        flight date - date data was obtained via UAS'''
    def __init__(self, lasFile, resolution, date):

    def createDSM(self, fieldBounds):
        Multipoint
        Interpolate
        return DSM

    def calcCropHeight(self, harvesterHeight, DEM):
        raster calc
        return cropHeightRast



    