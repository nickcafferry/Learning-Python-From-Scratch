:strong:`Class Coding Basics`
==============================

Three primary distinctions::
	
	- Generating mutiple objects
	
	- Namespaces inheritance
	
	- Operator overloading
	

Classes Generate Multiple Instance Objects
-------------------------------------------


Two kinds of objects in Python's OOP model: :title-reference:`class objects` and :title-reference:`instace objects`::
	
	- class objects provide default behavior and serve as factories for instance objects
	
	- instance objects are the real objects your programs process -- each is a namespace in its own right, but inherits
	(i.e., has automatic access to)
	

Class Objects Provide Default Behavior
----------------------------------------

Rundown of the main properties of :title-reference:`Python` classes::
	
	- The class statement createds a class object and assigns it a name.
	- Assignement inside class statements make class attributes.
	- Class attributes provide object state and behavior. 
	
Instance Objects Are Concrete Items
-----------------------------------

key points behind class instances::
	
	- Calling a class object like a function makes a new instance object.
	- Each instance object inherits class atrributes and gets its own namespace.
	- Assignments to attributes of self in methods make per-instance attributes.
	

To begin, let's define a class named FirstClass by running a Python class statement interactively:

.. code:: python
	
	>>> class FirstClass:             # Define a class object
	... 	def setdata(self, value): # Define class methods
	...			self.data = value     # self is the instance
	...		def display(self):
				print(self.data) 	  # self.data: per instance

.. code:: python

	>>> def FirstFunction:
	...		data = 0
	...		def setdata(value):
	...			nonlocal data
	...			data = value
	...			return data
	...		def display():
	...			print(data)

.. hint::
	In fact, any name assigned at the top level of the class's nested block becomes an attribute
	of the class.
	

.. important::
	Classes and instances are linked namespace objects in a class tree that is searched by inheritance.
	
.. code:: python

	>>> class FirstClass:
	...		def setdata(self, value):
	...			self.data = value
	...		def display(self):
	...			print(self.data)
	>>> x.setdata("King Arthur") # Call methods: self is x
	>>> y.setdata(3.14159)       # Runs: FirstClass.setdata(y, 3.14159)
	
.. Danger:: 
	Within a method, :italic:`self`--the name given to the leftmost argument by convention--automatically
	refers to the instance' namespaces, not the class's (that's how the data names in Figure 26-1 are created).
	

:strong:`By redefining attributes in subclasses that appear lower in the hierarchy, we override the more general definitions of those attributes higher in the tree.`

.. literalinclude:: Chapter26_Class_Coding_Basics.py
   :language: python
   :linesno: 
