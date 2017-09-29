# Climate Explorer KNMI Python Binding
# author: Andrej
# python pywps api
import pywps_climexp 
from pprint import pprint

inputfile = 'wps.json'
with open(inputfile, 'r') as fp:
	wpsinputs = json.load(fp)

pprint(wpsinputs)

process = pywps_climexp.KnmiClimateExplorerWpsProcess(wpsinputs)
process.execute()

