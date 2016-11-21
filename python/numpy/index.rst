
.. |br| raw:: html

   <br />


***********************
 Introduction to Numpy
***********************

V. A. Sole
ESRF Software Group

-----

Summary
=======

0. Introduction
#. Numpy
#. Creation of arrays
#. Array methods and functions
#. Linear algebra

-----

Introduction
============

\

-----

Basic operations
----------------

\+
    Addition
\-
    Substraction
\/
    Division
\**
    Exponentiation (I prefer to use pow(a, b) instead of a**b)
abs(x)
    Absolute value of x


%
    Remainder of a/b
\/\/
    Integer part of a/b

-----

Basic high level data types
---------------------------

- Numbers: 10, 10.0, 1.0e+01,  ( 10.0+3j )
- Strings, Unicode: “Hello World!”, u”Hello World!”
- Lists: [‘abc’, 3, “x”]
- Tuples: (‘abc’, 3, ‘x’)
- Dictionnaries: {‘key1’:’abc’, ‘key2’: 3, ‘key3’:’x’}

-----

Exercice - 1
------------

Use python as a simple calculator.
Start the python interpreter and try the previous operations on different numbers (integers, floats, ... ).

Operating with other data types. At the python prompt (``In [ ]:`` or ``>>>``), type:

.. code-block:: python

    a = [1, 2, 3]

What is the result of ``2 * a[2]`` ?

What is the result of ``2 * a``  ?

Combine operations and data types and comment your findings.

-----

Conclusion
----------

Without additional libraries, python is almost useless for scientific computing

-----

Scientist's Swiss knife
-----------------------

The ``numpy`` module

``IPython`` provides an improved interpreter environment

``matplotlib`` provides high quality graphics

``SciPy`` provides additional scientific capabilities

-----

Numpy
=====

``numpy`` is THE library providing number crunching capabilities to Python

It extends Python providing tools for

- Treatment of multi-dimensional data
- Access to optimized linear algebra libraries
- Encapsulation of C and Fortran code

-----

The Numpy ndarray objects
-------------------------

The (nd)array object:

- Collection of elements of the same type
- Implemented in memory as a true table optimized for performance
- Handled in similar way as any other Python object

Multi-dimensional, any type of data

- Dimensions can be modified, flexible indexation
- Internal optimization for 1D, 2D and 3D

It can be interfaced with other languages

.. code-block:: python

    >>> import numpy

-----

Array creation - 1
------------------

**Given its contents**:

From a list of values:

.. code-block:: python

  a = numpy.array([1, 2, 3, 5, 7, 11, 13, 17])

From a list of values and dimensions:

.. code-block:: python

  a = numpy.array([0.1, 0.0, 0.2])
  b = numpy.array([[1, 2, 3], [4, 5, 6]])

Also specifying the type of element:

.. code-block:: python

  a = numpy.array([0.1, 0.0, 0.2], dtype=numpy.float)
  b = numpy.array([[1, 2, 3], [4, 5, 6]], dtype=numpy.int)

-----

Array creation - 2
------------------

Besides using array, one can create arrays using **dedicated methods**:

``numpy.empty(dimensions_tuple, dtype=numpy.float)``:

.. code-block:: python

  >>> a = numpy.empty((2, 4), dtype=numpy.float)

``numpy.zeros(dimensions_tuple, dtype=numpy.float)``:

.. code-block:: python

  >>> a = numpy.zeros((2, 4), dtype=numpy.float)

``numpy.ones(dimensions_tuple, dtype=numpy.float)``:

.. code-block:: python

  >>> a = numpy.ones((3, 5), dtype=numpy.int)

``numpy.arange(start, end, step)``:

.. code-block:: python

  >>> a = numpy.arange(10.)
  >>> b = numpy.arange(1, 10, 2)

``numpy.identity(n, dtype=numpy.float)``:

.. code-block:: python

  >>> a = numpy.identity(3,dtype=numpy.int)

------

Array creation - 3
------------------

**As function of the indices**: ``numpy.fromfunction``

.. code-block:: python

  >>> def initFunction(i, j):
  ...     return 100. + 10 * i + j

  >>> c = numpy.fromfunction(initFunction, (5,3))
  >>> c
  array([[100., 101., 102.],
         [110., 111., 112.],
         [120., 121., 122.],
         [130., 131., 132.],
         [140., 141., 142.]])

**From a file**: ``numpy.load``

.. code-block:: python

  >>> a = numpy.ones((3, 5, 7))
  >>> numpy.save('data.npy', a)
  >>> b = numpy.load('data.npy')

-----

Exercice - 2
------------

Use python as a simple calculator. Start the python interpreter and try the basic operations on different arrays of numbers (integers, floats, ...).

At the python prompt (``In [ ]:`` or ``>>>``), type:

.. code-block:: python

  >>> import numpy
  >>> a = [1, 2, 3]
  >>> b = numpy.array(a)

- What is the result of ``2 * a[2]``?
- What is the result of ``2 * a``?
- What is the result of ``2 * b[2]``?
- What is the result of ``2 * b``?
- What is the result of ``b / 2``?
- What is the result of ``b / 2.0``?

-----

Solution - 2
------------

.. code-block:: python

  >>> import numpy

  >>> a = [1, 2, 3]
  >>> b = numpy.array(a)
  >>> a * 2
  [1, 2, 3, 1, 2, 3]
  >>> b * 2
  array([2, 4, 6])
  >>> b/2
  array([0, 0, 1])
  >>> b/2.
  array([0, 0.5, 1])

-----

Types of elements - 1
---------------------

Traditional types:

- Integers and real numbers in simple and double precision
- Complex
- Chains of characters
- Any python object

WARNING: better specify the element type for portability, particularly for integer types

- ``numpy.float`` corresponds to double precision (64 bit representation)
- ``numpy.int`` corresponds to a long integer (64 bit or 32 bit depending on platform)
- ``numpy.complex64`` corresponds to two 32 bit floats (real and imaginary parts)

Consider using the types ``numpy.float32``, ``numpy.float64``, ``numpy.int32``, ``numpy.int64``, ...

-----

Types of elements - 2
---------------------

**Arrays of objects**

The elements of an array may contain any other object. Try the following:

.. code-block:: python

  >>> a= {'dict':'a'}
  >>> b= {'dict':'b'}
  >>> c= {'dict':'c'}
  >>> v = numpy.array([a, b, c])
  >>> v

**Record Arrays**

They allows access to the data using named fields.
Imagine your data being a spreadsheet, the field names would be the column heading.

.. code-block:: python

  >>> img = numpy.zeros(
  ...    (2,2),
  ...    {'names': ('r','g','b'),
  ...     'formats': (numpy.float32, numpy.float32, numpy.float32)})
  >>> img['r'] = 10.

-----

Array attributes - 1
--------------------

**dtype**

Identifies the type of the elements of the array:

.. code-block:: python

  >>> a = numpy.array([1, 2, 3])
  >>> a.dtype
  dtype('int64')
  >>> a.dtype.char
  'l'

**shape**

Tuple containing the array dimensions.
It is a Read and Write attribute.

.. code-block:: python

  >>> a= numpy.ones((3, 5, 7))
  >>> a.shape
  (3, 5, 7)
  >>> a.shape = (21, 5)
  >>> numpy.shape(a)
  (21, 5)

-----

Array attributes - 2
--------------------

**flat**

1D view of the array.

It does not modify the array.

It is an iterator.

.. code-block:: python

  >>> a = numpy.arange(10.)
  >>> a.shape = (2, 5)
  array([[0, 1, 2, 3, 4],
         [5, 6, 7, 8, 9]])
  >>> a.flat
  <numpy.flatiter object at ...>

-----

Array attributes - 3
--------------------

**T**

It returns a transposed view of the array

.. code-block:: python

  >>> b = a.T

Exists also as function

.. code-block:: python

  >>> a.transpose()
  >>> numpy.transpose(a)

-----

Array attribues - 4
-------------------

**advances attributes**: nothing is hidden

- ``data``: The read/write buffer containing actually the data
- ``flags``: Information about the contiguity of the data in the buffer
- ``itemsize``: Size of a single item, also the size of dtype
- ``nbytes``: Size in bytes occupied bu the buffer in memory: size*itemsize
- ``ndim``: Number of dimensions of the nd_array: len(shape)
- ``size``: Total number of element in the nd_array: prod(shape)
- ``strides``: Tuple of bytes to step in each dimension when traversing an array

-----

Indexing - 1
------------

One can select elements as with any other Python sequence.

- Indexing starts at 0 for each array dimension
- Indexes can be negative: x[-1] is the same as x[len(x) -1]

The output refers to the original array and usually it is not contiguous in memory.

-----

Indexing - 2
------------

Syntax similar to other python sequences:

.. code-block:: python

  >>> a = numpy.arange(24).reshape((6, 4))
  >>> a[3, 2]
  14
  >>> a[3:4, 2]
  array([14])

  >>> a[3]  # all the elements of the fourth row
  >>> a[3,:]  # same as previous assuming a has at least two dimensions
  >>> a[0, -1]  # last element of the first row
  >>> a[0:2, 0:4:2]  # slicing allowed
  >>> a[0:2, :] = 5  # assignation is also possible

-----

Indexing - 3
------------

The indexation argument is a list or an array:

.. code-block:: python

  >>> a = numpy.arange(10.) * 2
  >>> a[[0, 3, 5]]
  array([ 0., 4., 8])

The indexation argument can be a logical array:

.. code-block:: python

  >>>a[a>3]
  array([4., 5., 6., 7., 8., 9.])

-----

Exercice - 3
------------

#. Calculate the element-wise difference between 2 arrays X and Y?
#. Provide an expression to calculate the difference X[i+1]-X[i] for all the elements of the 1D array X.

-----

Methods - 1
-----------

There are methods associated to the arrays -> ``dir(a)`` where a is an array

- ``a.min()`` Returns the minimum of the array
- ``a.max()`` Returns the maximum of the array
- ``a.size`` Returns the number of elements of the array
- ``a.sort()`` Returns an array with the sorted elements
- ``a.sum()`` Returns the sum of the elements of the array
- ``a.sum(axis=None, dtype=None, out=None)`` Perform the sum along a specified axis

There are functions associated to the module -> ``dir(numpy)``
Many methods are available in both forms:

.. code-block:: python

  b = numpy.copy(a)  # explicit copy of array a
  b = numpy.array(a, copy = True)  # explicit copy of array a

-----

Methods - 2
-----------

.. code-block:: python

  >>> idx = numpy.argsort(a)

Get the sorted indices, not the sorted the array.

.. code-block:: python

  >>> numpy.take(a, idx)

Returns a new sorted array

Complete function defined as ``argsort(a, axis=-1, kind=‘quicksort’, order=None)``

Try ``numpy.argsort(numpy.zeros(10.))``

WARNING: Consider setting the kind to ``'mergesort'``

-----

Methods - 3
-----------

- ``numpy.loadtxt(filename)	 # Load data from a text file.``
- ``numpy.savetxt(filename, array)``

Many more options:

- ``loadtxt(fname, dtype=<type 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)``
  Each row in the text file must have the same number of values.

-----

Views
-----

New object pointing to the same buffer:

.. code-block:: python

  >>> a = numpy.arange(10.)
  >>> a.shape = 2, 5
  >>> c = a.T
  >>> a[1, 2]
  7
  >>> c[2, 1] = 10
  >>> a[1, 2]
  10
  >>> b = a[:]
  >>> b.shape = -1  # makes whatever needed to get the matching number
  >>> b.shape = 10  # equivalent to previous
  >>> a.shape
  2, 5
  >>> b[0] = 25
  >>> a[0, 0]
  25

-----

Exercice - 4
------------

#. Generate a 100 x 100 array with elements in increasing order
#. Perform a 2 x 2 binning. Just for reminder, a binning operation consists in:

Original:

== == == ==
 1  2  3  4
 5  6  7  8
 9 10 11 12
13 14 15 16
== == == ==

2x2 binned:

========== ===========
  1+2+3+4    3+4+7+8
9+10+13+14 11+12+15+16
========== ===========

-----

Array operations
----------------

All standard operations when applied to arrays, operate element by element.

Other common operations are:

- ``numpy.dot(a, b)`` Standard linear algebra matrix multiplication
- ``numpy.inner(a, b)`` Inner product
- ``numpy.outer(a, b)`` Outer product

-----

Linear Algebra - numpy.linalg
-----------------------------

As usual, ``dir()`` and ``help()`` are your friends...
The operations you will usually use:

- ``det(x)`` Determinant of x
- ``eig(x)`` Returns the eigenvalues and eigenvectors of x
- ``eigh(x)`` Idem profiting of x being a hermitian matrix
- ``inv(x)`` Inverse matrix of x
- ``svd(x)`` Singular value decomposition of x
- ``dot(a, b)`` Standard linear algebra matrix multiplication
- ``inner(a, b)`` Inner product
- ``outer(a, b)`` Outer product

-----

Random sampling – numpy.random
------------------------------

Simple random data

- ``randint(low[, high, size])`` Return random integers from low (inclusive) to high (exclusive).
- ``random([size])`` Return random floats in the half-open interval [0.0, 1.0).
- ``bytes(length)`` Return random bytes.

Permutations

- ``shuffle(x)`` Modify a sequence in-place by shuffling its contents.
- ``permutation(x)`` Randomly permute a sequence, or return a permuted range.

Distributions:

- ``beta``, ``binomial``, ``chisquare``, ``dirichlet``, ``exponential``...

-----

Discrete Fourier Transform – numpy.fft
--------------------------------------

Based on FFTPACK translated to C, numpy provides:

- 1D FFT: complex, real or hermitian, direct and inverse

.. image:: fft1d.png
   :align: right

- 2D FFT: complex, real or hermitian, direct and inverse

.. image:: fft2d.png
   :align: right

- nD FFT: complex, real or hermitian, direct and inverse

-----

Polynomials – numpy.polynomial
------------------------------

Polynomials in NumPy can be created, manipulated, and even fitted.

Polynomial Package
^^^^^^^^^^^^^^^^^^

Using the Convenience Classes |br|
Polynomial Module (numpy.polynomial.polynomial) |br|
Chebyshev Module (numpy.polynomial.chebyshev) |br|
Legendre Module (numpy.polynomial.legendre) |br|
Laguerre Module (numpy.polynomial.laguerre) |br|
Hermite Module, "Physicists" (numpy.polynomial.hermite) |br|
HermiteE Module, "Probabilists" (numpy.polynomial.hermite_e) |br|

Old package Poly1d
^^^^^^^^^^^^^^^^^^

Basics |br|
Fitting |br|
Calculus |br|
Arithmetic |br|
Warnings |br|

-----

Exercice - 5
------------

#. Write a function ``fill_array(height, width)`` to generate an array of dimension (height, width) in which X[row, column] = cos(row) * sin(column)

#. Time it for n=1000, m = 1000

-----

Correction - 5
--------------

.. code-block:: python

  def inefficient_fill(height, width):
      data = numpy.zeros((height, width), dtype=numpy.float)
      for row in range(int(height)):
          for col in range(int(width)):
              data[row, col] = numpy.cos(row) * numpy.sin(col)
      return data

  def naive_fill(height, width):
      width_sin = numpy.sin(numpy.arange(width))
      height_cos = numpy.cos(numpy.arange(height))
      data = numpy.zeros((height, width), numpy.float)
      for row in range(int(height)):
          for col in range(int(width)):
              data[row, col] = height_cos[row] * width_sin[col]
      return data

  def clever_fill(height, width):
      width_sin = numpy.sin(numpy.arange(width))
      height_cos = numpy.cos(numpy.arange(height))
      cos_loop = numpy.outer(height_cos, numpy.ones(width))
      sin_loop = numpy.outer(numpy.ones(height), width_sin)
      return cos_loop * sin_loop

-----

Correction - 5
--------------

.. code-block:: python

  def practical_fill(height, width):
      width_sin = numpy.sin(numpy.arange(width))
      height_cos = numpy.cos(numpy.arange(height))
      sin_loop, cos_loop = numpy.meshgrid(width_sin, height_cos)
      return sin_loop * cos_loop

  def optimized_fill(height, width):
      width_sin = numpy.sin(numpy.arange(width))
      height_cos = numpy.cos(numpy.arange(height))
      return numpy.outer(height_cos, width_sin)

Speed is a question of algorithms.

It is not just a question of languages.

================ ==================
Implementation   Duration (seconds)
================ ==================
inefficient_fill 5.038374
naive_fill       0.886195
clever_fill      0.016798
practical_fill   0.014922
optimized_fill   0.004526
================ ==================

-----

Many more modules and documentation
-----------------------------------

Complete reference material:

http://docs.scipy.org/doc/numpy/reference/

numpy user guide:

http://docs.scipy.org/doc/numpy/numpy-user.pdf

Many recipes for different purposes:

http://www.scipy.org/Cookbook

Active mailing list where you can ask your questions:

numpy-discussion@scipy.org

-----

Some more exercises
-------------------

Thanks to Nicolas Rougier: https://github.com/rougier/numpy-100:

#. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal
#. Create a 8x8 matrix and fill it with a checkerboard pattern
#. Normalize a 5x5 random matrix
#. Create a 5x5 matrix with row values ranging from 0 to 4
#. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates
#. Create random vector of size 10 and replace the maximum value by 0
#. Consider a random vector with shape (100,2) representing coordinates, find point by point distances
#. Generate a generic 2D Gaussian-like array
#. Subtract the mean of each row of a matrix
#. How to I sort an array by the nth column ?
#. Find the nearest value from a given value in an array

-----

A more complex problem...
-------------------------

.. image:: exercice_resistor_grid.png
   :align: center

http://imgs.xkcd.com/comics/nerd_sniping.png
