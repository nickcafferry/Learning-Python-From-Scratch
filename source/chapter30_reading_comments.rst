Designing with Classes
======================

The previous chapter focuses on using Python's OOP, the class. But OOP is also about design issues, i.e., how to use classes to model useful objects.

Python and OOP
-------------

Python's implementation of OOP can be summarized by three ideas:


- **Inheritance**
  
  :strong:`Inheritance is based on attribute lookup in Python (in X.name expressions)`
  

- **Polymorphism**

  :strong:`In X.method, the meaning of method depends on the type(class) of X.`
  
- **Encapsulation**

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

OOP and Inheritance: "Is a" Relationships
---------------------------------------

To illustrate, let’s put that pizza-making robot we talked about at the start of this part of the book to work. Suppose we’ve decided to explore alternative career paths and open a pizza restaurant. One of the first things we’ll need to do is hire employees to serve customers, prepare the food, and so on. Being engineers at heart, we’ve bdecided to build a robot to make the pizzas; but being politically and cybernetically correct, we’ve also decided to make our robot a full-fledged employee with a salary. Our pizza shop team can be defined by the four classes in the example file, employees.py. The most general class, Employee, provides common behavior such as bumping up salaries (giveRaise) and printing (__repr__). There are two kinds of employees, and so two subclasses of Employee: Chef and Server. Both override the inherited work method to print more specific messages. Finally, our pizza robot is modeled by an even more specific class:PizzaRobot is a kind of Chef,which is a kind of Employee. In OOP terms, we call these relationships “is-a” links:a robot is a chef, which is a(n) employee. Here’s theemployees.py file:

.. code:: python

    >>> class Employee:
    ...     def __init__(self, name, salary =0):
    ...         self.name = name
    ...         self.salary = salary
    ...     def giveRaise(self, percent):
    ...         self.salary = self.salary+(self.salary*percent)
    ...     def work(self):
    ...         print(self.name, "does stuff")
    ...     def __repr__(self):
    ...         return "<Employee: name=%s, salary = s%>" %(self.name, self.salary)
    >>> class Chef(Employee):
    ...     def __init__(self,name):
    ...         Employee.__init__(self, name, 50000)
    ...     def work(self):
    ...         print(self.name, "makes food")
    >>> class Server(Employee):
    ...     def __init__(self,name):
    ...         Employee.__init__(self, name, 40000)
    ...     def work(self):
    ...         print(self.name, "interfaces with customer")
    >>> class PizzaRobot(Chef):
    ...     def __init__(self, name):
    ...         Chef.__init__(self, name)
    ...     def work(self):
    ...         print(self.name, "makes pizza")
    >>> if __name__ == "__main__":
    ...     bob = PizzaRobot("bob")
    ...     print(bob)
    ...     bob.work()
    ...     bob.giveRaise(0.20)
    ...     print(bob); print()
    ...     for klass in Employee, Chef, Sever, PizzaRobot:
    ...         obj = klass(klass.__name__)
    ...         obj.work()
    
