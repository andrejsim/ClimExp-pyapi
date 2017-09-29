# Climate Explorer KNMI Python Binding
# author: Andrej
# python pywps api
import pywps
import pywps.pywps_climexp 

process = pywps_climexp.KnmiClimateExplorerWpsProcess()
process.execute()

