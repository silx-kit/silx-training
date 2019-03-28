
.. role:: rst(code)
   :language: rst

reStructuredText
----------------

------

Introduction
............

ReStructuredText (`rst <http://docutils.sourceforge.net/rst.html>`_):

- *Easy-to-read* text markup syntax.
- Conversion to different formats (e.g., **html**, pdf).
- Version Control System friendly: Text files with one sentence per line.
- Primarily for Python documentation.

Source:

.. code-block:: rst

  Introduction
  ............

  ReStructuredText (`rst <http://docutils.sourceforge.net/rst.html>`_):

  - *Easy-to-read* text markup syntax.
  - Conversion to different formats (e.g., **html**, pdf).
  - ...

------

Features
........

- Paragraphs are separated by blank lines
- Sections: `Python documentation convention <https://docs.python.org/devguide/documenting.html#sections>`_
- Lists: ``- * +``
- Numbered lists: ``#.``
- Inline markup: *\*Emphasis\**, **\*\*Strong emphasis\*\***, :literal:`\`\`Literal\`\``
- Links: :literal:`\`example <https://example.com/>\`_`

\ 

- Code sample: :rst:`.. code-block:: rst`
- Figure: :rst:`.. figure:: image_filename`
- Math formula: :literal:`:math:\`\\sqrt{\\frac{x^2}{3}}\`` => :math:`\sqrt{\frac{x^2}{3}}`
- Tables: :rst:`.. csv-table::`
- ...

------

Syntax: Roles
.............

**Roles**:

.. code-block:: rst

   :role_name:`content`

Examples:

- :rst:`1\ :superscript:`st`` => 1\ :superscript:`st`
- :literal:`:math:\`\\sqrt{\\frac{x^2}{3}}\`` => :math:`\sqrt{\frac{x^2}{3}}`

`Roles documentation <http://docutils.sourceforge.net/docs/ref/rst/roles.html>`_

Inline markup limitations:

- No nesting.
- Whitespace around inline markup and no leading, trailing whitespaces inside.
- Escape \* \` with \\: :rst:`\*B\*` => \*B\*.

------

Syntax: Directives
..................

.. code-block:: rst

  .. directive_type:: arguments
     :option: value

     Content: indented and separated by blank lines.

Example: **Code block** with syntax highlighting:

.. code-block:: rst

  .. code-block:: python

     def add(a, b):
         return a + b

=>

.. code-block:: python

   def add(a, b):
       return a + b

`Directives documentation <http://docutils.sourceforge.net/docs/ref/rst/directives.html>`_.

.. And more...
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

- Sphinx RST Primer: http://sphinx-doc.org/rest.html
- Documenting Python: https://docs.python.org/devguide/documenting.html
- RST QuickRef: http://docutils.sourceforge.net/docs/user/rst/quickref.html

Blank lines and indentation count!

------

Tools to convert rst
....................

- Python package `docutils tools <http://docutils.sourceforge.net/docs/user/tools.html>`_:
  ``rst2html``, ``rst2latex``, ``rst2odt``, ``rst2s5``.
- `pandoc <http://pandoc.org/>`_ a universal document converter:
  ``pandoc -s -t rst file.rst -o file.html``
- `Sphinx <http://sphinx-doc.org/>`_.
