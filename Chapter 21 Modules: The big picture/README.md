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

`Code reuse`
      One of basic implementations is that you can save code in files permanently. 
