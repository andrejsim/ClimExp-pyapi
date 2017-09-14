# Climate Explorer KNMI Python Binding
# author: Andrej
# python api
import os
import bind
# generated

# fortran build location / add as env in docker...
try:
  location = os.environ['CLIMEXPFORTRAN']
except Exception, e:
  location = '../Fortran/build/'



#http://climexp.knmi.nl/fieldcorrseries.cgi?id=someone@somewhere&field=ghcn_cams_05

def correlatefield(inputs):
	
	try:

		sourceA = inputs["netcdf_source1"]["default"]
		sourceB = inputs["netcdf_source2"]["default"]
		freq    = inputs["frequency"]["default"]
		ratio   = inputs["ratio"]["default"]
		ave     = inputs["average"]["default"]
		var     = inputs["var"]["default"]
		target 	= inputs["netcdf_target"]["default"]

		fortran = 'correlatefield'
		
		script = location+fortran+' '+sourceA+' '+sourceB+' '+freq+' '+ratio+' '+ave+' '+var+' '+str(target)

		bind.execute(script)

	except Exception, e:
		raise e



# GENERATE HERE...


# test
# see test-climexp-pyapi.py