import numpy as np


def f1(x):
    return 2*x**2

def df1(x):
    4*x

def f2(x):
    return np.sin(x)

def df2(x):
    return np.cos(x)

print(f2(3))


x0 = 1.0
x1 = 5.0
spacing = 0.1


x = np.arange(x0,x1,spacing)

# x = list(range(x0,x1,spacing))
# y = [x * spacing for x in range(x0,x1)]

print(x)

# Get the function values: 

y1 = f1(x)

y2 = f2(x)

print(y1)

# Get the derivitive of the values over the domain:

dy1 = df1(x)

dy2 = df2(x)

print(dy1)

# Initialize the sequence of root approximations:
rx = list(range(11))

rx[0] = 1

print(rx)

# Obtain the root: 
'''
for i in range(2,5):
    rx[i+1] = rx[i] - y1[i]/dy1[i] 
'''
rx[1] = y1[0]/dy1[0]

print(rx)

