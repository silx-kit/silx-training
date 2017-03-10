
Virtual environments for Python
===============================


----

What is a virtual environment
-----------------------------

Virtual Python environment.

Each can have a different version of Python, and a different set of libraries.

Lightweight (not as many duplicated libraries as fat binaries).


----


Purposes
--------

- Users and production servers:

  - installing new software with modern library dependencies, without breaking older software relying on older versions of the same libraries
  - ensuring your installed libraries don't interfere with other users' libraries, when sharing a workstation and a user account
  - running applications created for different versions of Python

- Developers:

  - testing installer scripts (are all necessary dependencies installed on a blank system?)
  - testing that your software works with different sets of libraries (e.g PyQt4, PyQt5, PySide), or different versions of a single library

Using virtualenv for testing is fine for a few specific tests and for prototyping, but in the long term this goal is better achieved with *continuous integration*.


----

Installing:
-----------

Python 2
********

.. code-block:: shell
    
    pip install virtualenv --user

Python 3
********

Already shipped as a standard library (Python > 3.3): ``venv``

----

Creating a virtualenv
---------------------

This will create a new directory ``myvenv`` in the current directory.

Python 2
*********

.. code-block:: shell
    
    virtualenv myvenv


Python 3
*********

.. code-block:: shell
    
    python3 -m venv myvenv

.. note::

    This fails on Debian 8 and some Ubuntu versions due to a broken ``pyvenv``.

    Alternative using Python 2's virtualenv:

    .. code-block:: shell
    
        # pip install virtualenv --user
        virtualenv --python=/usr/bin/python3.4 myvenv

    Alternative by installing pip separately from ``myvenv``:

    .. code-block:: shell
    
        python3 -m venv --without-pip myvenv
        source myvenv/bin/activate
        # download and install setuptools and pip from source packages

----

Activating a virtual env
------------------------

.. code-block:: shell
    
    source myvenv/bin/activate

While this virtual environment is active:

    - the command ``python`` calls the python installed in ``myvenv``, and it is not aware of user libraries outside the environment.
    - the command ``pip`` installs new libraries  inside the environment

To deactivate the environment later, use the following command:

.. code-block:: shell

    deactivate


----
        
Upgrade pip, setuptools and wheel
---------------------------------

This step ensures that you will be able to install modern software and libraries, if your Python 2 version is outdated.

.. code-block:: shell

   python -m pip install --upgrade pip
   pip install setuptools --upgrade
   pip install wheel --upgrade

    
----

Installing libraries
--------------------

Let's install *silx* and its dependencies.

.. FIXME: export all_proxy="http://proxy.xxxx.fr:xxxx/"   (why is this needed? Else, error: "Missing dependencies for SOCKS support.")

Some dependencies can simply be installed from pypi:

.. code-block:: shell

    pip install numpy cython
    pip install matplotlib fabio h5py qtconsole pyopencl mako


PyQt5 wheels are provided for some Python version (OK for Python 3.5 & 3.6):

.. code-block:: shell

    pip install PyQt5

----

Symbolic link to library (linux)
--------------------------------

If no PyQt wheel is available for your environment, it can be complicated to compile it from scratch.

A "simple" solution is to create a symbolic link in the environment's library path, pointing to a PyQt version already installed on the system.

Python 2.7
**********

.. code-block:: shell

    ln -s /usr/lib/python2.7/dist-packages/PyQt4 myvenv/lib/python2.7/site-packages/
    ln -s /usr/lib/python2.7/dist-packages/sip.so myvenv/lib/python2.7/site-packages/


Python 3.4
**********

.. code-block:: shell

    ln -s /usr/lib/python3/dist-packages/PyQt4 myvenv/lib/python3.4/site-packages/
    ln -s /usr/lib/python3/dist-packages/sip.cpython-34m-x86_64-linux-gnu.so myvenv/lib/python3.4/site-packages/


----

Installing silx
---------------

Distribution
************

.. code-block:: shell

    pip install silx

From sources
************

.. code-block:: shell

    cd /path/to/silx
    pip install .

Run tests
*********

.. code-block:: python

    >>> import silx.test
    >>> silx.test.run_tests()







