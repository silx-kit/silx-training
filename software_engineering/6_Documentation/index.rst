
.. raw:: html

   <!-- Patch landslide slides background color --!>
   <style type="text/css">
   div.slide {
       background: #fff;
   }
   </style>

.. include:: <isonum.txt>

=============
Documentation
=============

----

Documenting Python packages
---------------------------

Outline
.......

#. Introduction
#. Readme
#. Docstrings
#. reStructuredText
#. Sphinx
#. Continuous Documentation

------

Introduction
------------

What is this function doing?

.. code-block:: python

   def p(x):
       return (x & (x - 1)) == 0

------

Introduction (2)
----------------

What is this function doing?

.. code-block:: python

   def is_power_of_two(value):
       return (value & (value - 1)) == 0

------

Introduction (3)
----------------

What is this function doing?

.. code-block:: python

   def is_power_of_two(value):
       """Returns True if value is a power of two.

       It supports numpy array of int of any dimensions and returns
       an array of bool of same dimensions.

       Limitation: Returns True for 0.
       """
       return (value & (value - 1)) == 0

------

Different types of documentations
---------------------------------

Credits:

Tarek Ziadé.
Expert Python Programming. Chapter 10: Documenting your project.
September 2008, PACKT Publishing.
https://tarekziade.files.wordpress.com/2008/09/chapter-10.pdf

------

Main rules for technical writing:

- Write in two steps: Ideas first, then organisation and style.
- Target the readership.
- Use a simple style.
- Limit the scope of the information: One concept at a time.
- Use realistic code examples.
- Choose which documentation to write and avoid endless document.
- (Re)Use templates.

-----

Different types of documentation:

- **Usage**: How to use the software from API, command line or GUI:

  - *Cookbooks*: how to *do* something specific,
  - *Tutorials*: how to *use* a feature step-by-step,
  - *module API*.

- **Design**: How the software works, how code is organized.

  Intended audience: developers, advanced users looking for insights.

- **Operation**: Installation, FAQ

Structure all the documents: Index page, tree structure.

------

reStructuredText (rst)
----------------------

wikipedia definition:

`reStructuredText <http://docutils.sourceforge.net/rst.html>`_ is a file format for textual data used [...] for technical documentation.

* *Easy-to-read* text markup syntax.
* Conversion to different formats (e.g., html, pdf, latex).
* Version Control System friendly: Text files with one sentence per line.
* Primarily for Python documentation.

.. note:: All this presentation has been made using only rst.

----

README
------

It will be the 'front door' of your project.

It should contains:

* Name of the project
* Brief description (i.e., abstract)
* Installation
* Documentation: Getting started and/or link to documentation.
* License
* Authors
* ...

You can start from an existing template file:
    * https://github.com/konstantint/python-boilerplate-template/blob/master/README.rst
    * https://github.com/rtfd/template/blob/master/README.rst

------

Hands-on
--------

Write the README.rst of the project.

It should at include the project name, description, installation, license and author.

You can use a `rst cheat sheet <https://github.com/ralsina/rst-cheatsheet/blob/master/rst-cheatsheet.rst>`_ and create/edit the README.rst file directly from github / gitlab (result preview can help you)


.. image:: images/rst_cheat_sheet.png
    :width: 80%

.. +-----------------------------------------------------+-----------------------------------------------+
.. | rst                                                 | result                                        |
.. +=====================================================+===============================================+
.. | .. code-block:: text                                |                                               |
.. |                                                     | Title                                         |
.. |    Title                                            |                                               |
.. |    =====                                            |                                               |
.. +-----------------------------------------------------+-----------------------------------------------+
.. | .. code-block:: text                                |                                               |
.. |                                                     |                                               |
.. |    Section title                                    |   Section title                               |
.. |    -------------                                    |                                               |
.. +-----------------------------------------------------+-----------------------------------------------+
.. | .. code-block:: text                                |                                               |
.. |                                                     |                                               |
.. |       .. image:: imagesmyimage.png                  | .. image:: images/myimage.png                 |
.. |           :width: 10%                               |     :width: 10%                               |
.. |                                                     |                                               |
.. +-----------------------------------------------------+-----------------------------------------------+
.. | .. code-block:: text                                |                                               |
.. |                                                     |                                               |
.. |       **bold text**                                 |     **bold text**                             |
.. +-----------------------------------------------------+-----------------------------------------------+
.. | .. code-block:: text                                |                                               |
.. |                                                     |                                               |
.. |       *italique text*                               |     *italique text*                           |
.. +-----------------------------------------------------+-----------------------------------------------+
.. | .. code-block:: text                                |                                               |
.. |                                                     | `Python hyperlink <http://www.python.org/>`_. |
.. |    `Python hyperlink <http://www.python.org/>`_.    |                                               |
.. +-----------------------------------------------------+-----------------------------------------------+
.. | .. code-block:: text                                |  .. code-block:: python                       |
.. |                                                     |                                               |
.. |       .. code-block:: python                        |     res = pypolynom.polymom(a=2, b=-6, c=1)   |
.. |                                                     |                                               |
.. |           res = pypolynom.polymom(a=2, b=-6, c=1)   |                                               |
.. +-----------------------------------------------------+-----------------------------------------------+


----

Docstrings
----------

.. code-block:: python

   """This module provides a random generator."""  # Module docstring

   RAND_SEED = 1
   """Seed used by rand."""  # Module attribute docstring

   def rand():
       """Returns a random floating point number."""  # Function docstring
       ...

   class RandomGenerator(object):
       """Pseudo random generator class.

       It is based on the XORShift algorithm.
       """  # Class docstring

       DEFAULT_SEED = 1
       """Default random generator seed."""  # Class attribute docstring

       def __init__(self, seed=None):
           self.seed = seed or self.DEFAULT_SEED
           """The generator's seed."""  # Instance attribute docstring

       def rand(self):
           """Returns a pseudo-random float."""  # Method docstring
           ...

------

Docstrings Content
..................

`PEP 257 <https://www.python.org/dev/peps/pep-0257/>`_ docstring content recommendation:

- For **script**: Module docstring should be its **usage message** from the command line.
- For **module**: List of the classes, exceptions and functions with a one-line summary of each.
- For **class**: **Behavior summary**, list of the public method and instance variables.
- For **function** and **method**: **Behavior summary**, documentation of **arguments**, **return value**, side effects, exceptions raised, restrictions.

-----

Sphinx
------

Wikipedia definition:

"Sphinx is a documentation generator written and used by the Python community. It is written in Python, and also used in other environments."

Sphinx is using rst.

.. code-block:: python

   def is_power_of_two(value):
       """Function to check given values are a power of two

       :param value: array of value to test
       :type value: numpy array of int
       :return: True if value is a power of two or is 0.
       :rtype: numpy array of bool
       """
       return (value & (value - 1)) == 0


.. image:: images/is_power_of_two_doc_screenshot.png

------


Roles
-----

.. code-block:: rst

   :role_name:`content`

Examples:

- :rst:`1\ :superscript:`st`` |rarr| 1\ :superscript:`st`
- :literal:`:math:\`\\sqrt{\\frac{x^2}{3}}\`` |rarr| :math:`\sqrt{\frac{x^2}{3}}`

`Documentation relative to roles <http://docutils.sourceforge.net/docs/ref/rst/roles.html>`_

----

Directive
---------

.. code-block:: rst

  .. directive_type:: arguments
     :option: value

     Content: indented and separated by blank lines.

Example: **Code block** with syntax highlighting:

.. code-block:: rst

  .. code-block:: python

     def add(a, b):
         return a + b

|rarr| This directive will produce:

.. code-block:: python

   def add(a, b):
       return a + b

`Documentation relative to directives <http://docutils.sourceforge.net/docs/ref/rst/directives.html>`_.

----

Extensions:

several library are defining there own directives / roles

* `matplotlib plot <https://matplotlib.org/devel/plot_directive.html>`_
* `embed video <https://github.com/sphinx-contrib/video>`_
* `list of reference contribution <https://www.sphinx-doc.org/en/master/develop.html>`_
* `github sphinx contrib <https://github.com/sphinx-contrib>`_


.. note:: the extensions to use has to be registred on your sphinx conf.py file
----


----

Building documentation

html
pdf


Hands on
--------

Generate the documentation of your clone.


Embed a jupyter notebook in the documentation
---------------------------------------------

TODO: use nbsphinx + add a jupyter note book in the source code and associate
documentation with it,

https://nbsphinx.readthedocs.io/en/0.4.2/

----


Continuous documentation
------------------------

Building documentation automatically: `Read the Docs <https://readthedocs.org/>`_.

It builds the documentation with Sphinx:

- Install dependencies defined in a *requirements file*.
- Install the package with ``setup.py install``.
- Look for a ``conf.py`` file and use it to build the documentation.
- Make documentation available: ``http://<project_name>.readthedocs.org/``.

`Documentation of Read the Docs <http://read-the-docs.readthedocs.org/>`_

------

Conclusion
----------

- Different documentation for different purposes.
- Tools to ease the process.
- Very modular (no need to use everything, e.g., making your own template).
- Having a build system that generates the documentation encourages writing it.
- Documentation becomes out-dated, keeping it with the source code helps maintaining it: update the code and the documentation at the same time.


This presentation is written in reStructuredText_.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
