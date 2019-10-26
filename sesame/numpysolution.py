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


def show(exercice_name):
    function = globals()[exercice_name]
    print(inspect.getsource(function))
    return function()


def solution_bining():
    data = numpy.arange(10000).reshape(100, 100)
    data = data + 1
    binned = data[::2, ::2] + data[::2, 1::2] + data[1::2, ::2] + data[1::2, 1::2]
    return data, binned



def ex3_1():
    """ Simple example of an element wise comparaison"""
    x = numpy.arange(10)
    y = numpy.arange(1, 11)

    difference = x - y
    return difference


def ex3_2():
    """ Simple way to compute the difference x[i+1]-x[i] for all the elements
    of the 1D array"""
    x = numpy.arange(10)

    difference = x[1:] - x[:-1]
    return difference


def ex4_1():
    """Generate a 1D array of [1..99] then operate a binning 1 2 3 4 -> 1+2 3+4
    """
    data = numpy.arange(100) + 1
    binned = data[::2] + data[1::2]
    return data, binned


def ex4_2():
    """Generate a 2D array of [1..9999] then operate a 2x2 binning
    """
    data = numpy.arange(10000).reshape(100, 100)
    data = data + 1
    binned = data[::2, ::2] + data[::2, 1::2] + data[1::2, ::2] + data[1::2, 1::2]
    return data, binned


def ex4_2_alt():
    """Generate a 2D array of [1..9999] then operate a 2x2 binning using numpy
    sum and moving the array to 4D
    """
    height = 100
    width = 100
    data = numpy.arange(10000).reshape(height, width)
    data = data + 1
    reshaped_data = data.reshape(height // 2, 2, width // 2, 2)
    binned = reshaped_data.sum(axis=3).sum(axis=1)
    return data, binned


def ex5_inefficient_fill(height=1000, width=1000):
    """Inefficient fill using 2 for loops"""
    data = numpy.zeros((height, width), dtype=numpy.float)
    for row in range(int(height)):
        for col in range(int(width)):
            data[row, col] = numpy.cos(row) * numpy.sin(col)
    return data


def ex5_naive_fill(height=1000, width=1000):
    """Fill using 2 for loops but pre-computing sin and cos"""
    width_sin = numpy.sin(numpy.arange(width))
    height_cos = numpy.cos(numpy.arange(height))
    data = numpy.zeros((height, width), numpy.float)
    for row in range(int(height)):
        for col in range(int(width)):
            data[row, col] = height_cos[row] * width_sin[col]
    return data


def ex5_clever_fill(height=1000, width=1000):
    """Fill using 2 outer products"""
    width_sin = numpy.sin(numpy.arange(width))
    height_cos = numpy.cos(numpy.arange(height))
    cos_loop = numpy.outer(height_cos, numpy.ones(width))
    sin_loop = numpy.outer(numpy.ones(height), width_sin)
    return cos_loop * sin_loop


def ex5_practical_fill(height=1000, width=1000):
    """Fill using meshgrid"""
    width_sin = numpy.sin(numpy.arange(width))
    height_cos = numpy.cos(numpy.arange(height))
    sin_loop, cos_loop = numpy.meshgrid(width_sin, height_cos)
    return sin_loop * cos_loop


def ex5_optimized_fill(height=1000, width=1000):
    """Fill using outer product"""
    width_sin = numpy.sin(numpy.arange(width))
    height_cos = numpy.cos(numpy.arange(height))
    return numpy.outer(height_cos, width_sin)


def ex5_atleast_2d_fill(height=1000, width=1000):
    """Fill using atleast_2d and transpose"""
    sine = numpy.sin(numpy.arange(width))
    cosine = numpy.cos(numpy.arange(height))
    return numpy.atleast_2d(sine) * numpy.atleast_2d(cosine).T
