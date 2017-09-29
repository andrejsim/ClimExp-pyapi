export FORTRAN=./Fortran
export PVM_ARCH=build


git clone https://github.com/andrejsim/ClimExp-fortran.git ${FORTRAN}

mkdir -p ${FORTRAN}/${PVM_ARCH}
# moved this library temporarily to git hub, can not locate relevant source online. (Pending)
git clone https://github.com/andrejsim/nrf
cd nrf
tar -xf nrf.tar 
make -f nrf.mk 
cd ..
cp ./nrf/libnr.a ${FORTRAN}/${PVM_ARCH}



cp Makefile.docker ${FORTRAN}/${PVM_ARCH}/Makefile

cd ${FORTRAN}/${PVM_ARCH}

make
