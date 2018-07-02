import math

c = 2.99792458e8

h = 6.62607004e-34

hbar = h/(2*math.pi)

G = 6.67408e-11

kb = 1.38064852e-23

sm = 1.98847e30


# Hawking radiation
M = 1e5
T = (hbar*c**3) / (8*math.pi*G*kb*M)
print(T)


# Photon momentum
f = 1
p = h*f/c
print(p)


# QM electron level
e = 9.109e-31
ec = 1.602176e-19
perm = 8.854187817e-12

elevel = (-1*e*ec**4) / (32*math.pi**2*perm**2 * hbar**2)

print(elevel)


# !!!!!
print(T*elevel)



