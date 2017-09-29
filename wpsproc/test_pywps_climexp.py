# Climate Explorer KNMI Python Binding
# author: Andrej
# python pywps api
import pywps_climexp 
import json
from climexp import climexp_pyapi

from pprint import pprint

inputfile = 'wps.json'
with open(inputfile, 'r') as fp:
	wpsinputs = json.load(fp)

process = pywps_climexp.KnmiClimateExplorerWpsProcess(wpsinputs)
process.execute()

