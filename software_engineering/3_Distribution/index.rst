
.. raw:: html

   <!-- Patch landslide slides background color --!>
   <style type="text/css">
   div.slide {
       background: #fff;
   }
   </style>

Distribute Python software
==========================

Outline
-------

#. setup.py and setuptools
#. Management of dependencies
#. Packages: wheels & deb
#. Fat binaries

References:

* https://packaging.python.org/
* https://docs.python.org/3.6/distutils/index.html

---------------

The core of the distribution: *setup.py*
----------------------------------------

.. figure:: setup.png
   :align: center
   :width: 500

As *setup.py* used to be doing to many things, other tools have been added:
*pip* (the official Python package installer) and *twine* (for uploading distributions to PyPI).

----

*setup.py*
----------

This *setup.py* is basically a call to the setup function provided by distutils or
setuptools (the later being preferred)

The next slides will present you an incremental way to make from scratch the
*setup.py* for your project.

For now, just import the setup function for setuptools or distutils:

.. code-block:: python
   try:
       from setuptools import setup
   except ImportError:
       from distutils.core import setup

   setup(name='silx',
         version='0.0.1',
         )

https://docs.python.org/3.6/distutils/apiref.html

---------------

Registration
------------


The central registration point is the Python Package Index `PyPI <http://pypi.python.org>`_

.. figure:: PyPI.png
   :align: center
   :width: 500

---------------

Actual registration (1/2):
--------------------------
Add information about the author, emails and `classifiers <https://pypi.python.org/pypi?:action=list_classifiers>`_ like:

.. code-block:: python

   setup(name='silx',
         version='0.0.1',
         url="https://github.com/silx-kit/silx",
         author="data analysis unit",
         author_email="silx@esrf.fr",
         classifiers = ["Development Status :: 1 - Planning",
            "Environment :: Console",
            "Environment :: MacOS X",
            "Environment :: Win32 (MS Windows)",
            "Environment :: X11 Applications :: Qt",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Programming Language :: Cython",
            "Programming Language :: Python",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Documentation :: Sphinx",
            "Topic :: Scientific/Engineering :: Physics",
            "Topic :: Software Development :: Libraries :: Python Modules"] )

---------------

Actual registration (2/2):
--------------------------

The registering to PyPI is simply performed with:

.. code-block:: shell

    python setup.py register

All information should now be available online.
It is advised to separate classifiers in a dedicated list.

List of available classifiers_; for our example we used:

.. code-block:: python

    classifiers = ["Development Status :: 1 - Planning",
                   "Environment :: Console",
                   "Environment :: MacOS X",
                   "Environment :: Win32 (MS Windows)",
                   "Environment :: X11 Applications :: Qt",
                   "Intended Audience :: Education",
                   "Intended Audience :: Science/Research",
                   "License :: OSI Approved :: MIT License",
                   "Natural Language :: English",
                   "Operating System :: Microsoft :: Windows",
                   "Operating System :: POSIX",
                   "Programming Language :: Cython",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: Implementation :: CPython",
                   "Topic :: Documentation :: Sphinx",
                   "Topic :: Scientific/Engineering :: Physics",
                   "Topic :: Software Development :: Libraries :: Python Modules",])

---------------

Define your package (1/3)
-------------------------

Create a directory of the name of your package and a *__init__.py* file in it.

::

  project/
     |---- setup.py
     |---- MANIFEST.in
     |---- package/
     |       |----- __init__.py



Often the *project*-name and the *package*-name can be the same. This is not an
issue as long as there is not /project/__init__.py file.

*MANIFEST.in* contains the list of non-python files to be shipped with the project build.

---------------

Define your package (2/3)
-------------------------

Modify your setup.py accordingly.

.. code-block:: python

   setup(name='silx',
         version='0.0.1',
         url="https://github.com/silex-kit/silx",
         author="data analysis unit",
         author_email="silx@esrf.fr",
         classifiers = classifiers,
         description="Software library for X-Ray data analysis",
         packages=["silx", "silx.io", "silx.third_party", "silx.gui"],
         )

In this example the *io*, *third_party* and *gui* sub-packages have also been
declared.

::

  silx/
     |---- setup.py
     |---- MANIFEST.in
     |---- silx/
     |       |---- __init__.py
     |       |---- gui
     |       |      |---- __init__.py
     |       |
     |       |---- io
     |       |      |---- __init__.py
     |       |
     |       |
     |       |---- third_party
     |       |      |---- __init__.py

----

Define your package (3/3)
-------------------------

You can now build your package with:

.. code-block:: shell

    python setup.py build

From now on, you should be able to:

Create a source package with:
.............................
.. code-block:: shell

    python setup.py sdist

Create a binary package with:
.............................
.. code-block:: shell

    python setup.py bdist_wheel


Install your package with:
..........................
.. code-block:: shell

    pip install .
    # deprecated: python setup.py install   

Nota:
.....
Only Python files will be part of your source package for now.
If you want to include additional files (like README, ...)
declare them in the *MANIFEST.in*, at the project's top-level.

---------------

Dependencies (1/2)
------------------

Dependency management is available at 3 different levels:

* from setuptools
* from PIP requirement file
* from Debian packages

Dependencies allow the user to know what other library is required.
Those requirements can be build requirements or use requirements:
*install_requires* and *setup_requires*:

.. code-block:: python

   install_requires = ["numpy", "h5py"]
   setup_requires = ["numpy", "cython"]

   setup(name='silx',
         version=get_version(),
         url="https://github.com/silex-kit/silx",
         author="data analysis unit",
         author_email="silx@esrf.fr",
         classifiers = classifiers,
         description="Software library for X-Ray data analysis",
         long_description=get_readme(),
         packages=["silx", "silx.io", "silx.third_party", "silx.visu"],
         install_requires=install_requires,
         setup_requires=setup_requires,
         )


---------------


*setup.py* dependency vs *requirement.txt*
..........................................

It may look contradictory to define dependencies at different places
`but it is not <https://caremad.io/2013/07/setup-vs-requirement/>`_.

* *setup.py* provides an abstract dependency (i.e. h5py)
* *requirement.txt* provides concrete implementation (often with hard coded
  versions and URL to download wheels from).
  This is often organization specific or CI-tool specific: h5py==2.5.0

  Usage::

      pip install -r requirements.txt

Dependencies defined in the setup.py are naturally propagated to packages (Debian, Windows, wheels...)

---------------

Building packages
-----------------

Packages are the best way to distribute a library, regardless of the operating system.
For (graphical) applications, fat-binaries may be a better choice, especially under Windows and MacOS.

There are 2 kind of packages to be distinguished:

* Operating system packages: RPM, DEB, MSI, ...
* Python specific packages: Wheels (it obsoletes eggs)

Advantages of packaging tools:

* Keeps track of installed packages
* Management of dependencies
* Provides access to a package repository.

---------------


Wheels: `PEP427 <https://www.python.org/dev/peps/pep-0427/>`_
-------------------------------------------------------------

Wheels are the `new standard <http://pythonwheels.com/>`_ of python distribution
and have replaced *eggs*.


Advantages of wheels:

#. Avoids arbitrary code execution for installation (no *setup.py* executed).
#. Does not require a compiler on the client side for binary extensions.
#. Faster installation, especially for binary extensions.
#. Allows better and faster testing and continuous integration.
#. Creates *.pyc* files at installation, matching the Python interpreter used.
#. More consistent installs across platforms and machines.

Wheels provide binary packages and a decent installer (pip) for Windows and MacOS.
Under Linux, the reference platform (*manylinux1* aka *centos5*) is very old and binary
wheels are much slower than native builds (~20%).

---------------

Building Wheels
---------------

You will need setuptools and wheel installed:

.. code-block:: shell

  apt-get install python-setuptools python-wheel

or:

.. code-block:: shell

  pip install setuptools wheel [--user]

then:

.. code-block:: shell

  python setup.py bdist_wheel

Pitfalls:
---------
External shared library (Qt, hdf5, ...) which needs to be incorporated in the wheel.

You can use utility software to check which libraries your package is linked against:

- MacOS: `delocate <https://github.com/matthew-brett/delocate>`_
- Windows: `depends <http://www.dependencywalker.com/>`_
- Linux: ldd, `auditwheel <https://github.com/pypa/auditwheel>`_

.. For example, this is the result of running delocate-listdeps --all on a binary wheel for the pyqt library:

---------------

Debian packages
---------------

To build debian packages we recommend an additional tool: `stdeb <https://pypi.python.org/pypi/stdeb/>`_

.. code-block:: shell

   sudo apt-get install python-stdeb python3-stdeb
   
   python setup.py --command-packages=stdeb.command bdist_deb

You should find your python-*package**.deb in deb_dist directory.

stdeb can be configured with an additionnal file: *stdeb.cfg*


To build both Python2 & Python3 packages use:

.. code-block:: shell

   python3 setup.py --command-packages=stdeb.command sdist_dsc \
                    --with-python2=True \
                    --with-python3=True \
                    --no-python3-scripts=True bdist_deb

Alternative to be considered: `pypi2deb <https://github.com/p1otr/pypi2deb>`_

------

Advanced setup.py: numpy.distutils
----------------------------------

`numpy.distutils <https://docs.scipy.org/doc/numpy/reference/distutils.html>`_ provides a way to use a hierarchy of setup.py::

  project/
    setup.py  -> Effective setup.py
    package/
      __init__.py
      setup.py      -> Handles main package build
      subpackage/
        __init__.py
        setup.py    -> Handles subpackage build

- Pros: Each sub-package is embedding its own build.
- Cons: numpy becomes a build dependency.

This is based on the `Configuration class <https://docs.scipy.org/doc/numpy/reference/distutils.html#numpy.distutils.misc_util.Configuration>`_.

------

.. include:: fat_binaries.rst
