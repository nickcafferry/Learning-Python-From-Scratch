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
