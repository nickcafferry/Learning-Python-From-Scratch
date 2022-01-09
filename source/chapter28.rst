.. _label28:
Chapter 28: Class Coding Details
========================================

As in C++. the class statement is Python's main OOP tool, but unlike in C++, Python's class is not a declaration. Like a def, a class statement is an object builder, and an implicit assignemnt-when run, it generates a class object and stores a reference to it in the name used in the header. when ru, your class exist.

The main distinction for classes is that :strong:`their namespaces are also the basis of inheritance in a class or instance object are fetched from other classes`.

:italic:`All the statements inside the class statement run when the class statement itself runs (not when the class is later called to make an instance). Assigning names inside the class statement makes class attributes, and nested defs make class methods, but other assignments make attributes, too.`

.. code:: python

   >>> classs <name> (superclass, ...):
            data = value
            def method(self,...):
               self.member = value

.. raw:: html
   :file: Chapter28.html
