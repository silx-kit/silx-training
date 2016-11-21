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

.. code-block:: bash

    >>> What is your name ?
    polo
    >>> How old are you ? 
    22
    >>> Your name is polo and you are 22 years old


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

Exercise
^^^^^^^^

    write into a file :
        - your name
        - the current date
        
    read the month of the date only using the functions given by the file object (the one returned by open(...))


----

Solution - writing
^^^^^^^^^^^^^^^^^^

.. code-block:: python

    f=open('myoutputfile', mode='w')
    f.write('Henri\n')
    import datetime
    f.write(str(datetime.datetime.now()))
    f.close()

----


Solution - reading
^^^^^^^^^^^^^^^^^^

.. code-block:: python

    f=open('myoutputfile', mode='r')
    # read the first line
    firstline=f.readline()
    # read the year
    year=f.read(4)
    # read the date separator (-)
    f.read(1)
    # read the month
    month=f.read(2)
    print("month is %s"%month)
    f.close()


----

Exercise
^^^^^^^^

- Read an ascii spreadsheet written by fit2d:
    - The first non commented line looks like:
        - 512 512 Start pixel = ( 1 1 )
    - Then 512 values per line, 512 lines
    - Read the file as a list of lists
    - Example file in : data/example.spr



    .. image:: img/fit2d_ascii_file.png
        :width: 700px
        :height: 400px


----

Solution
^^^^^^^^

.. code-block:: python

    def readspr(filepath):
        "Read a fit2d ascii spread file"
        if not os.path.isfile(filepath):
            print("No such file %s"%filepath)
            return None
        
        result=[]
        xsize=0
        ysize=0
        lines=open(filepath, 'r').readlines()
        for idx, line in enumerate(lines):
            strippedline=line.strip()
            # if this is a commented line
            if strippedline.startswith('#'):
                continue
                
            words=strippedline.split()
            if(len(words)==8) and (words[2:6]==["Start", "pixel", "=", "("]):
                xsize=int(words[0])
                ysize=int(words[1])
                print("Dimensions of the size are (%s, %s)" %(xsize, ysize))
                break
                
        if xsize is not None and ysize is not None:
            for line in lines[idx+1:]:
                words=line.split()
                if len(words) != xsize:
                    print("Error !!! Expected entries are %s, got %s"%(xsize, len(words)))
                    return None
                else:
                    result.append([float(i) for i in words])
                
        return result



Solution - The same reading bytes
^^^^^^^^

.. code-block:: python

    def readspr_b(filepath):
        "Read a fit2d ascii spread file"
        if not os.path.isfile(filepath):
            print("No such file %s"%filepath)
            return None
        
        result=[]
        xsize=0
        ysize=0
        lines=open(filepath, 'rb').readlines()
        for idx, line in enumerate(lines):
            strippedline=line.decode('utf-8').strip()
            # if this is a commented line
            if strippedline.startswith('#'):
                continue

            words=strippedline.split()
            if (len(words)==8) and (words[2:6]==["Start", "pixel", "=", "("]):
                xsize=int(words[0])
                ysize=int(words[1])
                print("Dimensions of the size are (%s, %s)"%(xsize, ysize))
                break
                
        if xsize is not None and ysize is not None:
            for line in lines[idx+1:]:
                words=line.decode('utf-8').split()
                if len(words) != xsize:
                    print("Error !!! Expected entries are %s, got %s"%(xsize, len(words)))
                    return None
                else:
                    result.append([float(i) for i in words])
                
        return result
