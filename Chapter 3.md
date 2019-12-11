 # Chapter Summary
 Several common ways to launch Python programs:
 
 1. Runing codes interactively using Python prompt.
 
 2. Runing codes typed in files with system command lines.
 
 3. File-icon clicks
 
 4. Module imports
 
 5. 'exec' calls.
 
 6. IDE GUIs such as IDIE.
 
 Tips: If you really want to force Python to run the file in the same session without stopping and restarting the session, you need to instead call the reload function available in the imp standard library module (this function is also a simple built-in Python 2.6, but not in 3.0)
 The reload function expects the name of an already loaded module object, so you have to have successfully imported a module once before reloading it.
 'reload' is a function that is called, and thereby should come with a parentheses around the module object name. 'import' is a statement. 
 
Modules serve the role of libraries of tools, and it is just a package of variable names, known as a namespace. The variable names within a module are called attributes.In the broader sheme of things, an attribute is simply a variable name that is attached to a specific object (like a module).
 
What makes from different from import?
From is just like an import, with an extra assignment to names in the importing component. Technically, 'from' copies a module's attributes, such that they become simple variables in the recipient-thus, you can simply refer to the imported string this time as title (a variable) instead of myfile.title (an attribute reference).

When the dir function is called with the name of an imported module passed in parentheses like this, it returns all the attributes inside that module. Some of the names it returns are names you get 'for free': names with leading and trailing double underscores are built-in names that are always predefined by Python and that have special meaning to the interpreter.

Because each file is a self-contained namespace,the names in one file cannot clash with those in another, even if they are spelled the same way.
 
 Useful tips:
 import versus from: I should point out that the from statement in a sense defeats the namespace partitioning purpose of modules--because the from copies variables from one file to another, it can cause same-named variables in the importing file to be overwritten (and won't warn you if it does). This essentially collapses namespaces together, at least in terms of the copied variables.
 
 
