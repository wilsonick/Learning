# Generate a random string of alphanumeric characters when run:

import random

length = 2000

alpha = 'abcdefghijklmnopqrstuvwxyz'

numbers = '0123456789'

alphanumero = alpha + numbers

rndstring = ''

for i in range(length): 
    rndstring = rndstring + alphanumero[ random.randint(0,35) ]

print(rndstring)

