.. raw:: html

   <!-- Patch landslide slides background color --!>
   <style type="text/css">
   div.slide {
       background: #fff;
   }
   </style>

silx.gui.plot3d
###############

Widgets for 3D visualisation

.. image:: img/silx-plot3d-screenshot.png
   :width: 80%
   :align: center

----

Content
=======

High-level widgets to visualize data in 3D:

- ``ScalarFieldView`` for 3D scalar field visualisation:

  - Iso-surfaces
  - Cutting plane

- A widget to set parameters of the visualisation: ``SFViewParamTree``

.. list-table::
   :widths: 1 1
   :header-rows: 1

   * - ScalarFieldView
     - SFParamTree
   * - |scalarfieldview|
     - |sfparamtree|

.. |scalarfieldview| image:: img/scalarfieldview.png
   :width: 40%

.. |sfparamtree| image:: img/sfparamtree.png
   :width: 30%


Based on an internal 3D scene structure over OpenGL.

----

Demo
====

`example/viewer3DVolume.py <https://github.com/silx-kit/silx/blob/master/examples/viewer3DVolume.py>`_

.. image:: img/silx-plot3d-screenshot.png
   :width: 80%
   :align: center

----

Dependencies
============

- PyQt.QtOpenGL
- PyOpenGL 3.x
- OpenGL 2.1 subset (mind the drivers over ssh)

----

Sample code
===========

.. code-block:: python

    import numpy
    from silx.gui import qt
    from silx.gui.plot3d.ScalarFieldView import ScalarFieldView
    from silx.gui.plot3d import SFViewParamTree

    app = qt.QApplication([])
    window = ScalarFieldView()  # Create the viewer main window

    treeView = SFViewParamTree.TreeView(window)  # Create parameter widget
    treeView.setSfView(window)  # Attach the parameter tree to the view

    # Add the parameter tree to the main window in a dock widget
    dock = qt.QDockWidget()
    dock.setWindowTitle('Parameters')
    dock.setWidget(treeView)
    window.addDockWidget(qt.Qt.RightDockWidgetArea, dock)

    x, y, z = numpy.ogrid[-10:10:20j, -10:10:20j, -10:10:20j]
    data = numpy.asarray(numpy.sin(x*y*z)/(x*y*z), dtype='float32')

    # Set ScalarFieldView data
    window.setData(data)
    window.show()
    app.exec_()

----

Upcoming features
=================

- Threaded iso-surface computation
- Visual improvements: e.g., ticks and label layout
- Non-orthogonal axes support
- Selection of a region of interest
- Surface plot
- Tests and continuous integration
