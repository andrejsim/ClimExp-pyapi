FROM ubuntu

MAINTAINER KNMI <info@knmi.nl>

RUN apt-get update
RUN apt-get install -y gfortran

WORKDIR /home/

RUN git clone http://climexp.knmi.nl/Fortran.git
RUN git clone http://climexp.knmi.nl/climexp.git
