

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

Dependancies: numpy , h5py , ipython , qtconsole , matplotlib

Release each 3 months

      

----

Structure of the silx library (1)
#################################

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

----

Structure of the silx library (2)
#################################

OpenCL
------
    Parallel computing on GPU

Third-Party external utilities
------------------------------
    Currently *TiffIO*, *six* and *EdfFile*

Utils
-----
    Various utility functions (HTML escaping, weak-references)

Sx
---
    Imports all silx in one go: aim at replacing pylab

----

Plot
####

Plot widgets for 1D, 2D and 3D to come

.. image:: img/plot2D.png
    :width: 400px
    :height: 300px

- Many tool included 
    - ROI
    - Mask widget
    - qt console
    - ...

----


Plot
####

+ multiple backends 
    + matplotlib
    + openGL (under development)
+ designed for heritage and personnalization by scientists and developers
    - plot actions
    - Qt signal/slot


.. image:: img/plot_qtconsole.png
    :width: 400px
    :height: 300px

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
'classical' histogram. Able to a compute distribution of a dataset.

- histogramnd (hands-on) : (N, ) or (N, D) array
    + silx.math.histogram.Histogramnd
- histogramnd_lut : (N, ) or (N, D) array
    + silx.math.histogram.HistogramndLut

        .. note:: the same as histogramnd but use a look up table (useful if multiple association are needed )

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


silx.math
#########

Marching cubes
--------------


Algorithm to generate mesh from a set of iso-vertices

http://paulbourke.net/geometry/polygonise/

Visualization from isoViewer (prototype status for now. Will be soon integrated into silx)

.. image:: img/marchingCubesThomas.png
    :width: 400px
    :align: center
    :height: 300px


----


OpenCL
######

opencl integration
------------------

Many function and setup to facilitate the integration of pyopencl in silx throught different platform (windows, linux, mac).
    - computation of possible kernels size
    - test of opencl platforms
    - ...

First functions using pyopencl 
    - sift
        + silx.image.sift


----

Upcoming features
#################

3D plot
-------

OpenGL backend under active development

ArrayWidget
-----------

Displaying 2D data-slices in a N-dimensional array

.. image:: img/arraywidget.png
    :align: center
    :width: 60%

----

Upcoming features
#################

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


This was the first silx tutorial. Please let use know about any ideas to improve it !!!

And if you want to contribute to the project : 

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

