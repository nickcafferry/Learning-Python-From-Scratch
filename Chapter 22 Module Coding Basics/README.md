# Chapter 22: Module Coding Basics

In a word, Python modules are easy to create and easy to use, user-friendly.

## Module Creation

To define a module, simply edit some Python code into a text file, and then save it with '.py' extension; any such file is automatically considered a Python module. For instance, if you type the following `def` statement into a file called `module1.py` and import it, you are creating an object with one attribute-the name `printer`, which happens to be a reference to a fucntion object.

```python
def printer(x):
  print(x)
```

## import and from Equivalence

Basically, a from statement like this one:

```python
from module import name1, name2 # Copy these two names
```
is equivalent to this statement sequence:

```python
import module # Fetch the module object
name1 = module.name1 # Copy names out by assignment
name2 = module.name2
del module          # Get rid of the module name
```

When we use the `from *` form of this statement (`from module import *`), the equivalence, but all the top-level names in the module are copied over to the importing scope this way.
