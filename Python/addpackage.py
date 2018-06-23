import scipy
import module

#print(scipy.mgrid[0:5,0:5])

x = scipy.mgrid[0:5]

print(x.flags)

y = module.crack(10)

print(module.crack(5))

