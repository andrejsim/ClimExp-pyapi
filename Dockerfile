FROM ubuntu

MAINTAINER KNMI <info@knmi.nl>

RUN apt-get update
RUN apt-get install -y 	gfortran \
	 					git \
	 					vim \
	 					curl

WORKDIR /home/

#RUN git clone http://climexp.knmi.nl/Fortran.git

#COPY /usr/people/mihajlov/docker/ClimExp-pyapi/Fortran .

RUN mkdir -p Fortran/
COPY Fortran/* /home/Fortran

#RUN mkdir -p mihajlov/

#VOLUME mihajlov/ #/usr/people/mihajlov

#RUN git clone http://climexp.knmi.nl/climexp.git


# docker build docker/. --rm -t cef:test
# docker run -it cef:test
# docker run -it cef:test -v /usr/people/mihajlov:/home/mihajlov