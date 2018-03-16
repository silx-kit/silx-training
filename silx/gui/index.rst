.. raw:: html

   <!-- Patch landslide slides background color --!>
   <style type="text/css">
   div.slide {
       background: #fff;
   }
   </style>


silx.gui
********


----

silx.gui
--------

Set of widgets based on (Py)Qt:

0. Data files browsing
#. Visualisation
#. Convenient widgets

Dependencies:

- **PyQt5**, PyQt4, PySide or PySide2 (experimental)
- **matplotlib**
- **h5py**
- **PyOpenGL**
- **IPython** and **qtconsole**

----

Data files browsing
-------------------

- **silx.gui.dialog**: Dialog widgets to select data from files
   .. image:: img/imagefiledialog_edf.png
      :width: 295px
      :height: 175px


- **silx.gui.hdf5**: Widgets to browse HDF5 files structure
   .. image:: img/Hdf5TreeView.png
      :width: 320px
      :height: 203px

----

Visualisation
-------------

0. **silx.gui.plot**: 1D and 2D Plot widgets
#. **silx.gui.plot3d**: 3D Visualisation widgets
#. **silx.gui.data**: Widgets for data visualisation

-----

.. include:: plot.rst

----

Visualisation
-------------

**silx.gui.plot3d**: Widgets to visualize data in 3D with OpenGL.

.. list-table::
   :header-rows: 1

   * - ScalarFieldView
     - SceneWindow
   * - .. image:: img/scalarFieldView.png
          :height: 200px
          :align: center
     - .. image:: img/sceneWindow.png
          :height: 200px
          :align: center
   * - ``viewer3DVolume.py``
     - ``plot3dSceneWindow.py``

Doc: http://www.silx.org/doc/silx/latest/modules/gui/plot3d/

----

Visualisation
-------------

**silx.gui.data**: Widgets selecting view depending on the kind of data

.. image:: img/DataViewerFrame.png
   :height: 300px
   :align: center

This is the basis of the `silx view` application.

----

More widgets
------------

- **silx.gui.widgets**

  .. list-table::
     :header-rows: 1

     * - FrameBrowser
       - PeriodicTable
       - PrintPreview
       - TableView
     * - .. image:: img/FrameBrowser.png
            :width: 150px
            :align: center
       - .. image:: img/periodicTable.png
            :width: 200px
            :align: center
       - .. image:: img/printPreview.png
            :width: 200px
            :align: center
       - .. image:: img/TableWidget.png
            :width: 150px
            :align: center

  \ 

  .. list-table::
     :widths: 1 1
     :header-rows: 1

     * - ThreadPoolPushButton
       - WaitingPushButton
     * - .. image:: img/ThreadPoolPushButton.png
            :width: 100px
            :align: center
       - .. image:: img/WaitingPushButton.png
            :width: 60px
            :align: center


.. Widgets
  - FrameBrowser: Widgets to browse frames
  - PeriodicTable: Periodic table as a table, a list, or a drop-down list
  - PrintPreview: Print preview dialog
  - TableWidget: Widget displaying a table with cut/copy and paste features
  - ThreadPoolPushButton: Button to execute a threaded task
  - WaitingPushButton: Button with waiting status

----

More widgets
------------

- **silx.gui.fit**: Fit widget
   .. image:: img/FitWidget.png
      :height: 200px
      :align: center
- **silx.gui.console**: IPython console widgets
   .. image:: img/IPythonWidget.png
      :height: 200px
      :align: center

----

Qt utils
--------

- **silx.gui.qt**: Common wrapper over Qt bindings: PyQt4, PyQt5, PySide and PySide2

  .. code-block:: python

     from silx.gui import qt
     app = qt.QApplication([])
- **silx.gui.icons**: Set of icons

  .. image:: img/icons.png
    :width: 240px
    :height: 300px

----

Resources
---------

- Documentation: http://www.silx.org/doc/silx/latest/modules/gui/
- Widgt gallery: http://www.silx.org/doc/silx/latest/modules/gui/gallery.html
- Sample code: http://www.silx.org/doc/silx/latest/sample_code/


