import module
import sys
import math
import numbers
import decimal
#import antigravity

# My first function
def prnt(n,m):
	print(m*n)

# My second function
def fibo(n):
	seq = list(range(0,n))
	seq[0] = 1
	seq[1] = 1
	for i in range(2,n):
		seq[i] = seq[i - 1] + seq[i - 2]
	return seq[n-1]

	
# My third, multi-output function
def multi(n,m):
	return [n,m]
	

# Function calls
prnt("Sup mark ", 10)
print(fibo(200))
print(multi(3,34))
print(module.crack(15))
#print(dir(sys))
print(math.acos(0))
print(math.log10(101))
print(decimal.Decimal(1)/decimal.Decimal(6))
print(math.cos(math.pi))

# String definitions
s = 'Hello, world.'
larry = 'cool'
sergey = 'bad'

# Number definitions
x = 42
sci = 3.1415e56
y = 5**20

# List definitions
firstfive = [1,2,3,4,5]
sliced = firstfive[2:]


# This is a comment!
print(firstfive)
print(y)



"""
# My first debug for understanding
seq = range(1,10)
print(seq)
#seq[0] = 1
seq[2] = 1
print(seq)
"""

"""
# My second debug for understanding
a = list(range(1,5))
b = [1,2,3,4,5]
print(a)
print(b)
a[0] = 5
b[0] = 7
print(a)
print(b)
"""


"""
# First Python if statement
if x==2:
	print('Hi Cami!')
	print(100*x)
elif x==43:
	print('Hi John!')
else:
	print('Hi Peter!')
	
	
# List for loop	
for i in range(1,10,3):
	print('Peter is shit')

	
# String list for loop	
for i in ['Nic', 'Cami', 'Peter']:
	print(i)

	
# Print all numbers in range	
for i in range(1,11):
	print(i)
	#pass

# if statement as simple as possible	
if x == 4:
	x = 5
elif x != 8:
	x = 10
print(x)


# Print numbers :O
for i in range(1,4):
	print(i)


# Clearly not mutable
1=2
'Hello' = 'Goodbye'


# Input from the user
what = input()
print(what)
"""


# Embedded data types
hellish = [[1,2,3],[1,[3,[5,7],4]],5]
print(hellish)
print(hellish[0] + hellish + hellish + hellish)
print([3,4] in hellish[1])
print(5 in hellish)
print(len(hellish + hellish))


# if with in
thing1 = 'abcdefg'
thing2 = 'qrstuvg'
if 'trs' in 'tuv':
	print('Sup Tove Lo')
else:
	print('Cool!')


