Introduction to Python
======================

----

Presentation of Python
----------------------

- Computer language invented by Guido van Rossum in 1989
    - Guido is still managing the development of Python
    - Massively used at Dropbox & Google (employers of Guido)

- Open source
    - BSD-like license
    - Means free for you
    - Guaranteed to stay free

- Portable
    - Runs on any computer you may have access to

- Easily extendable. The 'glue' language.
    - in C, Fortran, …
    - Once compiled, can be as fast as C

----

Examples of applications in Python
----------------------------------

- Scientific programs:
    - PyMol, Sage

- Web frameworks:
    - Django, Zope, Plone, …

- Scripting in large application:
    - Blender, gimp, …

- Graphical user interfaces & visualization:
    - Bindings to gtk, Qt, Tcl/Tk, wxWidgets, …
    - Libraries for visualization: gnuplot, matplotlib, VTK

- Scientific libraries:
    - Numpy, Scipy, (Scientific Python, numarray, Numeric, …)

- More locally developed programs (ESRF driven):
    - PyMca, PyHST, EDNA, MxCube, PyFAI, FabIO …

----

Python for data-analysis
------------------------

- Python can be learned in a couple of days
- Ideal for prototyping
- Alternative to Matlab
- Python is free
- It runs everywhere
- Batteries are included
- Excellent community support
- Can be embedded in larger projects
- Interfaces to low-level languages (for performances)
- Support from local ISDD software group

.. image:: img/batteries_included.png
    :width: 300px

----

Python in a notebook
--------------------

- Open a web browser and connect to:
    - http://scisoft12.esrf.fr:8000/
    - Login with your ESRF credentials
    - Create a new notebook

- Command in the notebook:
    - Shift-enter to execute a cell

- Play with the notebook:
    - What is the result of 4+7/2?
    - What Python version is used? Where is the Python interpreter on located on the machine?

----

.. code-block:: python
    
    >>> 4. + 7. / 2.
    7.5

    >>> 4+7//2
    7

    >>> import sys
    >>> sys.version
    '3.4.2 (default, Oct  8 2014, 10:45:20) \n[GCC 4.9.1]'
    >>> sys.executable
    '/usr/bin/python3'





    
      
