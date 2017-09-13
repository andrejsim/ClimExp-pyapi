# Climate Explorer KNMI Python Binding
# author: Andrej
# python api

# generated

# fortran build location / add as env in docker...
location = '../Fortran/build/'

def correlfield(inputs):
	
	try:

		sourceA = inputs["netcdf_source1"]["default"]
		sourceB = inputs["netcdf_source2"]["default"]
		freq    = inputs["frequency"]["default"]
		ratio   = inputs["ratio"]["default"]
		ave     = inputs["average"]["default"]
		var     = inputs["var"]["default"]
		target 	= inputs["netcdf_target"]["default"

		
		fortran = 'correlatefield'
		script = location+fortran+' '+sourceA+' '+sourceB+' '+freq+' '+ratio+' '+ave+' '+var+' '+str(target)

		bind.execute(script)

	except Exception, e:
		raise e



# GENERATE HERE...


# test
# see test-climexp-pyapi.py