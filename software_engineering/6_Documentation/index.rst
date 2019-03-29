
.. raw:: html

   <!-- Patch landslide slides background color --!>
   <style type="text/css">
   div.slide {
       background: #fff;
   }
   </style>

Documenting Python packages
===========================

Outline
-------

#. Introduction
#. Readme
#. Docstrings
#. reStructuredText
#. Sphinx
#. Continuous Documentation
#. Conclusion

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

Some rules for technical writing:

- Write in two steps: Content first, then organisation and style.
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

  Intended audiance: developers, advanced users looking for insights.

- **Operation**: Installation, FAQ

Structure all the documents: Index page, tree structure.

------

README
------

First look at the project.

README:

- Name of the project
- Brief description (i.e., abstract)
- Installation
- Documentation: Getting started and/or link to documentation.
- License
- ...

------

README Formatting
-----------------

Text file with readable markup syntax. On github:

- Markdown (README.md):
  `QuickRef <http://daringfireball.net/projects/markdown/basics>`_,
  `QuickRef on github <https://help.github.com/articles/markdown-basics/>`_.

  ::

    Module
    ======

    This is a Python module.

    Installation
    ------------

    pip install myexample
    ...

- reStructuredText_ (README.rst): See later.

------

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

TODO: spinx, speak about directives and roles

------

.. include:: restructuredtext.rst

------

.. include:: sphinx.rst

------

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
