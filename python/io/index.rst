************
Input/output
************

----

Accessing ESRF data
-------------------

ESRF data come in (too many) different formats:

- specfile
- EdfFile
- MarCCD
- Pilatus CBF
- HDF5
- …

HDF5 is expected to become the standard ESRF data format. Some beamlines have
already switched.

----

Getting ready to access ESRF data
---------------------------------

Option 1
++++++++

Python modules for data access developed by the BCU.

The simplest way to have access to those modules is to install the PyMca
sources.

- At the ESRF beamlines, use the blissinstaller.

- Linux, MacOS: 
   - Download source code from sourceforge.
   - ``python setup.py install``
   - Packages available from MacPorts, Gentoo and Fedora.
   - Debian and Ubuntu should also have it available.

- Windows:
   - Download from sourceforge the package installer for your python version.

----

Getting ready to access ESRF data
---------------------------------

Option 2
++++++++

FabIO provides access to several image data formats.

Developed as part of the Fable project, initially an ID11 development.
Now managed by the DAU.

The simplest way to install it: PIP

>>> pip install fabio

Debian, ubuntu, windows and MacOSX  packages available from sourceforge as
well.

Already installed on most ESRF computers

----

Reading SPEC files
------------------

.. code-block:: python

   from PyMca5.PyMca import specfilewrapper as specfile

   sf = specfile.Specfile(filename)
   sf.scanno()                # returns the number of scans
   scan = sf.select('1.1')    # select the scan 1.1
   scan = sf[0]               # select the first scan
   scan.alllabels()           # list the labels
   scan.data()                # retrieve all data
   scan.nbmca()               # returns the number of mca in the scan
   scan.mca(1)                # retrieve first mca

``specfilewrapper`` provides basic access to other text based formats like CVS.

----

Reading EDF files
-----------------

Option 1: PyMCA
+++++++++++++++

.. code-block:: python

   from PyMca5.PyMca import EdfFile

   edf = EdfFile.EdfFile(filename, access='rb')
   edf.GetNumImages()       # get the number of images in file
   data = edf.GetData(0)    # reads the first image
   info = edf.GetHeader(0)  # reads the first header

``PyMca5.PyMca.EdfFile`` provides read access to image formats like ADSC,
MarCCD, PilatusCBF.

----

Reading EDF files
-----------------

Option 2: fabio
+++++++++++++++

.. code-block:: python

   import fabio

   image = fabio.open(filename)
   image.data             # contains the image
   image.header           # contains the header

----

Writing EDF files
-----------------

Option 1: PyMCA
+++++++++++++++

.. code-block:: python

   from PyMca5.PyMca import EdfFile
   import numpy

   # we need some data to be written
   data = numpy.arange(10000.0)
   data.shape = 100, 100
   # and some frame header keywords
   header = {}

   edf = EdfFile.EdfFile(new_filename, access='a+')

   # writes the first image
   info ['Title'] = 'Test Image 1'
   edf.WriteImage(header, data)

   # writes a second image
   info ['Title'] = 'Test Image 2'
   edf.WriteImage(header, data * 2, Append=1)

----

Writing EDF files
-----------------

Option 2: fabio
+++++++++++++++

.. code-block:: python

   import fabio

   data = numpy.random.random((10,10)
   header = {'origin': 'random'}

   image = fabio.edfimage.edfimage(data=data, header=header)
   image.write('new.edf')

----

Converting files
----------------

Convert data:

.. code-block:: python

   import fabio

   image = fabio.open('filename.edf')
   image = image.convert('tif')
   image.save('filename.tif')

In addition to ESRF formats, FabIO supports image format from most
manufacturers: Mar, Rayonix, Bruker, Dectris, ADSC, Rigaku, Oxford,
General Electric…

A complete description is available on:
http://dx.doi.org/10.1107/S0021889813000150

----

Exercise
--------

1. Read the EDF file ``medipix.edf``.
2. Create a mask for all the values above a certain threshold.
3. Using the above mask, set the affected pixels to a particular value.
4. Force all the original image data to be between 10% and 90% of the maximum.

----

Basic HDF5 access using h5py
----------------------------

.. code-block:: python

   import numpy
   import h5py

   data = numpy.arange(10000.)
   data.shape = 100, 100

   # write
   f = h5py.File('myfirstone.h5', access='w')
   f['/data'] = data
   f.close()

   # read
   n = h5py.File('myfirstone.h5', access='r')
   data = n['/data']        # reference to the file content, no actual reading
   data.shape               # shape of the data
   2 * data[0, 5]           # read and apply the operation
   actualData = data.value  # perform the reading and store in an array

----

Using ESRF Widgets
------------------

ESRF widgets use PyQt4. 
We need to start ``ipython`` with the ``-q4thread`` flag for interactive use:

>>> ipython -pylab -q4thread    # ipython v0.10 or earlier

>>> ipython --pylab=qt          # ipython v0.11 or newer

.. code-block:: python

   import numpy
   from PyMca5.PyMca import MaskImageWidget

   x = numpy.arange(10000.)
   x.shape = 100, 100
   w = MaskImageWidget.MaskImageWidget()
   w.setImageData(x)
   w.show()
