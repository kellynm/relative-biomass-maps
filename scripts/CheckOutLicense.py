import arcpy

class LicenseError(Exception):
    pass

try:
    if arcpy.CheckExtension("3D") == "Available":
        arcpy.CheckOutExtension("3D")
    else:
        # raise a custom exception
        raise LicenseError

    arcpy.env.workspace = "c:/GrosMorne"
    arcpy.HillShade_3d("WesternBrook", "wbrook_hill", 300)
    arcpy.Aspect_3d("WesternBrook", "wbrook_aspect")
    arcpy.CheckInExtension("3D")

except LicenseError:
    print("3D Analyst license is unavailable")
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))