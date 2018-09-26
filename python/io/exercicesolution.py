# coding: utf-8

"""
Contain solution for the python/numpy training
"""

__authors__ = ["Pierre Knobel", "Jerome Kieffer", "Henri Payno",
               "Armando Sole", "Valentin Valls", "Thomas Vincent"]
__date__ = "18/09/2018"
__license__ = "MIT"


import numpy
import os


def solution(file_path):
    """Solution to the io notebook exercise"""
    raw_data = load_data(file_path)
    proc_data, mask = process_data(data=raw_data)
    save_data(mask=mask, proc_data=proc_data, raw_data=raw_data,
              output_file='process.h5')
    list_root('process.h5')
    return raw_data, proc_data, mask


def load_data(file_path):
    """load data contained in data/medipix.edf"""
    import fabio
    data = fabio.open(file_path).data
    return data


def process_data(data):
    """
    Process the data The goal of the processing is to clamp the pixels values
    to a new range of values ([10%, 90%] of the existing one). To do so:

    * Create a mask to detect pixel which are below 10% 
    * With the above mask, set the affected pixels to the 10% 'low value'.
    * do the same for value above 90%
    * create the mask of all the modify pixel

    """
    val_10 = (data.max() - data.min()) * 0.1 + data.min()
    val_90 = (data.max() - data.min()) * 0.9 + data.min()
    mask_10 = data <= val_10
    mask_90 = data >= val_90
    mask = numpy.logical_or(mask_10, mask_90)

    proc_data = numpy.copy(data)
    proc_data[mask_10 == True] = val_10
    proc_data[mask_90 == True] = val_90
    return proc_data, mask


def save_data(mask, proc_data, raw_data, output_file):
    """
    save mask, proc_data and raw_data into output_file
    """
    import h5py
    with h5py.File(output_file, "w") as h5_file:
        h5_file['/mask'] = mask
        h5_file['/result'] = proc_data
        h5_file['/raw'] = raw_data


def list_root(file_path):
    """List dataset / group contained at the root level"""
    import h5py
    assert os.path.exists(file_path)
    h5_file = h5py.File(file_path)
    print('root level:')
    print(list(h5_file['/'].keys()))
