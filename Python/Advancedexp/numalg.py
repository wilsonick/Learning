# Factor a composite number as a unique product of primes. 

number = 28

productsposs = list( range( number) )

products = [] * number

# Divide by 2 and if there is a remainder, add 2 to the products. 

for i in range(2,number):
    if (number % i) == 0:
        products.append(number / i)

print(products)





def getDivisors(n):
    divisors = []
    d = 1
    while d*d < n:
        if n % d == 0:
            divisors.append(d)
            divisors.append(n / d);
        d += 1
    if d*d == n:
        divisors.append(d)
    return divisors

print(getDivisors(28))


# Product of a few numbers in a list

numlist = [32,3,6,7,9,7,5,4,8,9,6,43,3,5,4,3,7,8]

product = 1

for i in numlist:
    product = product * i

print(product)

# Product of a few integers in a range

start = 5
finish = 10

product = 1

for i in range(start,finish+1):
    product = product * i

print(product)

# Sum of a few terms in a sequence

sequence = [1,1,2,3,5,8,13,21]

sum = 0

for i in range(len(sequence)):
    sum = sum + sequence[i]

print(sum)

# Sum of a few terms from a function

def func(n):
    return n*n

n = [4,3,1,2]

sumx_n = 0

for i in range(len(n)):
    sumx_n = sumx_n + func(n[i])

print(sumx_n)

# Product of a few terms from a function

def func2(n):
    return n*n

n2 = [4,6,7,2]

prodx_n = 1

for i in n2:
    prodx_n = prodx_n * func2(i)

print(prodx_n)


# Euclid's gcd algorithm

def gcd2(a,b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

print(gcd2(14,30))
print(gcd2(82,27))

# Most basic recursion with functions

def recurs(n):
    if n < 100:
        print(n)
        return recurs(n*n)

print(recurs(3))


# Binary method for gcd

def gcd(a,b):
    d = 0
    while ( (a % 2) == 0 and (b % 2) == 0 ):
        a /= 2
        b /= 2
        d += 1
    while a != b:
        if ( (a % 2) == 0):
            a /= 2
        elif ( (b % 2) == 0):
            b /= 2
        elif (a > b):
            a = (a - b)/2
        else:
            b = (b - a)/2
        g = a
    return g*2**d

print(gcd(18,48))
print(gcd(4356,8473))







# Euler's totient function

n = 14

divs = getDivisors(n)

print(divs)

for i in 
productnot = n*(1-1/









                
# Factorial

def fact(n):
    prod = 1
    for i in range(1,n+1):
        prod = prod*i
    return prod

print(fact(4))



# Permutations and combinations of various numbers

def comb(n,r):
    return fact(n) / ( fact(n-r) * fact(r) )

print(comb(5,3))




def perm(n,r):
    return fact(n) / fact(n-r)

print(perm(5,3))


