# Introducing Python Object Types

From a more concrete persoective, Python programs can be decomposed into modules, statements, expressions, and objects, as follows:

1. Programs are composed of modules.

2. Modules contain statements.

3. Statements contain expressions.

4. Expressions create and process objects.

## Why Use Built-in Types?

* Built-in objects make programs easy to write.

* Built-in objects are components of extensions.

* Built-in objects are often more efficient than custom data structures.

* Built-in objects are a standard part of the language.

Make programming easier and more powerful and efficient than most of what can be created from scratch. 

## Python's Core Data Types

Object type                        Example literals/creation

Numbers                            1234, 3.1415, 3+4j, Decimal, Fraction 

Strings                            'Spam', "guido's", b'a\x01c'

Lists                              [1,[2,'three'], 4]

Dictionaries                       {'food': 'spam', 'taste': 'yum'}

Tuples                             (1, 'spam', 4, 'U')

Files                              myfile = open('eggs','r')

Sets                               set('abc'), {'a','b','c'}

Other core types                   Booleans, types, None

Program unit types                 Functions, modules, classes (Part 4, Part 5, Part 6)

Implementation-related types       Compiled code, stack tracebacks (Part 4, Part 7)

Just as importantly, once you create an object, you bind its operation set for all time--you can perform only string operations on a string and list operations on a list. As you'll learn, Python is dynamically typed (it keeps track of types for you automatically instead of requiring declaration code), but it is also strongly typed (you can perform on an object only operations that are valid for its type)

