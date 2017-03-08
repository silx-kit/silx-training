
unittest Python module
----------------------

#. QuickStart
#. Chaining tests
#. Running tests
#. More on TestCase

------

QuickStart
..........

`unittest <https://docs.python.org/3/library/unittest.html>`_ is the default Python module for testing.

It provides features to:

- Write tests
- Discover tests
- Run those tests

------

TestCase
^^^^^^^^

``unittest.TestCase`` is the base class for writting tests for Python code.

Usage:

.. code-block:: python

   import unittest

   class ClassName(unittest.TestCase):

       def test*(self):
           ...  # Test code

       ...  # Other test* methods

Example: Test Python built-in round function

.. code-block:: python

   # test_builtin_round.py
   import unittest

   class TestBuiltInRound(unittest.TestCase):

       def test_round_positive(self):
           ...  # Test code

       def test_round_negative(self):
           ...  # Test code

       ...  # More test* methods

------

TestCase.assert*
^^^^^^^^^^^^^^^^

``TestCase.assert*(a, b, msg=None)`` or ``TestCase.assert*(x, msg=None)``:

- *a*, *b* or *x*: Argument(s) to compare/evaluate.
- *msg*: Additional error message.

========================= ==================== =======
Method 	                  Checks that 	       New in
========================= ==================== =======
assertEqual(a, b)         a == b 	 
assertNotEqual(a, b)      a != b 	 
assertTrue(x)             bool(x) is True 	 
assertFalse(x)            bool(x) is False 	 
assertIs(a, b)            a is b               2.7 3.1
assertIsNot(a, b)         a is not b           2.7 3.1
assertIsNone(x)           x is None            2.7 3.1
assertIsNotNone(x)        x is not None        2.7 3.1
assertIn(a, b)            a in b               2.7 3.1
assertNotIn(a, b)         a not in b           2.7 3.1
assertIsInstance(a, b)    isinstance(a, b)     2.7 3.2
assertNotIsInstance(a, b) not isinstance(a, b) 2.7 3.2
========================= ==================== =======

There's more, see `unittest.TestCase doc <https://docs.python.org/3/library/unittest.html#unittest.TestCase>`_.
Numpy also provides some asserts: `numpy.testing <http://docs.scipy.org/doc/numpy/reference/routines.testing.html>`_.

------

test_round.py:

.. code-block:: python

   import unittest


   class TestBuiltInRound(unittest.TestCase):

       def test_round_positive(self):
           result = round(1.3)
           self.assertEqual(result, 1)

       def test_round_negative(self):
           result = round(-1.3)
           self.assertEqual(result, -1)

       def test_round_halfway_even(self):
           result = round(2.5)
           self.assertEqual(result, 2, msg="round(2.5) -> %f != 2" % result)

       def test_round_returned_type(self):
           self.assertIsInstance(round(0.), int)

------

Run the tests
^^^^^^^^^^^^^

test_round.py:

.. code-block:: python

   ...

   if __name__ == "__main__":  # True if run as a script
       unittest.main()

``unittest.main()`` provides a command line interface to discover and run the tests.

------

Example
^^^^^^^

test_round.py:

.. code-block:: python

   import unittest


   class TestBuiltInRound(unittest.TestCase):

       def test_round_positive(self):
           result = round(1.3)
           self.assertEqual(result, 1)

       def test_round_negative(self):
           result = round(-1.3)
           self.assertEqual(result, -1)

       def test_round_halfway_even(self):
           result = round(2.5)
           self.assertEqual(result, 2, msg="round(2.5) -> %f != 2" % result)

       def test_round_returned_type(self):
           self.assertIsInstance(round(0.), int)


   if __name__ == "__main__":  # True if run as a script
       unittest.main()

------

Running tests from the command line on Python3::

  $ python3 test_builtin_round.py
  ....
  ----------------------------------------------------------------------
  Ran 4 tests in 0.000s

  OK


------

And on Python 2::

  $ python2 test_builtin_round.py
  F..F
  ======================================================================
  FAIL: test_round_halfway_even (__main__.TestBuiltInRound)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "test_builtin_round.py", line 16, in test_round_halfway_even
      self.assertEqual(result, 2, msg="round(2.5) -> %f != 2" % result)
  AssertionError: round(2.5) -> 3.000000 != 2

  ======================================================================
  FAIL: test_round_returned_type (__main__.TestBuiltInRound)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "test_builtin_round.py", line 19, in test_round_returned_type
      self.assertIsInstance(round(0.), int)
  AssertionError: 0.0 is not an instance of <type 'int'>

  ----------------------------------------------------------------------
  Ran 4 tests in 0.000s

  FAILED (failures=2)

------

Running a specific ``TestCase``::

  $ python3 test_builtin_round.py TestBuiltInRound
  ....
  ----------------------------------------------------------------------
  Ran 4 tests in 0.000s

  OK

Running a specific test method::

  $ python3 test_builtin_round.py TestBuiltInRound.test_round_positive
  .
  ----------------------------------------------------------------------
  Ran 1 test in 0.000s

  OK

------

Sum-up
^^^^^^

- Write tests in a ``unittest.TestCase`` sub-class.
- Use ``TestCase.assert*`` in the tests.
- Run the tests as a script from the command line.

This was a quickstart, ``unittest`` provides more features and flexibility.

------

Chaining tests
..............

How-to run tests from many ``TestCase`` and many files at once:

- Explicit
- Automatic

------

TestSuite
^^^^^^^^^

The `TestSuite <https://docs.python.org/3/library/unittest.html#unittest.TestSuite>`_ class aggregates test cases and test suites through:

- ``TestSuite.addTest(test)``
- ``TestSuite.addTests(tests)``

Example:

.. code-block:: python

   suite = unittest.TestSuite()
   suite.addTest(TestBuiltInRound('test_round_positive'))
   suite.addTest(TestBuiltInRound('test_round_negative'))
   ...

------

Explicit chaining 1/3
^^^^^^^^^^^^^^^^^^^^^

First, write a ``suite`` function for each module (i.e., file):

.. code-block:: python

   # test_round.py
   
   ...

   def suite():
       suite = unittest.TestSuite()
       suite.addTest(TestBuiltInRound('test_round_positive'))
       suite.addTest(TestBuiltInRound('test_round_negative'))
       ...
       return suite

------

Explicit chaining 2/3
^^^^^^^^^^^^^^^^^^^^^

Then a ``suite`` function collecting all tests in a package (i.e., directory).

.. code-block:: python

   # __init__.py or test_all.py

   from . import test_round
   ...

   def suite():
       suite = unittest.TestSuite()
       suite.addTest(test_builtin_round.suite())
       ...
       return suite

This can be used to create a ``TestSuite`` from all tests in a project:

- Full control over the creation of the ``TestSuite``.
- Requires some boilerplate code.

------

Explicit chaining 3/3
^^^^^^^^^^^^^^^^^^^^^

To run the ``suite`` from command line:

.. code-block:: python

   ...

   def suite():
       ...

   if __name__ == "__main__":  # True if run as a script
       unittest.main(defaultTest='suite')

------

Automatic aggregation 1/3
^^^^^^^^^^^^^^^^^^^^^^^^^

``unittest.defaultTestLoader`` (an instance of ``unittest.TestLoader``) creates ``TestSuite`` from classes and modules.

``TestLoader.loadTestsFromTestCase(testCaseClass)`` method creates a ``TestSuite`` from all ``test*`` method of a ``TestCase`` subclass.

Exemple:

.. code-block:: python

   # test_round.py
   
   ...

   def suite():
       suite = unittest.TestSuite()
       suite.addTest(
           unittest.defaultTestLoader.loadTestsFromTestCase(TestBuiltInRound))
       return suite

------

Automatic aggregation 2/3
^^^^^^^^^^^^^^^^^^^^^^^^^

``TestLoader.loadTestsFromModule(module)`` method creates a ``TestSuite`` from all ``TestCase`` subclass in a module.

Exemple:

.. code-block:: python

   # __init__.py or test_all.py

   from . import test_round  # or import test_round
   ...

   def suite():
       suite = unittest.TestSuite()
       suite.addTest(
           unittest.defaultTestLoader.loadTestsFromModule(test_round))
       ...
       return suite

Limitation: It is not always desirable to load tests this way.
E.g., if using a hierarchy of subclass of ``TestCase`` to share some code between different tests.

------

Automatic aggregation 3/3
^^^^^^^^^^^^^^^^^^^^^^^^^

With Python >= 2.7 / 3.2, it is possible to customize ``TestLoader.loadTestsFromModule(module)`` through a function ``load_tests``.

.. code-block:: python

  def load_tests(loader, tests, pattern):
      suite = unittest.TestSuite()
      ...  # Add tests to the suite in a custom way
      return suite

See `load_tests protocol <https://docs.python.org/3/library/unittest.html#load-tests-protocol>`_.

------

Test discovery (Python >= 2.7/3.2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``unittest`` offers test discovery based on automatic test aggregation.

From the command line::

  python -m unittest discover [-s <start_directory=.>] [-p <pattern=test*.py>]

From a script with the ``TestLoader.discover`` method.

It has the limitation of automatic aggregation.

It is customizable through the ``load_tests`` protocol.

------

Sum-up
^^^^^^

It is possible to chain tests from fully explicitly to fully automatically with test discovery:

- Explicit: Full control, boilerplate code.
- Mixing explicit and automatic.
- Automatic: No control unless using ``load_tests``.

------

Running the tests
.................

- ``unittest.main`` to run each module independantly.
- Command line: ``python -m unittest ...``
- With a ``run_tests.py`` script.

Minimal run_tests.py:

.. code-block:: python

   import unittest
   import mymodule.tests

   runner = unittest.TextTestRunner()
   runner.run(mymodule.tests.suite())

------

More on TestCase
................

\ 

------

Fixture
^^^^^^^

Tests might need to share some common initialisation/finalisation (e.g., create a temporary directory).

This can be implemented in ``setUp`` and ``tearDown`` methods of ``TestCase``.
Those methods are called before and after each test.

.. code-block:: python

   class TestCaseWithFixture(unittest.TestCase):

       def setUp(self):
           ...  # Pre-test code

       def tearDown(self):
           ...  # Post-test code

       ...  # Tests

----

More fixture
^^^^^^^^^^^^

.. code-block:: python

   # Module fixture

   def setUpModule():  # Called before all the tests of this module
       ...

   def tearDownModule():  # Called after all the tests of this module
       ...

   # Class fixture:

   class TestSample(unittest.TestCase):

       @classmethod
       def setUpClass(cls):  # Called before all the tests of this class
           ...

       @classmethod
       def tearDownClass(cls):  # Called after all the tests of this class
           ...

------

Testing exception
^^^^^^^^^^^^^^^^^

``TestCase.assertRaises``:

.. code-block:: python

   class TestBuiltInRound(unittest.TestCase):

       def test_raise_type_error(self):
           with self.assertRaises(TypeError)
               result = round('2')

``TestCase.assertRaisesRegexp`` also checks the message of the exception.

------

Skipping tests
^^^^^^^^^^^^^^

Why skipping a test: Test requires a specific OS or a specific version of a library...

To skip a test, call ``TestCase.skipTest(reason)`` from the test* or ``setUp`` method.

Also available through decorators ``unittest.skip``, ``unittest.skipIf``, ``unittest.skipUnless``.

.. code-block:: python

   import sys
   import unittest

   class TestBuiltInRound(unittest.TestCase):

       def test_python2(self):
           if sys.version_info[0] != 2:
               self.skipTest('Requires Python 2')
           self.assertEqual(round(2.5), 3.0)

       @unittest.skipIf(sys.version_info[0] != 3, 'Requires Python 3')
       def test_python3(self):
           self.assertEqual(round(2.5), 2)


------

Parametric tests
^^^^^^^^^^^^^^^^

Running the same test with multiple values:

.. code-block:: python

   class TestBuiltInRound(unittest.TestCase):

       HALFWAY_TESTS = ((0.5, 0), (1.5, 2), (2.5, 2))

       def test_halfways(self):
           for value, expected in self.HALFWAY_TESTS:
               self.assertEqual(round(value), expected)

Problems:

- The first failure stops the test, remaining test values are not processed.
- There is no information on the value for which the test has failed.

------

Parametric tests for Python >= 3.4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using ``TestCase.subTest``:

.. code-block:: python

   class TestBuiltInRound(unittest.TestCase):

       HALFWAY_TESTS = ((0.5, 0), (1.5, 2), (2.5, 2))

       def test_halfways(self):
           for value, expected in self.HALFWAY_TESTS:
               with self.subTest(value=value, expected=expected):
                   self.assertEqual(round(value), expected)

Run tests for all parameters and advertise which one has failed.

Limitation: Require Python >= 3.4

------

Parametric tests for Python < 3.4
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Use extra tools.
- Use a compatibility class providing the same API:
  `parametric_testcase.py <parametric_testcase.py>`_

  - Advertise the failed test parameters.
  - Limitation: Stop at the first failure.

------

Test data
^^^^^^^^^

How to handle test data?

Need to separate (possibly huge) test data from python package.

Download test data and store it in a temporary directory during the tests if not available.

Example: `pyFAI <https://github.com/kif/pyFAI>`_/test/utilstest.py

------

Sum-up
......

``unittest``:

- Write tests: ``TestCase``
- Chain tests: ``TestSuite``, explicit to automatic
- Run tests: ``main``, command line, script
