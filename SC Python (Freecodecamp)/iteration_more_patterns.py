# Counting in a Loop
zork = 0  # We often call this VARIABLE COUNT
print('Before', zork)
for thing in range(7):  # for thing in [1, 5, 6, 50, 46]:
  zork += 1
  print(zork, thing)
print('Afetr', zork)
''' To count how many times we excute a loop, 
we introduce a counter variable that starts at 0 and we add one to it each time through the loop'''

# Summing in a Loop
zork = 0
print('Before', zork)
for thing in [20, 63, 96, 48, 78]:
  zork += thing
  print(zork, thing)
print('Afetr', zork)
''' To add up a val. we encounter in a loop, 
we introduce a sum variable that starts at 0 and we add the val. to the sum each time through the loop'''

# Finding the Average in a Loop
count = 0
sum = 0
for i in [25, 42, 48, 39, 74, 66]:
  count += 1
  sum += i
  print(count, sum, i)
print('After', count, sum, sum / count)
''' An average just combines the counting and sum patterns and divides when the loop is done'''

# Filtering in a Loop
print('Before')
for z in [25, 29, 98, 16, 32]:
  if z > 30:
    print(z)
print('After')
''' We use an if statement in the loop to catch/filter the vals we are looking for'''

# Search using a Boolean Variable
k = False
for x in [30, 90, 48, 63, 47, 98]:
  if x == 98:
    k = True
  print(k, x)
print('After', k)
''' If we just want to search and know if a val was found, we use a variable that starts at 
FALSE and is set to TRUE as soon as  
we find what we are looking for'''

# How to find the smallest (largest) val.
# LARGEST VAL. (Loop Idioms)
largest_so_fsr = -1
print('Before', largest_so_fsr)
for i in [90, 60, 35, 87, 101, 165]:
  if i > largest_so_fsr:
    largest_so_fsr = i
  print(largest_so_fsr, i)
print('After', largest_so_fsr)

# SMALLEST VAL.
smallest_so_fsr = -1
print('Before', smallest_so_fsr)
for i in [45, 98, 63, 25, 78, 50]:
  if i < smallest_so_fsr:
    smallest_so_fsr = i
  print(smallest_so_fsr, i)
print('After', smallest_so_fsr)
'''There is a wrong way to find that. 
Let me show some different'''

# Finding the smallest val.
smallest = None
print('Before')
for g in [45, 78, 96, 34, 62, 25]:
  if smallest is None:
    smallest = g
  elif smallest > g:
    smallest = g
  print(smallest, g)
print('After', g)
''' We still have a variable that is SMALLEST so far. 
The  first time through the loop smallest is None, so we take the first val. to be the smallest'''

# The 'is' and 'is not' Operators
'''Python has an is operator that can be uesd in logical expressions. 
Implies "IS THE SAME AS". Similar to, but stronger than ==. 
IS NOT also is a logical operator.'''