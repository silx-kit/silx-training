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
  - Fit functions and background functions manager
  - Fit functions (C code wrapped in Cython)
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
  - Curve fitting, background filters
  - using FitManager
  - using FitWidget


