Classes
=======

Classes are used for Object Oriented Programming, they are out of the scope.

Definition
----------

.. code-block:: python

    class Myclass2(Myclass1):
        "Simple class inheriting from Myclass1"
        def __init__(self, param):
            Myclass1.__init__(self)
            self.param = param

        def mymethod(self):
            print('value of my param is: %s'% self.param)


Instantiation
-------------

.. code-block:: python

    # creation of a new class instance
    >>>c2 = MyClass2(2)
    # access to a class method
    >>>c2.mymethod()
    value of my param is: 2
    # access to a class attribute
    >>>c2.param
    2
    >>>isinstance(c2, MyClass2) # check the class of an object
    True
