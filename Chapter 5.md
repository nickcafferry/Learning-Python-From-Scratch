## Chapter 5---Numeric Types

A Complete inventory of Python's numeric toolbox includes:
* Integers and floating-point numbers
* Complex numbers
* Fixed-precision decimal numbers
* Rational fraction numbers
* Sets
* Booleans
* Unlimited integer precision
* A variety of numeric built-ins and modules

## Preview: Operator overloading and polymorphism

Python itself automatically overloads some operators to perform different actions depending on the type of built-in objects being processed.

The + operator performs addition when dealing with numbers but does concatenation when dealing with sequence objects such as strings and lists. This is usually called polymorphism.

## Variables and Basic Expressions

* Variables refer to objects and are created when assigned values, do need to be declared ahead of time

* When used in expression (normally this is done before being assigned), variables are replaced with their values

## Hexadecimal,Octal, and Binary Notation

* 0o1,0o20,0o377 # Octal literals
* 0x01,0x10,0xFF # Hex literals
* 0b1,0b10000,0b11111111 # Binary literals

hex(64) == Ox40, bin(64) == 0b100000

The eval function, which you'll meet later in this book, treats strings as Python code. 

