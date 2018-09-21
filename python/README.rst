
=================
 Python training
=================

Training for beginners in Python.

Content
=======

0. Python: the programming language
-----------------------------------

This part is a general introduction to the Python 3 programming language.

It covers:

- Available primitives, basic operations and containers (list, tuple, dictionary, iterator)
- Control structures: if/then/else, for and while loops
- Defining functions and modules

1. Array manipulation using NumPy
---------------------------------

This part is an introduction to the numpy library.

It covers:

- the creation of numpy arrays,
- access and manipulation of such arrays, and
- an overview of the different features available in numpy.

2. Accessing ESRF data files: HDF5, specfile, EDF
-------------------------------------------------

This part provides:

- an introduction to HDF5, EDF and spec file formats, and
- a presentation of the h5py, silx and fabio libraries to read and write such files.


Dependencies
============

The content of the training depends on:

- Python 3.x
- ``numpy``
- ``h5py``
- ``fabio``
- ``silx``
- ``matplotlib``

To run the notebooks and display the slides, you need:

- ``jupyter``
- ``rise``

How-to install rise::

  pip install rise
  jupyter-nbextension install rise --py --sys-prefix
  jupyter-nbextension enable rise --py --sys-prefix

