#!/usr/bin/env python3
# coding: utf-8

import numpy
import time


# Exercice 3

def exercice_3_1():
    """
    Exercice 3.1
    ============
    
    Calculate the element-wise difference between 2 arrays X and Y
    """
    x = numpy.random.random(10)
    y = numpy.random.random(10)
    print('x =', x)
    print('y =', y)

    difference = x - y
    print('x - y =', difference)


def exercice_3_2():
    """
    Exercice 3.2
    ============
    
    Provide an expression to calculate the difference X[i+1]-X[i]
    for all the elements of the 1D array X
    """
    x = numpy.random.random(10)
    print('x =', x)

    diff = x[1:] - x[:-1]
    print('x[i+1] - x[i] =', diff)


# Exercice 4

def exercice_4_1():
    """
    Exercice 4.1
    ============
    
    Generate a 100x100 array with elements in increasing order
    """
    data = numpy.arange(10000)
    data.shape = 100, 100
    # Alternatives:
    # data.shape = 100, -1
    # data = data.reshape(100, 100)
    print('data.shape =', data.shape)

def exercice_4_2():
    """
    Exercice 4.2
    ============

    Perform a 2 x 2 binning
    """
    data = numpy.arange(100).reshape(10, 10)
    print('data =', data)
    binned = data[::2, ::2] + data[::2, 1::2] + data[1::2, ::2] + data[1::2, 1::2]
    print('2x2 binned =', binned)

    # Alternative
    alt_binned = data.reshape(5, 2, 5, 2).sum(axis=3).sum(axis=1)
    print('2x2 binned (alternative) =', alt_binned)


# Exercice 5

def ex5_inefficient_fill(height, width):
    data = numpy.zeros((height, width), dtype=numpy.float)
    for row in range(int(height)):
        for col in range(int(width)):
            data[row, col] = numpy.cos(row) * numpy.sin(col)
    return data


def ex5_naive_fill(height, width):
    width_sin = numpy.sin(numpy.arange(width))
    height_cos = numpy.cos(numpy.arange(height))
    data = numpy.zeros((height, width), numpy.float)
    for row in range(int(height)):
        for col in range(int(width)):
            data[row, col] = height_cos[row] * width_sin[col]
    return data


def ex5_clever_fill(height, width):
    width_sin = numpy.sin(numpy.arange(width))
    height_cos = numpy.cos(numpy.arange(height))
    cos_loop = numpy.outer(height_cos, numpy.ones(width))
    sin_loop = numpy.outer(numpy.ones(height), width_sin)
    return cos_loop * sin_loop


def ex5_practical_fill(height, width):
    width_sin = numpy.sin(numpy.arange(width))
    height_cos = numpy.cos(numpy.arange(height))
    sin_loop, cos_loop = numpy.meshgrid(width_sin, height_cos)
    return sin_loop * cos_loop


def ex5_optimized_fill(height, width):
    width_sin = numpy.sin(numpy.arange(width))
    height_cos = numpy.cos(numpy.arange(height))
    return numpy.outer(height_cos, width_sin)


def exercice_5():
    """
    Exercice 5
    ==========

    Write a function fill_array(height, width) to generate an array of dimension (height, width) in which X[row, column] = cos(row) * sin(column)

    Time it for n=1000, m = 1000
    """
    height, width = 1000, 1000

    start_time = time.time()
    data1 = ex5_inefficient_fill(height, width)
    print('inefficient fill took about %f s' % (time.time() - start_time))
    
    start_time = time.time()
    data = ex5_naive_fill(height, width)
    print('naive fill took about %f s' % (time.time() - start_time))
    assert numpy.all(numpy.equal(data1, data))

    start_time = time.time()
    data = ex5_clever_fill(height, width)
    print('clever fill took about %f s' % (time.time() - start_time))
    assert numpy.all(numpy.equal(data1, data))

    start_time = time.time()
    data = ex5_practical_fill(height, width)
    print('practical fill took about %f s' % (time.time() - start_time))
    assert numpy.all(numpy.equal(data1, data))

    start_time = time.time()
    data = ex5_optimized_fill(height, width)
    print('optimized fill took about %f s' % (time.time() - start_time))
    assert numpy.all(numpy.equal(data1, data))


if __name__ == "__main__":
    print(exercice_3_1.__doc__)
    exercice_3_1()

    print(exercice_3_2.__doc__)
    exercice_3_2()

    print(exercice_4_1.__doc__)
    exercice_4_1()

    print(exercice_4_2.__doc__)
    exercice_4_2()

    print(exercice_5.__doc__)
    exercice_5()
