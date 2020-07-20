```python
#!/usr/bin/env python
# coding: utf-8
# This chapter will cover the advanced function topics theme, and revisit list comprehension and iteration. We won't talk about user-defined classes until Part VI-Classes. A thorough summary of various tools we mentioned before is going to be done since this is the last pass we'll make over built-in iteration tools.
# ### List Comprehensions Revisited: Functional Tools
# In addition to some built-in functional programming tools, Python 3.0 also provides us with a more generalized tool--list comprehension--. List comprehensions are more flexible than such built-in funcitonal programming tool as map or filter or reduce because they can deal with arbitrary expressions rather than specific functions.
# #### List comprehensions Versus map

# In[1]:
ord('s'), chr(115)
# suppose we have to collect all the ASCII integer code of all characters in an entire string. Of course, we can use for loop statements.
# In[2]:
res = []
for x in 'spam':
    res.append(ord(x))
res
# Alternatively, we can achieve the same result by maping the built-in function map to each item in iterables.
# In[4]:
res = list(map(ord,'spam'))
res
# However, the most straightforward approach is to use a list comprehension.
# In[5]:
res = [ord(x) for x in 'spam']
res
# Syntactically, list comprehensions are enclosed in square brackets (to remind yoy that they construct lists).
# In[7]:
print([x**2 for x in range(10)])
print([x**3 for x in range(10)])
# In[9]:
list(map((lambda x: x **2), range(10)))
# #### Adding Tests and Nested Loops: filter

# In[10]:


[x for x in range(5) if x % 2 == 0]
list(filter((lambda x: x % 2 == 0), range(5)))


# In[11]:


res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)
res


# In[4]:


#import sys
#from tkinter import Button, mainloop
#x = Button(
#    text = 'Press me',
#    command = (lambda: sys.stdout.write('Spam\n')))
#x.pack()
#mainloop()


# In[5]:


[ x**2 for x in range(10) if x % 2 == 0]


# In[6]:


list(map((lambda x : x**2), filter((lambda x: x % 2 == 0), range(10))))


# [ expression for target1 in iterable1 [if condition1]
#              for target2 in iterable2 [if condition2]...
#              for targetN in iterableN [if conditionN]]

# In[7]:


res = [x + y for x in [0,1,2] for y in [100,200,300]]
res


# In[8]:


res = []
for x in [0,1,2]:
    for y in [100,200,300]:
        res.append(x+y)
res


# In[10]:


print([x + y for x in 'spam' for y in 'SPAM'], end = ' ')


# In[11]:


print([(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y%2 == 1])


# In[12]:


res = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x,y))


# In[13]:


res


# ### List Comprehensions and Matrixes

# In[10]:


M = [[1,2,3],
    [4,5,6],
    [7,8,9]]
N = [[2,2,2],
    [3,3,3],
    [4,4,4]]


# In[12]:


[row[0] for row in M]
[row[1] for row in M]
[row[2] for row in M]


# In[16]:


[M[row][1] for row in (0,1,2)]


# In[13]:


[M[row][col] * N[row][col] for row in range(3) for col in range(3)]
[[M[row][col] * N[row][col] for col in range(3) for row in range(3)]]


# In[1]:


f = open('mytimer.py','w')


# In[2]:


f.write('import time \n')


# In[5]:


f.write('reps = 1000 \n')
f.write('repslist = range(reps) \n')
f.write('def timer(func,*pargs,**kargs): \n')
f.write('\tstart = time.clock() \n')
f.write('\tfor i in repslist: \n')
f.write('\t\tret=func(*pargs,**kargs)\n\telapsed = time.clock() - start\n\treturn (elapsed, ret)')


# In[6]:


f.close()


# In[7]:


file = open('mytimer.py','r')


# In[8]:


file.read()


# In[11]:


[M[row][col] * N[row][col] for row in range(3) for col in range(3)]


# In[12]:


[[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]


# In[14]:


M


# In[2]:


from sympy import *


# In[3]:


init_printing()


# In[4]:


x,y,z = symbols('x,y,z')


# In[8]:


T = integrate(cos(3*x*y*z**2),x)


# In[10]:


help(print_python)


# In[17]:


from sympy.printing.mathml import print_mathml


# In[24]:


T= integrate(cos(3*x+y*z**2),x)


# In[26]:


import sympy.printing.mathml


# In[28]:


sympy.printing.mathml(T)


# In[31]:


get_ipython().system('pip install --upgrade pip')


# In[32]:


from chempy import *


# In[36]:


myfile = open('myfile','w')
myfile.write('aaa\n')
myfile.write('bbb\n')
myfile.write('ccc\n')
myfile.close()

open('myfile').readlines()


# In[2]:


[line.rstrip() for line in open('myfile').readlines()]
[line.rstrip() for line in open('myfile')]
list(map((lambda line: line.rstrip()), open('myfile')))


# In[3]:


list(map((lambda line: line.rstrip()),open('myfile')))


# `The list is a tuple, tuples are rows, and items in tuples are column values`

# In[4]:


listoftuple = [('bob',35,'mgr'),('mel',40,'dev')]


# In[5]:


[age for (name,age,job) in listoftuple]


# In[6]:


list(map((lambda row: row[1]),listoftuple))


# In[13]:


def gensquare(N):
    for i in range(N):
        yield i ** 2


# In[15]:


list(gensquare(4))


# In[54]:


f = open('myfile')
def genf():
    yield f.readline()


# In[55]:


t = genf()


# In[56]:


next(t)


# In[53]:


f.readline()


# #### Iterators Revisited: Generators 

# ------------------------

# Today Python supports procrastination much more than it did in the \
# past.

# * `Generator functions` are coded as normal def statements but use `yield` instead of `return` statements to return results one at a time, suspending and resuming their state between each
# * `Generator expressions` are similar to the list comprehensions of the prior section, but they return an object that produces results on demand instead of building a result list.

# In[4]:


def gensquares(N):
    for i in range(N):
        yield i**2


# In[5]:


for i in gensquares(5):
    print(i,end=' : ')


# In[6]:


x = gensquares(4)


# In[7]:


x


# In[8]:


id(x)


# In[9]:


iter(x) == x


# In[10]:


next(x)


# In[11]:


next(x)


# In[12]:


next(x)


# In[13]:


next(x)


# In[17]:


y = gensquares(10)


# In[18]:


y.__next__(), y.__next__(), y.__next__(), y.__next__(), y.__next__(), y.__next__(),y.__next__()


# In[19]:


def buildsquares(n):
    res = []
    for i in range(n): res.append(i**2)
    return res


# In[20]:


for x in buildsquares(5): print(x, end = ' : ')


# In[21]:


for x in [n ** 2 for n in range(5)]:
    print(x, end = ' : ')


# In[2]:


for x in map((lambda n: n**2), range(5)):
    print(x, end = ': ')


# #### Extended generator function protocol: send versus next

# In[1]:


def gen():
    for i in range(10):
        X = yield i
        print(X)


# In[2]:


G = gen()


# In[3]:


next(G)


# In[4]:


next(G), next(G), next(G), next(G)


# In[5]:


G.send(77)


# In[6]:


G.send(88), next(G)


# `G.send(X)` method of an object can be implemented on built-in generator objects only while the `G.__next__()` method can be applied to all iterable objects (both built-in type and user-defined classes)

# #### Gnenerator Expressions: Iterators Meet Comprehensions

# In[2]:


[x**2 for x in range(4)]


# In[6]:


G=(x**2 for x in range(4))


# In[7]:


next(G),next(G), next(G), next(G)


# *In all recent versions of Python, the notions of iterators and list comprehensions are combined in a new feature of the language, generator expression. In terms of syntax, generator expressions are just like normal list comprehension, but they are enclosed in parentheses instead of square brackets*

# In[8]:


[x**2 for x in range(4)] # List comprehension: build a list
(x**2 for x in range(4)) # Generator expression: make a iterable


# *In fact, at least on a function basis, coding a list comprehension is essentially the same as wrapping a generator expression in a list built-in call to force it to produce all its result in a list at once.*

# In[9]:


list(x**2 for x in range(4))


# *Operationally, generator expressions are very different-instead of returning the result in a list, they return a generator object, which in turn supports the iteration protocol to yield one piece of the result list at a time in any iteration context:*

# In[11]:


G = (x**2 for x in range(4))
next(G), next(G), next(G), next(G)


# In[12]:


for num in (x**2 for x in range(4)):
    print('%s, %s ' % (num, num/2.0) )


# *Therefore, the for loop can trigger the next iterator machinery under the hood of a generator expression just as following:*

# In[14]:


for num in (x**2 for x in range(4)):
    print('%s, %s' %(num, num/2.0))


# In[1]:


''.join(x.upper() for x in 'aaa,bbb,ccc'.split(','))
a,b,c = (x+'\n' for x in 'aaa,bbb,ccc'.split(','))


# In[2]:


a,b,c


# In[3]:


sum(x**2 for x in range(4)), sorted(x**2 for x in range(4)), sorted((x**2 for x in range(4)), reverse = True)


# In[6]:


any(['a','v','','ad']), help(any)


# In[7]:


all(['a','v','','ad']), help(any)


# #### Generator expressions versus map

# *Like list comprehensions, generator expressions are much more simpler to use than map is when the operation applied is not a function call (maybe a plus or mutilplication*

# In[9]:


list(map(abs,(-1,-2,3,-4))), list(abs(x) for x in (-1,-2,3,4)) # map function on tuple, generator expression


# In[11]:


list(map(lambda x: x *2, (1,2,3,4))), list(x*2 for x in (1,2,3,4))


# In[37]:


list( x+y for x,y in enumerate(range(1,18,2))), list(map((lambda x, y: x+y), range(1,len(range(1,18,2))),range(1,18,2)))


# In[1]:


list(map(lambda x:  x *2, (1,2,3,4))) #Nonfunciton case


# In[3]:


list(x*2 for x in (1,2,3,4)) # Simpler as generator?


# *The same holds true for text-processing use cases like the join call we saw earlier-a list comprehension makes an extra temporary list of results, which is a completely pointless this context because the list is not retained.*

# In[4]:


line = 'aaa,bbb,ccc'
''.join([x.upper() for x in line.split(',')]) # Makes a pointless list
''.join(x.upper() for x in line.split(',')) # Generates results
''.join(map(str.upper,line.split(',')))  # Generates results
''.join(x*2 for x in line.split(',')) # Simpler as generator?
''.join(map(lambda x: x * 2, line.split(',')))


# *If generator expressions are the sole item enclosed in other parentheses, the parentheses are not required around a geneator expression*

# In[2]:


sum(x**2 for x in range(4))


# In[3]:


sorted(x**2 for x in range(4))


# In[4]:


sorted((x**2 for x in range(4)), reverse = True)


# In[5]:


import math
list(map(math.sqrt, (x**2 for x in range(4))))


# *Generator expressions are usually treated as a memory-space optimization. They don't work the same way as the squrared-brakceted list comprehension does, which means they won't generate the result list all at once. Sometimes, they are not so efficent as list comprehensions (they might run slightly slower in practice). Probably, their best usage is only for very large result sets. Actually, in this chapter we'll code a timing script for measuring their performance in reality.*

# ### Generator functions versus Generator expression

# In[10]:


G = (c*4 for c in 'SPAM') # Generator expression


# In[11]:


list(G) # Force generator to produce all results


# In[12]:


list(G)


# *The equivalent counterpart (gnenerator function) require slightly more code, 
# but as a multistatement funciton it will be able to code more logic and use more statement information if needed.*

# In[3]:


def timesfour(S):
    for c in S:
        yield c * 4


# In[4]:


G = timesfour('spam')


# In[15]:


list(G)


# In[16]:


G = (c*4 for c in 'SPAM')
I = iter(G)
next(I), next(I), next(I), next(I)


# In[7]:


G = timesfour('spam')
I = iter(G)
next(I),next(I),next(I),next(I)

It = iter(timesfour('spam'))
It.__next__(), It.__next__(), It.__next__(), It.__next__()


# #### Generators Are Single-Iterator Objects

# *Both generator function and generator expressions are their own iterators and thus support just one active iteration*

# In[1]:


G = (c*4 for c in 'SPAM')
iter(G) is G


# In[1]:


def gene(c):
    for i in c:
        yield i*4


# In[2]:


T = gene('SPAM')


# In[3]:


iter(T) is T, id(iter(T)) is id(T)


# In[4]:


G = (c*4 for c in 'SPAM')
I1 = iter(G)
next(I1), next(I1)


# In[5]:


I2 = iter(G)


# In[7]:


next(I2) # second iterator at same position


# In[8]:


I3 = iter(c*4 for c in 'SPAM')
I4 = (c*4 for c in 'SPAM')


# In[9]:


next(I3), next(I4)


# *The same holds true for generator functions-the following def statement-based equivalent supports just one active iterator and is exhausted after one pass*

# In[10]:


def timesfour(S):
    for c in S:
        yield c * 4


# In[11]:


G = timesfour('SPAM')
iter(G) is G


# In[12]:


I1, I2 = iter(G), iter(G)
next(I1), next(I1), next(I2)


# *Generator funcitons or generator expressions don't work the same way as some built-in types do. Such built-in types as lists or dictionarys support multiple iterators and passes and will reflect their in-place changes in active iterators*

# In[13]:


L = [1,2,3,4]
I1, I2 = iter(L), iter(L)
next(I1), next(I1), next(I2) 


# In[15]:


del L[2:]
try:
    next(I1) # Changes reflected in iterators
except:
    print('Changes are reflected in iterators')


# # Emulating zip and map with Iteration Tools

# In[2]:


S1 = 'abc'
S2 = 'xyz123'
list(zip(S1,S2)) # zip pairs items from iterables


# In[4]:


list(zip([-2,-1,0,1,2])) # Single sequence: 1-array tuples


# In[5]:


list(zip([1,2,3],[2,3,4,5])) # N sequence: N-array tuples


# *map passes paired itenms to a function, truncates*

# In[6]:


list(map(abs,[-2,-1,0,1,2]))


# In[7]:


list(map(pow, [1,2,3],[2,3,4,5]))


# #### Coding your own map(func,...)

# In[2]:


# map(func,seqs,...)workable with zip
def mymap(func,*seqs):
    res = []
    for args in zip(*seqs):
        res.append(func(*args))
    return res


# In[3]:


print(mymap(abs,[-2,-1,0,1,2]))
print(mymap(pow,[1,2,3],[2,3,4,5]))


# In[5]:


for args in zip([1,2,3],[2,3,4,5]):
    print(args)


# In[8]:


for args in zip([-2,-1,0,1,2]):
    print(args)


# In[9]:


def mymap(func,*seqs):
    return [func(*args) for args in zip(*seqs)]


# In[10]:


print(mymap(abs,[-2,-1,0,1,2]))
print(mymap(pow,[1,2,3],[2,3,4,5]))


# In[11]:


def mymap(func,*seqs):
    res = []
    for args in zip(*seqs):
        yield func(*args)
def mymap(func,*seqs):
    return (func(*args) for args in zip(*seqs))


# In[12]:


print(mymap(abs,[-2,-1,0,1,2]))
print(mymap(pow,[1,2,3],[2,3,4,5]))


# In[1]:


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


# In[9]:


S1, S2 = 'abc', 'xyz123'
seqs = [list(S) for S in ('abc','xyz123')]


# In[3]:


seqs


# In[10]:


res = []
res.append(tuple(S.pop(0) for S in seqs))
print(res)

res = []
res.append(tuple(S.pop(0) for S in seqs))
print(res)

res = []
res.append(tuple(S.pop(0) for S in seqs))
print(res)


# In[11]:


print(myzip(S1,S2))


# In[25]:


seqs = [list(S) for S in ('abc','xyz123')]
res = []
res.append(tuple((S.pop(0) if S else pad) for S in seqs))
print(res)


# In[18]:


seqs = [list(S) for S in ('abc','xyz123')]


# In[19]:


seqs


# In[20]:


res = []


# In[21]:


res.append(tuple((S.pop(0) if S else pad)) for S in seqs)


# In[24]:


mymapPad(S1,S2)


# In[26]:


print(mymapPad(S1,S2))


# In[28]:


print(mymapPad(S1,S2,pad = 99))


# *Alternate implementation with lengths*

# In[7]:


def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    print(minlen)
    print([tuple(S[i] for S in seqs) for i in range(minlen)])
    return [tuple(S[i] for S in seqs) for i in range(minlen)]


# In[8]:


S1, S2 = 'abc', 'xyz123'
print(myzip(S1,S2))


# In[12]:


def mymapPad(*seqs, pad = None):
    maxlen = max(len(S) for S in seqs)
    index = range(maxlen)
    return [tuple((S[i] if len(S) > i else pad) for S in seqs) for i in index]


# In[13]:


print(mymapPad(S1,S2))
print(mymapPad(S1,S2,pad = 99))


# In[19]:


[tuple(S[i] for S in ['abc','xyz123']) for i in range(len('abc'))]


# In[21]:


tuple(S[i] for S in ['abc','xyz123'] for i in range(len('abc')))


# In[22]:


def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    for i in range(minlen):
        for S in seqs:
            return tuple(S[i])


# *Notice that here we use indexing and the built-in function length, which means we assume that we are dealing with sequences rather than arbitrary iterables. The outer comprehensions step through argument index ranges while the innner step through the passed-in sequence to pull out arguments in parallel*

# In[24]:


# Using generators
def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))
print(list(myzip(S1,S2)))


# *In this case, a list call is needed to activate the generators and iterators to produce results*

# In[1]:


def myzip(*args):
    iters = map(iter,args)
    while iters:
        res = [next(i) for i in iters]
        yield tuple(res)


# #### Why you will care : One-Shot Iterations

# In[2]:


def myzip(*args):
    iters = map(iter,args)
    print(iters)
    while iters:
        res = [next(i) for i in iters]
        print(iters, res)
        yield tuple(res)


# `list(myzip('abc','lmnop'))`
# This code works fine in Python 2.6 as is:
# `[('a','l'),('b','m'),('c','n')]`
# But it falls into an infinite loop and fails in Python 3.0. In 3.0, map returns a one-shot iterable obejct instead of a list as in 2.6.

# In[2]:


list(map(iter,[('abc','lmnop')]))


# In[3]:


def myzip(*args):
    iters = list(map(iter,args))
    print(iters)
    while iters:
        res = [next(i) for i in iters]
        print(iters, res)
        yield tuple(res)


# In[4]:


list(myzip('abc','lmnop'))


# In[6]:


iters = map(iter,[('abc','lmnop')])


# In[13]:


bool(iters)


# In[10]:


[next(i) for i in iters]


# #### Value Generation in Built-in Types and Classes

# In[2]:


D = dict(a=1,b=2,c=3)


# In[3]:


D


# In[4]:


x = iter(D)


# In[5]:


next(x),next(x),next(x)


# In[6]:


for key in D:
    print(key,D[key])


# In[7]:


get_ipython().system('git clone https://github.com/nickcafferry/Python-for-Transport-Phenomena.git')


# In[8]:


ls


# In[9]:


cd Python-for-Transport-Phenomena/


# In[10]:


ls


# *Although beyond the scope of this chapter, it is also possible to implement arbitrary user-defined generator objects with classes that conform to the iteration protocol. Such classes define a special __iter__ method run by the iter built-in function that returns an object having a __next__ method run by the next built-in function (a __getitem__) indexing method is also available as a fallback option for iteration*

# In[13]:


[x*x for x in range(10)]


# In[14]:


(x*x for x in range(10))


# In[15]:


{x*x for x in range(10)}


# In[16]:


{x:x*x for x in range(10)}


# In[17]:


{x*x for x in range(10)}


# In[18]:


set(x*x for x in range(10))


# #### Comprehension Syntax Summary

# *We've been focusing on list comprehensions and generators in this chapter,but keep in mind that there are two other comprehension expression forms: set and dictionary comprehensions are also avaiable in Python 3.0. We already know enough about comprehensions and geneators, hence it is easy to acquire a good understanding of set and dictionary comprehensions.*

# In[8]:


print({1,3,2} == set([1,3,2])); 
print({ord(x) for x in '1,3,2' if ord(x)>20} == set(ord(x)for x in '1,3,2' if ord(x) > 20))


# > For sets, the new literal form `{1,3,2}` works like `set([1,3,2])`;
# > the new set comprehension `{f(x) for x in S if P(x)}` is equipvalent to `set(f(x) for x in S if P(x))`

# In[9]:


{key: val for (key, val) in zip('abcdefghijklmn','123456789')}


# In[1]:


dict(zip('abcdefghijklmn','123456789'))


# In[3]:


{x: int(x) for x in '123456789'} == dict((x,int(x)) for x in '123456789')


# In[4]:


dict((x,int(x)) for x in '123456789')


# In[6]:


[x*x for x in range(10)] #list comprehensions: builds list


# In[7]:


(x*x for x in range(10))


# In[8]:


{x*x for x in range(10)}


# In[9]:


{x: x*x for x in range(10)}


# In[10]:


{x*x for x in range(10)}


# In[11]:


set(x*x for x in range(10))


# In[ ]:
```



