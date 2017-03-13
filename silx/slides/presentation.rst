

silx training
#############

15th March, 2017
----------------

.. image:: img/silx_logo.png
    :width: 180px
    :height: 280px

----

silx project
############

.. image:: img/silx_project.png
    :width: 700px
    :height: 600px

----

Goals of the project
###################

- Scientific toolkit for all synchrotron radiation facilities

- Collaborative long term maintenance

- Easy installation (packaging, wheels)

- Release every 3 months

- Free and open source project (MIT license).

----

Timeline
########

- 2014:
    - Structure of the project
- 2015:
    - May: acceptation of the project within the EBS
    - December: 1st engineer & 1st scientist
- 2016:
    - Releases: silx v0.1 (March), v0.2 (July), v0.3 (October)
    - Team: 2nd engineer & 2nd scientist (January),  3rd engineer(May)
    - November: First training for scientists

- 2017:
    - Releases: silx v0.4 (February), planned v0.5 (May)
    - March: Second training for scientists

----

Resources and requirements
##########################

Documentation of releases is available at https://pythonhosted.org/silx/

Latest documentation (nightly build) is available at http://www.silx.org/doc/silx/

    - silx@esrf.fr


.. image:: img/cross-platform.png
    :width: 350px
    :height: 180px
    :align: left

Python2 (>=2.7), Python3 (>=3.4)

Dependencies: numpy, matplotlib, PyQt or PySide, h5py, ipython, qtconsole, PyOpenCL, PyOpenGL

      

----

Structure of the silx library
#############################

::

 silx
     gui
         data
         fit
         hdf5
         plot
         plot3d
         qt
         widgets
     images
         sift
     io
         fabioh5
         spech5
         spectoh5
     math
         fit
         histogram
         marchingcubes
     sx

----

Main features
#############

Graphical User Interface widgets
--------------------------------
    Plot, image display, mask, HDF5 tree view, fit configuration, Plot3d, Periodic table

Image processing tools
----------------------
    Image interpolation, registration and drawing primitives, image alignment

Input / Output
--------------
    Support for spec, HDF5 and image formats

Math
----
    Least-squares fit, volume isosurface, histograms, ...

Sx
---
    Imports all silx in one go: aim at replacing pylab

----

Today's training
----------------

1. Input/output
    - data structure
    - silx IO API
    - data widgets: HDF5 tree and DataViewer
2. Plot widgets
    - Plot1D, Plot2D, ImageView, StackView
    - ROI, Mask
    - plot3d widgets
3. Processing
    - SIFT (image alignement)
    - histograms
    - fit

----

If you want to contribute to the project: 

.. image:: img/forkme.png
    :align: center
    :target: https://github.com/silx-kit/silx

----
----

Authors
#######

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
##################

Exercices:

https://github.com/silx-kit/silx-training

Training data:

      /tmp_14_days/silx-training

