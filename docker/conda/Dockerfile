FROM ubuntu

RUN apt-get update && apt-get install -y \
	wget \
	less \
	vim \
	python \
	python-pip

RUN wget https://repo.continuum.io/archive/Anaconda2-5.0.0.1-Linux-x86_64.sh

#CMD bash Anaconda2-5.0.0.1-Linux-x86_64.sh

# https://conda.io/docs/user-guide/getting-started.html
# conda --version
# conda update conda
# conda install conda-build
# conda update conda-build

# conda create --name snowflakes biopython
# source activate snowflakes
# conda create --name bunnies python=3.5 astroid babel
# conda remove --name flowers --all
# conda info --envs
# conda list

ENTRYPOINT bash

# git clone https://github.com/conda/conda-recipes
# conda skeleton pypi pyinstrument

# https://github.com/conda/conda-recipes
# conda build pyinstrument
