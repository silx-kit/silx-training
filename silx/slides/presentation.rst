

silx training
#############

15th November, 2016
-------------------

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
    - January: 2nd engineer & 2nd scientist
    - March: First release: silx v0.1
    - May: 3rd engineer
    - July: silx v0.2
    - October: silx v0.3
    - November: Training for scientists

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

Dependencies: numpy, matplotlib, PyQt or PySide, h5py, ipython, qtconsole, PyOpenCL

      

----

Structure of the silx library
#############################

Graphical User Interface widget
-------------------------------
    Plot, image display, mask, HDF5 tree view, fit configuration

Image processing tools
----------------------
    Image interpolation, registration and drawing primitives

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

HDF5 widget
###########

Tree view for any data format that can be exposed through an *h5py*-like API:

 - HDF5 files (already implemented using *h5py*)
 - SPEC files (already implemented using *silx.io.spech5*)
 - all image file formats handled by FabIO (not implemented yet) 

.. image:: img/Hdf5TreeView.png
    :width: 400px
    :align: center

----

Plot
####

- Plot widgets for 1D, 2D

- heritage from PyMca

.. image:: img/plot2D.png
    :width: 350px
    :height: 260px

- Many tool included 
    - ROI
    - Mask widget
    - qt console
    - ...

----


Plot
####


+ backend  
    + currently matplotlib


.. image:: img/plot_qtconsole.png
    :width: 400px
    :height: 300px


----

Fit widget
----------

GUI for ``silx.math.fit.fitmanager`` with additional fit configuration widgets

.. image:: img/fitwidget1.png
    :width: 35%
    :align: center

.. image:: img/fitconfig.png
    :width: 30%
    :align: center

----

silx.image
##########

bilinear interpolation
----------------------

convert an image to a continuous function.

opencl integration
------------------

Many function and setup to facilitate the integration of pyopencl in silx throught different platform (windows, linux, mac).

sift
----

image alignement, using parallel algorithms on GPU

.. image:: img/image-alignement.png
    :width: 85%
    :align: center


----


silx.math
#########

histogram
---------
Multidimensional histogram.

- Histogramnd (hands-on) : (N, ) or (N, D) array
    + silx.math.histogram.Histogramnd
- HistogramndLut : (N, ) or (N, D) array
    + silx.math.histogram.HistogramndLut

        .. note:: HistogramndLut is doing the same job as Histogramnnd but is optimized to compute several histograms from data sharing the same coordinates.

----


silx.math
#########

fit
---

- ``silx.math.fit.leastsq``: Levenberg-Marquardt algorithm with constraints on the fitted parameters 
- ``silx.math.fit.functions``: Model functions
- ``silx.math.fit.peaks``: Peak search algorithm
- ``silx.math.fit.filters``: Smoothing, background computation (strip, snip)
- ``silx.math.fit.fittheories``: Combination of model functions, initial parameters estimation functions relying on peak search and background estimation
- ``silx.math.fit.fitmanager``: Advanced fit manager using all of the above

----

Upcoming features (1)
#####################

3D plot
-------

- OpenGL backend

- isoViewer

.. image:: img/marchingCubesThomas.png
    :width: 400px
    :align: center
    :height: 300px


----

Upcoming features (2)
#####################


ArrayWidget
-----------

Displaying 2D data-slices in a N-dimensional array

.. image:: img/arraywidget.png
    :align: center
    :width: 60%

----

Upcoming features (3)
#####################

fabioh5
-------

Exposing all data files handled by FabIO, the same way as *h5py* and *spech5*.

.. code-block:: python

    import silx.io.fabioh5
    f = silx.io.fabioh5.File("foobar.edf")

BackgroundWidget
----------------

Widget to configure background filters (used in ``FitWidget``)

.. image:: img/bgwidget.png
   :width: 45%
   :align: center


----

If you want to contribute to the project: 

.. image:: img/forkme.png
    :align: center
    :target: https://github.com/silx-kit/silx



----

Authors
#######

    - pierre.knobel@esrf.fr
    - valentin.valls@esrf.fr
    - henri.payno@esrf.fr
    - jerome.kieffer@esrf.fr
    - thomas.vincent@esrf.fr
    - sole@esrf.fr

----

Training resources
##################

Exercices:

https://github.com/silx-kit/silx-training

Training data:

      /tmp_14_days/silx-training

