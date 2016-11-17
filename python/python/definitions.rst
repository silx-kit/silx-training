Definitions
===========

**types, operations, loops, conditions**

1. Primitive types, basic operations
2. Composed types: Strings, lists, tuples, dictionaries
3. Everything is object
4. Control structures: blocks, branching, loops

----

Primitive types, basic operations
---------------------------------

----

Basic types:
^^^^^^^^^^^^

- Integers:
    - Fixed length (32 or 64 bits): 
        - -2, 1, 6452
    - Long integer (arbitrary/infinite length):  
        - -2L, 1L, 6452L, -9223372036854775808L (sys.maxsize + 1)

- Floating point number (64 bits by default):
    - 3.1415926535897931, 2.7182818284590451

- Complex numbers:
    - 3+4j 

- Boolean:  
    - ``True || False``

- None

----

.. code-block:: python
    
    >>> a, b = 5, 5.0
    >>> a == b
    True
    >>> type(a); type(b)
    <type 'int'>
    <type 'float'>
    >>> a is None
    False
    >>> None is None
    True

----

Basic operations
^^^^^^^^^^^^^^^^

- Primary operations: ``+ - * / % //``
    - warning: 
        - Python 2: ``3 / 2 = 1``
        - Python 3: ``3 / 2 = 1.5``
        - Explicitely use ``//`` for integer division

- Power, absolute value, …
    - ``a**b``, ``pow(a, b)``, ``abs(a)``

- Comparison: ``is   ==   !=   is not  >  >=  <  <=``

- Logical operators: ``and   or   not   xor``

- Bitwise operators: ``&   ^   |   <<   >>``
 

----

.. code-block:: python
    
    >>> 1 is None
    False
    >>> None is None
    True
    >>> 1.0 / 2.0
    0.5
    >>> 3 // 2
    1
    >>> (5. + 4.0j - 3.5) * 2.1
    (3.1500000000000004+8.4j)
    >>> 2 ** 8
    256
    >>> 256 >> 1
    128
    >>> 256 & 128
    0
    >>> 256 | 128
    384
    >>> 1 >= 0.5 and (2 > 3 or 5 % 2 == 1)
    True
    >>> 3+4j > 1
    TypeError: no ordering relation is defined for complex numbers

----

Composed types
--------------

----

Strings
^^^^^^^

.. code-block:: python
    
    >>> "I am a string"
    >>> 'Me too'
    >>> """"I am a 
    ... mutli-line string""" 
    >>> 'a multi-line string\ncan also be defined like that'

- Basic operations on strings:

.. code-block:: python
    
    >>> s + str(a); '%s %d' % (s, a)
    'a is equal to5'
    'a is equal to 5'
    >>> s + a
    TypeError: cannot concatenate 'str' and 'int' objects
    >>> '*--*' * 5
    '*--**--**--**--**--*'
    
- String access:

.. code-block:: python
    
    >>> 'I like playing with strings'[-1::-1]
    'sgnirts htiw gniyalp ekil I'

----


- String are not mutables

.. code-block:: python
        
    >>> 'helko'[3] = 'l'
    TypeError: 'str' object does not support item assignment

- Indices start at 0

.. code-block:: python
    
    >>> '123'[3]
    IndexError: string index out of range

----

Useful methods
""""""""""""""

- ``len(str)``
    - returns the length of the string
- ``str.find(subStr), str.index(subStr)`` 
    - returns the starting index. Find may return ``-1`` if not found, index fails.
- ``str.replace(str1, str2)`` 
    - replaces str1 with str2 in string 
- ``str.split()`` 
    - splits the string in a list of words

----

- ``str.startswith(sub), str.endswith(sub)`` 
    - returns ``True`` if main string ``str`` starts with ``sub``-string
- ``str.isalnum(), str.isalpha(), str.isdigit()`` 
    - returns ``True`` if the chain is alphanumeric, only letter or only numbers
- ``str.strip(), str.rstrip(), lstrip()`` 
    - removes spaces at the extremites of the string (R and L variant for Right/Left)
- ``str.upper(), str.lower, str.swapcase`` 
    - Converts to all upper-case, all lowercase, swap case


----


List and Tuple
^^^^^^^^^^^^^^

----

Mapping Types: Dictionaries
^^^^^^^^^^^^^^^^^^^^^^^^^^^

----

Everything is object
--------------------

----

Control structures: blocks, branching, loops
--------------------------------------------


