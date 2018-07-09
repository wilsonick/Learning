import math

import numpy as np



def f1(x):
    return 2*pow(x,3) - 3*pow(x,2) + x -2

def df1(x):
    return 6*pow(x,2) - 6*x + 1

print(f1(3))



def f2(x):
    return np.sin(x)

def df2(x):
    return np.cos(x)

print(f2(3))




x0 = -5.0
x1 = 5.0
spacing = 0.1
threshold = 0.05

x_num = math.floor( (x1 - x0) / spacing )

x = list(range(x_num+1))

y = list(range(x_num+1))

diffy = list(range(x_num+1))

root = list(range(x_num+1))

x[0] = x0
x[x_num] = x1

for i in range(x_num+1):

    x[i] = x[0] + spacing*i
    y[i] = f1(x[i])
    diffy[i] = df1(x[i])
    

root[0] = 1.5

for i in range(x_num):
    root[i+1] = root[i] - (y[i] / diffy[i])
    if (root[i+1] - root[i]) <= threshold:
        print('Break found according to threshold at', root[i])



#x = np.arange(x0,x1,spacing)
# x = list(range(x0,x1,spacing))
# y = [x * spacing for x in range(x0,x1)]

print(x)

print(y)

print(diffy)


print(root)



'''

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

for i in range(2,5):
    rx[i+1] = rx[i] - y1[i]/dy1[i] 

rx[1] = y1[0]/dy1[0]

print(rx)

'''
