class C2:
	pass
class C3:
	pass
class C1(C2, C3):
	print("passing")

class C1(C2, C3):
	"""
	If a class wants to guarantee that an attribute like name is always set in its instances,
	it more typically will fill out the attribute at construction time, like this:
	"""
	def __init__(self, who): # Set name when constructed
		self.name = who 
I1 = C1("bob")
I2 = C1("mel")
print(I1.name, I2.name)

"""
The __init__ method is known as the constructor because of when it is run. It's the most commonly
used representative of a larger class of methods called operator overloading methods, 
"""

""" The definition of operator overloading methods:
Such methods are inherited in class trees as usual and have double underscores at the start and end
of their names to make them distinct. Python runs them automatically when instances that support them
appear in the corresponding operations, and they are mostly an alternative to using simple method calls.
They're also optional: if omitted, the operations are not supported.
pattern: __xxxx__

"""

class test:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __setattr__(self, name, value):
		#self.name1 = name1
		#self.name2 = name2
		self.__dict__[name] = value
		object.__setattr__(self, name, value)
		object.__init__
		return self.__dict__[name]#, object.name
t1 = test(3,5)
t1.z = 23
print(t1.x, t1.y, t1.z)
print(dir(object.__setattr__))

"""
As an example, suppose you're assigned the task of implementing an employee database application.
As a Python OOP programmer, you might begin by coding a general superclass that defines default
behavior common to all the kinds of employees in your organization:
"""
class Employee:   # General superclass
	def computeSalary(self): # Common or default behavior
		pass
	def giveRaise(self):
		pass
	def promote(self):
		pass
	def retire(self):
		pass
"""
That is, you can code subclasses that customize just the bits of behavior that differ per employee type
the rest of the employee types' behavior will be inherited from the more general class. For example,
if engineers have a unique salary computation rule(i.e., not hours times rate), you can replace just that
one method in a subclass.
"""
class Engineer(Employee):
	def computeSalary(self):
		pass

"""
Because the computeSalary version here appears lower in the class tree, it will replace (override) the general
verison in Employee. You then create instances of the kinds of employee classes that the real employees belong to,
to get the correct behavior.
"""
bob = Employee()
mel = Engineer()

"""
when you later ask for these employees' salaries, they will be computed according to the classes from which the
objects were made, due to the principles of the inheritance search
"""
company = [bob, mel]  # A composite object
for emp in company:
	print(emp.computeSalary()) # Run this object's version
	


"""
This is yet another instance of the idea of polymorphism introduced in Chapter 4 and revisited in Chapter 16.
Recall that polymorphism means that the meaning of an operation depends on the object being 
operated on. Here, the method computeSalary is located by inheritance search in each object before it is called.
In other applications, polymorphism might also be used to hide(i.e., encapsulate) interface differences. For example,
a program that processes data streams might be coded to expect objects with input and output methods, without caring
what those methods actually do:
"""
def processor(reader, converter, writer):
	while 1:
		data = reader.read()
		if not data: break
		data = converter(data)
		writer.write(data)

class Reader:
	def read(self): pass  # Default behavior and tools
	def other(self): pass
class FileReader(Reader):
	def read(self): pass  # Read from a local file
class SocketReader(Reader):
	def read(self): pass # Read from a network socket

#processor(FileReader(), Converter, FileWriter())
#processor(SocketReader(), Converter, TapeWriter())
#proceesor(FtpReader(), Converter, XmlWriter())

"""
Inheritance hierarchy

Note that company list in this example could be stored in a file with Python object pickling, introduced
in Chapter 9 when we met files, to yield a persistent employee database. Python also comes with a module 
named shelve, which would allow you to store the pickled representation of the class instances in an access-
by-key filesystem; the third-party open source ZODB system does the same but has better support for production-
quality object-oriented databases.
"""

"""
Programming in such an OOP world is just a matter of combining and specializing already debugged code by writing
subclasses of your own
"""
"""
Objects at the bottom of the tree inherit attributes from objects higher up in the tree-a feature that enables us to
program by customizing code, rather than changing it, or starting from scratch.
"""

"""
2. Where does an inheritance search look for an attribute?
An inheritance search looks for an attribute first in the instance object, then in the class the instance was created
from, then in all higher superclasses, progressing from the bottom to the top of the object
tree, and from left to right (by default). The search stops at the first place the attribute is found. Because the lowest
version of a name found along the way wins, class hiearchies naturally support customization by extension.

3. What is the difference between a class object and an instance object?
Both class and instance objects are namespace(package of variablee that appear as attributes). The main difference between
is that classes are a kind of factory for creating multiple instances. Classes also support operator overloading methods,
which instances inherit, and treat any functions nested within them as special methods for processing instances.

4. Why is the first argument in a class method function special?
The first argument in a class method function is special because it always receives the instance object that is the implied
subject of the method call. It's usually called self by convention. Because method functions always have this implied subject
object context by default, we say they are "object-oriented" --i.e., designed to process or change objects.

5. What is the __init__ method used for?
If the __init__ method is coded or inherited in a class, Python calls it automatically each time an instance of that class is
created. It's known as the constructor method; it is passed the new instance implicitly, as well as any arguments passed explicitly
to the class name. It's also the most commonly used operator overloading method. If no __init__ method is present, instances simply 
begin life as empty namespaces.

6. How do you create a class instance?
You create a class instance by calling the class name as though it were a function; any arguments passed into the class name show up
as arguments two and beyond in the __init-_ constructor method. The new instance remembers the class it was created from for inheritance
purposes.

8. How do you specify a class's superclasses?
You specify a class's superclasses by listing them in parentheses in the class statement, after the new class's name. The left-to-right
order in which the classes are listed in the parentheses gives the left-to-right inheritance search order in the class tree,

"""
