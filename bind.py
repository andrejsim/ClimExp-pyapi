# Climate Explorer KNMI Python Binding
# author: Andrej

import subprocess

# pyhton bind for fortran

def execute( script ):

	print script

	try:
	    process = subprocess.Popen( script  , shell=True).communicate() 

	    print str(process)

	except Exception, e:

	    print "Popen process failed: "+script

	    raise e

	#,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE
	           
	#outs, errs = process.communicate()