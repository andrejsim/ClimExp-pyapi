# Climate Explorer KNMI Python Binding
# author: Andrej
# python api
import os
import bind
# generated


''' web api interfaces representing current instance of climate exp '''
''' possible representation of diagnostic tool baseline '''

# http://climexp.knmi.nl/start.cgi?id=someone@somewhere

''' field selection, right columb of web page: http://climexp.knmi.nl/start.cgi '''

def get_select_timeseries(seriesname):
  
  # implement portable data repository (required for c3s-magic)

  # implement data list

  # implement search wizard (model on climate4impact fasceted search tool)
    # Daily station data
    # Daily climate indices
    # Monthly station data
    # Monthly climate indices
    # Annual climate indices
    # View, upload your time series

  # important nino3 etc time series data links included here.

def get_select_a_field(fieldname):

  # implement portable data repository (required for c3s-magic)

  # implement data list

  # implement search wizard (model on climate4impact fasceted search tool)
    # Daily fields
    # Monthly observations # ( current example uses these )
    # Monthly reanalysis fields
    # Monthly and seasonal historical reconstructions
    # Monthly seasonal hindcasts
    # Monthly decadal hindcasts
    # Monthly CMIP3+ scenario runs
    # Monthly CMIP5 scenario runs # ( c3s-magic is focused on these )
    # Annual CMIP5 extremes
    # Monthly CORDEX scenario runs
    # Attribution runs
    # External data (ensembles, ncep, enact, soda, ecmwf, ...)


    # IMPORTANT PREPROCESSING DONE HERE
    ''' 
      conversion to time series offered
      filters offered
      masks offered
    '''  

def make_time_series(field):

def mask(field):

def temporal_slice():
  # can be done by wcs
def averaging():   
  # can be done by wps elsewhere.

''' viusalisation services, follow field selection '''
''' right column option under "Investigate this field" '''

def plot(field):
  ''' ADAGUC SERVICE ''' 
  #IMPLEMENT

def plot_difference_with_field(field1,field2):
  ''' COMBINE SERVICE see climate4impact '''
  # IMPLEMENT

''' filter selection, follows field choice '''
''' this is generically covered by OGC WCS tool '''


''' transformation of fields to time series '''
''' simple example is daily, monthly or annual average of data climate4impact has examples of these micro services'''

def compute_statistics(field):

  # IMPLEMENT, link to fortran code.

  # mean
  # sd
  # extremes

def trend_in_extremes(field):

  # IMPLEMENT

def make_EOFs(field):

  # IMPLEMENT




''' used as demo diagnostic feature for c3s-magic '''

def correlate_with_a_time_series(field,series):

    # IMPLEMENTED at 
    #   def correlatefield(inputs):


''' LATER '''
''' TO IMPLEMENT
Pointwise correlations with a field
  only observations
  only reanalyses
  only seasonal hindcasts
  only decadal hindcasts
  only CMIP5 scenario runs
  only user-defined fields

Spatial correlations with a field
  only observations
  only reanalyses
  only seasonal hindcasts
  only decadal hindcasts
  only CMIP5 scenario runs
  only user-defined fields

SVD
  only observations
  only reanalyses
  only seasonal hindcasts
  only CMIP5 scenario runs
  only user-defined fields

Verify field against observations

'''


''' python api for fortran code of climate exp '''

# fortran build location / add as env in docker...
try:
  location = os.environ['CLIMEXPFORTRAN']
except Exception, e:
  location = '../Fortran/build/'


''' correlatefield fortran function execution '''
# http://climexp.knmi.nl/fieldcorrseries.cgi?id=someone@somewhere&field=ghcn_cams_05

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