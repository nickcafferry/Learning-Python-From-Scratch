This chapter will cover the advanced function topics theme, and revisit list comprehension and iteration. We won't talk about user-defined classes until Part VI-Classes. A thorough summary of various tools we mentioned before is going to be done since this is the last pass we'll make over built-in iteration tools.

### List Comprehensions Revisited: Functional Tools

In addition to some built-in functional programming tools, Python 3.0 also provides us with a more generalized tool--list comprehension--. List comprehensions are more flexible than such built-in funcitonal programming tool as map or filter or reduce because they can deal with arbitrary expressions rather than specific functions.

#### List comprehensions Versus map


```python
ord('s'), chr(115)
```




    (115, 's')



suppose we have to collect all the ASCII integer code of all characters in an entire string. Of course, we can use for loop statements.


```python
res = []
for x in 'spam':
    res.append(ord(x))
res
```




    [115, 112, 97, 109]



Alternatively, we can achieve the same result by maping the built-in function map to each item in iterables.


```python
res = list(map(ord,'spam'))
res
```




    [115, 112, 97, 109]



However, the most straightforward approach is to use a list comprehension.


```python
res = [ord(x) for x in 'spam']
res
```




    [115, 112, 97, 109]



Syntactically, list comprehensions are enclosed in square brackets (to remind yoy that they construct lists).


```python
print([x**2 for x in range(10)])
print([x**3 for x in range(10)])
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]



```python
list(map((lambda x: x **2), range(10)))
```




    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



#### Adding Tests and Nested Loops: filter


```python
[x for x in range(5) if x % 2 == 0]
list(filter((lambda x: x % 2 == 0), range(5)))
```




    [0, 2, 4]




```python
res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)
res
```




    [0, 2, 4]




```python
#import sys
#from tkinter import Button, mainloop
#x = Button(
#    text = 'Press me',
#    command = (lambda: sys.stdout.write('Spam\n')))
#x.pack()
#mainloop()
```


```python
[ x**2 for x in range(10) if x % 2 == 0]
```




    [0, 4, 16, 36, 64]




```python
list(map((lambda x : x**2), filter((lambda x: x % 2 == 0), range(10))))
```




    [0, 4, 16, 36, 64]



[ expression for target1 in iterable1 [if condition1]
             for target2 in iterable2 [if condition2]...
             for targetN in iterableN [if conditionN]]


```python
res = [x + y for x in [0,1,2] for y in [100,200,300]]
res
```




    [100, 200, 300, 101, 201, 301, 102, 202, 302]




```python
res = []
for x in [0,1,2]:
    for y in [100,200,300]:
        res.append(x+y)
res
```




    [100, 200, 300, 101, 201, 301, 102, 202, 302]




```python
print([x + y for x in 'spam' for y in 'SPAM'], end = ' ')
```

    ['sS', 'sP', 'sA', 'sM', 'pS', 'pP', 'pA', 'pM', 'aS', 'aP', 'aA', 'aM', 'mS', 'mP', 'mA', 'mM'] 


```python
print([(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y%2 == 1])
```

    [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]



```python
res = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x,y))
```


```python
res
```




    [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]



### List Comprehensions and Matrixes


```python
M = [[1,2,3],
    [4,5,6],
    [7,8,9]]
N = [[2,2,2],
    [3,3,3],
    [4,4,4]]
```


```python
[row[0] for row in M]
[row[1] for row in M]
[row[2] for row in M]
```




    [3, 6, 9]




```python
[M[row][1] for row in (0,1,2)]
```




    [2, 5, 8]




```python
[M[row][col] * N[row][col] for row in range(3) for col in range(3)]
[[M[row][col] * N[row][col] for col in range(3) for row in range(3)]]
```




    [[2, 12, 28, 4, 15, 32, 6, 18, 36]]




```python
f = open('mytimer.py','w')
```


```python
f.write('import time \n')
```




    13




```python
f.write('reps = 1000 \n')
f.write('repslist = range(reps) \n')
f.write('def timer(func,*pargs,**kargs): \n')
f.write('\tstart = time.clock() \n')
f.write('\tfor i in repslist: \n')
f.write('\t\tret=func(*pargs,**kargs)\n\telapsed = time.clock() - start\n\treturn (elapsed, ret)')
```




    81




```python
f.close()
```


```python
file = open('mytimer.py','r')
```


```python
file.read()
```




    'import time \nreps = 1000 \nrepslist = range(reps) \ndef timer(func,*pargs,**kargs): \n\tstart = time.clock() \nreps = 1000 \nrepslist = range(reps) \ndef timer(func,*pargs,**kargs): \n\tstart = time.clock() \n\tfor i in repslist: \nreps = 1000 \nrepslist = range(reps) \ndef timer(func,*pargs,**kargs): \n\tstart = time.clock() \n\tfor i in repslist: \n\t\tret=func(*pargs,**kargs)\n\telapsed = time.clock() - start\n\treturn (elapsed, ret)'




```python
[M[row][col] * N[row][col] for row in range(3) for col in range(3)]
```




    [2, 4, 6, 12, 15, 18, 28, 32, 36]




```python
[[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
```




    [[2, 4, 6], [12, 15, 18], [28, 32, 36]]




```python
M
```




    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]




```python
from sympy import *
```


```python
init_printing()
```


```python
x,y,z = symbols('x,y,z')
```


```python
T = integrate(cos(3*x*y*z**2),x)
```


```python
help(print_python)
```

    Help on function print_python in module sympy.printing.python:
    
    print_python(expr, **settings)
        Print output of python() function
    



```python
from sympy.printing.mathml import print_mathml
```


```python
T= integrate(cos(3*x+y*z**2),x)
```


```python
import sympy.printing.mathml
```


```python
sympy.printing.mathml(T)
```




    '<apply><divide/><apply><sin/><apply><plus/><apply><times/><cn>3</cn><ci>x</ci></apply><apply><times/><ci>y</ci><apply><power/><ci>z</ci><cn>2</cn></apply></apply></apply></apply><cn>3</cn></apply>'




```python
!pip install --upgrade pip
```

    Collecting pip
      Downloading http://repo.myhuaweicloud.com/repository/pypi/packages/43/84/23ed6a1796480a6f1a2d38f2802901d078266bda38388954d01d3f2e821d/pip-20.1.1-py2.py3-none-any.whl (1.5MB)
    [K    100% |████████████████████████████████| 1.5MB 58.6MB/s ta 0:00:01
    [?25hInstalling collected packages: pip
      Found existing installation: pip 9.0.1
        Uninstalling pip-9.0.1:
          Successfully uninstalled pip-9.0.1
    Successfully installed pip-20.1.1



```python
from chempy import *
```


```python
myfile = open('myfile','w')
myfile.write('aaa\n')
myfile.write('bbb\n')
myfile.write('ccc\n')
myfile.close()

open('myfile').readlines()
```




    ['aaa\n', 'bbb\n', 'ccc\n']




```python
[line.rstrip() for line in open('myfile').readlines()]
[line.rstrip() for line in open('myfile')]
list(map((lambda line: line.rstrip()), open('myfile')))
```




    ['aaa', 'bbb', 'ccc']




```python
list(map((lambda line: line.rstrip()),open('myfile')))
```




    ['aaa', 'bbb', 'ccc']



`The list is a tuple, tuples are rows, and items in tuples are column values`


```python
listoftuple = [('bob',35,'mgr'),('mel',40,'dev')]
```


```python
[age for (name,age,job) in listoftuple]
```




    [35, 40]




```python
list(map((lambda row: row[1]),listoftuple))
```




    [35, 40]




```python
def gensquare(N):
    for i in range(N):
        yield i ** 2
```


```python
list(gensquare(4))
```




    [0, 1, 4, 9]




```python
f = open('myfile')
def genf():
    yield f.readline()
```


```python
t = genf()
```


```python
next(t)
```




    'aaa\n'




```python
f.readline()
```




    'bbb\n'



#### Iterators Revisited: Generators 

------------------------

Today Python supports procrastination much more than it did in the \
past.

* `Generator functions` are coded as normal def statements but use `yield` instead of `return` statements to return results one at a time, suspending and resuming their state between each
* `Generator expressions` are similar to the list comprehensions of the prior section, but they return an object that produces results on demand instead of building a result list.


```python
def gensquares(N):
    for i in range(N):
        yield i**2
```


```python
for i in gensquares(5):
    print(i,end=' : ')
```

    0 : 1 : 4 : 9 : 16 : 


```python
x = gensquares(4)
```


```python
x
```




    <generator object gensquares at 0x7f09f43f8fc0>




```python
id(x)
```




    139680729239488




```python
iter(x) == x
```




    True




```python
next(x)
```




    0




```python
next(x)
```




    1




```python
next(x)
```




    4




```python
next(x)
```




    9




```python
y = gensquares(10)
```


```python
y.__next__(), y.__next__(), y.__next__(), y.__next__(), y.__next__(), y.__next__(),y.__next__()
```




    (0, 1, 4, 9, 16, 25, 36)




```python
def buildsquares(n):
    res = []
    for i in range(n): res.append(i**2)
    return res
```


```python
for x in buildsquares(5): print(x, end = ' : ')
```

    0 : 1 : 4 : 9 : 16 : 


```python
for x in [n ** 2 for n in range(5)]:
    print(x, end = ' : ')
```

    0 : 1 : 4 : 9 : 16 : 


```python
for x in map((lambda n: n**2), range(5)):
    print(x, end = ': ')
```

    0: 1: 4: 9: 16: 

#### Extended generator function protocol: send versus next


```python
def gen():
    for i in range(10):
        X = yield i
        print(X)
```


```python
G = gen()
```


```python
next(G)
```




    0




```python
next(G), next(G), next(G), next(G)
```

    None
    None
    None
    None





    (1, 2, 3, 4)




```python
G.send(77)
```

    77





    5




```python
G.send(88), next(G)
```

    88
    None





    (6, 7)



`G.send(X)` method of an object can be implemented on built-in generator objects only while the `G.__next__()` method can be applied to all iterable objects (both built-in type and user-defined classes)

#### Gnenerator Expressions: Iterators Meet Comprehensions


```python
[x**2 for x in range(4)]
```




    [0, 1, 4, 9]




```python
G=(x**2 for x in range(4))
```


```python
next(G),next(G), next(G), next(G)
```




    (0, 1, 4, 9)



*In all recent versions of Python, the notions of iterators and list comprehensions are combined in a new feature of the language, generator expression. In terms of syntax, generator expressions are just like normal list comprehension, but they are enclosed in parentheses instead of square brackets*


```python
[x**2 for x in range(4)] # List comprehension: build a list
(x**2 for x in range(4)) # Generator expression: make a iterable
```




    <generator object <genexpr> at 0x7fd84c8bf7d8>



*In fact, at least on a function basis, coding a list comprehension is essentially the same as wrapping a generator expression in a list built-in call to force it to produce all its result in a list at once.*


```python
list(x**2 for x in range(4))
```




    [0, 1, 4, 9]



*Operationally, generator expressions are very different-instead of returning the result in a list, they return a generator object, which in turn supports the iteration protocol to yield one piece of the result list at a time in any iteration context:*


```python
G = (x**2 for x in range(4))
next(G), next(G), next(G), next(G)
```




    (0, 1, 4, 9)




```python
for num in (x**2 for x in range(4)):
    print('%s, %s ' % (num, num/2.0) )
```

    0, 0.0 
    1, 0.5 
    4, 2.0 
    9, 4.5 


*Therefore, the for loop can trigger the next iterator machinery under the hood of a generator expression just as following:*


```python
for num in (x**2 for x in range(4)):
    print('%s, %s' %(num, num/2.0))
```

    0, 0.0
    1, 0.5
    4, 2.0
    9, 4.5



```python
''.join(x.upper() for x in 'aaa,bbb,ccc'.split(','))
a,b,c = (x+'\n' for x in 'aaa,bbb,ccc'.split(','))
```


```python
a,b,c
```




    ('aaa\n', 'bbb\n', 'ccc\n')




```python
sum(x**2 for x in range(4)), sorted(x**2 for x in range(4)), sorted((x**2 for x in range(4)), reverse = True)
```




    (14, [0, 1, 4, 9], [9, 4, 1, 0])




```python
any(['a','v','','ad']), help(any)
```

    Help on built-in function any in module builtins:
    
    any(iterable, /)
        Return True if bool(x) is True for any x in the iterable.
        
        If the iterable is empty, return False.
    





    (True, None)




```python
all(['a','v','','ad']), help(any)
```

    Help on built-in function any in module builtins:
    
    any(iterable, /)
        Return True if bool(x) is True for any x in the iterable.
        
        If the iterable is empty, return False.
    





    (False, None)



#### Generator expressions versus map

*Like list comprehensions, generator expressions are much more simpler to use than map is when the operation applied is not a function call (maybe a plus or mutilplication*


```python
list(map(abs,(-1,-2,3,-4))), list(abs(x) for x in (-1,-2,3,4)) # map function on tuple, generator expression
```




    ([1, 2, 3, 4], [1, 2, 3, 4])




```python
list(map(lambda x: x *2, (1,2,3,4))), list(x*2 for x in (1,2,3,4))
```




    ([2, 4, 6, 8], [2, 4, 6, 8])




```python
list( x+y for x,y in enumerate(range(1,18,2))), list(map((lambda x, y: x+y), range(1,len(range(1,18,2))),range(1,18,2)))
```




    ([1, 4, 7, 10, 13, 16, 19, 22, 25], [2, 5, 8, 11, 14, 17, 20, 23])




```python
list(map(lambda x:  x *2, (1,2,3,4))) #Nonfunciton case
```




    [2, 4, 6, 8]




```python
list(x*2 for x in (1,2,3,4)) # Simpler as generator?
```




    [2, 4, 6, 8]



*The same holds true for text-processing use cases like the join call we saw earlier-a list comprehension makes an extra temporary list of results, which is a completely pointless this context because the list is not retained.*


```python
line = 'aaa,bbb,ccc'
''.join([x.upper() for x in line.split(',')]) # Makes a pointless list
''.join(x.upper() for x in line.split(',')) # Generates results
''.join(map(str.upper,line.split(',')))  # Generates results
''.join(x*2 for x in line.split(',')) # Simpler as generator?
''.join(map(lambda x: x * 2, line.split(',')))
```




    'aaaaaabbbbbbcccccc'



*If generator expressions are the sole item enclosed in other parentheses, the parentheses are not required around a geneator expression*


```python
sum(x**2 for x in range(4))
```




    14




```python
sorted(x**2 for x in range(4))
```




    [0, 1, 4, 9]




```python
sorted((x**2 for x in range(4)), reverse = True)
```




    [9, 4, 1, 0]




```python
import math
list(map(math.sqrt, (x**2 for x in range(4))))
```




    [0.0, 1.0, 2.0, 3.0]



*Generator expressions are usually treated as a memory-space optimization. They don't work the same way as the squrared-brakceted list comprehension does, which means they won't generate the result list all at once. Sometimes, they are not so efficent as list comprehensions (they might run slightly slower in practice). Probably, their best usage is only for very large result sets. Actually, in this chapter we'll code a timing script for measuring their performance in reality.*

### Generator functions versus Generator expression


```python
G = (c*4 for c in 'SPAM') # Generator expression
```


```python
list(G) # Force generator to produce all results
```




    ['SSSS', 'PPPP', 'AAAA', 'MMMM']




```python
list(G)
```




    []



*The equivalent counterpart (gnenerator function) require slightly more code, 
but as a multistatement funciton it will be able to code more logic and use more statement information if needed.*


```python
def timesfour(S):
    for c in S:
        yield c * 4
```


```python
G = timesfour('spam')
```


```python
list(G)
```




    ['ssss', 'pppp', 'aaaa', 'mmmm']




```python
G = (c*4 for c in 'SPAM')
I = iter(G)
next(I), next(I), next(I), next(I)
```




    ('SSSS', 'PPPP', 'AAAA', 'MMMM')




```python
G = timesfour('spam')
I = iter(G)
next(I),next(I),next(I),next(I)

It = iter(timesfour('spam'))
It.__next__(), It.__next__(), It.__next__(), It.__next__()
```




    ('ssss', 'pppp', 'aaaa', 'mmmm')



#### Generators Are Single-Iterator Objects

*Both generator function and generator expressions are their own iterators and thus support just one active iteration*


```python
G = (c*4 for c in 'SPAM')
iter(G) is G
```




    True




```python
def gene(c):
    for i in c:
        yield i*4
```


```python
T = gene('SPAM')
```


```python
iter(T) is T, id(iter(T)) is id(T)
```




    (True, False)




```python
G = (c*4 for c in 'SPAM')
I1 = iter(G)
next(I1), next(I1)
```




    ('SSSS', 'PPPP')




```python
I2 = iter(G)
```


```python
next(I2) # second iterator at same position
```




    'MMMM'




```python
I3 = iter(c*4 for c in 'SPAM')
I4 = (c*4 for c in 'SPAM')
```


```python
next(I3), next(I4)
```




    ('SSSS', 'SSSS')



*The same holds true for generator functions-the following def statement-based equivalent supports just one active iterator and is exhausted after one pass*


```python
def timesfour(S):
    for c in S:
        yield c * 4
```


```python
G = timesfour('SPAM')
iter(G) is G
```




    True




```python
I1, I2 = iter(G), iter(G)
next(I1), next(I1), next(I2)
```




    ('SSSS', 'PPPP', 'AAAA')



*Generator funcitons or generator expressions don't work the same way as some built-in types do. Such built-in types as lists or dictionarys support multiple iterators and passes and will reflect their in-place changes in active iterators*


```python
L = [1,2,3,4]
I1, I2 = iter(L), iter(L)
next(I1), next(I1), next(I2) 
```




    (1, 2, 1)




```python
del L[2:]
try:
    next(I1) # Changes reflected in iterators
except:
    print('Changes are reflected in iterators')
```

    Changes are reflected in iterators


# Emulating zip and map with Iteration Tools


```python
S1 = 'abc'
S2 = 'xyz123'
list(zip(S1,S2)) # zip pairs items from iterables
```




    [('a', 'x'), ('b', 'y'), ('c', 'z')]




```python
list(zip([-2,-1,0,1,2])) # Single sequence: 1-array tuples
```




    [(-2,), (-1,), (0,), (1,), (2,)]




```python
list(zip([1,2,3],[2,3,4,5])) # N sequence: N-array tuples
```




    [(1, 2), (2, 3), (3, 4)]



*map passes paired itenms to a function, truncates*


```python
list(map(abs,[-2,-1,0,1,2]))
```




    [2, 1, 0, 1, 2]




```python
list(map(pow, [1,2,3],[2,3,4,5]))
```




    [1, 8, 81]



#### Coding your own map(func,...)


```python
# map(func,seqs,...)workable with zip
def mymap(func,*seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res
```


```python
print(mymap(abs,[-2,-1,0,1,2]))
print(mymap(pow,[1,2,3],[2,3,4,5]))
```

    [2, 1, 0, 1, 2]
    [1, 8, 81]



```python
for args in zip([1,2,3],[2,3,4,5]):
    print(args)
```

    (1, 2)
    (2, 3)
    (3, 4)



```python
for args in zip([-2,-1,0,1,2]):
    print(args)
```

    (-2,)
    (-1,)
    (0,)
    (1,)
    (2,)



```python
def mymap(func,*seqs):
    return [func(*args) for args in zip(*seqs)]
```


```python
print(mymap(abs,[-2,-1,0,1,2]))
print(mymap(pow,[1,2,3],[2,3,4,5]))
```

    [2, 1, 0, 1, 2]
    [1, 8, 81]



```python
def mymap(func,*seqs):
    res = []
    for args in zip(*seqs):
        yield func(*args)
def mymap(func,*seqs):
    return (func(*args) for args in zip(*seqs))
```


```python
print(mymap(abs,[-2,-1,0,1,2]))
print(mymap(pow,[1,2,3],[2,3,4,5]))
```

    <generator object mymap.<locals>.<genexpr> at 0x7efe1efb0410>
    <generator object mymap.<locals>.<genexpr> at 0x7efe2c09f410>



```python
def myzip(*seqs):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

def mymapPad(*seqs, pad = None):
    seqs = [list(S) for S in seqs]
    res = []
    while any(seqs):
        res.append(tuple((S.pop(0) if S else pad) for S in seqs))
    return res
```


```python
S1, S2 = 'abc', 'xyz123'
seqs = [list(S) for S in ('abc','xyz123')]
```


```python
seqs
```




    [['a', 'b', 'c'], ['x', 'y', 'z', '1', '2', '3']]




```python
res = []
res.append(tuple(S.pop(0) for S in seqs))
print(res)

res = []
res.append(tuple(S.pop(0) for S in seqs))
print(res)

res = []
res.append(tuple(S.pop(0) for S in seqs))
print(res)
```

    [('a', 'x')]
    [('b', 'y')]
    [('c', 'z')]



```python
print(myzip(S1,S2))
```

    [('a', 'x'), ('b', 'y'), ('c', 'z')]



```python
seqs = [list(S) for S in ('abc','xyz123')]
res = []
res.append(tuple((S.pop(0) if S else pad) for S in seqs))
print(res)
```

    [('a', 'x')]



```python
seqs = [list(S) for S in ('abc','xyz123')]
```


```python
seqs
```




    [['a', 'b', 'c'], ['x', 'y', 'z', '1', '2', '3']]




```python
res = []
```


```python
res.append(tuple((S.pop(0) if S else pad)) for S in seqs)
```


```python
mymapPad(S1,S2)
```




    [('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]




```python
print(mymapPad(S1,S2))
```

    [('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]



```python
print(mymapPad(S1,S2,pad = 99))
```

    [('a', 'x'), ('b', 'y'), ('c', 'z'), (99, '1'), (99, '2'), (99, '3')]


*Alternate implementation with lengths*


```python
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    print(minlen)
    print([tuple(S[i] for S in seqs) for i in range(minlen)])
    return [tuple(S[i] for S in seqs) for i in range(minlen)]
```


```python
S1, S2 = 'abc', 'xyz123'
print(myzip(S1,S2))
```

    3
    [('a', 'x'), ('b', 'y'), ('c', 'z')]
    [('a', 'x'), ('b', 'y'), ('c', 'z')]



```python
def mymapPad(*seqs, pad = None):
    maxlen = max(len(S) for S in seqs)
    index = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]
```


```python
print(mymapPad(S1,S2))
print(mymapPad(S1,S2,pad = 99))
```

    [('a', 'x'), ('b', 'y'), ('c', 'z'), (None, '1'), (None, '2'), (None, '3')]
    [('a', 'x'), ('b', 'y'), ('c', 'z'), (99, '1'), (99, '2'), (99, '3')]



```python
[tuple(S[i] for S in ['abc','xyz123']) for i in range(len('abc'))]
```




    [('a', 'x'), ('b', 'y'), ('c', 'z')]




```python
tuple(S[i] for S in ['abc','xyz123'] for i in range(len('abc')))
```




    ('a', 'b', 'c', 'x', 'y', 'z')




```python
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    for i in range(minlen):
        for S in seqs:
            return tuple(S[i])
```

*Notice that here we use indexing and the built-in function length, which means we assume that we are dealing with sequences rather than arbitrary iterables. The outer comprehensions step through argument index ranges while the innner step through the passed-in sequence to pull out arguments in parallel*


```python
# Using generators
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))
print(list(myzip(S1,S2)))
```

    [('a', 'x'), ('b', 'y'), ('c', 'z')]


*In this case, a list call is needed to activate the generators and iterators to produce results*


```python
def myzip(*args):
    iters = map(iter,args)
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)
```

#### Why you will care : One-Shot Iterations


```python
def myzip(*args):
    iters = map(iter,args)
    print(iters)
    while iters:
        res = [next(i) for i in iters]
        print(iters, res)
        yield tuple(res)
```

`list(myzip('abc','lmnop'))`
This code works fine in Python 2.6 as is:
`[('a','l'),('b','m'),('c','n')]`
But it falls into an infinite loop and fails in Python 3.0. In 3.0, map returns a one-shot iterable obejct instead of a list as in 2.6.


```python
list(map(iter,[('abc','lmnop')]))
```




    [<tuple_iterator at 0x7f422a6c62b0>]




```python
def myzip(*args):
    iters = list(map(iter,args))
    print(iters)
    while iters:
        res = [next(i) for i in iters]
        print(iters, res)
        yield tuple(res)
```


```python
list(myzip('abc','lmnop'))
```

    [<str_iterator object at 0x7f422a6c6e48>, <str_iterator object at 0x7f422a6c6e80>]
    [<str_iterator object at 0x7f422a6c6e48>, <str_iterator object at 0x7f422a6c6e80>] ['a', 'l']
    [<str_iterator object at 0x7f422a6c6e48>, <str_iterator object at 0x7f422a6c6e80>] ['b', 'm']
    [<str_iterator object at 0x7f422a6c6e48>, <str_iterator object at 0x7f422a6c6e80>] ['c', 'n']


    /home/ma-user/anaconda3/lib/python3.6/site-packages/ipykernel/__main__.py:1: DeprecationWarning: generator 'myzip' raised StopIteration
      if __name__ == '__main__':





    [('a', 'l'), ('b', 'm'), ('c', 'n')]




```python
iters = map(iter,[('abc','lmnop')])
```


```python
bool(iters)
```




    True




```python
[next(i) for i in iters]
```




    []



#### Value Generation in Built-in Types and Classes


```python
D = dict(a=1,b=2,c=3)
```


```python
D
```




    {'a': 1, 'b': 2, 'c': 3}




```python
x = iter(D)
```


```python
next(x),next(x),next(x)
```




    ('a', 'b', 'c')




```python
for key in D:
    print(key,D[key])
```

    a 1
    b 2
    c 3



```python
!git clone https://github.com/nickcafferry/Python-for-Transport-Phenomena.git
```

    Cloning into 'Python-for-Transport-Phenomena'...
    remote: Enumerating objects: 29, done.[K
    remote: Counting objects: 100% (29/29), done.[K
    remote: Compressing objects: 100% (28/28), done.[K
    remote: Total 29 (delta 4), reused 0 (delta 0), pack-reused 0[K
    Unpacking objects: 100% (29/29), done.
    Checking connectivity... done.



```python
ls
```

    [0m[01;34mPython-for-Transport-Phenomena[0m/



```python
cd Python-for-Transport-Phenomena/
```

    /home/ma-user/work/Python-for-Transport-Phenomena



```python
ls
```

    [0m[01;34mPictures[0m/  README.md  Transport Phenoma.ipynb


*Although beyond the scope of this chapter, it is also possible to implement arbitrary user-defined generator objects with classes that conform to the iteration protocol. Such classes define a special __iter__ method run by the iter built-in function that returns an object having a __next__ method run by the next built-in function (a __getitem__) indexing method is also available as a fallback option for iteration*


```python
[x*x for x in range(10)]
```




    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




```python
(x*x for x in range(10))
```




    <generator object <genexpr> at 0x7f1d4c1414c0>




```python
{x*x for x in range(10)}
```




    {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}




```python
{x:x*x for x in range(10)}
```




    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}




```python
{x*x for x in range(10)}
```




    {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}




```python
set(x*x for x in range(10))
```




    {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}



#### Comprehension Syntax Summary

*We've been focusing on list comprehensions and generators in this chapter,but keep in mind that there are two other comprehension expression forms: set and dictionary comprehensions are also avaiable in Python 3.0. We already know enough about comprehensions and geneators, hence it is easy to acquire a good understanding of set and dictionary comprehensions.*


```python
print({1,3,2} == set([1,3,2])); 
print({ord(x) for x in '1,3,2' if ord(x)>20} == set(ord(x)\
for x in '1,3,2' if ord(x) > 20))
```

    True
    True


> For sets, the new literal form `{1,3,2}` works like `set([1,3,2])`;
> the new set comprehension `{f(x) for x in S if P(x)}` is equipvalent to `set(f(x) for x in S if P(x))`


```python
{key: val for (key, val) in zip('abcdefghijklmn','123456789')}
```




    {'a': '1',
     'b': '2',
     'c': '3',
     'd': '4',
     'e': '5',
     'f': '6',
     'g': '7',
     'h': '8',
     'i': '9'}




```python
dict(zip('abcdefghijklmn','123456789'))
```




    {'a': '1',
     'b': '2',
     'c': '3',
     'd': '4',
     'e': '5',
     'f': '6',
     'g': '7',
     'h': '8',
     'i': '9'}




```python
{x: int(x) for x in '123456789'} == dict((x,int(x)) for x in '123456789')
```




    True




```python
dict((x,int(x)) for x in '123456789')
```




    {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}




```python
[x*x for x in range(10)] #list comprehensions: builds list
```




    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]




```python
(x*x for x in range(10))
```




    <generator object <genexpr> at 0x7fbdecfcf938>




```python
{x*x for x in range(10)}
```




    {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}




```python
{x: x*x for x in range(10)}
```




    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}




```python
{x*x for x in range(10)}
```




    {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}




```python
set(x*x for x in range(10))
```




    {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}



#### Comprehending Set and Dictionary Comprehensions


```python
{x*x for x in range(10)} #comprehension
set(x*x for x in range(10)) # Generator and type name
```




    {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}




```python
{x:x*x for x in range(10)}
dict((x,x*x) for x in range(10)) 
```




    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}




```python
try:
    x
except:
    print("""NameError: name 'x' is not defined""")
```

    NameError: name 'x' is not defined



```python
res = set()
for x in range(10):
    res.add(x*x)
```


```python
res
```




    {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}




```python
res = {}
for x in range(10):
    res[x] = x*x
```


```python
res
```




    {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}




```python
G = ((x,x*x) for x in range(10))   
```


```python
next(G)
```




    (0, 0)




```python
next(G)
```




    (1, 1)



#### Extended Comprehension Syntax for Sets and Dictionaries

*Just like list comprehensions and generator expressions, both set and dictionary comprehensions support the nested if clauses to filter items out of the result. The following codes collect squares of even items in a range*


```python
[x*x for x in range(10) if x%2 == 0] # lists are ordered
```




    [0, 4, 16, 36, 64]




```python
{x*x for x in range(10) if x%2 == 0} # But sets are not
```




    {0, 4, 16, 36, 64}




```python
{x: x*x for x in range(10) if x%2 == 0} # Neither are dict keys
```




    {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}



*Nested for loops work as well, although the unoredered and no-duplicates nature of set and dict comprehensions make a little bit hard to decipher*


```python
[x+y for x in [1,2,3] for y in [4,5,6]] # Lists keep duplicates
```




    [5, 6, 7, 6, 7, 8, 7, 8, 9]




```python
{x+y for x in [1,2,3] for y in [4,5,6]} # But sets do not
```




    {5, 6, 7, 8, 9}




```python
{x: y for x in [1,2,3] for y in [4,5,6]} # Neither do dict keys
```




    {1: 6, 2: 6, 3: 6}



*The set and dictionary varities support any type of iterator, like lists, ranges, dictionaries, tuples, files. Literally anything that support iteration protocol*


```python
{x+y for x in 'ab' for y in 'cd'}
```




    {'ac', 'ad', 'bc', 'bd'}




```python
{x+y: (ord(x), ord(y)) for x in 'ab' for y in 'cd'}
```




    {'ac': (97, 99), 'ad': (97, 100), 'bc': (98, 99), 'bd': (98, 100)}




```python
{k*2 for k in ['spam','ham','sausage'] if k[0] == 's'}
```




    {'sausagesausage', 'spamspam'}




```python
{k.upper(): k*2 for k in ['spam','ham','sausage'] if k[0] == 's'}
```




    {'SAUSAGE': 'sausagesausage', 'SPAM': 'spamspam'}



#### Timing Iteration Alternatives

*We've encountered quite a few iteration alternatives in this book. To summarize, list comprehensions have slightly better performance than for loop statements do, and the performance of the built-in map function depends on calling patterns. Although generator expressions tend to be slighter slower than list comprehensions, they save memory space at least. All of what has been mentioned above are true today. But you still need a timing module to measure the performance of your scripts because of ever-changing Python's internals.*

#### Timing Script


```python
file1.close()
```


```python
# %load mytimer.py
import time
reps = 1000
repslist = range(reps)
def timer(func,*pargs, **kargs):
	start = time.clock() 
	for i in repslit:
		res.append(abs(x))
	return res
def listComp():
	return [abs(x) for x in repslist]
def mapCall():
	return list(map(abs,repslist))
def genExpr():
	return list(abs(x) for x in repslist)
def genFunc():
	def gen():
		for x in repslit:
			yield abs(x)
	return list(gen())
print(sys.version)

for test in (forLoop,listComp,mapCall, genExpr, genFunc):
	elasped, result = mytimer.timer(test)
	print('-'*33)
	print('%-9s: %.5f => [%s...%s]'%(test.__name__,elasped,result[0],result[-1]))
```


```python
file1 = open('mytimer.py','w')
```


```python
file1.write("import time\nreps = 1000\nrepslist=range(reps)\n\n")
```




    46




```python
file1.write("def timer(func,*pargs,**kargs):\n\tstart = time.clock()\n")
```




    54




```python
file1.write("\tfor i in repslist:\n\t\tret = func(*pargs,**kargs)\n")
```




    49




```python
file1.write("\telapsed = time.clock() - start\n\treturn (elapsed,ret)")
```




    53




```python
file1.close()
```


```python
from imp import reload
```


```python
reload(mytimer)
```




    <module 'mytimer' from '/home/ma-user/work/mytimer.py'>




```python
# %load mytimer.py
import time
reps = 1000
repslist=range(reps)

def timer(func,*pargs,**kargs):
	start = time.clock()
	for i in repslist:
		ret = func(*pargs,**kargs)
	elapsed = time.clock() - start
	return (elapsed,ret)
```


```python
file2 = open('timeseqs.py','w')
file2.write('import sys, mytimer\n')
file2.write('reps = 1000\n')
file2.write('repslist = range(reps)\n')
file2.write('def forLoop():\n')
file2.write("\tres = [] \n")
file2.write("\tfor x in repslist:\n")
file2.write("\t\tres.append(abs(x))\n")
file2.write("\treturn res\n")
file2.write("def listComp():\n")
file2.write("\treturn [abs(x) for x in repslist]")
file2.write("\ndef mapCall():\n")
file2.write("\treturn list(map(abs,repslist))")
file2.write("\ndef genExpr():\n")
file2.write("\treturn list(abs(x) for x in repslist)\n")
file2.write("def genFunc():\n")
file2.write("\tdef gen():\n")
file2.write("\t\tfor x in repslist:\n")
file2.write("\t\t\tyield abs(x)\n")
file2.write("\treturn list(gen())\n")
file2.write("print(sys.version)\n")
file2.write("for test in (forLoop,listComp,mapCall, genExpr, genFunc):\n")
file2.write("\telasped, result = mytimer.timer(test)\n")
file2.write("\tprint('-'*33)\n")
file2.write("\tprint('%-9s: %.5f => [%s...%s]'%(test.__name__,elasped,result[0],result[-1]))")
```




    78




```python
file2.close()
```


```python
%run timeseqs.py
```

    3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
    [GCC 7.2.0]
    ---------------------------------
    forLoop  : 0.10199 => [0...999]
    ---------------------------------
    listComp : 0.06049 => [0...999]
    ---------------------------------
    mapCall  : 0.03280 => [0...999]
    ---------------------------------
    genExpr  : 0.09077 => [0...999]
    ---------------------------------
    genFunc  : 0.08916 => [0...999]


1. *In the mytimer.py, time module will give us the current time with precision that depends sytem platform we are operating on.*
2. * The range call is hoisted out of the timing loop, so its construction cost is not charged to the timed function in Python 2.6. In 3.0 range is an iterator, so this step isn't required (but doesn't hurt)*
3. *The reps count is a global variable so that you change its value anytime outside of this moudle by using mytimer.reps = N*


```python
mytimer.reps = 10000
ti
```


```python
%run timeseqs.py
```

    3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
    [GCC 7.2.0]
    ---------------------------------
    forLoop  : 0.10372 => [0...999]
    ---------------------------------
    listComp : 0.06011 => [0...999]
    ---------------------------------
    mapCall  : 0.03368 => [0...999]
    ---------------------------------
    genExpr  : 0.09174 => [0...999]
    ---------------------------------
    genFunc  : 0.08882 => [0...999]


*For a larger perspective, mytimer becomes the module which we can import anywhere and anytime, and use any utilities within this module. You might need a refresher for module attributes and if you do, just see Chapter 3's coverage about it*

*If you study this code and its output long enough, you'll see the generator expressions run slower than list comprehensions. The internal implementations of wrapping a generator expression in a list call and a square-bracketed list comprehension seems to differ.*


```python
file1 = open('mytimer.py','w')
file1.write("import time\nreps = 1000\nrepslist=range(reps)\n\n")
file1.write("def timer(func,*pargs,**kargs):\n\tstart = time.clock()\n")
file1.write("\tfor i in repslist:\n\t\tret = func(*pargs,**kargs)\n")
file1.write("\telapsed = time.clock() - start\n\treturn (elapsed,ret)")
file1.close()

file3 = open('timeseqs.py','w')
file3.write('import sys, mytimer\n')
file3.write('reps = 1000\n')
file3.write('repslist = range(reps)\n')
file3.write('def forLoop():\n')
file3.write("\tres = [] \n")
file3.write("\tfor x in repslist:\n")
file3.write("\t\tres.append(x+10)\n")
file3.write("\treturn res\n")
file3.write("def listComp():\n")
file3.write("\treturn [ x + 10 for x in repslist]")
file3.write("\ndef mapCall():\n")
file3.write("\treturn list(map((lambda x: x+10),repslist))")
file3.write("\ndef genExpr():\n")
file3.write("\treturn list(x+10 for x in repslist)\n")
file3.write("def genFunc():\n")
file3.write("\tdef gen():\n")
file3.write("\t\tfor x in repslist:\n")
file3.write("\t\t\tyield x+10\n")
file3.write("\treturn list(gen())\n")
file3.write("print(sys.version)\n")
file3.write("for test in (forLoop,listComp,mapCall, genExpr, genFunc):\n")
file3.write("\telasped, result = mytimer.timer(test)\n")
file3.write("\tprint('-'*33)\n")
file3.write("\tprint('%-9s: %.5f => [%s...%s]'%(test.__name__,elasped,result[0],result[-1]))")
file3.close()
```


```python
%run timeseqs.py
```

    3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
    [GCC 7.2.0]
    ---------------------------------
    forLoop  : 0.09105 => [10...1009]
    ---------------------------------
    listComp : 0.04521 => [10...1009]
    ---------------------------------
    mapCall  : 0.09926 => [10...1009]
    ---------------------------------
    genExpr  : 0.07011 => [10...1009]
    ---------------------------------
    genFunc  : 0.07133 => [10...1009]


#### Timing Module Alternatives

*The timing module of the prior section works, but it seems a little bit primitive on multiple fronts*

* The time.clock call works mageneficiently on Windows, but does't work better than time.time call does on some Unix platforms.

* You can change the number of repetitions only on module level cause it is a global variable. Hence, the action you take will cause some malfunctions for other users whilst they are importing this function.

* In order to take random system load fluctuations into account, it might be better to select the best time rather than the total time.


```python
file3 = open('mytimer.py', 'w')
file3.write('"""\n')
file3.write("""timer(spam,1,2,a=3,b=4,_reps=1000) calls and times spam(1,2,a=3)\n""")
file3.write("_reps times, and returns total time for all runs, with final result;\n")
file3.write("best(spam, 1, 2, a=3, b=4, _reps=50) runs best-of-N timer to filter out\n")
file3.write("any system load variation, and returns best time among _reps tests\n")
file3.write('"""')
file3.write('\n')

file3.write("import time, sys\n")
file3.write("if sys.platform[:3] == 'win':\n")
file3.write("\ttimefunc = time.clock\n")
file3.write("else:\n")
file3.write("\ttimefunc = time.time\n")
file3.write("\n")
file3.write("def trace(*args): pass\n")
file3.write("def timer(func,*pargs,**kargs):\n\t_reps= kargs.pop('_reps',1000)\n")
file3.write("\ttrace(func,pargs,kargs,_reps)\n")
file3.write("\trepslist = range(_reps)\n")
file3.write("\tstart = timefunc()\n")
file3.write("\tfor i in repslist:\n")
file3.write("\t\tret=func(*pargs,**kargs)\n")
file3.write("\telapsed = timefunc()-start\n")
file3.write("\treturn (elapsed, ret)\n")

file3.write("\n")
file3.write("def best(func, *pargs, **kargs): \n")
file3.write("\t_reps = kargs.pop('_reps',50)\n")
file3.write("\tbest = 2**32\n")
file3.write("\tfor i in range(_reps): \n")
file3.write("\t\t(time,ret) = timer(func, *pargs,_reps=1,**kargs)\n")
file3.write("\t\tif time < best: best = time\n")
file3.write("\treturn (best, ret)")

file3.close()
```


```python
# %load mytimer.py
"""
timer(spam,1,2,a=3,b=4,_reps=1000) calls and times spam(1,2,a=3)
_reps times, and returns total time for all runs, with final result;
best(spam, 1, 2, a=3, b=4, _reps=50) runs best-of-N timer to filter out
any system load variation, and returns best time among _reps tests
"""
import time, sys
if sys.platform[:3] == 'win':
	timefunc = time.clock
else:
	timefunc = time.time

def trace(*args): pass
def timer(func,*pargs,**kargs):
	_reps= kargs.pop('_reps',1000)
	trace(func,pargs,kargs,_reps)
	repslist = range(_reps)
	start = timefunc()
	for i in repslist:
		ret=func(*pargs,**kargs)
	elapsed = timefunc()-start
	return (elapsed, ret)

def best(func, *pargs, **kargs): 
	_reps = kargs.pop('_reps',50)
	best = 2**32
	for i in range(_reps): 
		(time,ret) = timer(func, *pargs,_reps=1,**kargs)
		if time < best: best = time
	return (best, ret)
```


```python
file3 = open('timeseqs.py','w')
file3.write('import sys, mytimer\n')
file3.write('reps = 1000\n')
file3.write('repslist = range(reps)\n')
file3.write('def forLoop():\n')
file3.write("\tres = [] \n")
file3.write("\tfor x in repslist:\n")
file3.write("\t\tres.append(x+10)\n")
file3.write("\treturn res\n")
file3.write("def listComp():\n")
file3.write("\treturn [ x + 10 for x in repslist]")
file3.write("\ndef mapCall():\n")
file3.write("\treturn list(map((lambda x: x+10),repslist))")
file3.write("\ndef genExpr():\n")
file3.write("\treturn list(x+10 for x in repslist)\n")
file3.write("def genFunc():\n")
file3.write("\tdef gen():\n")
file3.write("\t\tfor x in repslist:\n")
file3.write("\t\t\tyield x+10\n")
file3.write("\treturn list(gen())\n")
file3.write("print(sys.version)\n")
file3.write("for test in (forLoop,listComp,mapCall, genExpr, genFunc):\n")
file3.write("\telasped, result = mytimer.timer(test)\n")
file3.write("\tprint('-'*33)\n")
file3.write("\tprint('%-9s: %.5f => [%s...%s]'%(test.__name__,elasped,result[0],result[-1]))")
file3.close()
```


```python
import imp
imp.reload(mytimer)
```




    <module 'mytimer' from '/home/ma-user/work/mytimer.py'>




```python
%run timeseqs.py
```

    3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
    [GCC 7.2.0]
    ---------------------------------
    forLoop  : 0.08799 => [10...1009]
    ---------------------------------
    listComp : 0.04401 => [10...1009]
    ---------------------------------
    mapCall  : 0.09801 => [10...1009]
    ---------------------------------
    genExpr  : 0.07087 => [10...1009]
    ---------------------------------
    genFunc  : 0.06869 => [10...1009]



```python
file3 = open('timeseqs.py','w')
file3.write('import sys, mytimer\n')
file3.write('reps = 1000\n')
file3.write('repslist = range(reps)\n')
file3.write('def forLoop():\n')
file3.write("\tres = [] \n")
file3.write("\tfor x in repslist:\n")
file3.write("\t\tres.append(x+10)\n")
file3.write("\treturn res\n")
file3.write("def listComp():\n")
file3.write("\treturn [ x + 10 for x in repslist]")
file3.write("\ndef mapCall():\n")
file3.write("\treturn list(map((lambda x: x+10),repslist))")
file3.write("\ndef genExpr():\n")
file3.write("\treturn list(x+10 for x in repslist)\n")
file3.write("def genFunc():\n")
file3.write("\tdef gen():\n")
file3.write("\t\tfor x in repslist:\n")
file3.write("\t\t\tyield x+10\n")
file3.write("\treturn list(gen())\n")
file3.write("print(sys.version)\n")
file3.write("for tester in (mytimer.timer,mytimer.best):\n")
file3.write("\tprint('<%s>' % tester.__name__)\n")
file3.write("\tfor test in (forLoop, listComp, mapCall, genExpr, genFunc):\n")
file3.write("\t\telasped, result = tester(test)\n")
file3.write("\t\tprint('-'*35)\n")
file3.write("\t\tprint('%-9s: %.5f => [%s...%s]'%(test.__name__,elasped,result[0],result[-1]))")
file3.close()
```


```python
# %load timeseqs.py
import sys, mytimer
reps = 1000
repslist = range(reps)
def forLoop():
	res = [] 
	for x in repslist:
		res.append(x+10)
	return res
def listComp():
	return [ x + 10 for x in repslist]
def mapCall():
	return list(map((lambda x: x+10),repslist))
def genExpr():
	return list(x+10 for x in repslist)
def genFunc():
	def gen():
		for x in repslist:
			yield x+10
	return list(gen())
print(sys.version)
for tester in (mytimer.timer,mytimer.best):
	print('<%s>' % tester.__name__)
	for test in (forLoop, listComp, mapCall, genExpr, genFunc):
		elasped, result = tester(test)
		print('-'*35)
		print('%-9s: %.5f => [%s...%s]'%(test.__name__,elasped,result[0],result[-1]))
```


```python
%run timeseqs.py
```

    3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
    [GCC 7.2.0]
    <timer>
    -----------------------------------
    forLoop  : 0.08883 => [10...1009]
    -----------------------------------
    listComp : 0.04536 => [10...1009]
    -----------------------------------
    mapCall  : 0.09935 => [10...1009]
    -----------------------------------
    genExpr  : 0.07744 => [10...1009]
    -----------------------------------
    genFunc  : 0.07182 => [10...1009]
    <best>
    -----------------------------------
    forLoop  : 0.00008 => [10...1009]
    -----------------------------------
    listComp : 0.00004 => [10...1009]
    -----------------------------------
    mapCall  : 0.00009 => [10...1009]
    -----------------------------------
    genExpr  : 0.00006 => [10...1009]
    -----------------------------------
    genFunc  : 0.00006 => [10...1009]



```python
file5 = open('mytimer.py','w')
file5.write('"""\n')
file5.write("Use 3.0 keyword-only default arguments, instead of ** and dict pops.\n")
file5.write("No need to hoist range() out of test in 3.0: a generator, not a list\n")
file5.write('"""\n')

file5.write('import time, sys\n')
file5.write('trace = lambda *args: None\n')
file5.write("timefunc = time.clock if sys.platform == 'win32' else time.time\n")
file5.write("\n")

file5.write("def timer(func,*pargs, _reps=1000, **kargs):\n")
file5.write("\ttrace(func,pargs,kargs,_reps)\n")
file5.write("\tstart=timefunc()\n")
file5.write("\tfor i in range(_reps):\n")
file5.write("\t\tret=func(*pargs,**kargs)\n")
file5.write("\telapsed = timefunc()-start\n")
file5.write("\treturn (elapsed,ret)\n")
file5.write("def best(func,*pargs,_reps=50,**kargs):\n")
file5.write("\tbest = 2**32\n")
file5.write("\tfor i in range(_reps):\n")
file5.write("\t\t(time,ret) = timer(func,*pargs,_reps=1,**kargs)\n")
file5.write("\t\tif time < best: best = time\n")
file5.write("\treturn (best,ret)")
file5.close()
```


```python
# %load mytimer.py
"""
Use 3.0 keyword-only default arguments, instead of ** and dict pops.
No need to hoist range() out of test in 3.0: a generator, not a list
"""
import time, sys
trace = lambda *args: None
timefunc = time.clock if sys.platform == 'win32' else time.time

def timer(func,*pargs, _reps=1000, **kargs):
	trace(func,pargs,kargs,_reps)
	start=timefunc()
	for i in range(_reps):
		ret=func(*pargs,**kargs)
	elapsed = timefunc()-start
	return (elapsed,ret)
def best(func,*pargs,_reps=50,**kargs):
	best = 2**32
	for i in range(_reps):
		(time,ret) = timer(func,*pargs,_reps=1,**kargs)
		if time < best: best = time
	return (best,ret)
```


```python
%run timeseqs.py
```

    3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 18:10:19) 
    [GCC 7.2.0]
    <timer>
    -----------------------------------
    forLoop  : 0.08841 => [10...1009]
    -----------------------------------
    listComp : 0.04325 => [10...1009]
    -----------------------------------
    mapCall  : 0.09851 => [10...1009]
    -----------------------------------
    genExpr  : 0.06866 => [10...1009]
    -----------------------------------
    genFunc  : 0.06768 => [10...1009]
    <best>
    -----------------------------------
    forLoop  : 0.00008 => [10...1009]
    -----------------------------------
    listComp : 0.00004 => [10...1009]
    -----------------------------------
    mapCall  : 0.00009 => [10...1009]
    -----------------------------------
    genExpr  : 0.00006 => [10...1009]
    -----------------------------------
    genFunc  : 0.00006 => [10...1009]



```python
from mytimer import timer, best
```


```python
def power(x,y): return x**y
```


```python
timer(power,2,32)
```




    (0.00031685829162597656, 4294967296)




```python
timer(power,2,32,_reps=10000000)
```




    (3.1611108779907227, 4294967296)




```python
timer(power,2,10000000)[0]
```




    30.692503452301025




```python
best(power,2,32)
```




    (4.76837158203125e-07, 4294967296)




```python
best(power,2,10000)[0]
```




    1.5020370483398438e-05




```python
best(power,2,10000,_reps=500)[0]
```




    1.5020370483398438e-05




```python
cat /proc/cpuinfo
```

    processor	: 0
    vendor_id	: GenuineIntel
    cpu family	: 6
    model		: 79
    model name	: Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz
    stepping	: 1
    microcode	: 0x1
    cpu MHz		: 2599.996
    cache size	: 35840 KB
    physical id	: 0
    siblings	: 4
    core id		: 0
    cpu cores	: 2
    apicid		: 0
    initial apicid	: 0
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch arat invpcid_single ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm rdseed adx smap xsaveopt spec_ctrl intel_stibp flush_l1d
    bogomips	: 5199.99
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 42 bits physical, 48 bits virtual
    power management:
    
    processor	: 1
    vendor_id	: GenuineIntel
    cpu family	: 6
    model		: 79
    model name	: Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz
    stepping	: 1
    microcode	: 0x1
    cpu MHz		: 2599.996
    cache size	: 35840 KB
    physical id	: 0
    siblings	: 4
    core id		: 0
    cpu cores	: 2
    apicid		: 1
    initial apicid	: 1
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch arat invpcid_single ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm rdseed adx smap xsaveopt spec_ctrl intel_stibp flush_l1d
    bogomips	: 5199.99
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 42 bits physical, 48 bits virtual
    power management:
    
    processor	: 2
    vendor_id	: GenuineIntel
    cpu family	: 6
    model		: 79
    model name	: Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz
    stepping	: 1
    microcode	: 0x1
    cpu MHz		: 2599.996
    cache size	: 35840 KB
    physical id	: 0
    siblings	: 4
    core id		: 1
    cpu cores	: 2
    apicid		: 2
    initial apicid	: 2
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch arat invpcid_single ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm rdseed adx smap xsaveopt spec_ctrl intel_stibp flush_l1d
    bogomips	: 5199.99
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 42 bits physical, 48 bits virtual
    power management:
    
    processor	: 3
    vendor_id	: GenuineIntel
    cpu family	: 6
    model		: 79
    model name	: Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz
    stepping	: 1
    microcode	: 0x1
    cpu MHz		: 2599.996
    cache size	: 35840 KB
    physical id	: 0
    siblings	: 4
    core id		: 1
    cpu cores	: 2
    apicid		: 3
    initial apicid	: 3
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch arat invpcid_single ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm rdseed adx smap xsaveopt spec_ctrl intel_stibp flush_l1d
    bogomips	: 5199.99
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 42 bits physical, 48 bits virtual
    power management:
    
    processor	: 4
    vendor_id	: GenuineIntel
    cpu family	: 6
    model		: 79
    model name	: Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz
    stepping	: 1
    microcode	: 0x1
    cpu MHz		: 2599.996
    cache size	: 35840 KB
    physical id	: 1
    siblings	: 4
    core id		: 0
    cpu cores	: 2
    apicid		: 4
    initial apicid	: 4
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch arat invpcid_single ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm rdseed adx smap xsaveopt spec_ctrl intel_stibp flush_l1d
    bogomips	: 5199.99
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 42 bits physical, 48 bits virtual
    power management:
    
    processor	: 5
    vendor_id	: GenuineIntel
    cpu family	: 6
    model		: 79
    model name	: Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz
    stepping	: 1
    microcode	: 0x1
    cpu MHz		: 2599.996
    cache size	: 35840 KB
    physical id	: 1
    siblings	: 4
    core id		: 0
    cpu cores	: 2
    apicid		: 5
    initial apicid	: 5
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch arat invpcid_single ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm rdseed adx smap xsaveopt spec_ctrl intel_stibp flush_l1d
    bogomips	: 5199.99
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 42 bits physical, 48 bits virtual
    power management:
    
    processor	: 6
    vendor_id	: GenuineIntel
    cpu family	: 6
    model		: 79
    model name	: Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz
    stepping	: 1
    microcode	: 0x1
    cpu MHz		: 2599.996
    cache size	: 35840 KB
    physical id	: 1
    siblings	: 4
    core id		: 1
    cpu cores	: 2
    apicid		: 6
    initial apicid	: 6
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch arat invpcid_single ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm rdseed adx smap xsaveopt spec_ctrl intel_stibp flush_l1d
    bogomips	: 5199.99
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 42 bits physical, 48 bits virtual
    power management:
    
    processor	: 7
    vendor_id	: GenuineIntel
    cpu family	: 6
    model		: 79
    model name	: Intel(R) Xeon(R) CPU E5-2690 v4 @ 2.60GHz
    stepping	: 1
    microcode	: 0x1
    cpu MHz		: 2599.996
    cache size	: 35840 KB
    physical id	: 1
    siblings	: 4
    core id		: 1
    cpu cores	: 2
    apicid		: 7
    initial apicid	: 7
    fpu		: yes
    fpu_exception	: yes
    cpuid level	: 13
    wp		: yes
    flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss ht syscall nx pdpe1gb rdtscp lm constant_tsc rep_good nopl xtopology eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch arat invpcid_single ssbd ibrs ibpb stibp fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm rdseed adx smap xsaveopt spec_ctrl intel_stibp flush_l1d
    bogomips	: 5199.99
    clflush size	: 64
    cache_alignment	: 64
    address sizes	: 42 bits physical, 48 bits virtual
    power management:
    



```python
cat /proc/cpuinfo| grep "physical id"| sort| uniq| wc -l
```

    2



```python
cat /proc/cpuinfo| grep "cpu cores"| uniq
```

    cpu cores	: 2



```python
cat /proc/cpuinfo| grep "processor"| wc -
```

          8      24     112 -


*It might be useful as well to experiment with using the new str.fornat method

#### Function Gotchas

* Local Names Are Detected Statically


```python
X = 99
def selector(): # X used but not assigned
    print(X)    # X found in global scope
selector()
```

    99



```python
def selector():
    print(X)
    X = 88
try:
    selector()
except:
    print("local variable 'X' referenced before assignment")
```

    local variable 'X' referenced before assignment


*The problem occurs because assigned names are treated as locals everywhere in a function, not just after the statements where they are assigned*


```python
def selector():
    global X
    print(X)
    X = 88
    print(X)
try: 
    selector()
except:
    print("local variable X referenced before assignment")
```

    99
    88



```python
X = 99
def selector():
    import __main__
    print(__main__.X)
    X = 88
    print(X)
```


```python
selector()
```

    99
    88


*Imports, =, nested defs, nested classes, and so on are all susceptible to this behavior.*

* Defaults and Mutable Objects


```python
def saver(x=[]):
    x.append(1)
    print(x)
saver([2])
```

    [2, 1]



```python
saver([2])
```

    [2, 1]



```python
saver()
saver()
saver()
```

    [1]
    [1, 1]
    [1, 1, 1]


*You don't get a new list every time the function is called, so the list grows with each new append; it is not reset to empty on each call*


```python
def saver(x=[]):
    x = x + [1]
    print(x)
```


```python
saver()
```

    [1]



```python
saver()
saver()
saver()
```

    [1]
    [1]
    [1]



```python
def saver(x=None):
    if x is None:
        x = []
    x.append(1)
    print(x)
```


```python
saver([2])
```

    [2, 1]



```python
saver(),saver(),saver()
```

    [1]
    [1]
    [1]





    (None, None, None)




```python
def saver(x=None):
    x = x or []
    x.append(1)
    print(x)
saver([2])
saver()
saver()
```

    [2, 1]
    [1]
    [1]



```python
[2,3] or [], None or []
```




    ([2, 3], [])




```python
def saver():
    saver.x.append(1)
    print(saver.x)
```


```python
saver.x = []
saver()
saver()
saver()
```

    [1]
    [1, 1]
    [1, 1, 1]


*This is another way to achieve the effect of mutable defaults in a possibly less confusing way to use the function attributes we discussed in previous chapter 19*

* Functions without returns


```python
def proc(x):
    print(x)
x = proc('testing 123...')
```

    testing 123...



```python
print(x)
```

    None


*Considering the following scenarios, this is really worthing knowing, cause many built-in functions are defined without returning a result.*


```python
List = [1,2,3]
List = List.append(4)
print(List)
```

    None


* Enclosing Scope Loop Variables

*We described this gotcha in Chapter 17’s discussion of enclosing function scopes, but as a reminder, be careful about relying on enclosing function scope lookup for variables that are changed by enclosing loops—all such references will remember the value of the last loop iteration.*

#### Chapter Summary

*This chapter wrapped up our coverage of built-in comprehension and iteration tools. It explored list comprehensions in the context of functional tools and presented generator functions and expressions as additional iteration protocol tools. As a finale, we also measured the performance of iteration alternatives, and we closed with a review of common function-related mistakes to help you avoid pitfalls.*

This concludes the functions part of this book. In the next part, we will study modules— the topmost organizational structure in Python, and the structure in which our functions always live. After that, we will explore classes, tools that are largely packages of functions with special first arguments. As we’ll see, user-defined classes can implement objects that tap into the iteration protocol, just like the generators and iterables we met
here. Everything we have learned in this part of the book will apply when functions pop up later in the context of class methods.

#### Test Your Knowledge: Part IV Exercises


```python
def basics(x):
    print(x)
basics(1),basics('basics'),basics([1,2,3,4]),basics(dict(a=1,b=2))
```

    1
    basics
    [1, 2, 3, 4]
    {'a': 1, 'b': 2}





    (None, None, None, None)




```python
try:
    basics()
except:
    print("basics() missing 1 required positional argument: 'x'")
```

    basics() missing 1 required positional argument: 'x'



```python
try:
    basics(1,2)
except:
    print("basics() takes 1 positional argument but 2 were given")
```

    basics() takes 1 positional argument but 2 were given



```python
file = open('adder.py','w')
file.write('def adder(x,y):\n\treturn x+y')
file.close()
```


```python
file = open('adder.py','a')
file.write("\nadder(1,2)\nadder('1','2')\nadder(1.23,3.45)\n")
file.close()
```


```python
%run adder.py
```


```python
file = open('adder.py','a')
file.write("\nprint(adder(1,2))\nprint(adder('1','2'))\nprint(adder(1.23,3.45))")
```




    64




```python
file.close()
```


```python
%run adder.py
```

    3
    12
    4.68



```python

```
