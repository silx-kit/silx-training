Definitions
===========

----

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

- Negative indexing to refer to element starting from the end

.. code-block:: python
    
    >>> my_str = 'abcd'
    >>> my_str[-2]
    'c'
    >>> my_str[-4] == my_str[0]
    True
    
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

List
^^^^

.. code-block:: python

    >>> help(list)

* Lists can contain any type of objects

.. code-block:: python
    
    >>> a=['my string',True, 5+7] ; a; len(a)
    ['my string', True, 12]
    3
    >>> import math
    >>> a.append(math.pi) ; a ; len(a)
    ['my string', True, 12, 3.141592653589793]
    4
    >>> list(range(10)) ; 
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list(range(5,12,2))
    [5, 7, 9, 11]
    >>>
    >>> l_str = list('My string')
    >>> l_str
    ['M', 'y', ' ', 's', 't', 'r', 'i', 'n', 'g']
    >>> ''.join(l_str)
    'My string'

----

Useful methods for lists
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> L = ['spam', 'eggs', 'sausages']

- ``append``: add one element at the end

.. code-block:: python

    >>> L.append("spam"); print(L)
    ['spam', 'eggs', 'sausages', 'spam']

- ``insert``: insert one element at a given index

.. code-block:: python

    >>> L.insert(2, "spam"); print(L)
    ['spam', 'eggs', 'spam', 'sausages', 'spam']

- ``index``: find first index containing a value

.. code-block:: python

    >>> L.index("spam"); L.index("sausages");
    0
    3
    
----

- ``count()``

.. code-block:: python

    >>> L.count("spam"); L.count("sausages");
    3
    1

- ``pop()``: remove and return one element by index

.. code-block:: python

    >>> L.pop()
    'spam'
    >>> L.pop(3)
    'sausages'

- ``remove()``: remove an element by value

.. code-block:: python

    >>> L.remove("eggs")
    >>> L.remove("eggs")
    ValueError: list.remove(x): x not in list

- ``sort()``, ``reverse()``: In place methods (no return value, original list is changed)

----

Operations on lists
^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> L1, L2 = [1, 3, 5], [2, 4, 6] 
    >>> L1 + L2
    [1, 3, 5, 2, 4, 6]
    >>> L1 *3
    [1, 3, 5, 1, 3, 5, 1, 3, 5]
    >>> list(zip(L1, L2))
    [(1, 2), (3, 4), (5, 6)]

* A list is a reference to a block of memory
.. image:: img/warning.png
    :width: 50px
    :align: left

.. code-block:: python

    >>> L3 = L2
    >>> L3[1] = 100
    >>> print(L3)     # as expected
    [2, 100, 6]
    >>> print(L2)     # !
    [2, 100, 6]

*L2* and *L3* are two *labels* pointing to the **same data** (same memory block)

.. code-block:: python

    >>> L3 = L2[:]              # creates a new list
    >>> L3 = copy.deepcopy(L2)  # more explicit




    
    

----

Tuple
^^^^^

.. code-block:: python

    >>> help(tuple)

* Tuple are immutable lists

.. code-block:: python

    >>> mytuple = ('spam', 'eggs', 5, math.pi, 'sausages')
    >>> mytuple[0] ; mytuple[-1]
    'spam'
    'sausages'
    >>> mytuple[3] = "ham"
    TypeError: 'tuple' object does not support item assignment

* Tuples are faster than lists, but less convenient

* Use ``list(tuple)`` or ``tuple(list)`` to convert

* Tuples are not defined by presence of "``(…)``", but by presence of "``,``"

.. code-block:: python

    >>> valid_tuple = 'spam', 'eggs', 5, math.pi, 'sausages'
    >>> valid_tuple_one_element = 'spam',
    >>> print(valid_tuple_one_element)
    ('spam',)

----

List and tuple comprehensions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Conveniant and elegant way of creating lists and tuples, very *pythonic*

.. code-block:: python
    
    >>> [x for x in range(10) if x**3 - 15*x**2 + 71*x == 105]
    [3, 5, 7]
    >>> tuple(math.sqrt(x) for x in range(5))
    (0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0)

* Alternative way to create the previous tuple: use ``map`` (functional programming)

.. code-block:: python

    >>> list(map(math.sqrt, range(10)))


----

Iterator
^^^^^^^^

- Like a list, but generates elements on demand: *fast*, *low-memory usage*

.. code-block:: python

    >>> r = range(10)
    >>> print(r)
    range(0, 10)
    >>> m = map(math.sqrt, range(10))
    >>> print(m)
    <map object at 0x7f9e719331d0>

- Often, elements cannot be accessed by index (OK for `range`, not for `map`)

.. code-block:: python

    >>> m[2]
    TypeError: 'map' object is not subscriptable
    >>> r[2]
    2

- Convert to list for convenience of use, unless performance is a concern

.. code-block:: python

    >>> list(r)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> [x for x in m]
    [0.0, 1.0, 1.4142135623730951, ...]

----

Mapping Types: Dictionaries
^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Dictionaries associate a key to a value:
    - Key must be *hashable*, i.e. any object that is unmutable
    - Also known as  *hash table*

- Dictionaries are not ordered (``OrderedDict`` exist as well)

.. code-block:: python

    >>> help(dict)

----

.. code-block:: python

	>>> dico = { 'key1': 'value1', 2: 'val2', math.pi: 3.14}
	>>> dico['key1']
        'value1'
	>>> dico.keys()
	dict_keys([3.1415926535897931, 'key1', 2])  # Iterator in Python3!
	>>> dico.values()
	dict_values([3.1400000000000001, 'value1', 'val2']) # Iterator in Python3!
	>>> 'key1' in dico
	True
	>>> len(dico)
	3
	>>> dico[math.e] 	
        KeyError: 2.718281828459045	
        >>> dico.get(math.e, 2.7)  # returns a default value if key not in dict
	2.7
	>>> myDict = dico.copy()
	>>> myDict.pop('key1')  # return 'value1', remove 'key1':'value1'

----

Everything is object
--------------------

- In Python everything is object (inherits from ``object``)


- Names are just labels attached to an object
    - Memory is freed when the number of references drops to 0
 
- ``dir(obj)``: list the attributes of an object


- ``help(obj)``: prints the help of the object

- ``type(obj)``: get the type of an object

- ``id(obj)``: gets the memory adress of an object

----

.. code-block:: python
     
     >>> a=object()
     >>> dir(a) ; dir(5)
     ['__class__', '__delattr__', '__dir__', '__doc__',...]
     >>> help(str)
     ... (long help message)
     >>> type(True)
     <class 'bool'>
     >>> id(a)
     140318487896256


----

Control structures: blocks, branching, loops
--------------------------------------------


