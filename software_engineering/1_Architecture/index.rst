
.. raw:: html

   <!-- Patch landslide slides background color --!>
   <style type="text/css">
   div.slide {
       background: #fff;
   }
   </style>

1. Structure your project
=========================

#. Have a clean structure
#. A word about licenses
#. Coding convention

   #. PEP8
   #. PEP20

#. Version control system - git

----

Have a clean structure
----------------------

- Separate library from scripts:

  * libraries are reusable

- Separate GUI from calculation:

  *  Otherwise maintenance becomes a nightmare
  *  allows to change the front-end
  *  allows to access to core function without the GUI
  *  simplify unit tests

- Separate I/O from calculation

- avoid code duplication

Presenter Notes
...............

Will also help you to :

- find back your code
- avoid code duplication

----

example
-------

TODO

----

Define a license for your work !!!
----------------------------------

According to the French law, one should distinguish authorship from ownership:

 - Authorship is inalienable: your work becomes public domain 50 years after
   your death.
 - ESRF, your employer, owns the code you may have written during your contract
   (unless you can prove this development has no correlation with your work)

Licenses define how a piece of software can be used (and sometimes what for).
None of them claim any liability of the author.

If there is not license on your code he cannot be distributed or reused

----

One can define 2 categories:
----------------------------

- Proprietary licenses

  * Commercial licenses: one needs to purchase a license to use the code
  * Academic licenses: free for academic research

- Open source licenses:

  * GPL like enforces the distribution of source code
  * LGPL like enforces the publication of modified code
  * MIT/BSD which provides the name of the author for information
    (for scientific citation)

The Python scientific stack has a BSD-like licenses.

Defining licenses for your developments is important as the beamline can not
build code on top of unlicensed or proprietary work without explicit license
agreement.

Presenter Notes
...............

Warning : code under MIT/BSD/Apache licenses can be integrated under proprieteray licences, redistributed...

Why MIT instead of GPL or LGPL?
    -> GPL enforces publication of source code
    -> LGPL enforces publication of any modification of the original work
Why MIT instead of BSD ?
    -> Different version of BSD, complexify a bit
Why MIT instead of Apache 2.0 ?
    -> MIT is shorter and simpler

----

Coding convention
=================

----

Python 2 end of support
-----------------------

By 2020, the `support of Python2 will end <https://pythonclock.org/>`_.
All your projects should be python3 based.

Supporting Python3 is a must have today.

Look at the download statistics of projects like
`WinPython <https://sourceforge.net/projects/winpython/files/>`_: about 5900 downloads/week for Python_3.x vs 324 for Python_2.7

You can use the `six library <https://pypi.python.org/pypi/six>`_ to provide code that
runs both under Python2 and Python3.

Presenter Notes
...............

python-future is a higher-level compatibility layer than six that includes more backported functionality from Python 3, more forward-ported functionality from Python 2

----

Coding convention: `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_
----------------------------------------------------------------------

- Wrap lines at 79 char.
- Indent with 4 spaces.
- Put spaces around arguments (except in function declaration).
- English docstrings and triple quoted.
- One single import per line.
- Variable, method, modules name should be lower_case
  (with underscore, only if needed).
- Constant should be UPPER_CASE (with underscores).
- Class names should be CamelCased.
- Single letter variable should be limited to loop indexes.
- One single statement per line
- Two empty lines between top-level objects, only one later.

`PEP 7 <https://www.python.org/dev/peps/pep-0007/>`_: Style Guide for C Code

Presenter Notes
...............

PEP : python enhancement proposal
Why PEP ? :

- insure code homogeneity
- insure readability
- insure maintenance / avoid some classical errors

----

Zen of Python: `PEP20 <https://www.python.org/dev/peps/pep-0020/>`_
...................................................................

.. code-block:: python

   import this

::

 Beautiful is better than ugly.
 Explicit is better than implicit.
 Simple is better than complex.
 Complex is better than complicated.
 Flat is better than nested.
 Sparse is better than dense.
 Readability counts.
 Special cases aren't special enough to break the rules.
 Although practicality beats purity.
 Errors should never pass silently.
 Unless explicitly silenced.
 In the face of ambiguity, refuse the temptation to guess.
 There should be one-- and preferably only one --obvious way to do it.
 Although that way may not be obvious at first unless you're Dutch.
 Now is better than never.
 Although never is often better than *right* now.
 If the implementation is hard to explain, it's a bad idea.
 If the implementation is easy to explain, it may be a good idea.
 Namespaces are one honking great idea -- let's do more of those!

----

Tools
-----

* `flake8 <https://pypi.python.org/pypi/flake8>`_
* `pylint <https://www.pylint.org/>`_
* `modernize <https://pypi.python.org/pypi/modernize>`_
* `autopep8 <https://pypi.python.org/pypi/autopep8>`_
* `landscape.io <https://landscape.io/>`_: `Example <https://landscape.io/github/silx-kit/silx/>`_
* IDE

  - `pyDev (eclipse) <http://www.pydev.org/>`_
  - `pyCharm <https://www.jetbrains.com/pycharm/>`_
