# Climate Explorer KNMI Python Binding
# author: Andrej
# python pywps api
import wpsproc.pywps_climexp 

process = pywps_climexp.KnmiClimateExplorerWpsProcess()
process.execute()

