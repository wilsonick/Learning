import math

print('---------------- OTHER MISC RESERVED WORDS ---------------')

# assert, async, await, continue, finally, in, raise, try, with, yield,

# class, None, lambda 


#################################### PLAYING BEGINS HERE ################################

# yield

def test():
    yield 1

print(test)
print(test())

def even(x):
    yield x*2

print(even(2))



# lambda

parabola = lambda x: pow(x,2)

print(parabola(423))
print(parabola(11))

# None

x = None

# Most Basic Class

class Peter:
    pass

police = Peter()

print(police)

# Class with everything classes can have and some basic OO

class Classroom:
    obediencelevel = 5
    staffroster = 'High'
    students = 4
    teachers = 250

    
    # Define a method for the behaviour class:

    def discipline(self, reduction):
        self.obediencelevel = reduction

    def brickinwall(self, floyd):
        brickinwall.roster = floyd


    # Do something else I don't understand yet:

   # __init__(


print(Classroom)

print(Classroom())
BBC = Classroom()
print(BBC)

print(BBC.teachers)
print(BBC.staffroster)


#BBC.discipline(Classroom,3)


#BBC.brickinwall('Low')

        
#print(BBC.level)



print('---------------- FUNCTIONS THAT DO SIMPLE MATHEMATICAL ALGORITHMS ----------------')

def sumoflist(hi):
    sum = 0
    for i in range(len(hi)):
        sum = sum + hi[i]    
    return sum

print(sumoflist([1,3,3,5]))


def maxoflist(hi):
    max = 0
    for i in range(len(hi)):
        if hi[i] > hi[i-1]:
            max = hi[i]
    return max

print(maxoflist([1,342432,243923478]))
print(maxoflist([1,2,3,6,7,100,101]))


def inlist(number,thelist):
    for i in range(len(thelist)):
        if number == thelist[i]:
            isthere = True
        else:
            isthere = False
    return isthere

print(inlist(6,[1,2,3,4,6]))


def ceilinglol(number):
    return math.ceil(number)

print(ceilinglol(3.4))

def ceilingreal(number):
    #if (number - (number - 1) == )
    res = int(number)
    return res if res == number or number < 0 else res+1

print(ceilingreal(4))

print(ceilingreal(4.4))

print(ceilingreal(5.4))

print(ceilingreal(4432.442343244234))

# Apparently, kind reader, the algorithm is not implementable in the standard language! It needs C to do (I think). 


################################## SIMPLE GRAPH ALGORITHMS ###########################

first_graph_vertex = ['London','Brisbane','Paris']

first_graph_edge = [['London','Paris'],['Paris','London'],['Brisbane','Brisbane']]

# How many unique flights can I go on around my 'world'?

print(len(first_graph_edge))

# Can I go one-way from Brisbane to Paris?

for i in range(len(first_graph_edge)):
    if first_graph_edge[i] == ['Brisbane','Paris']:
        print('Yes, you can')
    else:
        print('No, you can\'t')

# Are there any return flights?

print(range(len(first_graph_edge)))


'''
for i in range(len(first_graph_edge)):
    for j in range(len(first_graph_edge[1])):
        if first_graph_edge[i][j] == [[j],[i]]:
            print('Found a return flight!')
'''
