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

.. On MacOS:
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
