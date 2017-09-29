import pywps
from pywps.Process import WPSProcess
import os
from datetime import datetime
import provenance
# import sys, traceback #traceback.print_exc(file=sys.stdout)
import netCDF4
import json
# project: C3S 34a Lot2
# author: ANDREJ
# adapting wps from c4i to provenance culture.

'''
    PyWPS API for Climate Exmplorer Diagnostic tool
'''    


# generic KNMI process
class KnmiClimateExplorerWpsProcess(WPSProcess):

    def __init__(self,wpsin):

        # self.fileOutPath1 = None
        # self.fileOutURL = ""
        self.bundle = None # used to add provs...
        # self.output = None


        # wps = {}
        # wps["identifier"]   = 'climexp' 
        # wps["title"]        = 'Climate Exmplorer KNMI'
        # wps["abstract"]     = 'KNMI Diagnostic Tool Climate Explorer'
        # wps["version"]      = '1.0.0'
        # wps["storeSupported"]  = True
        # wps["statusSupported"] = True   
        # wps["grassLocation"]   = False

        wps = wpsin["wps"]

        WPSProcess.__init__(self,
                            identifier      = wps["identifier"], 
                            title           = wps["title"],
                            abstract        = wps["abstract"],
                            version         = wps["version"],
                            storeSupported  = wps["storeSupported"],
                            statusSupported = wps["statusSupported"],
                            grassLocation   = wps["grassLocation"]
                            )
        
        self.inputs = wpsin["inputs"]

        from pprint import pprint
        #pprint(self.inputs)
        

        print self.inputs.keys()

        # for inputDict in descriptor.inputsTuple:
        for inputDict in self.inputs.values():
            pprint(inputDict.keys())
            try:
                self.inputs[inputDict["identifier"]] = self.addLiteralInput(  identifier = inputDict["identifier"] ,
                                                                              title      = inputDict["title"],
                                                                              type       = inputDict["type"],
                                                                              default    = inputDict["default"], 
                                                                              abstract   = inputDict["abstract"]
                                                                              ) 
            except Exception, e:
                self.inputs[inputDict["identifier"]] = self.addLiteralInput(  identifier = inputDict["identifier"] ,
                                                                              title      = inputDict["title"],
                                                                              type       = inputDict["type"],
                                                                              default    = inputDict["default"] 
                                                                      ) 
            #######
            #abstract="application/netcdf"
            try:              
                if inputDict["maxOccurs"] is not None:
                    self.inputs[inputDict["identifier"]].maxOccurs = inputDict["maxOccurs"]
            except Exception, e:
                #print "no maxOccurs"
                pass
                
            try:              
                if inputDict["values"] is not None:
                    self.inputs[inputDict["identifier"]].values = inputDict["values"]
            except Exception, e:
                #print "no values"
                pass


        # self.processExecuteCallback = descriptor.processExecuteCallback

        # self.opendapURL = self.addLiteralOutput(identifier = "opendapURL",title = "opendapURL"); 

    # logging using pywps status module   
    # def callback(self,message,percentage):
    #     ''' status update '''
    #     self.status.set("%s" % str(message),str(percentage));


       
    # key:    
    # runs WPS
    def execute(self):

        ''' runs wps with provenance '''
        # Very important: This allows the NetCDF library to find the users credentials (X509 cert)
        # homedir = os.environ['HOME']
        # os.chdir(homedir)


        # self.callback( "EXECUTE "+homedir,0)

        # ''' file path based on oauth and cert user.'''
        # if self.fileOutPath1 is None:
        #     """ pathToAppendToOutputDirectory """
        #     # pathToAppendToOutputDirectory = "/WPS_"+self.identifier+"_" + datetime.now().strftime("%Y%m%dT%H%M%SZ")
        #     pathToAppendToOutputDirectory = "/WPS_"+self.identifier+"_" + datetime.now().strftime("%Y%m%dT%H%M")

        #     #self.callback("POF_OUTPUT_URL: "+os.environ['POF_OUTPUT_URL'],1)
        #     # """ URL output path """
        #     self.fileOutURL  = os.environ['POF_OUTPUT_URL']  + pathToAppendToOutputDirectory+"/"
            


        #     """ Internal output path"""
        #     self.fileOutPath1 = os.environ['POF_OUTPUT_PATH']  + pathToAppendToOutputDirectory +"/"

        #     """ Create output directory """
        #     if not os.path.exists(self.fileOutPath1):
        #         os.makedirs(self.fileOutPath1)
        # # else nothing        

        # #self.callback(fileOutURL,10)
        # self.callback(self.fileOutPath1,1)    
        # this can be extended for better debug...
        # def callback(b,info=""):
        #     self.callback("Processing wps_knmi "+str(info),b)

        # PE used is dispel4py should be here
        # currently    
        # self.callback("KnmiWpsProcess", 2)

        ''' create metadata object, initiate bundle if not existing '''
        # bundle created here
        # username = homedir.split("/")[-2]

        # use prov call back later... each start creates lineage info
        prov = provenance.MetadataD4P(  name=self.identifier , 
                                        description=self.abstract ,
                                        username="c3s_user" ,
                                        inputs=self.inputs ,
                                        bundle0=self.bundle 
                                        ) #does wps provide a user id...
        
        # self.bundle = prov.bundle
        # MOVED IN PROCESS CAUSES DEPENDACNY... for demo...
        #prov.start( self.inputs ) # use prov call back later... each start creates lineage info
        # self.callback("Start wps.", 3)

        ''' run: process_execute_function, defined in descriptor '''
        #try:
        # self.callback("Start wps.", 4)
        
        # for k in self.inputs.keys():
            # self.callback(str(k)+": "+str( self.inputs[k].getValue()), 4)
        
        
        # logging.debug("Something has been debugged")

        
        # self.callback(str(self.fileOutPath1), 4)
        
        ''' PROCESS OUTPUTs '''
        # content, source , fileO = self.processExecuteCallback( self.inputs , callback , self.fileOutPath1 )

        

        # self.netcdf_w = fileO

        size = 0
        
        # if fileO is not None:
            # self.callback("Finished wps."+str(fileO), 70)
            # try:
            #     size = os.stat(fileO.filepath()).st_size
            # except Exception, e:
            #     content(71,info=str(e))
            

    #except Exception, e:
            #prov.errors(str(e))

            #traceback.print_exc(file=sys.stderr)
            #raise e

        # callback(80)


        #prov.content = { "prov:type" : "data_element" }
        #prov.content.update( content )
        #prov.content = content

        #callback(90,info='finish provenance')

        # prov.output = fileO  
        
        # ''' provenance related can be moved'''
        # try:
        #     outputurl = str(self.fileOutURL)+self.inputs['netcdf_target'].getValue()
        # except Exception, e:
        #     outputurl = str(self.fileOutURL)+"/wpsoutputs"
     

        ''' adds knmi_prov '''
        prov.finish( source , outputurl ,size)  

        ''' finalise prov and write to netcdf '''
        prov.closeProv()

        #logging.debug("self.fileOutURL == "+str(self.fileOutURL))
        # self.opendapURL.setValue(outputurl)

        ''' output to local json '''
        prov.writeMetadata('bundle.json')
        # self.callback("metadata inserted.", 100)


        #
        # issues with prov library here, need to ironout...
        #xml = provexport.toW3Cprov( [prov.lineage] , [prov.bundle])
        #provenance.writeXML('w3c-prov.xml' , xml )




