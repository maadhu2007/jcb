import math
from sympy import mod_inverse
p = 7  
q = 5  
n = p*q 
print("n:",n) 
phi = (p-1)*(q-1) 
print("phi:",phi)
e=2 
while (e < phi):  
  if(math.gcd(e, phi) == 1):  
       break  
  else:  
        e = e+1  
d=mod_inverse(e,phi)
print("d:",d) 
M=12
print("Original Message:",M) 
C = pow(M, e) 
print("c:",C) 
c= math.fmod(C, n)  
print("Encrypted data = ", c)  
m = pow(c, d) 
print("m:",m) 
OM= math.fmod(m, n)  
print("decrypte data = ", OM) 