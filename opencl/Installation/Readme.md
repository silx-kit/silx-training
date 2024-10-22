# Installation procedure:

## Use the Visa instance:
* Log into https://visa.esrf.fr
* Create new instance
* Custommize the instance settings with:
    + Choose 32cores, 128GB memory: esrf.gpu.a16.large
    + check "I accept"
    + Create the instance (takes several minutes)
* Connect to the instance

You will land to a linux environment (xfce) where you will have to install the environment.

## Install the environment
* Open a web browser in the visa machine and go to on https://github.com/conda-forge/miniforge
* Open a terminal in the visa machine
* Install miniforge from:
  - wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
  - bash Miniforge3-Linux-x86_64.sh
  - mamba install ipykernel pyopencl ocl-icd clinfo clpeak pillow matplotlib ipympl oclgrind
  - python -m ipykernel install --user --name=opencl
  - git clone https://github.com/silx-kit/silx-training

## Jupyterlab
Deconnect from the emulated environment and Reconnect to the instance using Jupyter-Lab

