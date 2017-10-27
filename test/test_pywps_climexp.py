# Climate Explorer KNMI Python Binding
# author: Andrej
# python pywps api
from wpsproc import pywps_climexp 

process = pywps_climexp.KnmiClimateExplorerWpsProcess()
process.execute()

