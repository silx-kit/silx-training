
*************
silx training
*************

20th March, 2018
================

.. image:: img/silx_logo.png
    :width: 180px
    :height: 280px

----

silx project
============

.. image:: img/silx_project.png
    :width: 700px
    :height: 600px

----

Goals of the project
====================

- Scientific toolkit for all synchrotron radiation facilities

- Collaborative long term maintenance

- Easy installation (packaging, wheels)

- Release every 4 months

- Free and open source project: MIT + LGPL license.

----

Timeline
========

- 2014:
    - Structure of the project
- 2015:
    - May: acceptation of the project within the EBS
    - December: 1st engineer & 1st scientist
- 2016:
    - Releases: silx v0.1 (March), v0.2 (July), v0.3 (October)
    - Team: 2nd engineer & 2nd scientist (January),  3rd engineer (May)
    - November: First training for scientists

- 2017:
    - Releases: silx v0.4 (February), v0.5 (May), v0.6 (October)
    - March: Second training for scientists

- 2018:
    - Releases: silx v0.7 (March)
    - March: Third training for scientists

----

Resources and requirements
==========================

Documentation of releases is available at http://www.silx.org/doc/silx/

Latest documentation (nightly build) is available at http://www.silx.org/doc/silx/dev

    - silx@esrf.fr


.. image:: img/cross-platform.png
    :width: 350px
    :height: 180px
    :align: left

Python2 (>=2.7), Python3 (>=3.4)

Dependencies: numpy, matplotlib, PyQt or PySide, h5py, ipython, qtconsole, PyOpenCL, PyOpenGL

      

----

Structure of the silx library
=============================

::

 silx
     app
     gui
     image
     io
     math
     opencl
     sx
    
----

Main features
=============


- A set of applications:
    - a unified viewerfor HDF5, SPEC and image file formats
    - a unified converter to HDF5 format
- Support of HDF5, SPEC and FabIO images file formats.
- A set of Qt widgets, including:
    - 1D and 2D visualization widgets with a set of associated tools using multiple backends (matplotlib or OpenGL)
    - OpenGL-based widgets to visualize data in 3D (scalar field with isosurface and cut plane, scatter plot)
    - a unified browser for HDF5, SPEC and image file formats supporting inspection and visualization of n-dimensional datasets.
- OpenCL-based data processing: image alignment (SIFT), image processing (median filter, histogram), filtered backprojection for tomography
- Data reduction: histogramming, fitting, median filter

----

Today's training
================

1. Applications
    - silx view
    - silx convert

2. Interactive usage (sx)

3. Input/output
    - data structure
    - silx IO API
    - other features

4. Widgets
    - data file browsing
    - visualisation
    - other widgets

5. Processing
    - ...

----

If you want to contribute to the project: 

.. image:: img/forkme.png
    :align: center
    :target: https://github.com/silx-kit/silx

----

Authors
=======

    - jerome.kieffer@esrf.fr
    - pierre.knobel@esrf.fr
    - damien.naudet@esrf.fr
    - pierre.paleo@esrf.fr
    - henri.payno@esrf.fr
    - sole@esrf.fr
    - valentin.valls@esrf.fr
    - thomas.vincent@esrf.fr

----

Training resources
==================

Exercices:

https://github.com/silx-kit/silx-training

Training data:

      /tmp_14_days/silx-training

