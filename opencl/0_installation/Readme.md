# Installation procedure:

## Visa
Log into https://visa.esrf.fr
Create new instance
Custommize the instance settings
Choose 32cores, 128GB memory: esrf.gpu.a16.large
check "I accept"
Create the instance
Connect to the instance

## Install the environment
Open a web browser on https://github.com/conda-forge/miniforge
Open a terminal
Install miniforge from:
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh

mamba install ipykernel pyopencl ocl-icd clinfo clpeak pillow matplotlib ipympl
python -m ipykernel install --user --name=opencl

## Clone the working directory
git clone https://github.com/silx-kit/silx-training

## Jupyterlab
Reconnect to the instance using jupyterlab

