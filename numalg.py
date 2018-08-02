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

# 





# Euclid's gcd algorithm



# Euler's totient function




# Print first 1000 primes



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


