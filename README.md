:heavy_exclamation_mark: This repo contains a hacky workaround to install brightway2 with conda. This is not needed anymore. The recommended way (April 17)  to install brightway2 with conda is:  
```conda install -c conda-forge -c cmutel -c haasad brightway2```  

# brightway2-conda-installer
[![Anaconda-Server Badge](https://anaconda.org/haasad/brightway2-conda-installer/badges/version.svg)](https://anaconda.org/haasad/brightway2-conda-installer) 

This is a little conda package, that creates a new virtual environment with brightway2 and all dependencies.

## Install
[![Anaconda-Server Badge](https://anaconda.org/haasad/brightway2-conda-installer/badges/installer/conda.svg)](https://conda.anaconda.org/haasad)

`conda install -c haasad brightway2-conda-installer`

## Use
`create_new_brightway2_env` or `bw_env`  
- You will be asked for an environment name and the python version

## Troubleshooting
- if the installation fails, try `conda update conda` and install again
- if you upgraded this package from 0.0.1, but python 3.6 is not an available option, delete any remaining old `brightway2-conda-installer*.egg` files in the site-packages directory and install again

