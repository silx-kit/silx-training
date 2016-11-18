Functions
=========

----

Definition
----------

use the 'def' statement to define a new function

    .. code-block:: python

        def myfunction(myparam):
            print('my parameter is %s' % myparam)

Documentation    
-------------

.. image:: img/documentationOfAFunction.png
    :width: 600px
    :height: 200px


----


Hands on
--------

Write a function that takes a, b and c as imput and return the list of solutions for:
    :math:`{a.x^2}+b.x+c=0`

----

Solution
--------

Definition of the function :

    .. code-block:: python

        import math
        def polynom(a, b, c):
        delta=b*b - 4.0*a*c
        solutions=[]
        if delta > 0 :
            solutions.append(b+math.sqrt(delta) / (2.0*a))
            solutions.append(b-math.sqrt(delta) / (2.0*a))
        elif delta == 0 :
            solutions.append(b/(2.0*a))
        return solutions


Call of the function : 

    .. code-block:: python

        solution(1, 2, -3)

----

function parameter (1)
----------------------

- optional parameters

    .. code-block:: python

        def myfunction(myparam=5):
            print('my parameter is %s' % myparam)

    
    - myfunction() return my parameter is 5
    - myfunction('toto') return my parameter is toto

- any parameters

    - The parameter preceded by a star is a list containing all un-named arguments 
    - The parameter preceded by two stars is a dictionary  containing all named arguments 


----

function parameter (2)
----------------------

    Example of a function with 'any parameters' 

    .. code-block:: python

        def myfunction(r, n=12, *arglist, **argdict):
            print('r param = %s' %r)
            print('n param = %s' %n)
            if len(arglist) > 0:
                print('got %s unnamed argument ' %len(arglist))
                for arg in arglist :
                    print('- %s' % arg)
            if len(argdict) > 0:
                print('got %s named argument ' %len(argdict))
                for key in argdict :
                    print('- name = %s , value = %s ' % (key, argdict[key]))
            

    .. image:: img/function_anyparameteroutput.png
        :width: 600px
        :height: 200px


----

function parameter (2)
----------------------


.. warning:: Never use mutable object as default parameter !!!

    If the parameter is a mutable, is default value should generally be None (immutable)

    .. image:: img/functionwithmutabledefaultparam.png
        :width: 500px
        :height: 250px
        :align: center


----


lambda function
---------------


You can defined function 'on the fly' :

    .. code-block:: python

        pow2 = lambda x: x*x

