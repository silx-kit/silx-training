Definitions
===========

----

1. Primitive types, basic operations
2. Composed types: strings, lists, tuples, dictionaries
3. Everything is an object
4. Control structures: blocks, branching, loops

----

Primitive types
---------------

Integers:
^^^^^^^^^

- Fixed length (32 or 64 bits): ``-2, 1, 6452``
- Long integer (arbitrary length):
    - ``-2L, 1L, 6452L, -9223372036854775808L (sys.maxsize + 1)``

Floating point numbers:
^^^^^^^^^^^^^^^^^^^^^^^

- 64 bits (double-precision): 3.1415926535897931, 2.7182818284590451

Complex numbers:
^^^^^^^^^^^^^^^^
- 3+4j

Booleans:
^^^^^^^^^
- ``True`` and ``False``

None
^^^^

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
----------------

- Primary operations: ``+ - * / % //``
    - warning:
        - Python 2: ``3 / 2 = 1``
        - Python 3: ``3 / 2 = 1.5``
        - Explicitely use ``//`` for integer division
        - Get use to Python3 syntax

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

Strings
^^^^^^^

.. code-block:: python
    
    >>> "I am a string"
    >>> 'Me too'
    >>> """I am a 
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

- help associated to strings: print all functions (methods) of strings

.. code-block:: python
    
    >>> help(str)
    
----

Useful string methods
"""""""""""""""""""""

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

Formatting strings
------------------

C type
^^^^^^
    .. code-block:: python

        '%s %i %d %f %8.3f'%(5,5,5,5,5)
    return '5 5 5 5.000000    5.000'

Python formatting
^^^^^^^^^^^^^^^^^

    .. code-block:: python

        '{2} {1} {2} {0}'.format('a','b','c')
    return 'c b c a'

----

python2 vs python3
""""""""""""""""""

in python3 :

- strings are Unicode by default
- there is a clear separation between bytes and unicode (not in python2)

some outputs in python 2 and python 3:

+-----------------------+-----------------------+-+
| python2               | python3               | |
+=======================+=======================+=+
| >>> print(type('b'))  | >>> print(type('b'))  | |
| <class 'str'>         | <class 'str'>         | |
|                       |                       | |
| >>> print(type(b'b')) | >>> print(type(b'b')) | |
| <type 'str'>          | <class 'bytes'>       | |
|                       |                       | |
| >>> str(b'3')==b'3'   | >>> str(b'3')==b'3'   | |
| True                  | False                 | |
|                       |                       | |
| >>> b'123'[1] == b'2' | >>> b'123'[1] == 50   | |
| True                  | True                  | |
|                       |                       | |
+-----------------------+-----------------------+-+

----

List
^^^^

.. code-block:: python

    >>> help(list)

* Lists can contain any type of objects

.. code-block:: python
    
    >>> a = ['my string',True, 5+7]
    >>> print(a)
    ['my string', True, 12]
    >>> print(len(a))
    3
    
    >>> import math
    >>> a.append(math.pi) 
    >>>  print(a) 
    ['my string', True, 12, 3.141592653589793]
    >>> print(len(a))
    4
    
    >>> list(range(10)) ; 
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> list(range(5,12,2))
    [5, 7, 9, 11]
    
    >>> l_str = list('My string')
    >>> print(l_str)
    ['M', 'y', ' ', 's', 't', 'r', 'i', 'n', 'g']
    >>> print(''.join(l_str))
    'My string'

----

Useful methods for lists
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    >>> L = ['spam', 'eggs', 'sausages']

- ``append``: add one element at the end

.. code-block:: python

    >>> L.append("spam")
    >>> print(L)
    ['spam', 'eggs', 'sausages', 'spam']

- ``insert``: insert one element at a given index

.. code-block:: python

    >>> L.insert(2, "spam")
    >>> print(L)
    ['spam', 'eggs', 'spam', 'sausages', 'spam']

- ``index``: find first index containing a value

.. code-block:: python

    >>> L.index("spam")
    0
    >>> L.index("sausages")
    3
    
----

- ``count()``

.. code-block:: python

    >>> L.count("spam")
    3
    >>> L.count("sausages");
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

    - **Warning**: this deletes the list: ``L = L.sort()``


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


 
----

Tuple
^^^^^

.. code-block:: python

    >>> help(tuple)

* Tuples are immutable lists

.. code-block:: python

    >>> mytuple = ('spam', 'eggs', 5, math.pi, 'sausages')
    >>> mytuple[0] ; mytuple[-1]
    'spam'
    'sausages'
    >>> mytuple[3] = "ham"
    TypeError: 'tuple' object does not support item assignment

* Tuples are (slightly) faster than lists, but less convenient

* Use ``list(tuple)`` or ``tuple(list)`` to convert

* Tuples are not defined by presence of parenthesis "``()``", but by presence of comma "``,``"

.. code-block:: python

    >>> valid_tuple = 'spam', 'eggs', 5, math.pi, 'sausages'
    >>> valid_tuple_one_element = 'spam',
    >>> print(valid_tuple_one_element)
    ('spam',)

----

List & tuple comprehension
^^^^^^^^^^^^^^^^^^^^^^^^^^

* Very *pythonic* and convenient way of creating lists and tuples

.. code-block:: python

    >>> [2*x+1 for x in range(5)] 
    [1, 3, 5, 7, 9]
    
    >>> tuple(math.sqrt(x) for x in range(5))
    (0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0)
    
    >>> [x for x in range(10) if x**3 - 15*x**2 + 71*x == 105]
    [3, 5, 7]
    

* An alternative to functional programming: ``lambda``,  ``map`` & ``filter``

  - less *pythonic* and harder to read.
  - ``Lambda``, ``map`` and ``filter`` are reserved keywords, they should not be
    used as variable names.
  - Functional programming is no more faster than list comprehension

.. code-block:: python
   
    >>> list(map(math.sqrt, range(5)))
    [0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0]
    
    >>> list(filter(lambda x: x**3 - 15*x**2 + 71*x == 105, range(10)))
    [3, 5, 7]
    

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

- Often, elements cannot be accessed by index (`range`, is an exception !)

.. code-block:: python

    >>> m[2]
    TypeError: 'map' object is not subscriptable
    >>> r[2]
    2

- Convert to list for convenience of use, if access to elements in non-sequential order is needed

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

Dictionaries: examples
^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    >>> dico = {'key1': 'value1', 
                    2: 'val2',
                    math.pi: 3.14}
    
    >>> print(dico['key1'])
    'value1'

    >>> print(list(dico.keys()))
    [3.1415926535897931, 'key1', 2]
    
    >>> print(list(dico.values()))
    [3.1400000000000001, 'value1', 'val2']
    

**Nota:** `keys` and `values` are iterators in Python3!

.. code-block:: python

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

Everything is object (1/3)
--------------------------

- In Python everything is object (inherits from ``object``)


- Names are just labels, references, attached to an object
    - Memory is freed when the number of references drops to 0

- ``dir(obj)``: list the attributes of an object


- ``help(obj)``: prints the help of the object

- ``type(obj)``: get the type of an object

- ``id(obj)``: gets the memory adress of an object

----

Everything is object (2/3)
--------------------------

.. code-block:: python
     
     >>> a=object()
     
     >>> print(dir(a))
     ['__class__', '__delattr__', '__dir__', '__doc__',...]
     
     >>> type(True)
     <class `bool`>
     
     >>> type(a)
     <type 'object'>
     
     >>> id(a)
     140318487896256

     >>> b = 5
     >>> c = 5
     print(id(b), id(c))
     (34636024, 34636024)
     >>> id(b) == id(c)
     True
     >>> b is c
     True
     
-----

Everything is object (3/3)
--------------------------

.. image:: img/warning.png
    :width: 50px
    :align: right

.. code-block:: python
    :emphasize-lines: 2, 6, 7

    >>> L2 = [2, 4, 6]
    >>> L3 = L2
    >>> L3[1] = 100
    >>> print(L3)     # as expected
    [2, 100, 6]
    >>> print(L2)     # !
    [2, 100, 6]
    >>> id(L3) == id(L2)
    True

*L2* and *L3* are two *references* pointing to the **same data** (same memory block)

.. code-block:: python

    >>> L3 = L2[:]              # creates a copy of the data
    >>> id(L3) == id(L2)
    False
     
    >>> import copy
    >>> L4 = copy.deepcopy(L2)  # same, more explicit
    >>> id(L4) == id(L2)
    False

**Warning:** This is very error prone when manipulating any mutable objects.

----

Control structures
------------------

Code structure
^^^^^^^^^^^^^^

Python uses a column (:) at the end of the line and 4 white-spaces indentation
to establish code block structure.
Many other programming languages uses braces { }.


.. code-block:: python

    Block 1
    ...
    Header making new block:
        Block 2
        ...
        Header making new block:
            Block 2
            ...
        Block 2 (continuation)
        ...
    Block 1 continuation
    ...

The advantage
^^^^^^^^^^^^^

- Clearly indicates the beginning of a block
- Coding style is mostly uniform. Use **4 spaces**, never <tabs>
- Code structure is much more readable and clear.


----

Branching
^^^^^^^^^

- Condition branching are made with *if elif else* statements

.. code-block:: python
    :emphasize-lines: 5, 7, 11

    >>> a = -1
    >>> b = 2
    >>> c = 1
    >>> q2 = b * b - 4.0 * a * c
    >>> if q2 < 0:
    ...     print("No real solution")
    ... elif q2 > 0:
    ...     x1 = (-b + math.sqrt(q2)) / (2.0 * a)
    ...     x2 = (-b - math.sqrt(q2)) / (2.0 * a)
    ...     print("Two solutions %.2f and %.2f" % (x1, x2))
    ... else:
    ...     x = -b / (2.0 * a)
    ...     print("One solution: %.2f" % x)
    ... 
    Two solutions -0.41 and 2.41

- Can have many ``elif``'s (not recommended)
- Can be nested (too much nesting is bad for readability)

----

For loop
^^^^^^^^

- iterate over a sequence (list, tuple, char in string, keys in dict, …)
- no indexes, directly the object in the sequence

.. code-block:: python
    :emphasize-lines: 2

    >>> ingredients = ["spam", "eggs", "ham", "sausages"]
    >>> for food in ingredients:
    ...     print("I like %s" % food)
    ... 
    I like spam
    I like eggs
    ...

----

While loop
^^^^^^^^^^

- Iterate while a condition is fulfilled

.. code-block:: python
    :emphasize-lines: 4

    >>> a, b = 175, 3650
    >>> stop = False
    >>> possible_divisor = max(a, b) / 2.0
    >>> while possible_divisor >= 1 and not stop:
    ...     if a % possible_divisor == 0 and b % possible_divisor == 0:
    ...         print("Found greatest common divisor: %d" % possible_divisor)
    ...         stop = True
    ...     possible_divisor = possible_divisor - 1
    ...
    Found greatest common divisor: 25


- Make sure the condition becomes unfulfilled, else it could result in infinite loops:

.. code-block:: python

    >>> while True: 
    ...     print("I will print this forever")

----

Useful commands in loops
""""""""""""""""""""""""

- ``continue``: go directly to the next iteration of the most inner loop

.. code-block:: python
    :emphasize-lines: 4
    
    for i in range(100):
        if not i % 7 == 0:
            print("%d is *not* a multiple of 7" % i)
            continue
        print("%d is a multiple of 7" % i)

- ``break``: quit the most inner loop

.. code-block:: python
    :emphasize-lines: 6

    n = 112
    # divide n by 2 until this does no longer return an integer
    while True:
        if n % 2 != 0:
            print("%d is not a multiple of 2" % n)
            break
        print("%d is a multiple of 2" % n)
        n = n // 2
            
- ``pass``: a block cannot be empty; ``pass`` is a command that does nothing
- ``else``: block executed after the normal exit of the loop.

----

Practice: Fibonacci series
""""""""""""""""""""""""""

- Fibonacci:
    - Each element is the sum of the previous two elements
    - The first two elements are 0 and 1

- Calculate all elements in this series up to 1000, put them in a list, then print the list.

``[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]``

----

Fibonacci series: solutions
"""""""""""""""""""""""""""
Solution 1:

.. code-block:: python

    a, b = 0, 1
    res = [a, b]
    while b < 1000: 
        a, b = b, a + b
        res.append(b)

    print(res[:-1])

Solution 2: Shorter ... but is it faster ?

.. code-block:: python

    res = [0, 1]
    next_element = 1
    while next_element < 1000: 
        res.append(next_element)
        next_element = res[-2] + res[-1]

    print(res[:-1)

Solution 3: Without dropping the last element

.. code-block:: python

    a, b = 0, 1
    res = [a,]
    while b < 1000: 
        res.append(b)
        a, b = b, a + b

    print(res)


----

Enumerate and zip
"""""""""""""""""

- use ``enumerate()`` to get the indices of an iterator (0-based!)

.. code-block:: python

    >>> print("I like following foods:")
    >>> for idx, food in enumerate(ingredients):
    ...     print("%d. %s" % (idx + 1, food))
    ... 
    1. spam
    2. eggs


- ``zip()`` is a convenient way to loop over multiple sequences

.. code-block:: python

    >>> subjects = ["Roses", "Violets", "Sugar"]
    >>> verbs = ["are", "are", "is"]
    >>> adjectives = ["red,", "blue,", "sweet."] 
    >>> for s, v, a in zip(subjects, verbs, adjectives):
    ...     print("%s %s %s" % (s, v, a))
    ...  
    Roses are red,
    Violets are blue,
    Sugar is sweet.


