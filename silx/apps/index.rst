************
Applications
************

----

Introduction to data formats
============================

HDF5 is the preferred data format at the ESRF.

The NeXus format adds a layer of standard to write data as HDF5
(or any other hierarchical format) for neutron, x-ray, and muon science.

Applications provided by *silx* interpret all other supported data formats
(EDF, SPEC...) as NeXus + HDF5 data. 

More on this subject later, in the IO section of the training.  
 
----

silx view
=========

- Visualisation of data formats used at the ESRF

  - Support HDF5 files, Spec files, EDF files (plus all formats supported by `FabIO`)
  - All formats viewed through a hierarchical nexus-like lense
  - HDF5 tree widget for selecting data items
  - DataViewer for visualising datasets as curves, or images, 
    or stack of images, or raw values in a table


.. code-block:: bash

    silx view somefile.edf

----

.. image:: img/silx_view_as_curve.png

----

silx convert
============

- Conversion of all supported data formats to HDF5 + NeXus.

  - The output file has exactly the same structure as displayed 
    by the *silx view* application.

- Merging stack of single image files into a 3D cube


----

silx convert: examples
======================


.. code-block:: bash

    silx convert somefile.edf

.. code-block:: bash

    silx convert spec_file.dat -o output_file.h5
    silx convert image.edf -o output_file.h5::/27.1 --mode a
    
.. code-block:: bash

    silx convert --file-pattern ch09__mca_0005_0000_%d.edf -o ch09__mca_0005_0000_multiframe.h5

----

Exercises
=========

?
