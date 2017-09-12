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
RUN apt-get install -y 	build-essential \
					 	  					libhdf5-dev \
					 	  					netcdf-bin \
					 	  					netcdf-doc \
					 	  					libnetcdf-dev \
					 	  					libnetcdff6 \ 
					 	  					libnetcdff-dev


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
RUN git clone http://climexp.knmi.nl/Fortran.git 

WORKDIR /home/Fortran
# missing files add to git.
COPY ./Fortran/annual2shorter.f .
COPY ./Fortran/patternfield.F .

ENV PVM_ARCH /home/Fortran/ce
RUN mkdir -p ${PVM_ARCH}

RUN cp /home/ClimExp-pyapi/Makefile .
RUN cp /home/ClimExp-pyapi/Makefile.common ../Makefile.common


# run nc-config --all and compare to Makefile

# docker build . --rm -t cef:test
# docker run -it cef:test
# docker run  -v /usr/people/mihajlov:/home/mihajlov -it  cef:test