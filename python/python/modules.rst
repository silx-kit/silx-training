=======
Modules
=======

----

Create libraries with your functions.

.. warning:: Start each new python file with the following lines : 

    .. code-block:: python

        #!/usr/bin/env python
        # coding: utf8


----

.. image:: img/mylibrary.png
    :width: 550px
    :height: 620px

----

..note :: 
    
    ':param', ':type',  etc can be used for
    formatting documentation using automatic documentation generators like : 
    

- Sphinx ( http://www.sphinx-doc.org/en/1.4.8/ )
- Epydoc ( https://pypi.python.org/pypi/epydoc/ )


----

import
------

There is many ways to import modules / from module

    .. code-block:: python

        import mymodule
        mymodule.myfunction()
        
        import mymodule as module
        module.myfunction()

        from mymodule import pow2
        pow2()

        # ! import all from a module can be dangerous because
        # it will polutes the local name-space
        from mymodule import *      
        pow2()
        anyfunction()


You can also access to the attributes of the module

    .. code-block:: python

        import mymodule
        mymodule.__authors__
        mymodule.__doc__


----

Standard modules
----------------
    
"Batteries included philosophy"

.. image:: img/mylibrary.png
    :width: 50px
    :height: 120px
    :align: right


