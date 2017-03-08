
Fat binaries
------------

Standalone self-contained applications or installers.

- Include Python interpreter and all dependencies.
- Fits Windows and Mac OS X application distribution, as unlike Linux they lack a dependency management tools.

Beware:

- Fat binaries are fat.
- You are redistributing (many) other people work, so take care about licences.

------

Freezing
........

There is a number of tools to 'freeze' a Python application for distribution from an installation on a computer.

Principle:

- Analyze a script to find its dependencies (i.e., its imports).
- Collect all dependencies and python interpreter in a directory.
- Add a launcher and eventually bundle every thing in a single file or installer.

Issues:

- Analysis can miss some hidden imports.
- All runtime dependencies must be included (including external libraries wrapped by Python packages).
- Data files cannot be guessed and need to be explicitly added.

Test on a different computer.

------

Tools
.....

- `PyInstaller <http://www.pyinstaller.org/>`_: Cross-platform
- `cx_Freeze <http://cx-freeze.readthedocs.org/>`_: Cross-platform
- `py2app <https://pythonhosted.org/py2app/>`_: Mac OS X

\ 

- `Platypus <http://www.sveinbjorn.org/platypus>`_: Mac OS X
- `pynsist <https://pypi.python.org/pypi/pynsist>`_: Windows
- `py2exe <https://pypi.python.org/pypi/py2exe/>`_: Windows
- `bbFreeze <https://pypi.python.org/pypi/bbfreeze>`_: Windows, Linux
- `pex <https://github.com/pantsbuild/pex>`_: Linux, Mac OS X

------

PyInstaller
...........

`PyInstaller <http://www.pyinstaller.org/>`_ is a command line tool to freeze Python scripts into executables.

Its goal is to integrate specific stuff for 3rd-party packages (e.g., PyQt, matplotlib) and Windows Runtime.

It is cross-platform.

------

PyInstaller QuickStart
......................

How-to make an application from a script:

- Install the Python of your choice and the script dependencies.
- Install PyInstaller: ``pip install PyInstaller``
- Run: ``pyinstaller <script>.py``
- It performs the analysis of the script, and creates a ``dist/<script>`` directory with all the required files to run the script.

PyInstaller options:

- ``--onefile`` to make a single .exe file instead of a directory.
- ``--windowed`` to hide the console for GUI scripts.

------

PyInstaller
...........

On Windows:

- Result is in ``dist/<script>``
- Then you can use a tool such as `NSIS <http://nsis.sourceforge.net/>`_ to create an installer from the directory.

.. On Mac OS X:
   
   - Always create a command line executable.
   - With ``--windowed`` create a Mac Application (i.e., ``.app``).

------

PyInstaller
...........

Limitations:

- It might include useless packages.
- It might miss some dependencies, some external file resources...

It uses a ``*.spec`` to configure the build, which can be tuned.
See `doc <http://pythonhosted.org/PyInstaller/>`_.

------

cx_Freeze
.........

`cx_Freeze <http://cx-freeze.readthedocs.org/>`_ extends ``distutils``.

It is cross-platform.

Install ``cx_Freeze``: ``pip install cx_Freeze``.

------

cx_Freeze
.........

cx_setup.py:

.. code-block:: python

   from cx_Freeze import setup, Executable

   build_exe_options = {
       'packages': [],
       'includes': [],
       'excludes': [],
       'include_files': []
   }

   if sys.platform == 'win32':
       build_exe_options['include_msvcr'] = True

   base = 'Win32GUI' if sys.platform == 'win32' else None

   setup(name='my_app',
         version='0.1',
         options={
             'build_exe': build_exe_options,
             'bdist_dmg': {'applications-shortcut': True}
         },
         executables=[Executables('my_app.py', base=base)])

------

cx_Freeze
.........

First install your package and its dependencies.

On Windows, run ``python cx_setup.py build_exe`` to build a directory with all required files.
Then create an installer with a tool such as `NSIS <http://nsis.sourceforge.net/>`_.

On Mac OS X, run ``python cx_setup.py bdist_dmg`` to build a .dmg with an .app included.

------

py2app
......

MAC OS X specific *freezing* tool.

py2app_setup.py:

.. code-block:: python

  from setuptools import setup

  setup(app=['my_app_script.py'],
        setup_requires=['py2app'],
        options={'py2app': {
            'argv_emulation': True,
            'packages': [],  # List of packages
            'iconfile': 'icon_file.icns',
        }}
  )

Run ``python py2app_setup.py py2app`` to build an application bundle ``.app`` in ``dist/``.

------

Mac Application Bundle
......................

A Mac OS X application (``.app``) is a directory also called an *application bundle*.

It contains::

  App.app/
      Contents/
          Info.plist  -> Bundle configuration file (XML)
          MacOS/      -> Contains the executable file
          Resources/  -> Application resources
          Frameworks/ -> frameworks: dynamic libraries and there resources
          ...

See `bundle doc <https://developer.apple.com/library/mac/documentation/CoreFoundation/Conceptual/CFBundles/BundleTypes/BundleTypes.html>`_.

------

Sum-up
......

Different tools to freeze.

Main issue: Making sure it is standalone and include everything required.

