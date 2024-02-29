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


