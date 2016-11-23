Exceptions
==========

----

Definition
----------

- Syntax errors are checked before actual execution
- Any other error are called exceptions:

    .. image:: img/exceptionsoutput.png
        :width: 500px
        :height: 400px

- ZeroDivisionError, NameError, TypError are all exceptions

----


Catching exceptions
-------------------

code to deal with exceptions

    .. code-block:: python

        try:
            ...
        except(TypeError, ExceptionXXX...):
            what to do if those exception appears
        else:
            executed if no error found


Exceptions are classes:

- Plenty of exceptions are available (ImportError, RuntimeError, ...)
- You can create your own exceptions
    - This is out of the scope of this training

Raise exception:

    .. code-block:: python

        raise Exception('My personal message')