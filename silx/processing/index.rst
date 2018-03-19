**********
Processing
**********

----

silx.image
==========

- Image processing tools

  - Bilinear interpolator (used by ``silx.gui.plot`` when computing profiles)
  - 2D shapes drawing (used by ``silx.gui.plot`` when drawing masks)
  - 2D image alignemnt (SIFT)

    
The first 2 modules are written in cython (~ C) to offer good performances.

SIFT uses OpenCl kernels, for parallel computation on GPU and CPU.

----

silx.math
=========

- Multidimensional histogram

  - Implemented in cython
  - Optimized variant using a lookup-table to compute several histograms from data sharing the same coordinates

- Fit:

  - Levenberg-Marquardt algorithm to fit a function, with optional constraints on the fitted parameters
  - Manager for fit functions and background functions
  - Built-in fit functions (C code wrapped in Cython)
  - Non-analytical background filters (C code wrapped with Cython)

- Marching cubes: algorithm to compute iso-surface in a 3D volume (used in ``silx.gui.plot3d``)

----

Practice
========

- SIFT demo
  - find keypoints on two images
  - match the keypoints
  - align the images

- Histogram exercise
  - Using a histogram to compute azimutal integration

- Fit exercise
  - Fitting data for a detector across multiple scans

----

Fit exercise
============

- Read detectors *TZ3* and *If2* in scans *21.1* to *27.1*, in SPEC file `31oct98.dat`
- Fit :math:`If2 = f(TZ3)` with a gaussian distributions.
    - find the peaks' positions
    - estimate the gaussian parameters (*height, center position, full-width at half-maximum*), used as initial input for the iterative fit
    - run the fit and print the results

- Tips:
    - API documentation: http://www.silx.org/doc/silx/0.7.0/modules/
    - fitting algorithm: *silx.math.fit.leastsq* 
    - multi-gaussians function: *silx.math.fit.functions.sum_gauss*
    - peak search and peak width estimation module *silx.math.fit.peaks.peak_search*
