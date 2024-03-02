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

# this is code with calculated summary
from math import sqrt

a = input('Nhập vào số nguyên A: ')
b = input('Nhập vào số nguyên B: ')

a = int(a)
b = int(b)
total = 0
s = ''


def nguyento(x):
    if x == 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


for i in range(a, b + 1):
    if nguyento(i):
        total += 1
    if i % 5 == 0:
        s += str(i) + ', '

print(total)
print(s[:len(s) - 2])



