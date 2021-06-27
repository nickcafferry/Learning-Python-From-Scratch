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

To illustrate, let’s put that pizza-making robot we talked about at the start of this part of the book to work. Suppose we’ve decided to explore alternative career paths and open a pizza restaurant. One of the first things we’ll need to do is hire employees to serve customers, prepare the food, and so on. Being engineers at heart, we’ve bdecided to build a robot to make the pizzas; but being politically and cybernetically correct, we’ve also decided to make our robot a full-fledged employee with a salary. Our pizza shop team can be defined by the four classes in the example file, employees.py. The most general class, Employee, provides common behavior such as bumping up salaries (giveRaise) and printing (__repr__). There are two kinds of employees, and so two subclasses of Employee: Chef and Server. Both override the inherited work method to print more specific messages. Finally, our pizza robot is modeled by an even more specific class: PizzaRobot is a kind of Chef,which is a kind of Employee. In OOP terms, we call these relationships “is-a” links:a robot is a chef, which is a(n) employee. Here’s theemployees.py file:

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
    
    <Employee: name=bob, salary = 50000>
    bob makes pizza
    <Employee: name=bob, salary = 60000.0>

    Employee does stuff
    Chef makes food
    Server interfaces with customer
    PizzaRobot makes pizza

Stream Processors Revisited
-----------------------------

For a more realistic composition example, recall the generic data stream processor function we partially coded in the introduction to OOP in Chapter 25:

.. code:: python

  >>> def processor(reader, converter, writer):
          while 1:
              data = reader.read()
              if not data: break
              data = converter(data)
              writer.write(data)
 
Rather than using a simple function here, we might code this as a class that uses composition to do its work to provide more structure and support inheritance. The following file, ```streams.py```, demonstrates one way to code the class:

.. code:: python

  >>> class Processor:
      def __init__(self, reader, writer):
          self.reader = reader
          self.writer = writer
      def processor(self):
          while 1:
              data = self.reader.readline()
              if not data: break
              data = self.converter(data)
              self.writer.write(data)
      def converter(self,data):
          assert False, "converter must be defined" # Or raise exception


Why You Will Care: Classes and Persistence
--------------------------------------------

I’ve mentioned pickling a few times in this part of the book because it works especially well with class instances. For example, besides allowing us to simulate real-world interactions,the pizza shop classes developed here could also be used as the basis of a
persistent restaurant database.Instances of classes can be stored away on disk in a single step using Python’s pickle or shelve modules. The object pickling interface is remarkably easy to use:

.. code:: python

  >>> import pickle
  >>> class Employee:
  ...  def __init__(self, name, salary =0):
  ...      self.name = name
  ...      self.salary = salary
  ...  def giveRaise(self, percent):
  ...      self.salary = self.salary+(self.salary*percent)
  ...  def work(self):
  ...      print(self.name, "does stuff")
  ...  def __repr__(self):
  ...      return "<Employee: name=%s, salary = %s>" %(self.name, self.salary)
  >>> class Chef(Employee):
  ...  def __init__(self,name):
  ...      Employee.__init__(self, name, 50000)
  ...  def work(self):
  ...      print(self.name, "makes food")
  >>> class Server(Employee):
  ...  def __init__(self,name):
  ...      Employee.__init__(self, name, 40000)
  ...  def work(self):
  ...      print(self.name, "interfaces with customer")
  >>> class PizzaRobot(Chef):
  ...  def __init__(self, name):
  ...      Chef.__init__(self, name)
  ...  def work(self):
  ...      print(self.name, "makes pizza")
  >>> if __name__ == "__main__":
  ...  bob = PizzaRobot("bob")
  ...  sara = Server("sara")
  ...  nick = Chef("nick") 
  ...  tony = Employee("tony")
  ...  print(bob)
  ...  bob.work()
  ...  bob.giveRaise(0.20)
  ...  print(bob); print()
  ...  for klass in Employee, Chef, Server, PizzaRobot:
  ...      obj = klass(klass.__name__)
  ...      obj.work()
  ...  print("---------------------------------")
  ...  with open("1.pickle", "wb") as file:
  ...      pickle.dump((sara,nick,tony,bob),file)

  ...  with open("1.pickle", "rb") as file:
  ...      obj = pickle.load(file)
  ...  print(obj)

params are parameter names and "python" is value and if there are many parameters, just use "&" between two parameters.

.. code:: python

  >>> import requests
  >>> r = requests.get("https://www.baidu.com/s?wd=python")
  >>> url = "https://www.baidu.com/s"
  >>> params = {"wd": "python"}
  >>> r = requests.get(url, params=params)
  >>> print(r.url)
  
Chapter 25. OOP：The Big Picture
---------------------------------

So far in this book, we’ve been using the term “object” generically. Really, the code written up to this point has been object-based—we’ve passed objects around our scripts, used them in expressions, called their methods, and so on. For our code to qualify as being truly object-oriented (OO), though, our objects will generally need to also participate in something called an inheritance hierarchy.

.. literalinclude:: text.py
   :language: python
   :linesnos:

