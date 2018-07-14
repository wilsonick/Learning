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


