############## IMPORT PLAYING ##############
#import math
from math import *

#import cmath
from cmath import *

#from math import pi

#import numbers
#import pylab


################## TESTING PACKAGE REWRITING AND PRIORITY ###################

'''
print(pi)
print(math.pi)
'''


#print(exp(1j))   # Tell whether which package is loaded first and if they are overridden


#print(math.sin(1))
#print(cmath.sin(1))

#print(sin(1j))
#print(sin(1j))


############## GLOBAL PLAYING ###############


def globe():
        global yo
        global hi
        yo = 'sup'

globe()
hi = 'friend'
print(hi)
print(yo)

yo = 'pop'

print(yo)

############### FUNCTION DEFINITION PLAYING ###########
def func():
        return 100

def nothing():
        pass

def nats(n):
        return range(1,n+1)

def bubble(nums):   # Bubble sort algorithm
        for i in range(0 , len(nums) - 1 ):
                for j in range(0 , len(nums) - 1 ):
                        # print(j)
                        if nums[j] > nums[j + 1]:   # IF ONE IS BIGGER THAN THE OTHER.....
                                numstemp1 = nums[j]
                                numstemp2 = nums[j+1]     # SWAP THEM AROUND! 
                                nums[j] = numstemp2
                                nums[j+1] = numstemp1
        return nums

print( bubble( [10,12,100,6,5,4,7] ) )

print( bubble( [100,99,67,4,5,50,38,5849,0] ) )


################ DATA TYPE PLAYING ##############

unit = 1j
i = 1j
comp1 = 3 + 5j
comp2 = 7 + 2j
comp3 = -6 - 8j

print('--------------- COMPLEX START ------------')

print(comp1*unit)
print(comp1*i)
print(comp1/comp2)
print(comp2/comp1)

print(comp1/1e-10)
print(comp1/1j)

print(abs(comp3))
print(polar(exp(1j*pi)))
print(rect(1,pi))

print(comp3.real)
print(comp2.imag)

print(phase(1j))
print(pi/2)

print(exp(1j*pi) + 1)

print(cos(1j*pi))

#sin(



print('--------------- COMPLEX END ------------')

############### FLOW CONTROL PLAYING #############

######## IF #######

if ((10 - 7) == 3) or (1 == 2):
        print('Wrong')

if ( ( 6 * 8 ) == 48 ) and ( ( 5 * 12 ) == 60 ):
        print('Sup')


if (func() * 3  == 300):
        print('Wow')


######## ELSE ############
        
if (10 == 8 + 3):
        print('not else')
else:
        print('else')


if (10 == 11):
        print('not elif')
elif (11 == 11):
        print('elif')
else:
        if (2==2):
                print('confusing')
                if (1==1):
                        print('even more confusing')


if (10 == 11):
        print('long elif')
else:
        if (9 == 11):
                print('elif sucks')


case = 6
cases = 3
if case == 1:
        print('case1')
elif cases == 2:
        print('case2')
elif case == 3:
        print('case3')
elif case == 4:
        print('case4')
elif case == 5:
        print('case5')



'''
#### ATTEMPT TO USE DICTIONARY AS SWITCH #########
temp = 1
def casey(temp):
        return {
                1: print('case1'),
                2: print('case2'),
                }[temp]
'''

########### WHILE ##########
        
while 1==2:
        print('Hi')

i = 1
while (i < 5):
        i += 1
        print('Yay')

while False:
        print('NEVER')

############ FOR #############

for i in [1,3,7]:
        print('hi')

for i in [2,1]:
        print(i-1)

for i in 'Python':
        print(i)

for i in 'Python':
        print(10*i)


pi = 3.1415926535897932384626433835729

print(pi)

for i in str(pi):
        print(pi)

zucks = 'MarkPris '
for i in range(3):
        zucks = 2 * zucks

print(zucks[34:46])

print(zucks[0 : len(zucks)//2  ] )

print('%%%%%%%%%%%%%%%%SPACES%%%%%%%%%%%%')

print(zucks)

############# STRING PLAYING ############
print('Py' 'thon')
print('Py' + 'y')
print( 4 * 'SUP')

name = 'Barbara'
if (name[0] == 'B'):
        print('Cool')

print(name[2:6])

if (name[3:5] == 'ba'):
        print('Sliced!')




########### LIST PLAYING ##############

initlist = list(range(1,20))
for i in range(len(initlist)):
        initlist[i] = (i**3)
print(initlist)

natural = list(range(1,15))
print([i**2 for i in natural])

print(list(range(1,51)))


for i in [1,2]:
        print('FOR LOOP')


print(natural)

natural.append(4389)
natural.append(4379789)

print(natural)

del natural[len(natural) - 1]       ############# DEL! #############

print(natural)

del natural[4:]

print(natural)

'''        ### PRINT MULTIPLICATION TABLES ###
listy = [[0 for i in range(13)] for j in range(13) ]

for i in range(13):
        for j in range(13):
                listy[i][j] = i*j
                #print(listy[i][j])
                print(str(listy[1][j]) + ' times ' + str(listy[i][1]) + ' = ' +  str(listy[i][j]) )
'''


########### PASS PLAYING ##############
pass
pass
pass
pass
pass
pass
pass

