
# mkdir Fortran/ce
# cd Fortran/ce

# cp ../Makefile.linux_gfortran_64 .

# FFLAGS = -Ktrap=fp -g -C
###FFLAGS = -g -Dlinux -fbounds-check -fbackslash -ffpe-trap=invalid,zero,overflow

#[mihajlov@pc150396 ce]$ nc-config --fflags
#-I/usr/include
#[mihajlov@pc150396 ce]$ nc-config --includedir
#/usr/include

FFLAGS = -O -Dlinux -fbackslash -ffpe-trap=invalid,zero,overflow -I/usr/include
EOFFLAGS = $(FFLAGS)

CFLAGS = -O2

#nc-config --lib
#L/usr/lib64 -lnetcdf
#[mihajlov@pc150396 ce]$ nc-config --fc
#gfortran
#[mihajlov@pc150396 ce]$ nc-config --flibs
#-lnetcdff


SYSLIBS = -L/usr/lib -L/usr/lib64/ -lnetcdff -lnetcdf -lhdf5 -llapack -lblas
FC = gfortran
LD = gfortran
RANLIB = echo ready with

###LDBIGFLAG = -Wl,-Bstatic

EXTRAOBJS = getppid.o swapbyte.o

# requires nrf.a
# mkdir nrf; cd !$
# from philippe: cp /usr/people/sager/proj/nrf/nrf.tar .
# from philippe: cp /usr/people/sager/proj/nrf/nrf.mk  .
# from philippe: cp /usr/people/sager/proj/nrf/nrf.dep .
# tar -xf nrf.tar 
# make -f nrf.mk 
# cp libnr.a Fortran/ce


# rm from Makefile.common		annual2shorter.o \ (missing source file)

# rm patternfield no source


include ../Makefile.common
