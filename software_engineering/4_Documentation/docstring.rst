
Docstrings
----------

\ 

------

Docstrings
..........

Docstring conventions `PEP 257 <https://www.python.org/dev/peps/pep-0257/>`_:

- Specify where: String as the first statement.
- Convention: Use triple quotes ``"""``.

rand.py:

.. code-block:: python

   """This module provides a random generator."""  # Module docstring

   def rand():
       """Returns a random floating point number."""  # Function docstring
       ...

   class RandomGenerator(object):
       """Pseudo random generator class.

       It is based on the XORShift algorithm.
       """  # Class docstring

       def rand(self):
           """Returns a pseudo-random float."""  # Method docstring
           ...

------

Purpose
.......

- Document the source code.

- Online help in Python console:

.. code-block:: python

  >>> import rand
  >>> help(rand.rand)  # Display function profile and the docstring

::

  Help on function rand in module rand:

  rand()
      Returns a random floating point number.

.. code-block:: python

  >>> rand.rand.__doc__  # Access to docstring
  "Returns a random floating point number."

- Used by external tools to generate the documentation.

------

Content
.......

`PEP 257 <https://www.python.org/dev/peps/pep-0257/>`_ docstring content recommendation:

- For **script**: Module docstring should be its **usage message** from the command line.
- For **module**: List of the classes, exceptions and functions with a one-line summary of each.
- For **class**: **Behavior summary**, list of the public method and instance variables.
- For **function** and **method**: **Behavior summary**, documentation of **arguments**, **return value**, side effects, exceptions raised, restrictions.

------

Attribute docstrings
....................

.. code-block:: python

   # rand.py
   RAND_SEED = 1
   """Seed used by rand."""  # Module attribute docstring

   class RandomGenerator(object):

       DEFAULT_SEED = 1
       """Default random generator seed."""  # Class attribute docstring

       def __init__(self, seed=None):
           
           self.seed = seed or self.DEFAULT_SEED
           """The generator's seed."""  # Instance attribute docstring

       ...

- Instance attribute docstring only in ``__init__`` method.
- Not available in console help (No ``__doc__`` attribute).
- But used by tools to generate the offline documentation.
