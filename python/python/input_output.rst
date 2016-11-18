Input and output
================

----

File (1)
--------

Opening a file
^^^^^^^^^^^^^^

How to open a file ?
    .. code-block:: python

        f=open(filename, mode='r')

modes can be: 
    - “r” for read-only mode
    - “w” for write mode
    - “a” for append mode
    - “+” for read+write mode
    - “b” for binary mode (disable encoding handling)


Common methods for all file objects:
    - seek(pos) → Moves to a given position in the file
    - f.close() → close the file    


----

File (2)
--------


Writing into a file
^^^^^^^^^^^^^^^^^^^

- file.write(str) → write a string to the file
- file.writelines([list of strings]) → write multiple lines
- file.flush() → write (actually) the data to the disk


Reading from a file
^^^^^^^^^^^^^^^^^^^

- file.read(size) → read size bytes or the whole file in a string
- file.readlines() → read the whole file in a list of lines
- file.readline() → read the next line

----

File (3)
--------

File as iterator
^^^^^^^^^^^^^^^^

Files can behave as iterators over readlines

    .. code-block:: python
        
        for oneLine in open('myoutputfile'):
            print(oneLine)

    will display:
        first line
        second line
        ...

- Very concise typing
    - efficient reading 
    - limited memory footprint 
    - file is not fully loaded in memory: only one line


---- 


Interaction with the console
----------------------------

- Output to the console:
    - print(str) used to be a statement (now function behaviour is enforced)
    - sys.stdout is a file: <open file '<stdout>', mode 'w' at 0x7f63919fe150>
    - sys.stdout.write(str+os.linesep) equivalent to print(str)

- Stdin, stdout and stderr are just opened files …

- Input from the console:
    - input() reads the standard input and returns a string (raw_input in python2)
    - input(prompt)  equivalent to eval(raw_input(prompt))
    - sys.stdin is a file open in read mode:
    - <open file '<stdin>', mode 'r' at 0x7f63919fe0c0>
    - eval('5+6') evaluates a string representing python code DANGEROUS !!! 

----

Exercise
--------

Create a programme wich ask for the name and the age and then display it

----

Solution
--------

.. code-block:: python

    def questioner():
        print("What is your name ?")
        name=input()
        print("How old are you ? ")
        age=input()
        print("Your name is %s and you are %s years old" % (name, age))

----

TODO : deplacer cette splide

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

Exercise
^^^^^^^^

    Read an ascii file
    TODO


----

TODO : Parler des differences python2 / python3 pour les strings

Python2         Python3
string (default)    →   bytes
unicode     →   string (default) 

