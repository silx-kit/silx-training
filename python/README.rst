

Python training
===============

Training for beginner in Python.

Contains:

- ``python``:

    Python basis using Python 3

- ``numpy``:

    How to use numpy to compute your data

- ``io``:

    How to read and write data at the ESRF

Dependancies
============

To generate the document, you have to install

- ``landslide``
- ``princexml`` (http://princexml.com/) for the PDF output
- ``inkscape`` to convert SVG to PNG
- ``pdfunite`` to merge many PDF into a single one

Makefile
========

There is 4 targets to the makefile

- ``make png``:

    Generate svg files into PNG (princexml do not allow to display SVG)

- ``make html``:

    Generate HTML output into ``build/html``

- ``make pdf``:

    Generate single PDF for each part plus a master PDF ``build/html/slides.pdf``

- ``make clean``:

    Clean up generated files
