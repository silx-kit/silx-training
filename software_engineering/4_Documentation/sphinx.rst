
Sphinx
------

\ 

-----

Introduction
............

`Sphinx <http://sphinx-doc.org/>`_ is the tool used to generate the Python documentation:

- `Python 3 documentation <https://docs.python.org/3/>`_
- `Python 2 documentation <https://docs.python.org/2/>`_

Generates html, LaTeX, ePub, Texinfo, man pages, plain text from reStructuredText.

Also supports C/C++ language.

Installing Sphinx: ``pip install sphinx`` or with the OS package manager.

------

Principle
.........

Sphinx parses rst files and docstrings in source code to generate the documentation.

It uses a configuration file ``conf.py`` to control the way the documentation is built.

------

QuickStart
..........


Provided that your Python package and its dependencies are **installed** on your computer, the shortest way to Sphinx is the ``sphinx-apidoc`` command line tool:

- At the root of your source project, run::

    sphinx-apidoc -F -o doc/ <package_directory>

  This creates and populates the ``doc/`` directory.
- In the ``doc/`` directory, run ``make html`` and your documentation is generated in the ``_build/html/`` directory, starting with ``index.html``.

`sphinx-apidoc documentation <http://sphinx-doc.org/invocation.html#invocation-apidoc>`_

------

Set-up Sphinx for a project
...........................

The longer story.

``sphinx-quickstart`` is a shell command line tool that sets-up a default documentation project.
It asks you questions and generates ``conf.py`` and the entry point of the documentation ``index.rst``.

You probably want to enable some Sphinx extensions:

- **autodoc**: automatically insert docstrings from modules
- *doctest*: automatically test code snippets in doctest blocks
- *pngmath*: include math, rendered as PNG images
- *mathjax*: include math, rendered in the browser by MathJax
- *viewcode*: include links to source

Edit ``index.rst`` and add ``*.rst`` files to write the documentation.

Edit ``conf.py`` to change the documentation settings.

------

The ``doc/`` folder contains::

  doc/
    _static/    Custom stylesheets and static files (e.g., images)
    _template/  Custom html templates
    conf.py     Sphinx documentation configuration
    index.rst   Documentation entry point
    *.rst       Documentation as rst files
    make.bat    To build the doc on Windows
    Makefile    To build the doc, e.g.,  make html

Add \*.rst files (and images, ...) for the different parts of the documentation.

See `First steps with Sphinx <http://sphinx-doc.org/tutorial.html>`_.

------

Build the doc
.............

- ``make html`` in the ``doc/`` directory
- ``sphinx-build -b html sourcedir builddir``
- It is also possible build the doc with ``setup.py``

Warning: Sphinx might import the Python modules to be documented when building the documentation.
So the modules must be installed (or at least in the path Python is searching for modules).

------

Write documentation for Sphinx
..............................

Sphinx parses rst syntax, source code and docstrings.

It adds some extension to rst to document Python code:

Sphinx `Python domain <http://sphinx-doc.org/domains.html#the-python-domain>`_:
rst roles and directives to document Python code.

------

Table of content
................

.. code-block:: rst

  .. toctree::
     :maxdepth: 2

     install.rst
     tuto.rst
     module.rst

Create a table of content and link to the content of files:
install.rst, tuto.rst, module.rst.

------

Module helper
.............

For API documentation, the source files are not enough, some \*.rst files are needed:

- To structure the documentation.
- To select what is documented.
- To avoid pollution of the source code with too much documentation.

------

autodoc
.......

The sphinx extension ``sphinx.ext.autodoc`` includes docstrings from source code in the generated documentation.

.. code-block:: rst

  .. autofunction:: <function_name>

  .. automodule:: <module_name>
     :members: <optional: list of members>
     :undoc-members:

  .. autoclass:: <class_name>
     :members: <optional: list of members>
     :undoc-members:
     :inherited-members:

And more: ``autoexception, autodata, automethod, autoattribute``

Warning: autodoc **imports** the modules to be documented.
The modules must be installed or added to ``sys.path`` in ``conf.py``.
Take care which version gets documented.

------

``autodoc`` configuration in ``conf.py``:

- ``autoclass_content``: ``"class"``, ``"both"``, ``"init"``
- ``autodoc_member_order``: ``"alphabetical"`` (default), ``"groupby"`` (by type), ``"bysource"``
- ...

See `sphinx.ext.autodoc documentation <http://sphinx-doc.org/ext/autodoc.html#module-sphinx.ext.autodoc>`_.

------

Info field list
...............

.. code-block:: python

   def random_xorshift32(last_value, shift_triple=(13, 17, 5)):
       """32 bits pseudo-random generator.

       :param numpy.uint32 last_value: Previously returned number or the seed.
       :param shift_triple: Bit shifts to use.
       :type shift_triple: 3-tuple of int
       :return: The generated random number.
       :rtype: numpy.uint32
       :raises ValueError: if x is not a numpy.uint32
       """
       x = numpy.uint32(last_value)  # Work with 32bits unsigned integer
       x ^= numpy.uint32(last_value) << shift_triple[0]
       x ^= x >> shift_triple[1]
       x ^= x << shift_triple[2]
       return x

Alternative syntax: Sphinx extension `Napoleon <http://sphinxcontrib-napoleon.readthedocs.org>`_

- `Google style <http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_google.html>`_
- `Numpy style <http://sphinxcontrib-napoleon.readthedocs.org/en/latest/example_numpy.html#example-numpy>`_

------

Cython and C functions
......................

To document a `cython <http://cython.org/>`_ (C) function, the profile of the function can be given as the first line of the docstring.

code.pyx:

.. code-block:: python

  def cython_function(arg1, arg2):
      """cython_function(arg1, arg2)

      Documentation of the function written in cython.

      :param arg1:
      :param arg2:
      :return:
      """
      ...

------

Cross-referencing Python objects
................................

.. code-block:: rst

  Cross-reference:

  - A module :mod:`module_name`.
  - A function :func:`function_name`.
  - A class :class:`class_name`.
  - ...

Also consider readability of the docstring in the source file.

------

Sum-up
.......

Sphinx:

- Provides a build toolchain and reStructuredText extensions to write documentation for Python.
- Supports both API documentation (based on docstrings) and other documents.
- Outputs to different formats.

See `Sphinx documentation <http://sphinx-doc.org/contents.html>`_.
