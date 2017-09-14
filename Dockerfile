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

# work from home or opt?
WORKDIR /home/

# Fortran ClimExp sourche. 
# incomplete, edit Makefile.
RUN git clone https://github.com/andrejsim/ClimExp-pyapi.git


# build of climate explorer fortran source.
ENV FORTRAN Fortran
#RUN git clone http://climexp.knmi.nl/Fortran.git
RUN git clone https://github.com/andrejsim/ClimExp-fortran.git ${FORTRAN}

ENV PVM_ARCH build

RUN mkdir -p ${FORTRAN}/${PVM_ARCH}

RUN mkdir -p /nrf
WORKDIR /home/nrf

# get online
####################RUN wget nrf.tar????
COPY nrf/nrf.tar .
COPY nrf/nrf.mk .
RUN tar -xf nrf.tar 
RUN make -f nrf.mk 
RUN cp libnr.a ../${FORTRAN}/${PVM_ARCH}
#############

# need to be commited to core repo.
WORKDIR /home/${FORTRAN}
# missing files add to git.
COPY ./${FORTRAN}/annual2shorter.f .
COPY ./${FORTRAN}/patternfield.F .


RUN cp /home/ClimExp-pyapi/Makefile.docker ${PVM_ARCH}/Makefile
#RUN cp /home/ClimExp-pyapi/Makefile.common .
COPY ./${FORTRAN}/Makefile.common .

WORKDIR /home/${FORTRAN}/${PVM_ARCH}

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
