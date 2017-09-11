FROM ubuntu

MAINTAINER KNMI <info@knmi.nl>

RUN apt-get update && apt-get install -y gfortran \
						 					git \
						 					vim \
						 					apt-utils \
						 					wget \
						 					m4 \        
						 					curl


#netcdf libraries
RUN apt-get install -y build-essential wget libhdf5-dev


# see netcdf install
# 
#RUN apt-get -y --no-install-recommends install m4

# 
# running netcdf4 version 4.4.1.1
WORKDIR /tmp

RUN wget https://support.hdfgroup.org/ftp/HDF5/current18/src/hdf5-1.8.18.tar && \
    tar -xvf hdf5-1.8.18.tar && \
    mkdir /hdf5 
RUN wget https://support.hdfgroup.org/ftp/HDF5/current18/src/CMake-hdf5-1.8.18.tar.gz


RUN	wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.4.1.1.tar.gz
RUN	tar zxvf netcdf-4.4.1.1.tar.gz
WORKDIR /tmp/netcdf-4.4.1.1
RUN export CPPFLAGS=-I/usr/include/hdf5
RUN export LDFLAGS=-L/usr/lib/x86_64-linux-gnu/hdf5

#./configure --prefix=/netcdf4 && \

RUN ./configure && make && make install

RUN rm -rf /tmp/netcdf-4.4.1.1 /tmp/netcdf-4.4.1.1.tar.gz

WORKDIR /home/

# Fortran ClimExp sourche. 
# incomplete, edit Makefile.
RUN git clone http://climexp.knmi.nl/Fortran.git 

#
#RUN mkdir -p Fortran/
#COPY Fortran/ /home/Fortran

#RUN mkdir -p mihajlov/

#VOLUME mihajlov/ #/usr/people/mihajlov

#RUN git clone http://climexp.knmi.nl/climexp.git


# docker build . --rm -t cef:test
# docker run -it cef:test
# docker run  -v /usr/people/mihajlov:/home/mihajlov -it  cef:test