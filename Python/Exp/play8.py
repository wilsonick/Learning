#from scipy import constants as sp

import scipy as sp

import math

from scipy import constants as spc

#from constants import physical_constants as spi #Subsubmodule importation?!

print(spc.c*spc.hbar)
print(spc.eV)

import numpy as np

num1 = np.float64(48329743294723974)
num2 = np.complex128(54394538953795347+9357493543543575397j)

print(num1,num2)


x1 = np.array( [ [1,2] , [3,4] ] )

print(x1)
print(x1.shape)
print(x1[0,0])

x2 = np.array( [ [1,2,6] , [7,4,4]  ] )

print(x2)
print(x2[:,1])
print(x2[1,:])


print( np.inner( [1,2,3] , [4,5,6] ) )

print( np.linalg.eig( [[2,1] , [1,2]]  ) )

print( np.linalg.inv( [[497432,3297] , [209824,2082038]]  )  )

print( np.linalg.det( [[497432,3297] , [209824,2082038]]  )  )

print( np.floor( np.sin(np.pi) ) )

print(  np.exp(np.pi*1j) + 1  )

x3 = 4324329085

print( round( np.exp( np.log(x3) ) ) )





p = np.poly1d([3,3,3])

print(p)



#print(spi.atomic_unit_of_mass)
