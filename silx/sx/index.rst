.. raw:: html

   <!-- Patch landslide slides background color --!>
   <style type="text/css">
   div.slide {
       background: #fff;
   }
   </style>


Using silx from [I]Python console
*********************************


----

Using silx from [I]Python console
---------------------------------

**silx.sx** is a convenient Python module to use from the console:

.. code-block:: python

   >>> from silx import sx


- provides access to different features of silx (e.g., plotting, accessing files) in a single module.
- loads and initialize (Py)Qt (except in notebooks)
- From IPython, loads numpy and matplotlib

Doc: http://www.silx.org/doc/silx/latest/modules/sx.html

----

Accessing files
---------------

``silx.sx`` also provides functions from ``silx.io`` (e.g., ``open``)

----

1D/2D Plot
----------

- ``sx.plot`` to plot curves

  .. code-block:: python

     x = numpy.linspace(0, 12, 1000)
     y = numpy.sin(x)
     sx.plot(x, y, 'red')
- ``sx.imshow`` to plot an image

  .. code-block:: python

     image = numpy.random.random(1024*1024).reshape(1024, 1024)
     sx.imshow(image)
- ``sx.ginput`` for interactive input

  .. code-block:: python

     sx.ginput(3)


Note: Not available from notebooks

----

3D Plot
-------

- ``sx.contour3d``: isosurface and contour in 3D scalar field

  .. image:: img/ScalarFieldView.png
     :height: 300px
     :align: center
- ``sx.points3d``: 2D/3D scatter plots

Note: Not available from notebooks, requires OpenGL 2.1

----

silx.sx extra content
---------------------

- Widgets from ``silx.gui.plot``
- Some features from ``silx.math``

