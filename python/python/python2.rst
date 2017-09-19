Python2
=======

----

End of python 2
---------------

Python 2.7 will not be maintained past 2020 !!!

https://pythonclock.org/

.. image:: img/theEndIsNear.jpg
    :width: 500px
    :height: 500px
	    
----

Tricky differences python2 - python3
------------------------------------

- Operator: ``/``
    - Python 2: ``3 / 2 = 1``
    - Python 3: ``3 / 2 = 1.5``
    - Get used to Python3 syntax

- print:

    +-----------------------+-----------------------+
    | python2               | python3               |
    +=======================+=======================+
    | >>> print "Bonjour"   | >>> print("Bonjour")  |
    | Bonjour               | Bonjour               |
    +-----------------------+-----------------------+

----

Tricky differences python2 - python3
------------------------------------

in python3 :

- strings are Unicode by default
- there is a clear separation between bytes and strings (not in python2)

+-----------------------+-----------------------+
| python2               | python3               |
+=======================+=======================+
| >>> print(type('a'))  | >>> print(type('a'))  |
| <class 'str'>         | <class 'str'>         |
|                       |                       |
| >>> print(type(b'a')) | >>> print(type(b'a')) |
| <type 'str'>          | <class 'bytes'>       |
|                       |                       |
| >>> '3' is b'3'       | >>> '3' is b'3'       |
| True                  | False                 |
|                       |                       |
| >>> '3' is u'3'       | >>> '3' is u'3'       |
| False                 | True                  |
|                       |                       |
| >>> list(b"abc")      | >>> list(b"abc")      |
| ['a', 'b', 'c']       | [97, 98, 99]          |
+-----------------------+-----------------------+

----

Tricky differences python2 - python3
------------------------------------

Some function now returning iterators

+-----------------------+-----------------------+
| python2               | python3               |
+=======================+=======================+
| >>> r = range(5)      | >>> r = range(5)      |
| >>> print(r)          | >>> print(r)          |
| [0, 1, 2, 3, 4]       | range(0, 5)           |
|                       |                       |
| >>> list(r)           | >>> list(r)           |
| [0, 1, 2, 3, 4]       | [0, 1, 2, 3, 4]       |
+-----------------------+-----------------------+

----

Integers  python2  - python3
----------------------------


Python 2: two types
^^^^^^^^^^^^^^^^^^^

- Fixed length (32 or 64 bits): ``-2, 1, 6452``
- Long integer (arbitrary length):
  - ``-2L, 1L, 6452L, -9223372036854775808L (sys.maxsize + 1)``

Python 3
^^^^^^^^

Single unified type (``int``) for all integers

+--------------------------+----------------------------------------+
| python2                  | python3                                |
+==========================+========================================+
| >>> isinstance(3L, long) | >>> 3L                                 |
| True                     | SyntaxError: invalid syntax            |
|                          |                                        |
| >>> isinstance(3L, int)  | >>> isinstance(3, long)                |
| False                    | NameError: name 'long' is not defined  |
|                          |                                        |
| >>> type(10**20)         | >>> type(10**999)                      |
| long                     | int                                    |
|                          |                                        |
| >>> 3L is 3              |                                        |
| False                    |                                        |
+--------------------------+----------------------------------------+

