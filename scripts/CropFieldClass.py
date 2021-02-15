import arcpy, sys, urllib2
sys.path.append('C:/gispy/sample_scripts/ch20')
import BeautifulSoup
arcpy.CheckOutExtension("Spatial")
arcpy.env.workspace = "C:/gispy/Project/data/input"
arcpy.env.overwriteOutput = True

class CropField:
    '''Field of interest for creating relative biomass maps and report.
    Properties:
    fieldName - Name used to identify crop field
    crop - type of crop planted in field
    harvesterHeight - height at which machine cuts plant when harvested
    fieldBoundary - bounding limits of crop field for analysis
    denstiy - average number of plants per cell based on field observation
    h2w - ratio for estimating weight of plant based on height, from field observation
    plantDate - date crop was planted
    harvestDate - date crop was harvested, or is expected to be harvested'''
    def __init__(self, name, crop, harvesterHeight, fieldBoundary, density, h2w, plantDate, harvestDate):
        '''Initialize cropField properties.'''
        self.name = name
        self.crop = crop
        self.harvesterHeight = harvesterHeight
        self.fieldBoundary = fieldBoundary
        self.density = density
        self.h2w = h2w
        self.plantDate = plantDate
        self.harvestDate = harvestDate

    def calcAcreage(self):
        '''Calculate the area of the crop field in acres.'''
        cursor = arcpy.da.SearchCursor(self.fieldBoundary, ['SHAPE@AREA'])
        row = cursor.next()
        #convert map units (square meters) to acres
        return row[0] * 0.000247105

    def calcBiomass(self, cropHeightRast):
        '''Calculate the biomass of crop in field in pounds.
        First, convert harvester height given in inches to map units (meters).
        Then, calculate biomass(lbs) per cell with equation: biomass = ((CH-HH)/h2w)*density)'''
        harvesterHeightMeters = float(self.harvesterHeight)*0.0254
        biomassRast = ((arcpy.sa.Raster(cropHeightRast) - harvesterHeightMeters)/(float(self.h2w)))*(float(self.density))
        biomassRast.save('C:/gispy/Project/data/output/biomassRast')
        outTable = 'C:/gispy/Project/data/output/biomasssum.dbf'
        biomassSumTable = arcpy.sa.ZonalStatisticsAsTable(self.fieldBoundary, 'FID', biomassRast, outTable)
        cursor = arcpy.da.SearchCursor(biomassSumTable, ['SUM'])
        row = cursor.next()
        return row[0]

    def getWeatherData(self):
        '''Kellyn fills this in, right'''
        dataPath = "https://climate.ncsu.edu/dynamic_scripts/cronos/getCRONOSdata.php?station=LAKE&start=" + self.plantDate + "&end=" + self.harvestDate + "&obtype=D&parameter=precip,tempmin,tempmax&hash=8a8f8fd5e81269b0fa63ed540be91ad745ec72ae3d49a7a715815dfda1ed7"
        response = urllib2.urlopen(dataPath)
        contents = response.read()
        response.close()
        soup = BeautifulSoup.BeautifulSoup(contents)
        txt = soup.text.split('\n')
        for index, line in enumerate(txt):
            if "##" in line:
                lastHeaderLine = index
            if 'Station metadata' in line:
                firstStationLine = index
                lastStationLine = index + 10
        stationHeader = txt[firstStationLine:lastStationLine]
        parsedDataList = []
        for line in txt[lastHeaderLine+2:]:
            row = line.split("|")
            parsedDataList.append(row)

        return (stationHeader, parsedDataList)



chTestRast = 'C:/gispy/Project/data/output/chrastTest2'
field = CropField('Midpines 1A', 'grain sorghum', '3', 'Field_Boundary.shp', 0.152, 4.061821622, '2017-06-01', '2017-11-02')


