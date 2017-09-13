FROM ubuntu


MAINTAINER KNMI <info@knmi.nl>


RUN apt-get update && apt-get install -y gfortran \
                      git \
                      vim \
                      apt-utils \
                      m4 \        
                      wget \
                      curl


#netcdf libraries
RUN  apt-get update &&  apt-get install -y  build-essential \
                        libhdf5-dev \
                        netcdf-bin \
                        netcdf-doc \
                        libnetcdf-dev \
                        libblas-dev \
                        liblapack-dev \
                        libnetcdff6 \
                        libnetcdff-dev \
                        r-base


  #installed here by libhdf5-dev (there is also a libhdf5-serial-dev...)
  #ENV H5DIR /usr/lib/x86_64-linux-gnu/hdf5/serial
  #ENV CPPFLAGS -I${H5DIR}/include 
  #ENV LDFLAGS -L${H5DIR}/lib

  #ENV PATH $PATH:${H5DIR}/lib
  #ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:${H5DIR}/lib 
  #ENV PATH $PATH:${H5DIR}/lib

# work from home or opt?
WORKDIR /home/

# Fortran ClimExp sourche. 
# incomplete, edit Makefile.
RUN git clone https://github.com/andrejsim/ClimExp-pyapi.git


# build of climate explorer fortran source.
RUN git clone http://climexp.knmi.nl/Fortran.git 

ENV PVM_ARCH build

RUN mkdir -p Fortran/${PVM_ARCH}

RUN mkdir -p /nrf
WORKDIR /home/nrf

# get online
####################RUN wget nrf.tar????
COPY nrf/nrf.tar .
COPY nrf/nrf.mk .
RUN tar -xf nrf.tar 
RUN make -f nrf.mk 
RUN cp libnr.a ../Fortran/${PVM_ARCH}
#############

# need to be commited to core repo.
WORKDIR /home/Fortran
# missing files add to git.
COPY ./Fortran/annual2shorter.f .
COPY ./Fortran/patternfield.F .


RUN cp /home/ClimExp-pyapi/Makefile.docker ${PVM_ARCH}/Makefile
#RUN cp /home/ClimExp-pyapi/Makefile.common .
COPY ./Fortran/Makefile.common .

WORKDIR /home/Fortran/${PVM_ARCH}

RUN make
# run nc-config --all and compare to Makefile

# docker build . --rm -t cef:test
# docker run -it cef:test
# docker run  -v /usr/people/mihajlov:/home/mihajlov -it  cef:test

# install python, test and api.
WORKDIR /home/ClimExp-pyapi

RUN apt-get install -y python python-dev python-distribute python-pip
RUN pip install --upgrade pip
RUN pip install scipy numpy pandas netcdf4 xarray datetime pprint

# data is not provided
# download location:  http://opendap.knmi.nl/knmi/thredds/dodsC/climate_explorer/
#
# or map with volume:
# docker run -v ~/climexp/DATA/:/root/climexp/DATA/ -it cef
