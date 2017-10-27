import subprocess
import netCDF4 as nc
import xarray
import datetime
import json
from pprint import pprint



####
# metadata
# #
#ds = xarray.open_dataset('out.nc')

ds = nc.Dataset('out.nc','a')

print(ds)


# issues debug...

#ncout = xarray.Dataset(target,'a')

# ''' metadata appended, inspire worthy '''
# ncout.setncattr(  "title"        , "KNMI Climate Explorer correlate field service output" )
# ncout.setncattr(  "summary"      , "KNMI Climate Explorer correlate field service output "+sourceA+" for "+sourceB )
# ncout.setncattr(  "keywords"     , "climate,correlation,wps_knmi" )
# ncout.setncattr(  "institute_id" , "KNMI" )            
# ncout.setncattr(  "contact"      , "oldenborgh@knmi.nl" )
# ncout.setncattr(  "date_created" , datetime.now().isoformat() )
# ncout.setncattr(  "knmi_wps"     , self.structure["identifier"] )
# ncout.setncattr(  "software"     , 'https://github.com/andrejsim/ClimExp-pyapi' )

