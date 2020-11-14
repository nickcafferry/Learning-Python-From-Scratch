.. _label26:
Chapter 26: Class Coding Basics
========================================

.. raw:: html
   :file: Chapter26.html

.. code:: python
   
   >>> class FirstClass:             # Define a class object
   ...   def setdata(self,value):    # Define class methods
   ...      self.data = value        # self is the instance
   ...   def display(self):          
   ...      print(self.data)         # self.data: per instance

   >>> x = FirstClass()              # Make two instances
   >>> y = FirstClass()              # Each is a new namespace
   
   >>> x.setdata("King Arthur")      # Call methods: self is x
   >>> y.setdata(3.14159)            # Runs: FirstClass setdata(y,3.14159)
   
   >>> x.display()
   King Arthur
   >>> y.display()
   3.14159
   >>> x.data = "New value"
   >>> y.display()
   New value
   
   >>> x.anothername = "spam"
