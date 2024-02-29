# this code with ROOT.INPT.py and ROOT.OUT.py
from math import *

fopen = open('ROOT.INPT.py')
iopen = open('ROOT.OUT.py', 'w')
a = fopen.readline()
b = fopen.readline()
c = fopen.readline()

a = int(a)
b = int(b)
c = int(c)

t = a**2 + b**2 + c**2
m = a * b * c
s = t/m + sqrt(m)
s = str(round(s, 2))
print(s)
iopen.write(s)

fopen.close()
iopen.close()

# this code with TOANCO.INP.py and TOANCO.OUT.py
ropen = open('TOANCO.INP.py')
hopen = open('TOANCO.OUT.py', 'w')

s = ropen.readline()
s = s.split()

total = int(s[0])
legs = int(s[1])

cs = ds = 0  # cs: chickens, ds: dogs

for cs in range(total):
    ds = total - cs
    if cs * 2 + ds * 4 == legs:
        break

hopen.write(str(cs) + ' ' + str(ds))

ropen.close()
hopen.close()



