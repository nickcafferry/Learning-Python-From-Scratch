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

def fibonacci(n):
	return 1 if n < 2 else fibonacci(n-1)+fibonacci(n-2)

n = int(input('Please type the number n if you want the n th number of fibonacci array:'))
printYellowRed(u'Initializing...\n')
printSkyBlue(u'--------------------------------------------------------------------------------\n')
S1 = '9'
S2 = '10'
for i in range(1,n+1,1):
	if i == 1:
		printPink(u'Start generating the fibonacci number smaller than 10: \n')
		printYellow(u'###############################################################################\n')
	print(HASH('The %d th number of a fibonacci array is %d'%(i,fibonacci(i))))
	
	if fibonacci(i+1) > 9 and fibonacci(i) < 10:
		printYellow(u'###############################################################################\n')
		print('\r')
		printPink(u'Start generating the fibonacci number < 100 but > 10 : \n')
		printYellow(u'###############################################################################\n')
		S1 = S1 + '9'
		S2 = S2 + '0'

	if fibonacci(i+1) > int(S1) and fibonacci(i) < int(S2):
		printYellow(u'###############################################################################\n')
		print('\r')
		printPink(u'Start generating the fibonacci number < %s0 but > %s: \n'%(S2,S2))
		printYellow(u'###############################################################################\n')
		S1 = S1 + '9'
		S2 = S2 + '0'