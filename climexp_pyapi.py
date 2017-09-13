# Climate Explorer KNMI Python Binding
# author: Andrej
# python api

# generated

def correlfield(location , inputs):
	
	try:

		sourceA = inputs["netcdf_source1"]["default"]
		sourceB = inputs["netcdf_source2"]["default"]
		freq    = inputs["frequency"]["default"]
		ratio   = inputs["ratio"]["default"]
		ave     = inputs["average"]["default"]
		var     = inputs["var"]["default"]
		target 	= inputs["netcdf_target"]["default"

		location = '../Fortran/build/correlatefield'
		script = location+' '+sourceA+' '+sourceB+' '+freq+' '+ratio+' '+ave+' '+var+' '+str(target)

		bind.execute(script)

	except Exception, e:
		raise e



# GENERATE HERE...


# test
# see test-climexp-pyapi.py