
.. raw:: html

   <!-- Patch landslide slides background color --!>
   <style type="text/css">
   div.slide {
       background: #fff;
   }
   </style>

.. |br| raw:: html

   <br />

Testing
=======

#. Introduction
#. unittest
#. Additional tools
#. Continuous integration

------

What kinds of tests?
--------------------

- **Unit tests**: Test from the developer point of view.
  Test the code without the dependencies.
- **Integration tests**: Test from the developer point of view.
  Test that the code is integrated correctly with some external system or libraries.
- **Functional tests**: Test from a user point of view.
  Call a script, use the public API of a pacakge, test from the GUI.

------

When to write tests?
--------------------

- Never
- Always and before anything else: Test-Driven Development (*TDD*) [TDDwithPython]_ |br|
  Workflow:

  - First write a test, run it and check that it fails...
  - Only then write the code, and test it.
  - Then eventually do some refactoring.

*TDD* for maintenance: Reproduce bug in a test, then fix it.

Anyway, having the structure set-up for testing encourages writing tests.

.. [TDDwithPython] `Harry J.W. Percival. Test-Driven Development with Python. O'Reilly 2014. <http://chimera.labs.oreilly.com/books/1234000000754>`_
  (Oriented towards web development).

------

For who?
--------

Tests (and test coverage) are primarily for developers.

------

Where to put the tests?
-----------------------

Separate tests from the source code:

- Run the test from the command line.
- Separate test code when distributing.
- `... <https://docs.python.org/3/library/unittest.html#organizing-test-code>`_

Tests folder structure:

- In a separate ``tests/`` folder.
- In ``tests`` sub-packages in each Python package/sub-package,
  so that tests remain close to the source code.
  Tests are installed with the package and can be run from the installation.
- A ``test_*.py`` for each module and script (an more if needed).
- Consider separating tests that are long to run from the others.

------

::

  project/
      setup.py
      run_tests.py
      package/
          __init__.py
          module1.py
          tests/
              __init__.py
              test_module1.py
              subpackage/
                  __init__.py
                  module1.py
                  module2.py
                  tests/
                      __init__.py
                      test_module1.py
                      test_module2.py
      scripts/
          my_script.py
          my_other_script.py
      tests/
          test_my_script.py
          test_my_other_script.py

------

.. include:: unittest.rst

------

Extra tools
-----------

\ 

------

QTest
.....

For GUI based on ``PyQt``, ``PySide`` it is possible to use Qt's `QTest <http://doc.qt.io/qt-5/qtest.html>`_.

It provides the basic functionnalities for GUI testing.
It allows to send keyboard and mouse events to widgets.

.. code-block:: python

  from PyQt4.QtTest import QTest
  from PyQt4 import QtCore

  ...

  widget = ...

  QTest.qWaitForWindowShown(widget)
  QTest.mouseClick(widget, QtCore.Qt.LeftButton, pos=QtCore.QPoint(1, 1))
  QTest.keyClicks(widget, 'test', delay=100)  # Wait 100ms

  ...

Tighly coupled with the code it tests.
It needs to know the widget instance and hard code the position of mouse events.

------

Test coverage
.............

Using `coverage.py <https://coverage.readthedocs.org>`_ to gather coverage statistics while running the tests:

#. Install ``coverage.py`` package: ``pip install coverage``.
#. Run the tests: ``python -m coverage run --source <package_dir> run_tests.py``
#. Show report:

  - ``python -m coverage report``
  - ``python -m coverage html``

::

  Name                                   Stmts   Miss  Cover
  ----------------------------------------------------------
  rounding/__init__                          5      1    80%
  rounding/tests/__init__                   13      4    69%
  rounding/tests/test_parametric_round      27      1    96%
  rounding/tests/test_round                 23      1    96%
  ----------------------------------------------------------
  TOTAL                                     68      7    90%

------

Extra test tools
................

Extending ``unittest``:

- `pytest <http://pytest.org/>`_
- `nose <https://nose.readthedocs.org/>`_

Running the tests on different Python environments:

- `tox <https://tox.readthedocs.org/>`_ automates testing of Python packages

------

Continuous integration
----------------------

Benefits:

- Test on multiple platform/configuration (e.g., different version of Python).
- Test often: each commit, each pull request, daily...

Costs:

- Set-up and maintenance.
- Test needs to be automated.

------

In-house
--------

`Jenkins <https://jenkins-ci.org/>`_:

- 'Master' server with a web interface that controls the tests.
- 'Slave' nodes that runs the tests.

------

External
--------

- `Travis-CI <https://travis-ci.org/>`_: CI for Linux and Mac OS X
- `AppVeyor <http://www.appveyor.com/>`_: CI for Windows

Principle:

- Add a ``.yml`` file to your repository describing:

  - The test environment
  - Build and installation of the dependencies and the package
  - The way to run the tests.

- Upon commit, clones the repository and runs the tests.
- Displays the outcome on a web page.

------

Sum-up
------

- Different test strategies.
- Python ``unittest`` (and extra packages) to write and run the tests.
- Additionnal tools to efficiently run the tests: Continuous Integration.
- Next step: Continuous Deployment.
