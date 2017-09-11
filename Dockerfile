FROM ubuntu

MAINTAINER KNMI <info@knmi.nl>

RUN apt-get update && apt-get install -y gfortran \
						 					git \
						 					vim \
						 					apt-utils \
						 					m4 \        
						 					curl


#netcdf libraries
RUN apt-get install -y build-essential \
					   						wget \
					 	  					libhdf5-dev


# install libraries... 
# running netcdf4 version 4.4.1.1
WORKDIR /tmp

RUN H5DIR=/usr/lib/x86_64-linux-gnu/hdf5/serial/

	# this should not be necessary since libhdf5 is already here,
	#RUN wget https://support.hdfgroup.org/ftp/HDF5/current18/src/hdf5-1.8.19.tar && tar -xvf hdf5-1.8.19.tar
	#RUN wget https://support.hdfgroup.org/ftp/HDF5/current18/src/CMake-hdf5-1.8.19.tar.gz
	#RUN mkdir hdf5
	#WORKDIR /tmp/hdf5-1.8.19
	#RUN ./configure --prefix=/hdf5 --enable-fortran && make && make check && make install && make check-install


# latest verions 10-Sept-2017
# install netcdf4
RUN	wget ftp://ftp.unidata.ucar.edu/pub/netcdf/netcdf-4.4.1.1.tar.gz
RUN	tar zxvf netcdf-4.4.1.1.tar.gz
WORKDIR /tmp/netcdf-4.4.1.1

RUN CPPFLAGS=-I${H5DIR}/include 
RUN LDFLAGS=-L${H5DIR}/lib

ENV PATH $PATH:${H5DIR}/lib
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:${H5DIR}/lib 
ENV PATH $PATH:${H5DIR}/lib

# unsure about --disable-netcdf-4, else build fails.
RUN ./configure  --disable-netcdf-4 --prefix=/netcdf4 && make && make install

RUN rm -rf /tmp/netcdf-4.4.1.1 /tmp/*.tar.gz 

WORKDIR /home/

# Fortran ClimExp sourche. 
# incomplete, edit Makefile.
RUN git clone http://climexp.knmi.nl/Fortran.git 

WORKDIR /tmp/

#RUN mkdir -p mihajlov/
#VOLUME mihajlov/ #/usr/people/mihajlov
#RUN git clone http://climexp.knmi.nl/climexp.git


# docker build . --rm -t cef:test
# docker run -it cef:test
# docker run  -v /usr/people/mihajlov:/home/mihajlov -it  cef:test