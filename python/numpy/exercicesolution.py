import numpy

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