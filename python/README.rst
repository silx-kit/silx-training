

Python training
===============

Training for beginners in Python.

Contains:

- ``python``:

    Python 3 basics

- ``numpy``:

    How to use numpy for computing data

- ``io``:

    How to read and write data at the ESRF

Dependencies
============

To generate the document, you have to install

- ``landslide``
- ``princexml`` (http://princexml.com/) for the PDF output
- ``inkscape`` to convert images from SVG to PNG
- ``pdfunite`` to merge many PDF files into a single one

Makefile
========

There are 4 targets to the makefile

- ``make png``:

    Generate PNG files from SVG (princexml does not support SVG)

- ``make html``:

    Generate the HTML output in ``build/html``

- ``make pdf``:

    Generate a single PDF for each part plus a master PDF in ``build/html/slides.pdf``

- ``make clean``:

    Clean up generated files
