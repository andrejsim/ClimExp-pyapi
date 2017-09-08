import subprocess

class CorrelatefieldDescriptor( KnmiWebProcessDescriptor ):

    ''' 
    Correlatefield function developed for ClimateExplorer 
    # via terminal
    # cd /usr/people/mihajlov/climexp
    # ./bin/correlatefield DATA/cru_ts3.22.1901.2013.pre.dat.nc DATA/nino3.nc mon 1:12 ave 3 DATA/out.nc
    '''

    # override with validation process
    def process_execute_function(self , inputs, callback,fileOutPath):
        
        callback(10)

        content1 = {}

        sourceA = inputs['netcdf_source1'].getValue()
        sourceB = inputs['netcdf_source2'].getValue()

        ratio = inputs['ratio'].getValue()
        freq = inputs['frequency'].getValue()
        ave = inputs['average'].getValue()

        target = fileOutPath+inputs['netcdf_target'].getValue()
        source1 = [sourceA,sourceB]
        
        try:            
            # cd /usr/people/mihajlov/climexp/bin/correlatefield
            #'./bin/correlatefield DATA/cru_ts3.22.1901.2013.pre.dat.nc DATA/nino3.nc mon 1:12 ave 3 DATA/out.nc'

            callback(21)

            dirscript = os.environ['PYWPS_PROCESSES']

            #PYWPS_PROCESSES
            # os.environ['PYWPS_PROCESSES']

            loc = '/usr/people/mihajlov/climexp'
            # script = './climexp/correlatefield '+loc+sourceA+' '+loc+sourceB+' '+freq+' '+ratio+' '+ave+' 3 '+str(target)

            # process = Popen(cmd, stdout=PIPE, stderr=PIPE, env=envhpc, shell=True)
            script = dirscript+'/climexp/correlatefield '+sourceA+' '+sourceB+' '+freq+' '+ratio+' '+ave+' 3 '+str(target)

            callback(22,info=script)

            try:
                process = subprocess.Popen( script  , shell=True).communicate() 
                callback(23,info=str(process))
            except Exception, e:
                callback(23,info="Popen process failed")
                raise e
            
            #,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE

                       
            #outs, errs = process.communicate()

           
            #callback(24,info="errs: "+errs)

            #process.wait()

            #  /usr/people/mihajlov/climexp/

            callback(25,info=target)

            netcdf_w = netCDF4.Dataset(target,'a')

            ''' metadata appended, inspire worthy '''
            netcdf_w.setncattr(  "title"        , "KNMI Climate Explorer correlate field service output" )
            netcdf_w.setncattr(  "summary"      , "KNMI Climate Explorer correlate field service output "+sourceA+" for "+sourceB )
            netcdf_w.setncattr(  "keywords"     , "climate,correlation,wps_knmi" )
            netcdf_w.setncattr(  "institute_id" , "KNMI" )            
            netcdf_w.setncattr(  "contact"      , "oldenborgh@knmi.nl" )
            netcdf_w.setncattr(  "date_created" , datetime.now().isoformat() )

            # for sinspire...
            #netcdf_w.setncattr(  "time_coverage_start" , " " )
            #netcdf_w.setncattr(  "time_coverage_end"   , " " )
            #netcdf_w.setncattr(  "geospatial_lat_min"  , " " )
            #netcdf_w.setncattr(  "geospatial_lat_max"  , " " )
            #netcdf_w.setncattr(  "geospatial_lon_min"  , " " )
            #netcdf_w.setncattr(  "geospatial_lon_max"  , " " )
            #netcdf_w.setncattr(  "geospatial_lat_resolution" , "1 m" )
            #netcdf_w.setncattr(  "geospatial_lon_resolution" , "1 m" )

            netcdf_w.setncattr(  "knmi_wps" , self.structure["identifier"] )

            callback(24,info="creating knmi prov var")
            processlib.createKnmiProvVar(netcdf_w)
            
            content1 = generateContent(netcdf_w)    

        except Exception, e:
            content1 = {"copy_error 1264": str(e) , "target":target , "process" : process} 
            logging.info(netcdf_w)
            logging.info(content1)
            logging.info(str(e))

            raise e

        #prov.content.append(content1)
        return content1 , source1, netcdf_w



    def __init__( self ):

        self.structure = {}      
        self.inputsTuple = []

        self.structure["identifier"] = "wps_climexp_correlatefield"   # = 'wps_simple_indice', # only mandatary attribute = same file name
        self.structure["title"]= "climate explorer correlatefield" # = 'SimpleIndices',
        self.structure["abstract"] = "KNMI Climate Explorer: correlatefield function" #'Computes single input indices of temperature TG, TX, TN, TXx, TXn, TNx, TNn, SU, TR, CSU, GD4, FD, CFD, ID, HD17; of rainfal: CDD, CWD, RR, RR1, SDII, R10mm, R20mm, RX1day, RX5day; and of snowfall: SD, SD1, SD5, SD50.'
        self.structure["version"] = "1.0.0"
        self.structure["storeSupported"] = True
        self.structure["statusSupported"] = True
        self.structure["grassLocation"] = False
        self.structure["metadata"] = "METADATA D4P"

        # input tuple describes addLiteralInput, values
        self.inputsTuple = [
                            { 
                            "identifier" : "netcdf_source1" , 
                            "title"      : "Copy input: Input 1 netCDF opendap." ,
                            "type"       : type("String"),
                            "default"    : "http://opendap.knmi.nl/knmi/thredds/dodsC/climate_explorer/cru_ts3.22.1901.2013.pre.dat.nc" ,
                            "abstract"   : "application/netcdf",
                            "values"     : None
                            } ,
                            { 
                            "identifier" : "netcdf_source2" , 
                            "title"      : "Copy input: Input 2 netCDF opendap." ,
                            "type"       : type("String"),
                            "default"    : "http://opendap.knmi.nl/knmi/thredds/dodsC/climate_explorer/nino3.nc" ,
                            "abstract"   : "application/netcdf",
                            "values"     : None
                            } ,
                            { 
                            "identifier" : "netcdf_target" , 
                            "title"      : "Output netCDF." ,
                            "type"       : type("String"),
                            "default"    : "out.nc",
                            "values"     : None
                            } ,
                            { 
                            "identifier" : "frequency" , 
                            "title"      : "Frequency" ,
                            "type"       : type("String"),
                            "default"    : "mon" ,
                            "values"     : None
                            } ,
                            { 
                            "identifier" : "ratio" , 
                            "title"      : "Ratio" ,
                            "type"       : type("String"),
                            "default"    : "1:12" ,
                            "values"     : None
                            } ,
                            { 
                            "identifier" : "average" , 
                            "title"      : "Average" ,
                            "type"       : type("String"),
                            "default"    : "ave" ,
                            "values"     : None
                            } ,
                            { 
                            "identifier" : "tags" , 
                            "title"      : "User Defined Tags CLIPC user tags." ,
                            "type"       : type("String"),
                            "default"    : "provenance_research_knmi",
                            "values"     : None
                            }                   
                          ]


        self.processExecuteCallback = self.process_execute_function

print self