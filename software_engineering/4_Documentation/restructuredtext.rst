
.. role:: rst(code)
   :language: rst

reStructuredText
----------------

\ 

------

Introduction
............

ReStructuredText (`rst <http://docutils.sourceforge.net/rst.html>`_):

- "Easy-to-read" text markup syntax.
- Conversion to different formats (e.g., html, pdf).
- Version Control System friendly: Text files with one sentence per line.
- Primarily for Python documentation.

Source:

.. code-block:: rst

  Introduction
  ............

  ReStructuredText (`rst <http://docutils.sourceforge.net/rst.html>`_):

  - "Easy-to-read" text markup syntax.
  - Conversion to different formats (e.g., html, pdf).
  - ...

------

Features
........

- Paragraphs and sections
- Lists
- Inline markup
- Links

\ 

- Code sample
- Figure
- Math formula
- Tables
- ...

------

Paragraphs and sections
.......................

.. code-block:: rst

  =====
  Title
  =====

  Paragraphs are separated by blank lines.

  This is another paragraph.

  Chapter
  =======

  Titles have underlines and overlines.

  Section headers have underlines.

  Section
  -------

  Subsection
  ..........

  There is no specified heading levels.
  Section levels are determined from the succession of section headers determines.

`Sphinx Python documentation convention <http://sphinx-doc.org/rest.html#sections>`_

------

Lists
.....

.. code-block:: rst

  Bullet list:

  - Items start with ``- * +`` and a whitespace.
    Multi-line text must be aligned.
  - There is a blank line before and after the list.

  Numbered list:

  #. First item
  #. Second item

More lists: definitions, fields, options.

------

Inline markup
.............

- *\*Emphasis\**
- **\*\*Strong emphasis\*\***
- :literal:`\`\`Literal\`\``
- **Roles**: :rst:`:role_name:`content``

  - :rst:`1\ :superscript:`st`` => 1\ :superscript:`st`
  - :literal:`:math:\`\\sqrt{\\frac{x^2}{3}}\`` => :math:`\sqrt{\frac{x^2}{3}}`
  - `... <http://docutils.sourceforge.net/docs/ref/rst/roles.html>`_

Limitations:

- No nesting.
- Whitespace around inline markup and no leading, trailing whitespaces inside.
- Escape \* \` with \\: :rst:`\*B\*` => \*B\*.

------

Links
.....

External hyperlinks:

- https://github.com/kif/SE_training
- `SE_training repository <https://github.com/kif/SE_training>`_, syntax:

  .. code-block:: rst

    `SE_training repository <https://github.com/kif/SE_training>`_

Internal hyperlinks:

.. code-block:: rst

   =========
   The title
   =========

   .. _link_target:

   Link to link_target_ (note the single :).

   Link to `The title`_.

------

Directives
..........

.. code-block:: rst

  .. directive_type:: arguments
     :option: value

     Content: indented and separated by blank lines.

**Code block** with syntax highlighting:

.. code-block:: rst

  .. code-block:: python

     def add(a, b):
         return a + b

**Figure**:

.. code-block:: rst

  .. figure:: image_filename
     :align: center
     :width: 300

     This is the caption.

`Directives documentation <http://docutils.sourceforge.net/docs/ref/rst/directives.html>`_.

------

And more...
...........

This was just a primer:

- More lists, roles and directives.
- Tables, :rst:`.. csv-table::`.
- :rst:`.. include:: file.rst` to include another rst file.
- :rst:`.. raw:: [html|latex]` to include raw html or latex.
- Extendable: It is possible to add roles and directives.

------

QuickRef
........

To find more information:

- Sphinx reST Primer: http://sphinx-doc.org/rest.html
- reST QuickRef: http://docutils.sourceforge.net/docs/user/rst/quickref.html

Blank lines and indentation count.

------

Tools to convert rst
....................

- Python package `docutils tools <http://docutils.sourceforge.net/docs/user/tools.html>`_:
  ``rst2html``, ``rst2latex``, ``rst2odt``, ``rst2s5``.
- `pandoc <http://pandoc.org/>`_ a universal document converter:
  ``pandoc -s -t rst file.rst -o file.html``
- `Sphinx <http://sphinx-doc.org/>`_.

------

Sum-up
......

reStructuredText is a text markup syntax:

- Simple and readable for simple things.
- Roles and directives.
- Blank lines and indentation count.
- Conversion to different formats.

