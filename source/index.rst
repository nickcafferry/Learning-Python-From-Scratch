|Documentation Status| |MIT License| |Python version| |today|

-------------------

.. |Documentation Status| image:: https://readthedocs.org/projects/learning-python-from-scratch/badge/?version=latest
   :target: https://learning-python-from-scratch.readthedocs.io/en/latest/?badge=latest
.. |MIT License| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat
   :target: http://choosealicense.com/licenses/mit/
.. |Python version| image:: https://img.shields.io/badge/python-3.7,3.8-brightgreen.svg
   :target: https://www.python.org/

Copyright |copy| Wei MEI, |MLMS (TM)| |---|
all rights reserved. 
|bamboo|

.. |copy| unicode:: 0xA9 .. copyright sign
.. |MLMS (TM)| unicode:: MLMS U+2122
   .. with trademark sign
.. |---| unicode:: U+02014 .. em dash
   :trim:

.. |bamboo| unicode:: 0x1F024 .. bamboo

Learning Python From Scratch (version : |version|)
============================

Learning Python From Scratch ::
   How to learn python from scratch. Python is a popular open source programming language used for both standalone programs and scripting applications. Free, portable, powerful, and easy to learn, and fun to use are what make python outstanding among many programming language. This repository is to bring you quickly up to speed on the fundamentals of the core Python language. 


.. important::

   - :ref:`Chapter 1: Getting Started <label1>` And that concludes the hype portion of this book. In this chapter, we’ve explored some of the reasons that people pick Python for their programming tasks. We’ve also seen how it is applied and looked at a representative sample of who is using it today. My goal is to teach Python, though, not to sell it. The best way to judge a language is to see it in action, so the rest of this book focuses entirely on the language details we’ve glossed over here.
   
   - :ref:`Chapter 2: How Python Runs Programs <label2>` This chapter introduced the execution model of Python (how Python runs your programs) and explored some common variations on that model (just-in-time compilers and the like). Although you don’t really need to come to grips with Python internals to write Python scripts, a passing acquaintance with this chapter’s topics will help you truly understand how your programs run once you start coding them. In the next chapter, you’ll start actually running some code of your own. First, though, here’s the usual chapter quiz.
   
   - :ref:`Chapter 3: How You Run Programs <label3>` In this chapter, we’ve looked at common ways to launch Python programs: by running code typed interactively, and by running code stored in files with system command lines, file-icon clicks, module imports, exec calls, and IDE GUIs such as IDLE. We’ve covered a lot of pragmatic startup territory here. This chapter’s goal was to equip you with enough information to enable you to start writing some code, which you’ll do in the next part of the book. There, we will start exploring the Python language itself, beginning with its core data types.
   
   - :ref:`Chapter 4: Introducing Python Object Types <label4>` And that’s a wrap for our concise data type tour. This chapter has offered a brief introduction to Python’s core object types and the sorts of operations we can apply to them. We’ve studied generic operations that work on many object types (sequence operations such as indexing and slicing, for example), as well as type-specific operations available as method calls (for instance, string splits and list appends). We’ve also defined some key terms, such as immutability, sequences, and polymorphism.
   
   - :ref:`Chapter 5: Numeric Types <label5>` This chapter has taken a tour of Python’s numeric object types and the operations we can apply to them. Along the way, we met the standard integer and floating-point types, as well as some more exotic and less commonly used types such as complex numbers, fractions, and sets. We also explored Python’s expression syntax, type conversions, bitwise operations, and various literal forms for coding numbers in scripts.
   
   - :ref:`Chapter 6: The Dynamic Typing Interlude <label6>` This chapter took a deeper look at Python’s dynamic typing model—that is, the way that Python keeps track of object types for us automatically, rather than requiring us to code declaration statements in our scripts. Along the way, we learned how variables and objects are associated by references in Python; we also explored the idea of garbage collection, learned how shared references to objects can affect multiple variables, and saw how references impact the notion of equality in Python.
   
   - :ref:`Chapter 7: Strings <label7>` In this chapter, we took an in-depth tour of the string object type. We learned about coding string literals, and we explored string operations, including sequence expressions, string method calls, and string formatting with both expressions and method calls. Along the way, we studied a variety of concepts in depth, such as slicing, method call syntax, and triple-quoted block strings. We also defined some core ideas common to a variety of types: sequences, for example, share an entire set of operations.
   
   - :ref:`Chapter 8: Lists and Dictionaries <label8>` In this chapter, we explored the list and dictionary types—probably the two most common, flexible, and powerful collection types you will see and use in Python code. We learned that the list type supports positionally ordered collections of arbitrary objects, and that it may be freely nested and grown and shrunk on demand. The dictionary type is similar, but it stores items by key instead of by position and does not maintain any reliable left-to-right order among its items. Both lists and dictionaries are mutable, and so support a variety of in-place change operations not available for strings: for example, lists can be grown by append calls, and dictionaries by assignment to new keys.
   
   - :ref:`Chapter 9: Tuples, Files, and Everything Else <label9>` This chapter explored the last two major core object types—the tuple and the file. We learned that tuples support all the usual sequence operations, have just a few methods, and do not allow any in-place changes because they are immutable. We also learned that files are returned by the built-in open function and provide methods for reading and writing data. We explored how to translate Python objects to and from strings for storing in files, and we looked at the pickle and struct modules for advanced roles (object serialization and binary data). Finally, we wrapped up by reviewing some properties common to all object types (e.g., shared references) and went through a list of common mistakes (“gotchas”) in the object type domain.
   
   - :ref:`Chapter 10: Introducing Python Statements <label10>` That concludes our quick look at Python statement syntax. This chapter introduced the general rules for coding statements and blocks of code. As you’ve learned, in Python we normally code one statement per line and indent all the statements in a nested block the same amount (indentation is part of Python’s syntax). However, we also looked at a few exceptions to these rules, including continuation lines and single-line tests and loops. Finally, we put these ideas to work in an interactive script that demonstrated a handful of statements and showed statement syntax in action.
   
   - :ref:`Chapter 11: Assignments, Expressions, and Prints <label11>` In this chapter, we began our in-depth look at Python statements by exploring assignments, expressions, and print operations. Although these are generally simple to use, they have some alternative forms that, while optional, are often convenient in practice: augmented assignment statements and the redirection form of print operations, for example, allow us to avoid some manual coding work. Along the way, we also studied the syntax of variable names, stream redirection techniques, and a variety of common mistakes to avoid, such as assigning the result of an append method call back to a variable.
   
   - :ref:`Chapter 12: if Tests and Syntax Rules <label12>` In this chapter, we studied the Python if statement. Additionally, because this was our first compound and logical statement, we reviewed Python’s general syntax rules and explored the operation of truth tests in more depth than we were able to previously. Along the way, we also looked at how to code multiway branching in Python and learned about the if/else expression introduced in Python 2.5.
   
   - :ref:`Chapter 13: while and for Loops <label13>` In this chapter, we explored Python’s looping statements as well as some concepts related to looping in Python. We looked at the while and for loop statements in depth, and we learned about their associated else clauses. We also studied the break and continue statements, which have meaning only inside loops, and met several built-in tools commonly used in for loops, including range, zip, map, and enumerate (although their roles as iterators in Python 3.0 won’t be fully uncovered until the next chapter).
   
   - :ref:`Chapter 14: Iterations and Comprehensions, Part 1 <label14>` In this chapter, we explored concepts related to looping in Python. We took our first substantial look at the iteration protocol in Python—a way for nonsequence objects to take part in iteration loops—and at list comprehensions. As we saw, a list comprehension is an expression similar to a for loop that applies another expression to all the items in any iterable object. Along the way, we also saw other built-in iteration tools at work and studied recent iteration additions in Python 3.0.
   
   - :ref:`Chapter 15: The Documentation Interlude <label15>` This chapter took us on a tour of program documentation—both documentation we write ourselves for our own programs, and documentation available for built-in tools. We met docstrings, explored the online and manual resources for Python reference, and learned how PyDoc’s help function and web page interface provide extra sources of documentation. Because this is the last chapter in this part of the book, we also reviewed common coding mistakes to help you avoid them.
   
   - :ref:`Chapter 16: Function Basics <label16>` This chapter introduced the core ideas behind function definition—the syntax and operation of the def and return statements, the behavior of function call expressions, and the notion and benefits of polymorphism in Python functions. As we saw, a def statement is executable code that creates a function object at runtime; when the function is later called, objects are passed into it by assignment (recall that assignment means object reference in Python, which, as we learned in Chapter 6, really means pointer internally), and computed values are sent back by return. We also began exploring the concepts of local variables and scopes in this chapter, but we’ll save all the details on those topics for Chapter 17. First, though, a quick quiz.
   
   - :ref:`Chapter 17: Scopes <label17>` In this chapter, we studied one of two key concepts related to functions: scopes (how variables are looked up when they are used). As we learned, variables are considered local to the function definitions in which they are assigned, unless they are specifically declared to be global or nonlocal. We also studied some more advanced scope concepts here, including nested function scopes and function attributes. Finally, we looked at some general design ideas, such as the need to avoid globals and cross-file changes.
   
   - :ref:`Chapter 18: Arguments <label18>` In this chapter, we studied the second of two key concepts related to functions: arguments (how objects are passed into a function). As we learned, arguments are passed into a function by assignment, which means by object reference, which really means by pointer. We also studied some more advanced extensions, including default and keyword arguments, tools for using arbitrarily many arguments, and keyword-only arguments in 3.0. Finally, we saw how mutable arguments can exhibit the same behavior as other shared references to objects—unless the object is explicitly copied when it’s sent in, changing a passed-in mutable in a function can impact the caller.
   
   - :ref:`Chapter 19: Advanced Function Topics <label19>` This chapter took us on a tour of advanced function-related concepts: recursive functions; function annotations; lambda expression functions; functional tools such as map, filter, and reduce; and general function design ideas. The next chapter continues the advanced topics motif with a look at generators and a reprisal of iterators and list comprehensions—tools that are just as related to functional programming as to looping statements. Before you move on, though, make sure you’ve mastered the concepts covered here by working through this chapter’s quiz.
   
   - :ref:`Chapter 20: Iterations and Comprehensions, Part 2 <label20>` This chapter wrapped up our coverage of built-in comprehension and iteration tools. It explored list comprehensions in the context of functional tools and presented generator functions and expressions as additional iteration protocol tools. As a finale, we also measured the performance of iteration alternatives, and we closed with a review of common function-related mistakes to help you avoid pitfalls. This concludes the functions part of this book. In the next part, we will study modules—the topmost organizational structure in Python, and the structure in which our functions always live. After that, we will explore classes, tools that are largely packages of functions with special first arguments. As we’ll see, user-defined classes can implement objects that tap into the iteration protocol, just like the generators and iterables we met here. Everything we have learned in this part of the book will apply when functions pop up later in the context of class methods.
   
   - :ref:`Chapter 21: Modules: The Big Picture <label21>` In this chapter, we covered the basics of modules, attributes, and imports and explored the operation of import statements. We learned that imports find the designated file on the module search path, compile it to byte code, and execute all of its statements to generate its contents. We also learned how to configure the search path to be able to import from directories other than the home directory and the standard library directories, primarily with PYTHONPATH settings. As this chapter demonstrated, the import operation and modules are at the heart of program architecture in Python. Larger programs are divided into multiple files, which are linked together at runtime by imports. Imports in turn use the module search path to locate files, and modules define attributes for external use. Of course, the whole point of imports and modules is to provide a structure to your program, which divides its logic into self-contained software components. Code in one module is isolated from code in another; in fact, no file can ever see the names defined in another, unless explicit import statements are run. Because of this, modules minimize name collisions between different parts of your program.
   
   - :ref:`Chapter 22: Module Coding Basics <label22>` This chapter delved into the basics of module coding tools—the import and from statements, and the reload call. We learned how the from statement simply adds an extra step that copies names out of a file after it has been imported, and how reload forces a file to be imported again without stopping and restarting Python. We also surveyed namespace concepts, saw what happens when imports are nested, explored the way files become module namespaces, and learned about some potential pitfalls of the from statement.
   
   - :ref:`Chapter 23: Module Packages <label23>` This chapter introduced Python’s package import model—an optional but useful way to explicitly list part of the directory path leading up to your modules. Package imports are still relative to a directory on your module import search path, but rather than relying on Python to traverse the search path manually, your script gives the rest of the path to the module explicitly. As we’ve seen, packages not only make imports more meaningful in larger systems, but also simplify import search path settings (if all cross-directory imports are relative to a common root directory) and resolve ambiguities when there is more than one module of the same name (including the name of the enclosing directory in a package import helps distinguish between them). Because it’s relevant only to code in packages, we also explored the newer relative import model here—a way for imports in package files to select modules in the same package using leading dots in a from, instead of relying on an older implicit package search rule.
   
   - :ref:`Chapter 24: Advanced Module Topics <label24>` This chapter surveyed some more advanced module-related concepts. We studied data hiding techniques, enabling new language features with the __future__ module, the __name__ usage mode variable, transitive reloads, importing by name strings, and more. We also explored and summarized module design issues and looked at common mistakes related to modules to help you avoid them in your code.
   
   - :ref:`Chapter 25: OOP: The Big Picture <label25>` We took an abstract look at classes and OOP in this chapter, taking in the big picture before we dive into syntax details. As we’ve seen, OOP is mostly about looking up attributes in trees of linked objects; we call this lookup an inheritance search. Objects at the bottom of the tree inherit attributes from objects higher up in the tree—a feature that enables us to program by customizing code, rather than changing it, or starting from scratch. When used well, this model of programming can cut development time radically.
   
   - :ref:`Chapter 26: Class Coding Basics <label26>` This chapter introduced the basics of coding classes in Python. We studied the syntax of the class statement, and we saw how to use it to build up a class inheritance tree. We also studied how Python automatically fills in the first argument in method functions, how attributes are attached to objects in a class tree by simple assignment, and how specially named operator overloading methods intercept and implement built-in operations for our instances (e.g., expressions and printing).
   
   - :ref:`Chapter 27: A More Realistic Example <label27>` In this chapter, we explored all the fundamentals of Python classes and OOP in action, by building upon a simple but real example, step by step. We added constructors, methods, operator overloading, customization with subclasses, and introspection tools, and we met other concepts (such as composition, delegation, and polymorphism) along the way. In the end, we took objects created by our classes and made them persistent by storing them on a shelve object database—an easy-to-use system for saving and retrieving native Python objects by key. While exploring class basics, we also encountered multiple ways to factor our code to reduce redundancy and minimize future maintenance costs. Finally, we briefly previewed ways to extend our code with application-programming tools such as GUIs and databases, covered in follow-up books.
   
   - :ref:`Chapter 28: Class Coding Details <label28>` This chapter took us on a second, more in-depth tour of the OOP mechanisms of the Python language. We learned more about classes, methods, and inheritance, and we wrapped up the namespace story in Python by extending it to cover its application to classes. Along the way, we looked at some more advanced concepts, such as abstract superclasses, class data attributes, namespace dictionaries and links, and manual calls to superclass methods and constructors.
   
   - :ref:`Chapter 29: Operator Overloading <label29>` That’s as many overloading examples as we have space for here. Most of the other operator overloading methods work similarly to the ones we’ve explored, and all are just hooks for intercepting built-in type operations; some overloading methods, for example, have unique argument lists or return values. We’ll see a few others in action later in the book. In addition, some of the methods we’ve studied here, such as __call__ and __str__, will be employed by later examples in this book. For complete coverage, though, I’ll defer to other documentation sources—see Python’s standard language manual or reference books for details on additional overloading methods.
   
   - :ref:`Chapter 30: Designing with Classes <label30>` In this chapter, we sampled common ways to use and combine classes to optimize their reusability and factoring benefits—what are usually considered design issues that are often independent of any particular programming language (though Python can make them easier to implement). We studied delegation (wrapping objects in proxy classes), composition (controlling embedded objects), and inheritance (acquiring behavior from other classes), as well as some more esoteric concepts such as pseudoprivate attributes, multiple inheritance, bound methods, and factories.
   
   - :ref:`Chapter 31: Advanced Class Topics <label31>` This chapter presented a handful of advanced class-related topics, including subclassing built-in types, new-style classes, static methods, and decorators. Most of these are optional extensions to the OOP model in Python, but they may become more useful as you start writing larger object-oriented programs. As mentioned earlier, our discussion of some of the more advanced class tools continues in the final part of this book; be sure to look ahead if you need more details on properties, descriptors, decorators, and metaclasses.
   
   - :ref:`Chapter 32: Exception Basics <label32>` And that is the majority of the exception story; exceptions really are a simple tool. To summarize, Python exceptions are a high-level control flow device. They may be raised by Python, or by your own programs. In both cases, they may be ignored (to trigger the default error message), or caught by try statements (to be processed by your code). The try statement comes in two logical formats that, as of Python 2.5, can be combined—one that handles exceptions, and one that executes finalization code regardless of whether exceptions occur or not. Python’s raise and assert statements trigger exceptions on demand (both built-ins and new exceptions we define with classes); the with/as statement is an alternative way to ensure that termination actions are carried out for objects that support it.
   
   - :ref:`Chapter 33: Exception Coding Details <label33>` In this chapter, we took a more detailed look at exception processing by exploring the statements related to exceptions in Python: try to catch them, raise to trigger them, assert to raise them conditionally, and with to wrap code blocks in context managers that specify entry and exit actions. So far, exceptions probably seem like a fairly lightweight tool, and in fact, they are; the only substantially complex thing about them is how they are identified. The next chapter continues our exploration by describing how to implement exception objects of your own; as you’ll see, classes allow you to code new exceptions specific to your programs. Before we move ahead, though, let’s work though the following short quiz on the basics covered here.
   
   - :ref:`Chapter 34: Exception Objects <label34>` In this chapter, we explored coding user-defined exceptions. As we learned, exceptions are implemented as class instance objects in Python 2.6 and 3.0 (an earlier string-based exception model alternative was available in earlier releases but has now been deprecated). Exception classes support the concept of exception hierarchies that ease maintenance, allow data and behavior to be attached to exceptions as instance attributes and methods, and allow exceptions to inherit data and behavior from superclasses. We saw that in a try statement, catching a superclass catches that class as well as all subclasses below it in the class tree—superclasses become exception category names, and subclasses become more specific exception types within those categories. We also saw that the built-in exception superclasses we must inherit from provide usable defaults for printing and state retention, which we can override if desired.
   
   - :ref:`Chapter 35: Designing with Exceptions <label35>` This chapter wrapped up the exceptions part of the book with a survey of related statements, a look at common exception use cases, and a brief summary of commonly used development tools. This chapter also wrapped up the core material of this book. At this point, you’ve been exposed to the full subset of Python that most programmers use. In fact, if you have read this far, you should feel free to consider yourself an official Python programmer. Be sure to pick up a t-shirt the next time you’re online.
   
   - :ref:`Chapter 36: Unicode and Byte Strings <label36>` This chapter explored advanced string types available in Python 3.0 and 2.6 for processing Unicode text and binary data. As we saw, many programmers use ASCII text and can get by with the basic string type and its operations. For more advanced applications, Python’s string models fully support both wide-character Unicode text (via the normal string type in 3.0 and a special type in 2.6) and byte-oriented data (represented with a bytes type in 3.0 and normal strings in 2.6). In addition, we learned how Python’s file object has mutated in 3.0 to automatically encode and decode Unicode text and deal with byte strings for binary-mode files. Finally, we briefly met some text and binary data tools in Python’s library, and sampled their behavior in 3.0.
   
   - :ref:`Chapter 37: Managed Attributes <label37>` This chapter covered the various techniques for managing access to attributes in Python, including the __getattr__ and __getattribute__ operator overloading methods, class properties, and attribute descriptors. Along the way, it compared and contrasted these tools and presented a handful of use cases to demonstrate their behavior.
   
   - :ref:`Chapter 38: Decorators <label38>` In this chapter, we explored decorators—both the function and class varieties. As we learned, decorators are a way to insert code to be run automatically when a function or class is defined. When a decorator is used, Python rebinds a function or class name to the callable object it returns. This hook allows us to add a layer of wrapper logic to function calls and class instance creation calls, in order to manage functions and instances. As we also saw, manager functions and manual name rebinding can achieve the same effect, but decorators provide a more explicit and uniform solution.
   
   - :ref:`Chapter 39: Metaclasses <label39>` In this chapter, we studied metaclasses and explored examples of them in action. Metaclasses allow us to tap into the class creation protocol of Python, in order to manage or augment user-defined classes. Because they automate this process, they can provide better solutions for API writers then manual code or helper functions; because they encapsulate such code, they can minimize maintenance costs better than some other approaches. Along the way, we also saw how the roles of class decorators and metaclasses often intersect: because both run at the conclusion of a class statement, they can sometimes be used interchangeably. Class decorators can be used to manage both class and instance objects; metaclasses can, too, although they are more directly targeted toward classes.

-------------


.. raw:: html

    <div class="zzsc-content">
	         <canvas id="clock1_" width="200px" height="200px">
	         </canvas>
    </div>

    <script src="https://www.html5tricks.com/demo/html5-canvas-15-clock/js/canvas_clock.js"></script>
    <script>
    	  clockd1_={
    			  "indicate": true,
    			  "indicate_color": "#222",
    			  "dial1_color": "#666600",
    			  "dial2_color": "#81812e",
    			  "dial3_color": "#9d9d5c",
    			  "time_add": 1,
    			  "time_24h": true,
    			  "date_add":3,
    			  "date_add_color": "#999",
    			 };
    	  var c = document.getElementById('clock1_');
    	  cns7_ = c.getContext('2d');
    
    	  clock_dots(200,cns7_,clockd1_);
    
    </script>


Table of Content
====


.. raw:: html
   :file: introduction.html


.. toctree::
   :maxdepth: 5
   :caption: Preface
   
   preface

.. toctree::
   :maxdepth: 3
   :caption: Getting Started
   
   getting_started


.. toctree::
   :maxdepth: 5
   :caption: Types and operations
   
   types_and_operations


.. toctree::
   :maxdepth: 5
   :caption: Statements and syntax
   
   statements_and_syntax


.. toctree::
   :maxdepth: 5
   :caption: functions
   
   functions


.. toctree::
   :maxdepth: 5
   :caption: modules
   
   modules


.. toctree::
   :maxdepth: 5
   :caption: classes and oop
   
   classes_and_oop


.. toctree::
   :maxdepth: 5
   :caption: exceptions and tools
   
   exceptions_and_tools


.. toctree::
   :maxdepth: 5
   :caption: advanced topics
   
   advanced_topics


.. toctree::
   :maxdepth: 5
   :caption: Appendixes
   
   Appendixes

.. toctree::
   :maxdepth: 3
   :caption: index
   
   index_last

License
==============

See `MIT LICENSE <https://github.com/nickcafferry/tensorflow/blob/master/LICENSE>`_

