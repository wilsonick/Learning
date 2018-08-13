import numpy as np

num1 = np.float64(48329743294723974)
num2 = np.complex128(54394538953795347+9357493543543575397j)

print(num1,num2)

print(np.identity(2))

print(np.zeros((4,4)))

print(np.array((3,4)))




sx = np.array([[0,1],[1,0]])

sy = np.array([[0,-1j],[1j,0]])

sz = np.array([[1,0],[0,-1]])

print(sx)

print(np.linalg.eig(sx))

print(np.linalg.eig(sy))

print(sx*sy)

print(sx*sx*sx*sx)
