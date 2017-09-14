# Climate Explorer KNMI Python Binding
# author: Andrej
# python api
import os
import json
import climexp_pyapi

inputfile = 'inputs_local.json'
with open(inputfile, 'r') as fp:
  inputs = json.load(fp)

try:
  location = os.environ['CLIMEXPFORTRAN'] 
except Exception, e:
  location = './Fortran/build/'

# api call...

# notes???
api_model = {
				'api' 		: 'climexp_pyapi'
				'type'		: 'python'
				'descript'	: 'python to fortran binding for climexp'
				'git'		: ''
			}

climexp_pyapi.correlfield(inputs)