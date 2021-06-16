Designing with Classes
======================

The previous chapter focuses on using Python's OOP, the class. But OOP is also about design issues, i.e., how to use classes to model useful objects.

Python and OOP
-------------

Python's implementation of OOP can be summarized by three ideas:


- :caption:`Inheritance`
  
  :strong:`Inheritance is based on attribute lookup in Python (in X.name expressions)`
  

- :caption:`Polymorphism`

  :strong:`In X.method, the meaning of method depends on the type(class) of X.`
  
- :caption:`Encapsulation`

  :strong:`Methods and operators implement behavior; data hiding is a convention by default`
  
  
  Overloading by Call Signatures (or Not)
  ---------------------------------------
  
  Some OOP languages also define polymorhism to mean :emphasis:`overloading functions based on the type signatures of their arguments`.
  But because there are no type declarations in Python, this concept doesn't really apply; :strong:`Polymorhism in Python is based on object interfaces, not types`
  
.. code:: python

    >>> class C:
    ...     def meth(self,x):
    ...       return x + x
    ...     def meth(self, x, y, z):
    ...       return x + y + z
    >>> kda = C(); kad = C()
    >>> print(kda.meth(2), kad.meth(2,3,4))
    TypeError: meth() missing 2 required positional arguments: 'y' and 'z'
