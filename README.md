# ClimExp-pyapi

### KNMI
work integrated into C3S 34a Lot2 project

binding python functions to fortran source code

ClimExp source code is available on ClimExp-fortran.git, original source at http://climexp.knmi.nl

Project is Docker ready.
```
docker build . --rm -t cef:test
docker run -it cef:test
docker run -v <localmount_of_opendap_data>:/root/climexp/DATA/ -it cef
```

Data for deomo is available as, open data for correlate function:
```
http://opendap.knmi.nl/knmi/thredds/dodsC/climate_explorer/
```

Test souce by running following line in docker:
```
python simple_bind_correlatefield.py
```

Special thanks to the Geert Jan van Oldenborgh (KNMI) for his long term work in building the Climate Explorer.
