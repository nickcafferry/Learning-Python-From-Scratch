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
 
 
 
