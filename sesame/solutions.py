# coding: utf-8

"""
Contain solution for the python/numpy training
"""

__authors__ = ["Pierre Knobel", "Jerome Kieffer", "Henri Payno",
               "Armando Sole", "Valentin Valls", "Thomas Vincent"]
__date__ = "18/09/2018"
__license__ = "MIT"


import inspect

import numpy

def solution_bining():
    data = numpy.arange(10000).reshape(100, 100)
    data = data + 1
    binned = data[::2, ::2] + data[::2, 1::2] + data[1::2, ::2] + data[1::2, 1::2]
    return data, binned
