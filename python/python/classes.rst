Classes
=======

Classes are out of the scope of the training ( used for Object Oriented approach)

Definition
----------

    .. code-block:: python
    
        class Myclass2(Myclass1):
            "Simple class heriting from Myclass1"
            def __init(self, param):
                Myclass1.__init__()
                self.param=param

            def mymethod(self):
                print('value of my param is : %s'% self.param)


Instanciation
-------------
    .. code-block:: python

        # creation of a new class instance
        c2=myclass2(2)
        # access to a class method
        c2.mymethod()
        # access to a class atribute
        c2.param
        # check the class of an object
        isinstance(c2, Myclass2)

