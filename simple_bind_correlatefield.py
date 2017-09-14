import subprocess
import xarray
import datetime
import json
from pprint import pprint




###
# input
inputfile = 'inputs.json' #opendap
inputfile = 'inputs_local.json'

with open(inputfile, 'r') as fp:
  inputs = json.load(fp)


pprint(inputs)

###
# binding
#

sourceA = inputs["netcdf_source1"]["default"]
sourceB = inputs["netcdf_source2"]["default"]
freq    = inputs["frequency"]["default"]
ratio   = inputs["ratio"]["default"]
ave     = inputs["average"]["default"]
var     = inputs["var"]["default"]
target 	= inputs["netcdf_target"]["default"] 

script = '../Fortran/build/correlatefield '+sourceA+' '+sourceB+' '+freq+' '+ratio+' '+ave+' '+var+' '+str(target)

print script

try:
    process = subprocess.Popen( script  , shell=True).communicate() 
    print str(process)
except Exception, e:
    print "Popen process failed: "+script
    raise e

#,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
           
#outs, errs = process.communicate()

#callback(24,info="errs: "+errs)

#process.wait()

#  /usr/people/mihajlov/climexp/


# VIEW with ncview out.nc

####
# metadata
# #
#ncout = xarray.open_dataset('out.nc')

#print(ncout)

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