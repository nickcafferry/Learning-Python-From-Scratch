Chapter 21 Modules: The Big Picture
-----------------------------------

Python module, the highest-level program organization unit, will be discussed in depth
in this chapter. In concrete terms, modules usually correspond to Python program files.
Modules are processed with two statements and one important function:

`import`:     
       
 Lets a client (or importer) fetch a module as a whole

`from`:
      
 Allows clients to fetch some particular units from a module
   
`imp.reload`:
      
 Provides a way to reload a module without stopping Python
   
Since Chapter 3 introduced module basics before and we've been using them ever since, this chapter will expand on __core module concepts__ and more __advanced module usage__.
The first chapter offers an overlook at role of modules in overall program structure.

When stepping through this chapter, you'll learn about `reloads`, the `__name__` and 
`__all__` attributes, package imports, relative import syntax, and so on. 


## Why Use Modules?
Modules usually serve as self-contained packages of variables known as namespaces. 
Ultimately, Python's modules allow us to link individual files into a larger program 
system.

Modules have at least three roles from an abstract perspective:

`Code reuse`: 
      
 One of basic implementations is that you can save code in files permanently. 
 
 `System namespace partitioning`:
 
 Modules are also the highest-level program organization unit in Python. Essentially, 
 they are just packages of names. Module is just the guy who can group system components
 
 `Implementing shared services or data`:
 
 From an operational perspective, modules are very helpful when it comes to embedding 
 a large object into a module. This object will be usually shared by many clients.
 
 ## Python Program Architecture
 
The complexity of Python programs might be underestimated by you because of my description of Python programs. In reality, programs usually involve more than just one file. At the end of day, you will certainly wind up using external files that someone else has already written.
 
This section introduces the general architecture of Python programs - the way you divide a program into a collection of source files (a.k.a modules). You baiscally need to link parts into a whole. 

## How to Structure a Program

Basically, a Python program consist of two parts. One is _top_level_ file, which contains the main flow of your program-this is the file you run to launch your application. The other is zero or more supplemental files, which we usally name _modules_ in Python. The module files are libraries of tools used to collect compoents
used by the top-level file(and possibly elsewhere). In a word, top-level files use tools defined in module files, and modules use tools defined in other modules.

## Imports and Attributes

A more concrete example will be given. Suppose that the file a.py is chosen to be the top-leve file, it will be a simple text file of statments, which is executed from top to bottom when launched. Both file b.py and file c.py are modules. 

`b.py`

```python
def spam(text):
    print(text,'spam')
```

`a.py`

```python
import b
b.spam('gumby')
```

The object.attribute notation is used through Python scripts.
 
## Standard Library Modules

Python automatically comes with a large collection of utility modules known as the standard library. This collection has roughly 200 modules large at last count, contains platform-independent support for common programming tasks: operating system interfaces, object persistence, text pattern matching, network and Internet scripting, GUI construction.

## How Imports Work

So far in this book, the author hasn't explained what happens when you are importing modules. Let's make it a little bit more concerete. 

Some C programmers like to compare the Python module import operation to a C `#include`. They really shouldn't. In Python, imports are not just textual insertions of one file into another. They are really runtime operations that will perform 3 distinct steps:
1. Find the module's file;
2. Compile it to byte code (if needed);
3. Run the module's code to build the objects it defines.

Just bear in mind that all three of these steps are carried out only the first time a module is imported during a program's execution; later imports will bypass all of three steps and simply fetch the already loaded module object in memory. Technically, Python does this by sorting loaded modules in a table named sys.modules and checking there at start of an import operation.

1. Find It
Python will locate the module file referenced by an import statement. Python uses a standard module search path to locate the module file corresponding to an import statement.

2. Compile It (Maybe)
After finding a source code file that matches an import statement by traversing the module search path, Pytho next compiles it to byte code, if necessary. 

Python will check the file timestamps and if the byte code file is older than the source file, automatically regeneratres the byte code when the program is run. In addition, if Python only find the .pyc file without the source file, it simply loads the byte code directly (this means you can ship a program as just byte code files and don't necessarily need source file). In other words, the compile step is bypassed if possible to speed program startup.

Top-level files are oftern designed to be executed directly and not imported at all.

3. Run It

The final step is to execute the byte code generated in step 2. As mentioned before, the byte code file '.pyc' is necessary for execution and even without the source file '.py', the program can run smoothly.

Python keeps already imported modules in the built-in `sys.modules` and you can always keep track of what's been loaded. And a single command `list(sys.modules.keys())` will print all the imported modules, including built-ins and standard library.

