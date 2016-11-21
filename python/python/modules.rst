Modules
=======

----

Create modules with your functions
----------------------------------

.. warning:: Start each new python file with the following lines : 

    .. code-block:: python

        #!/usr/bin/env python
        # coding: utf8


----

Example of a module
^^^^^^^^^^^^^^^^^^^

.. image:: img/mymodule.png
    :width: 550px
    :height: 620px

----

Documentation generator
^^^^^^^^^^^^^^^^^^^^^^^

.. note:: 
    
    ':param', ':type',  etc can be used for
    formatting documentation using automatic documentation generators like : 
    

- Sphinx ( http://www.sphinx-doc.org/en/1.4.8/ )
- Epydoc ( https://pypi.python.org/pypi/epydoc/ )
- Doxygen ( http://www.stack.nl/~dimitri/doxygen/)


----

import
------

There is many ways to import modules / from module

    .. code-block:: python

        import mymodule
        mymodule.myfunction()

        import mymodule as module
        module.myfunction()

        from mymodule import pow2
        pow2()

        # ! import all from a module can be dangerous because
        # it will pollutes the local name-space
        from mymodule import *
        pow2()
        anyfunction()


You can also access to the attributes of the module

    .. code-block:: python

        import mymodule
        mymodule.__authors__
        mymodule.__doc__


----

Standard modules
----------------

"Batteries included philosophy"

- Modules sys, os, shutil, glob, copy
- Modules string, re, collections
- Modules math, random, decimal
- Module time, datetime
- Internet access with email, urllib2, smtplib
- Multi-core programming with multiprocessing, threading, thread
- Handle compressed archives with gzip, bz2, zlib, zipfile, tarfile
- Execute another program with subprocess, shlex
- Quality control with unittest and doctest
- Performance control with timeit, profile and cProfile
- Logging capabilities: logging


----

Non standard modules
--------------------


- General purpose mathematics libraries:
    - NumPy
    - SciPy
- Input/Output libraries to handle data acquired at ESRF
    - EdfFile/SpecFile
    - FabIO
    - H5py
- Visualization libraries (curves, images, ...)
    - Matplotlib
    - Silx
- Image handling library:
    - Python Imaging Library (PIL → Pillow)

They will be introduced this afternoon.
