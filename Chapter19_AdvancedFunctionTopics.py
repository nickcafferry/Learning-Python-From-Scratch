# -*- coding: utf-8 -*-
#!/usr/local/bin/python
from Color import *
def HASH(s):
	L = '# '
	L = L + s
	if len(L) < 78:
		L = L + (78-len(L))*' '
	else:
		print('The length of the string given is no smaller than 78')
	L = L + '#'
	return L

printYellowRed(u'Advanced Funciton Topics\n')
printBlue(u'--------------------------------------------------------------------------------\n')

printDarkSkyBlue(u'This chapter introduces a collection of more advanced fucntion-related topics: recursive functions, function attributes and annotations, the lambda expression, and functional programming tools such as map and filter.\n')
print(u'\r')

printBlue(u'The interactions between functions are very important and some general funciton design priniciples will be explored here. More advanced function-related topics like generator functions and expressions, for instance will be discussed later in Chapter 20.\n')
print(u'\r')

printWhiteBlack(u'Function Design Concepts\n')
printSkyBlue(u'--------------------------------------------------------------------------------')
printRed(u'###############################################################################\n')
print(HASH('* Coupling: Arguments for inputs and return for outputs.'))
print(HASH('* Coupling: Minimise usage of global variables.'))
print(HASH('* Coupling: Do not change mutable arguments arbitraryly.'))
print(HASH('* Cohesion: one single, unified purpose per function.'))
print(HASH('* Size: The smaller, simpler, the better.'))
print(HASH('* Coupling: Avoid direct change of variables in another module file.'))
printRed(u'###############################################################################\n')

print('\r')
printYellow(u'Python class objects depend on a passed-in mutable object-class functions set attributes of an automatically passed-in argument called self to change per-object state information.And if classes are not used, global variables are supposed to be used if truly necessary.\n')
print('\r')

printPink(u'-------------------------------------------------------------------------------\n')
print(HASH('class func(): '))
print(HASH('   def __init__(self, name, number): '))
print(HASH('      self.name = name'))
print(HASH('      self.number = number'))
print(HASH('   def iteration(self,a):'))
print(HASH('      print(self.name, self.number'))
print(HASH('      self.name = a'))
print(HASH('      self.number += 1'))
print(HASH('   def __add__(self,b): '))
print(HASH('      print(self.name, self.number)'))
print(HASH('      self.name = b'))
print(HASH('      self.number = self.number + 1'))
print(HASH("I = func('apple',0)"))
print(HASH("I.iteration('orange')"))
print(HASH("I.iteration('banana')"))
print(HASH("I.iteration('potato')"))
print(HASH("I + 'tomato'"))
print(HASH("I + 'wineapple'"))
printPink(u'--------------------------------------------------------------------------------\n')

class func():
	def __init__(self,name,number):
		self.name = name
		self.number = number
	def iteration(self,a):
		print(self.name,self.number)
		self.name = a
		self.number += 1
	def __add__(self,b):
		print(self.name,self.number)
		self.name = b
		self.number = self.number + 1
I = func('apple',0)
I.iteration('orange')
I.iteration('banana')
I.iteration('potato')
I + 'tomato'
I + 'wineapple'
print('\r')

printWhiteBlack(u'Recursive Functions\n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')

printDarkSkyBlue(u'Recursion is a somewhat advanced topic. And it is a useful technique to know about. And more importantly, it can traverse structures that have arbitrary and unpredictable shapes.\n')
print(u'\r')


printWhiteBlack_2(u'* Summation with Recursion\n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')
printSkyBlue(u'We can either use the built-in sum functions or write a more custom version of our own to sum a list (or other sequence) of numbers. \n')

printPink(u'-------------------------------------------------------------------------------\n')
print(HASH('def mysum(L): '))
print(HASH('   if not L: '))
print(HASH('      return 0'))
print(HASH('   else: '))
print(HASH('      return L[0] + mysum(L[1:])'))
print(HASH('mysum([1,2,3,4,5])'))
printPink(u'-------------------------------------------------------------------------------\n')


def mysum(L):
	if not L:
		return 0
	else:
		return L[0]+mysum(L[1:])
print(mysum([1,2,3,4,5]))
print('\r')

printSkyBlue(u'It is not that difficult to understand how these codes operate but it is very helpful to add a print of L to the function and run it again, to trace the current list at each level.\n')

printGreen(u'-------------------------------------------------------------------------------\n')
print(HASH('def mysum(L): '))
print(HASH('   if not L: '))
print(HASH('      return 0'))
print(HASH('   else: '))
print(HASH('      print(L)'))
print(HASH('      return L[0] + mysum(L[1:])'))
print(HASH('mysum([1,2,3,4,5])'))
printGreen(u'-------------------------------------------------------------------------------\n')

def mysum(L):
	if not L:
		return 0
	else:
		print(L)
		return L[0]+mysum(L[1:])
print(mysum([1,2,3,4,5]))
print('\r')

printWhiteBlack(u'Coding Alternatives\n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')

printDarkSkyBlue(u'The if/else ternary expression can be used to save some code real-estate here, hence simplifying the function.\n')
print('\r')

printGreen(u'-------------------------------------------------------------------------------\n')
print(HASH('def mysum(L): '))
print(HASH('   print(L) '))
print(HASH('   return 0 if not L else L[0] + mysum(L[1:])'))
print(HASH('print(mysum(1,2,3,4,5))'))
print(HASH('try: '))
print(HASH("   print(mysum(('s','p','a','m')))"))
print(HASH('except:'))
print(HASH("   printRed(u'mysum('s','p','a','m'))'"))
print(HASH("TypeError: can only concatenate str(not 'int') to str."))
print(HASH("try: "))
print(HASH("   print('s'+'p'+'a'+'m'+0)"))
print(HASH("except: "))
print(HASH("   printRed(u'print('s'+'p'+'a'+'m'+0)"))
print(HASH("TypeError: can only concatenate str (not 'int') to str.")) 
printGreen(u'-------------------------------------------------------------------------------\n')

def mysum(L):
	print(L)
	return 0 if not L else L[0] + mysum(L[1:])
print(mysum((1,2,3,4,5)))
try:
	print(mysum('spam'))
except:
	printRed(u"print(mysum('spam')) \nTypeError: can only concatenate str ( not 'int') to str.\n")
print('\r')

printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
printYellow(u"The codes above might not be suitable for all object types.As a matter of fact, the input object types should support '+' operand with integer. Otherwise, it will raise a TypeError: can only concatenate str (not 'int' ) to str.\n")
printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print('\r')

try:
	print(mysum(('s','p','a','m')))
except:
	printRed(u"mysum(('s','p','a','m')) \nTypeError: can only concatenate str (not 'int') to str.\n")
try:
	print('s'+'p'+'a'+'m'+0)
except:
	printRed(u"print('s'+'p'+'a'+'m'+0) \nTypeError: can only concatenate str ( not 'int') to str.\n")
print('\r')

printGreen(u'-------------------------------------------------------------------------------\n')
print(HASH('def mysum(L): '))
print(HASH('   return L[0] if len(L) == 1 else L[0] + mysum(L[1:])'))
print(HASH("print(mysum('s','p','a','m'))"))
print(HASH("mysum(['spam','ham','eggs'])"))
printGreen(u'-------------------------------------------------------------------------------\n')

def mysum(L):
	return L[0] if len(L) == 1 else L[0] + mysum(L[1:])

print(mysum(('s','p','a','m')))
print(mysum(['spam','ham','eggs']))

printGreen(u'-------------------------------------------------------------------------------\n')
print(HASH('def mysum(L): '))
print(HASH('   first,*rest = L'))
print(HASH("   return first if not rest else first + mysum(rest)"))
printGreen(u'-------------------------------------------------------------------------------\n')

def mysum(L):
	first, *rest = L
	return first if not rest else first + mysum(rest)
print(mysum((1,2,3,4,5,6)))
print(mysum(('s','p','a','m')))
print(mysum(['spam','ham','eggs']))
try:
	print(mysum([]))
except:
	printRed(u"print(mysum([])) \nValueError: not enough value to unpack (expected at least 1, got 0")
print('\r')
print('\r')

printWhiteBlack(u'Loop Statements Versus Recurison\n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')

import time
n = int(input('Please type the number n if you want to get the n th fibonacci array: '))
print('\r')

printYellowRed(u'Initializing...\n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')
S1 = '9'
S2 = '10'
for i in range(n+1):
	if i < 2:
		a = b = 1
		SUM = a = b
		if i == 1:
			printPink(u'Start generating the fibonacci number smaller than 10: \n')
			printYellow(u'###############################################################################\n')
	else:
		SUM = a + b
		a = b
		b = SUM
	if i > 0:
		print(HASH('The %d th number of a fibonacci array is %d'%(i,SUM)))
		if a + b > 9 and SUM < 10:
			printYellow(u'###############################################################################\n')
			print('\r')
			printPink(u'Start generating the fibonacci number < 100 but > 10 : \n')
			printYellow(u'###############################################################################\n')
			S1 = S1 + '9'
			S2 = S2 + '0'

		if a + b > int(S1) and SUM < int(S2):
			printYellow(u'###############################################################################\n')
			print('\r')
			printPink(u'Start generating the fibonacci number < %s0 but > %s: \n'%(S2,S2))
			printYellow(u'###############################################################################\n')
			S1 = S1 + '9'
			S2 = S2 + '0'
	time.sleep(2)
print('\n')
printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
printPink(u"Keep in mind that recursion can be direct, as in the examples so far, or indirect, as in the following (a function that calls another function, which calls back to its caller.\n")
printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print('\r')

printGreen(u'-------------------------------------------------------------------------------\n')
print(HASH('def mysum(L): '))
print(HASH('   if not L: return 0'))
print(HASH("   return nonempty(L)"))
print(HASH("def nonempty(L): "))
print(HASH("   return L[0] + mysum(L[1:])"))
printGreen(u'-------------------------------------------------------------------------------\n')

def mysum(L):
	if not L: return 0
	return nonempty(L)
def nonempty(L):
	return L[0] + mysum(L[1:])
print(mysum([1.1,2.2,3.3,4.4]))
print('\r')

printWhiteBlack(u'Handling Arbitrary Structures\n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')

printDarkSkyBlue(u'On the other hand, if you want to investigate the role of recursion in traversing arbitrarily shaped structures. Just take a look at the following example about a nested sublists structure like this: \n			[1,[2,[3,4],5],6,[7,8]]\n')
print('\r')

printGreen(u'-------------------------------------------------------------------------------\n')
print(HASH('def sumtree(L): '))
print(HASH('   tot = 0'))
print(HASH("   for x in L:"))
print(HASH("      if not isinstance(x,list):"))
print(HASH("         tot += x"))
print(HASH("      else: "))
print(HASH("         tot += sumtree(x)"))
print(HASH("   return tot"))
print(HASH("L = [1,[2,[3,4],5],6,[7,8]]"))
print(HASH("sumtree(L)"))
printGreen(u'-------------------------------------------------------------------------------\n')

def sumtree(L):
	tot = 0
	for x in L:
		if not isinstance(x,list):
			tot += x
		else:
			tot += sumtree(x)
	return tot
L = [1,[2,[3,4],5],6,[7,8]]
print(sumtree(L))

# Pathological cases
print(sumtree([1,[2,[3,[4,[5]]]]]))
print(sumtree([[[[[[1],2],3],4],5]]))

print('\r')
printYellow(u'Although we should care more about looping statements than recursion for the simplicity and efficiency of the former, we should be aware that recursion plays an important and unreplacable role in these scenarios. \n')
print('\r')

printYellow(u"Just be aware that recursion has the potential to be unexpected guy in programming. As you'll also see later in the book, some operator overloading method in classes such as __setattr__ and __getattribute__.\n")
print('\r')

printRed(sumtree.__name__+'\n')
print('\r')
printRed(str(dir(sumtree))+'\n')
print('\r')
printRed(str(dir(sumtree.__code__))+'\n')
print('\r')
printRed(str(sumtree.__code__.co_varnames)+'\n')
print('\r')
printRed(str(sumtree.__annotations__)+'\n')
print('\r')

def func(a: 'spam', b: (1,10), c: float) -> int:
	return a + b + c
print(func(1.0,2.3,4.5))
print(func.__annotations__)

for arg in func.__annotations__:
	print(arg,'=>',func.__annotations__[arg])

def func(a:'spam'=4, b: (1,10) =5, c: float =6) -> int:
	return a + b + c
print(func.__annotations__)

print('\r')
printGreen(u'-------------------------------------------------------------------------------\n')
printRed(HASH("def func(a:'spam'=4, *b: (1,10), **c: float) -> int: ")+'\n')
printRed(HASH('   return a + b + c')+'\n')
printGreen(u'-------------------------------------------------------------------------------\n')
print('\r')

def func(a:'spam'=4, *b: (1,10), **c: float) -> int:
	return a + b + c
print(func.__annotations__)

print('\r')
printSkyBlue("Annotations are a new feature in Python 3.0. They can be used to specify constraints for argument types or values and larger APIs use this features as a way to register function interface information. Chapter 39 will tell us more details about their potential application, We'll see annotations will be used as an alternative to function decorator arguments.\n")

Smartfunction = lambda x, y : x + y if x < y else x -y
print(Smartfunction(102,10))

x = lambda a = 'fee', b= 'fie', c = 'foe': a + b + c
print(x('wee'))

printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
printPink("* lambda is an expression, not a statement. A lambda expression can appear in some places where a def is not allowed to exist according to Python's syntax.\n")
print('\r')
printPink("* lambda's body is a single expression, not a block of statements. You simply type the result as a naked expression, instead of explicitly returning it.\n")
printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print('\r')

def knights():
	title = "Ser"
	action = lambda x: title + ' ' + x
	return action
act = knights()
print(act('Jorah'))

lower = lambda x,y,z: x if x < y and x < z else ( y if y < z else z)
import sys
sys.stdout.write(lower('bb','cc','aa'))
print('\r')

import sys
showall = lambda x: list(map(sys.stdout.write,x))

t = showall(['spam\n','toast\n','eggs\n'])
showallforall = lambda x: map(sys.stdout.write, x)
print(showallforall(['spam\n','toast\n','eggs\n']))

showall2 = lambda x: [sys.stdout.write(line) for line in x]
t = showall2(('bright\n','side\n','of\n','life\n'))

print('\r')
printYellow("Another common application of lambda express is to define inline callback functions for Python's tkinter GUI API\n")

print('\r')
printBlue(u'-------------------------------------------------------------------------------\n')
printRed(HASH("                  Why You Will Care: Callbacks") + '\n')
printRed(HASH("import sys")+'\n')
printRed(HASH('from tkinter import Button, mainloop')+'\n')
printRed(HASH("Button( ") + '\n')
printRed(HASH("text = 'Press me',") + '\n')
printRed(HASH(u"command=(lambda: sys.stdout.write('Spam')))")+'\n')
printRed(HASH("x.pack()")+'\n')
printRed(HASH("mainloop()")+'\n')
printBlue(u'-------------------------------------------------------------------------------\n')
print('\r')

print('\r')
printYellow("In effect, the lambda defers execution of the handler until the event occurs: the write call happens on button presses, not when the button is created.\n")

print('\r')
printBlue(u'-------------------------------------------------------------------------------\n')
printRed(HASH("class MyGui: ") + '\n')
printRed(HASH("   def makewidgets(self):")+'\n')
printRed(HASH("      Button(command=(lambda: self.onPress('spam')")+'\n')
printRed(HASH("   def onPress(self,message):") + '\n')
printRed(HASH("...use message...") + '\n')
printBlue(u'-------------------------------------------------------------------------------\n')
print('\r')

print('\r')
printWhiteBlack('Mapping Functions over Sequences: map\n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')

counters = [1,2,3,4]
updated = []
for x in counters:
	updated.append(x+10)
print(updated)

def inc(x): return x + 10
print(list(map(inc,counters)))

print('\r')
printYellow('map expects a function to be passed in, it also happens to be one of the places where lambda commonly appears\n')

def mymap(func,seq):
	res = []
	for x in seq: res.append(func(x))
	return res
print(list(map(inc,[1,2,3])))
print(mymap(inc,[1,2,3]))

print(pow(3,4))
print(list(map(pow,[1,2,3],[2,3,4])))

print('\r')
printWhiteBlack('Functional Programming Tools: filter and reduce\n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')

printRed("Map's relatives filter out items based on a test function(filter) and apply functions to pairs of items and running results(reduce).\n")

print(list(range(-5,5)))
print(list(filter((lambda x: x > 0), range(-5,5))))

res = []
for x in range(-5,5):
	if x > 0:
		res.append(x)
print(res)

printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
printPink("* some observers might also extend the functional programming toolset in Python to include lambda and list comprehensions.\n")
printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print('\r')

printYellowRed('Chapter Summary\n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')

printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
printPink("Some important concepts about advanced fucntion-related have been mentioned in this Chapter, like recursive functions,function ananotations, lambda expression functions, functional tools (map, filter, reduce), and general function design ideas. The next chapter will talk about function generators and a reprisal of iterators and list comprehensions.\n")
printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
print('\r')

printWhiteBlack('Test Your Knowledge: Quiz\n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')

printDarkSkyBlue('1.How are lambda expression and def statments related ? \n')
import time
time.sleep(5)
print('\r')
Q1 = input("Do you want to check your answer now: [y or n] ? ")
print('\r')
if Q1 == 'y' or Q1 == 'Y':
	printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	printPink("Answer:\n")
	printYellow("The similarity of lambda and def lies in that both lambda and def create function objects to be called later. Because lambda is an expression, though, it returns a function object instead of assigning a function object to a name, and it can be used to nest a function definition in places where a def will not work syntactically.\n")
	printYellow("A lambda only allows for a single implicit return value expression, though. Because it does not support a block of statements, it is not ideal for larger functions.\n")
	printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	print('\r')
else:
	pass
 
printDarkSkyBlue("2. What's the point of using lambda ? \n")
time.sleep(5)
print('\r')
Q2 = input("Do you want to check your answer now: [y or n] ? ")
print('\r')
if Q2 == 'y' or Q2 == 'Y':
	printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	printPink("Answer:\n")
	printYellow("lambdas allow us to inline small units of executable code, defer its execution, and provide it with state in the form of default arguments and enclosing scope variables.\n")
	printYellow("lambdas often appear in callback-based program such as GUIs, and they have a natural affinity with function tools like map and filter that expect a processing function.\n")
	printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	print('\r')
else:
	pass

printDarkSkyBlue("3. Compare and contrast map, filter, and reduce ? \n")
time.sleep(5)
print('\r')
Q3 = input("Do you want to check your answer now: [y or n] ? ")
print('\r')
if Q3 == 'y' or Q3 == 'Y':
	printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	printPink("Answer:\n")
	printYellow("These three built-in functions all apply another function to items in a sequence (iterable) object and collect results. map passes each item to the function and collects all results, filter collects items for which the function returns a True value.\n")
	printYellow("reduce computes a single value by applying the function to an accumulator and successive items. Unlike the other two, reduce is available in the functools module in 3.0, not the built-in scope.\n")
	printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	print('\r')
else:
	pass

printDarkSkyBlue("4. What are function annotations, and how are they used ? \n")
time.sleep(5)
print('\r')
Q4 = input("Do you want to check your answer now: [y or n] ? ")
print('\r')
if Q4 == 'y' or Q4 == 'Y':
	printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	printPink("Answer:\n")
	printYellow("function annotations, available in 3.0 and later, are syntactic embellishments of a function's arguments and result, which are collected into a dictionary assigned to the function's annotations attribute.Python places no semantic meaning on these annotations, but simply packages them for potential use by other tools.\n")
	printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	print('\r')
else:
	pass


printDarkSkyBlue("5. What are recursive functions, and how are they used ? \n")
time.sleep(5)
print('\r')
Q5 = input("Do you want to check your answer now: [y or n] ? ")
print('\r')
if Q5 == 'y' or Q5 == 'Y':
	printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	printPink("Answer:\n")
	printYellow("Recursive functions call themselves either directly or indirectly in order to loop. They may be used to traverse arbitrarily shaped structures, but they can also be used for iteration in general (though the latter role is often more simply and efficiently coded with looping statements).\n")
	printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	print('\r')
else:
	pass

printDarkSkyBlue("6. What are some general design guidelines for coding functions ? \n")
time.sleep(5)
print('\r')
Q6 = input("Do you want to check your answer now: [y or n] ? ")
print('\r')
if Q6 == 'y' or Q6 == 'Y':
	printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	printPink("Answer:\n")
	printYellow("Functions should generally be small, as self-contained as possible, have a single unified purpose, and communicate with other components through input arguments and return values. They may use mutable arguments to communicate results too if changes are expected, and some types of programs imply other communication mechanisms.\n")
	printGreen(u'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
	print('\r')
else:
	pass