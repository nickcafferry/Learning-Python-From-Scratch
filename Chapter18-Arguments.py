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

print('\n')
print('-------------------------------------------------------------------------------')

print('* In a function call, arguments must appear in this order : any pargs (value), followed by kargs and * sequence form, followed \
by the ** dict form.')

print('-------------------------------------------------------------------------------')

print('\n')
print('-------------------------------------------------------------------------------')

print('* In a function header, arguments must appear in this order: any normal arguments (name), followed by default arguments (name) = value, followed by the * name (or * in 3.0) form if present, followed by any name or name = value keyword-only argument (in 3.0), followed by the ** name form.')
print('-------------------------------------------------------------------------------')

print('\n')


print('Unpacking arguments')
print('--------------------')
def func(a,b,c,d):
	print(a,b,c,d)

func(1,c=3, **{'d':4,'b':2})

print('-------------------------------------------------------------------------------')
print('In order not to cause ambiguousness, the positional argument should be placed in order, the following example is given to demonstrate that if the values are not passed to the right position in a function header, an error might occur!')

print('-------------------------------------------------------------------------------')
print('\r')

def f(a,b,c): print(a,b,c)

print('#########################################################################')
print('# f(3, a = 2, b = 4.0 TypeError: f() got multiple values for argument a # ') 
print('#########################################################################')
print('\n')
f(3,c=2,b=4)
f(3,*(2,4))
f(*(2,3),c=4)
f(c=4,*(2,4))

print('\r')
print('-------------------------------------------------------------------------------')
print('The * star sequence form is normally used to unpack some argument parameters but these unpacked parameters are sent to arguments in order. Hence, the function call f(*(2,3),c=4) works in the same way as the function call f(c=4, *(2,4)) does ! That is to say *(2,3) or *(2,4) statement is going to assign 2 to the argument named a while assigning 3 to the argument named b. ')
print('-------------------------------------------------------------------------------')

print('\r')
print('Combining keywords and defaults')
print('-------------------------------')

print('\r')
print('-------------------------------------------------------------------------------')
print("""A larger example for illustrating keywords and defaults in action. In the following example, the calller must pass at least two arguments to match 'spam' and 'eggs'. If only two arguments are passed in a function call, Python assigns 'toast' and 'ham' to the defaults specified in the function header.""")
print('-------------------------------------------------------------------------------')
print('\r')

print('###############################################################################')
print('# def func(spam,eggs,toast=0,ham=0):                                          #\n#\tprint(spam,eggs,toast,ham)                                            #\n# func(1,2)                                                                   #\n# func(1, ham=1, eggs=0)                                                      #\n# func(spam=1,eggs=0)                                                         #\n# func(toast=1,eggs=2,spam=3)                                                 #\n# func(1,2,3,4) 						              #')
print('###############################################################################')

def func(spam,eggs,toast=0, ham=0):
	print(spam, eggs, toast, ham)
func(1,2)
func(1,ham=1,eggs=0)
func(spam=1,eggs=0)
func(toast=1,eggs=2,spam=3)
func(1,2,3,4)

print('\r')
print('Applying functions generically')
print('------------------------------')

print('\r')
print('-------------------------------------------------------------------------------')
print("""Some programs need to call arbitrary functions in a generic fashion, without knowing their names or arguments ahead of time. Actually, you don't need to know a function name before writing a script. You just use if logic to select from a set of funciton to complete your tasks.""")
print('-------------------------------------------------------------------------------')
print('\r')

print('###############################################################################')
print(HASH('if <test>: '))
print(HASH('   action, args = func1, (1,)'))
print(HASH('else: '))
print(HASH('   action, args = func2,(1,2,3)'))
print(HASH('...'))
print(HASH('action(*args)'))
print('###############################################################################')

def func1(*args):
	print('This is func1 with one argument in this case',args)

def func2(*args):
	print('This is func2 with three arguments in this case',args)

T = input('Please type the name of the function you wanna check: \n')
if T == 'func1':
	action, args = func1, (1,)
else:
	action, args = func2, (1,2,3)
action(*args)

print('\r')

def tracer1(func,*pargs,**kargs):
	print('calling:',func.__name__, end='  ')
	return func(*pargs,**kargs)

def funct(a,b,c,d):
	return a+b+c+d
print(tracer1(funct,1,2,c=3,d=4))

print('\r')

def tracer2(func,*pargs,**kargs):
	print('calling:',func.__name__, end='  ')
	#return func(*pargs,**kargs)
import os
for func in dir(os):
	try:
		exec('print(tracer2(os.'+ func + '),end=', ')')
	except:
		print(func+' is not a function...', end = '| ')

print('\r')
print('\n')

printYellowRed(u'Python 3.0 Keyword-Only Arguments\n')
printBlue(u'--------------------------------------------------------------------------------\n')
print('\n')

printPink(u'--------------------------------------------------------------------------------\n')
printDarkSkyBlue(u'Python 3.0 allows us to specify the keyword-only arguments-arguments that must be passed by keyword only. This function is very helpful if we want a function to both process any number of arguments and accept possibly optional configuration options. \n')
printPink(u'--------------------------------------------------------------------------------\n')
print('\r')

printPink(u'--------------------------------------------------------------------------------\n')
printDarkSkyBlue(u'Keyword-only arguments are coded as named arguments that appear after *args in the arguments list. All such arguments must be passed by keyword syntax in the call.In the following example, a may be passed by name or position, b collects any extra positional arguments, and c must be passed by keyword only.\n')
printPink(u'--------------------------------------------------------------------------------\n')
print('\r')

print('###############################################################################')
print(HASH('def kwonly(a,*b,c): '))
print(HASH('   print(a,b,c)'))
print(HASH('kwonly(1,2,c=3)'))
print(HASH('kwonly(a=1,c=3)'))
print(HASH('kwonly(1,2,3)'))
print('###############################################################################')

def kwonly(a,*b,c):
	print(a,b,c)
kwonly(1,2,c=3)
kwonly(a=1,c=3)

printRed(u'kwonly(1,2,3) will only return TypeError: kwonly() missing 1 required keyword-only argument: c\n')
print('\r')

printYellow(u'###############################################################################\n')
print(HASH('def kwonly(a,*,b,c): '))
print(HASH('   print(a,b,c)'))
print(HASH('kwonly(1,b=2,c=3)'))
print(HASH('kwonly(a=1,c=3,b=2)'))
print(HASH('kwonly(1,2,3)'))
printYellow(u'###############################################################################\n')

print('\r')
printPink(u'--------------------------------------------------------------------------------\n')
printDarkSkyBlue(u'a * character itself can indicate that a function does not accept an argument list with the same length of variable but can accept all arguments following the * to be passed as keywords. \n')
printPink(u'--------------------------------------------------------------------------------\n')
print('\r')

def kwonly(a,*,b,c):
	print(a,b,c)
kwonly(1,c=3,b=2)
kwonly(a=1,c=3,b=2)
kwonly(1,**{'c':2,'b':3})
kwonly(**{'a':1,'b':2,'c':3})

printRed(u'kwonly(1,2,3) will only return TypeError: kwonly() takes exactly 1 positional argument (3 given) c. \n')
printRed(u'kwonly(1) will only return TypeError: kwonly() needs keyword-only argument b. \n')
print('\r')

printYellow(u'###############################################################################\n')
print(HASH("def kwonly(a, *, b='spam',c='ham'): "))
print(HASH('   print(a,b,c)'))
print(HASH('kwonly(1)'))
print(HASH('kwonly(1,c=3)'))
print(HASH('kwonly(a=1)'))
print(HASH('kwonly(c=3,b=2,a=1'))
printYellow(u'###############################################################################\n')

def kwonly(a, *, b='spam',c='ham'):
	print(a,b,c)
kwonly(1)
kwonly(1,c=3)
kwonly(a=1)
kwonly(c=3,b=2,a=1)

printRed(u'kwonly(1,2) will only return TypeError: kwonly() takes 1 positional argument but 2 were given.\n')

print('\r')
printPink(u'-------------------------------------------------------------------------------\n')
printDarkSkyBlue(u'Actually, keyword-only arguments with defaults are optional, but those without default effectively become required keywords for the function. \n')
printPink(u'-------------------------------------------------------------------------------\n')
print('\r')

printYellow(u'###############################################################################\n')
print(HASH("def kwonly(a, *, b,c='spam'): "))
print(HASH('   print(a,b,c)'))
print(HASH("kwonly(1, b='eggs')"))
print(HASH("kwonly(1,c='eggs')"))
print(HASH(">>>TypeError: kwonly() needs keyword-only argument b. "))
print(HASH("kwonly(1,2)"))
print(HASH(">>>TypeError: kwonly() takes exactly 1 positional argument (2 given)."))
print(HASH('def kwonly(a,*, b=1,c,d=2): '))
print(HASH('   print(a,b,c,d)'))
print(HASH('kwonly(3,c=4)'))
print(HASH('kwonly(3,c=4,b=5)'))
print(HASH('kwonly(3)'))
print(HASH('kwonly(1,2,3)'))
print(HASH('>>>TypeError: kwonly() takes exactly 1 positional argument (3 given)'))
printYellow(u'###############################################################################\n')
print('\r')
print('\r')


printYellowRed(u'Ordering Rules\n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')
print('\r')
printPink(u'-------------------------------------------------------------------------------\n')
printDarkSkyBlue(u'The keyword-only arguments must appear after a single star character, and cannot appear after two stars. Named arugments cannot appear after the ** args arbitrary keywords form, and a ** cannot appear by itself in the arguments list.\n')
printPink(u'-------------------------------------------------------------------------------\n')
print('\r')

printYellow(u'###############################################################################\n')
print(HASH("def kwonly(a, **pargs, b , c): "))
print(HASH('>>> SyntaxError: Invalid Syntax.'))
print(HASH("def kwonly(a,**,b,c)"))
print(HASH(">>> SyntaxError: Invalid Syntax."))
printYellow(u'###############################################################################\n')
print('\r')

printPink(u'-------------------------------------------------------------------------------\n')
printDarkSkyBlue('In a function header, the keyword-only arguments must be coded before the ** args arbitrary keywords form and after the *args arbitrary positional form, when both are present. Whenever an argument name appears before star arguments(no matter how many stars those arguments have), it is possibly default positional argument, not keyword-only.\n')
printPink(u'-------------------------------------------------------------------------------\n')
print('\r')

printYellow(u'###############################################################################\n')
print(HASH("def f(a,*b,**d,c=6): print(a,b,c,d)"))
print(HASH('>>> SyntaxError: Invalid Syntax.'))
print(HASH("def f(a,*b,c=6,**d): print(a,b,c,d)"))
print(HASH("f(1,2,3,x=4,y=5)"))
print(HASH("f(1,2,3,x=4,y=5,c=7)"))
print(HASH("f(1,2,3,c=7,x=4,y=5)"))
print(HASH("def f(a,c=6,*b,**d): print(a,b,c,d)"))
print(HASH("f(1,2,3,x=4)"))
printYellow(u'###############################################################################\n')
print('\r')

def f(a,*b,c=6,**d): print(a,b,c,d)
f(1,2,3,x=4,y=5)
f(1,2,3,x=4,y=5,c=7)
f(1,2,3,c=7,x=4,y=5)
f(1,2,3,x=4,c=7,y=5)

print('\r')
printSkyBlue(u'# def function(a,c=6,*b,**d): print(a,b,c,d) \n')
printSkyBlue(u'# function(1,2,(23,4,2),x=23,y=25))\n')

def function(a, c=6, *b, **d): print(a,b,c,d)
function(1,2,(23,4,2), x=23,y=25)
print('\r')

printPink(u'-------------------------------------------------------------------------------\n')
printDarkSkyBlue('The same ordering rules hold true in function calls: Keyword-only argument are passed, they must appear befor a **args form. The keyword-only argument can be coded either before or after the *args, though,and may be included in **args:\n')
printPink(u'-------------------------------------------------------------------------------\n')
print('\r')

def f(a,*b,c=6,**d): print(a,b,c,d)
f(1,*(2,3),**dict(x=4,y=5))
print('\r')
printYellow(u'Actually, f(1,*(2,3),**dict(x=4,y=5),c=123) works on Python 3.8 \n')
f(1,*(2,3),**dict(x=4,y=5),c=123)
print('\r')
f(1,*(2,3),c=7,**dict(x=4,y=5))
f(1,c=7,*(2,3),**dict(x=4,y=5))
f(1,*(2,3),**dict(x=4,y=5,c=7))

printYellow(u'###############################################################################\n')
print(HASH("def f(a,*b,**d,c=6): print(a,b,c,d)"))
print(HASH("def f(a,*b,c=6,**d): print(a,b,c,d)"))
print(HASH("f(1,2,3,x=4,y=5)"))
print(HASH("f(1,2,3,x=4,y=5,c=7)"))
print(HASH("f(1,2,3,c=7,x=4,y=5)"))
print(HASH("def f(a,c=6,*b,**d): print(a,b,c,d)"))
print(HASH("f(1,2,3,x=4)"))
printYellow(u'###############################################################################\n')
print('\r')

print('\r')
printYellowRed(u'Why should we care about keyword-only arguments \n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')

printPink(u'-------------------------------------------------------------------------------\n')
printDarkSkyBlue('In short, keyword-arguments make it easier to both accept positional arguments and configuration options passed as keywords.\n')
printPink(u'-------------------------------------------------------------------------------\n')
print('\r')

printWhiteBlack(u"The min Wakeup Call!\n")
printSkyBlue(u'--------------------------------------------------------------------------------\n')
print('\r')

printBlue(u'This part is given to illustrate concepts discussed above by a concrete example.')
printBlue(u'Suppose you want to make comparsions between some arbitrary objects.You can try these three following solutions: \n')
print('\r')

printPink(u'-------------------------------------------------------------------------------\n')
printDarkSkyBlue('The first solution fetches the first argument using index and traverses the rest by slicing off the first and then makes comparisions.\n')
printPink(u'-------------------------------------------------------------------------------\n')
print('\r')

printYellow(u'###############################################################################\n')
print(HASH("def min1(*args): "))
print(HASH("   res = args[0]"))
print(HASH("   for arg in args[1:]: "))
print(HASH("      if arg < res:"))
print(HASH("         res = arg"))
print(HASH("   return res"))
print(HASH("print(min1(1,2,3,4,5))"))
print(HASH("print(min1('a','b','c','e','z','f'))"))
print(HASH("print(min1('acd','sdew','dswe','swew'))"))
printYellow(u'###############################################################################\n')
print('\r')

def min1(*args):
	res = args[0]
	for arg in args[1:]:
		if arg < res:
			res = arg
	return res
print(min1(1,2,3,4,5))
print(min1('a','b','c','e','z','f'))
print(min1('acd','sdew','dswe','swew'))

def intersect(*args):
	res = []
	for x in args[0]:
		for other in args[1:]:
			if x not in other: break
		else:
			res.append(x)
	return res
print(intersect('abac','acads','dsafda','afas','adaeew'))

def union(*args):
	res = []
	for seq in args:
		for x in seq:
			if not x in res:
				res.append(x)
	return res
print(union('abac','acads','dsafda','afas','adaeew'))


import sys
def print30(*args,**kargs):
	sep = kargs.get('sep',' ')
	end = kargs.get('end', '\n')
	file = kargs.get('file',sys.stdout)
	output = ''
	first = True
	for arg in args:
		output += ('' if first else sep) + str(arg)
		first = False
	file.write(output+end)
print30(1,2,3, sep='XD')
print30(30,name='bob')

print30(1,2,3)
print30(1,2,3,sep='')
print30(1,2,3,sep='...')
print30(1,[2],(3,),sep='...')

print30(4,5,6,sep='',end='')
print30(7,8,9)
print30()

import sys
print30(1,2,3,sep='??', end='.\n',file=sys.stderr)

#Use keyword-only args
def print30(*args,sep=' ', end='\n', file=sys.stdout):
	output = ''
	first = True
	for arg in args:
		output += ('' if first else sep) + str(arg)
		first = False
	file.write(output+end)
print30(99,'bob')

#Use keyword args deletion with defaults
def print30(*args,**kargs):
	sep = kargs.pop('sep',' ')
	end = kargs.pop('end','\n')
	file = kargs.pop('file',sys.stdout)
	if kargs: raise TypeError('extra keywords: %s' % kargs)
	output = ''
	first = True
	for arg in args:
		output+=('' if first else sep)+str(arg)
		first = False
	file.write(output+end)
print30(99,sep='bob')