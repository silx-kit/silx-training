.. raw:: html

   <!-- Patch landslide slides background color --!>
   <style type="text/css">
   div.slide {
       background: #fff;
   }
   </style>


Fable Input/Output library
==========================

FabIO is a Python module for reading and handling data from two-dimensional X-ray detectors.

Idea:
-----

* One unique way to read images for all kind of (area-) detectors.
* Exposes always one frame which contains:

 + Metadata (header) exposed  as a dictionary
 + Data as a numpy array

* handles transparently compression (compressed format and compressed images)
* Offers ways to iterate over frames in an file or files in a serie

Benefit:
--------

Data analysis software do not need to take care of the data-format.

No object oriented programming is needed to use FabIO (but a bit for developing it)

Open source library

----

Installation of FabIO
---------------------

* As most Python libraries:

.. code-block:: shell

    pip install --user fabio  

Works under any operating system

* Under Debian/Ubuntu/Mint:

.. code-block:: shell

    sudo apt-get install python-fabio python3-fabio


----

Basic usage: reading
--------------------

.. code-block:: python

   import fabio
   im100 = fabio.open('Quartz_0100.tif') # Open image file
   print(im0.data[1024,1024])            # Check a pixel value
   im101 = im100.next()                  # Open next image
   im270 = im1.getframe(270)             # Jump to file number 270: Quartz_0270.tif

*Nota:* on multi-frame images, FabIO iterates first over the frames inside one file before going from one file to the next.

----

Basic usage: normalization
--------------------------

.. code-block:: python

    import fabio
    img = fabio.open('exampleimage0001.edf')
    for key in img.header:
        print(key, img.header[key])
    ('ByteOrder', 'LowByteFirst')
    ('DATE (scan begin)', 'Mon Jun 28 21:22:16 2010')
    ('ESRFCurrent', '198.099')
    ...
    
    # Normalise to beam current and save data
    srcur = float(img.header['ESRFCurrent'])
    img.data *= 200.0/srcur
    img.write('normed_0001.edf')

----

Supported files
---------------

.. csv-table:: Supported formats
   :header: "Python Module", "Detector / Format", "Extension", "Read", "Multi-image", "Write"
   :widths: 30, 30, 20, 10, 15, 10

   "ADSC", "ADSC Quantum", ".img ", "Yes", "No", "Yes"
   "Bruker", "Bruker formats", ".sfrm ", "Yes", "No", "Yes"
   "DM3", "Gatan Digital Micrograph ", ".dm3 ", "Yes", "No", "No"
   "EDF", "ESRF data format ", ".edf ", "Yes", "Yes ", "Yes"
   "EDNA-XML", "Used by EDNA", ".xml ", "Yes", "No", "No"
   "CBF", "CIF binary files", ".cbf ", "Yes", "No", "Yes"
   "kcd", "Nonius KappaCCD", ".kccd ", "Yes", "No", "No"
   "fit2d mask", "Used by Fit2D", ".msk ", "Yes", "No", "Yes"
   "fit2d spreadsheet", "Used by Fit2D", ".spr ", "Yes", "No", "Yes"
   "GE", "General Electric", "No", "Yes", "Yes ", "No"
   "HiPiC", "Hamamatsu CCD", ".tif ", "Yes", "No", "No"
   "HDF5", "Hierachical data dormat", ".h5", "Yes", "No", "No" 
   "marccd", "MarCCD/Mar165", ".mccd ", "Yes", "No", "No"
   "mar345", "Mar345 image plate", ".mar3450 ", "Yes", "No", "Yes"
   "numpy", "numpy 2D array", "npy ", "Yes", "No", "Yes"
   "OXD", "Oxford Diffraction", ".img ", "Yes", "No", "Yes"
   "Pixi", "pixi", ". ", "Yes", "No", "No"
   "pilatus", "Dectris Pilatus Tiff", ".tif ", "Yes", "No", "Yes"
   "PNM", "Portable aNy Map", ".pnm ", "Yes", "No", "Yes"
   "Raxis", "Rigaku Saxs format", ".img", "Yes", "No", "No"
   "TIFF", "Tagged Image File Format", ".tif ", "Yes", "No", "Yes"

----

How it works:
-------------

Each file-formats correspond to a class, derived from FabioImage, which defines
how to read and write each image-format.

* Reading:
  *fabio.open* analyzes the file and chooses the right FabioImage derivative class.
  Once instantiated, the object reads the file and exposes *data* and *header*

* Writing:
  One instantiates the right class (depending on the requested file format) with
  *data* array and *header* dictionary, then uses the *write* method to save to
  the file.

* Conversion:
  File-format can be converted into another format, using the *convert* method.
  This tries to handle float to integer conversion when needed but not the header conversion.

----

Fabio-viewer
------------

A simple viewer has been developed by Gaël Goret for displaying simply diffraction images:

.. figure:: viewer.png
   :align: center
   :width: 500

----------------

Some more links:
----------------

* Citation: Knudsen, E. B., Sørensen, H. O., Wright, J. P., Goret, G. & Kieffer, J. (2013). J. Appl. Cryst. 46, 537-539.
  `DOI: 10.1107/S0021889813000150 <http://dx.doi.org/10.1107/S0021889813000150>`_.

* Full documentation: `Read The Docs <http://fabio.readthedocs.org/en/latest/>`_

* Download: `PyPI.python.org <https://pypi.python.org/pypi/fabio/0.3.0>`_

* Development: `GitHub <https://github.com/kif/fabio>`_

Contribution goes on with *issue* reporting and *pull-request* on GitHub.

----

Limitations
-----------

There is (good) support for HDF5/NeXus. For this use `h5py <http://docs.h5py.org/en/latest/high/dataset.html>`_.

----

Exercise: Image normalization
-----------------------------

Download images from:
https://github.com/kif/python_tutorials/tree/master/scipy_exercise_0

* Load *raw.edf*: it is an absorption images which need to be corrected for dark current and flat-field.
* Correct from dark noise of the camera, use information from the headers.
* Average the two flat field images after correction from their dark.
* Divide the raw signal by the flat field
* Visualize the result using *matplotlib*.
* Save the result as an *EDF* image and a *Tiff* image, visualize them using fabio-viewer.

