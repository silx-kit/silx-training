# Copyright (c) 2019 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""Laue simulation code"""


import numpy


def laue_array_size(ncells: int, oversampling: int) -> int:
    """Compute the output array size in each dimension

    :param ncells:
        Number of unit cells in both directions
    :param oversampling: Oversampling factor
    """
    return ncells * oversampling


def laue_image(ncells: int, h: float, k: float, oversampling: int) -> numpy.ndarray:
    """

    :param ncells:
        Number of unit cells in both directions
    :param h:
        H Miller index of reflection where to sample space
    :param k:
        K Miller index of reflection where to sample space
    :param oversampling:
        Oversampling factor
    :return: 2D array
    """
    size = laue_array_size(ncells, oversampling)

    # Prepare cristal structure
    n = numpy.arange(ncells)
    m = numpy.arange(ncells)

    # Prepare sampling positions
    h_sampling_pos = numpy.linspace(h - 0.5, h + 0.5, size, endpoint=True)
    k_sampling_pos = numpy.linspace(k - 0.5, k + 0.5, size, endpoint=True)

    # Do the computation
    h, k, n, m = numpy.meshgrid(h_sampling_pos, k_sampling_pos, n, m, sparse=True)

    # Sum over the unit-cells (last axis of the array) and take the squared modulus
    return numpy.abs(numpy.exp(2j*numpy.pi*(h*n + k*m)).sum(axis=(2,3)))**2
