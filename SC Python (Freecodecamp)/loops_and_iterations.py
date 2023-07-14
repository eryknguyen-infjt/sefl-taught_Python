# Repeated Steps

# While Statement. It's likely IF STATEMENT
n = 5
while n > 0:
  print(n)
  n -= 1  # n = n - 1
print('Blowshup')
print(n)

# An infinite loop
x = 5
while x > 0:
  print('blowshup')
  print('Michael')
print('London')
'''An infinite loop is so crazy. It runs forever, so it can be run until your computer runs out of battery, or anything else'''

# Another Loop( we call that zero trip )
y = 0
while y > 0:
  print('gret')
  print('porle')
print('Scot')

# Breaking out of a Loop
while True:
  grt = input('>>> ')
  if grt == 'done':
    print('All right')
  elif grt == 'finished':
    print('Yeah')
  else:
    print('Something is different than most')
  break
  print('Stop here')

# Finishing an iteration with continue
while True:
  fkl = input('/ ')
  if fkl[0] == '?':
    continue
  if fkl == 'blows':
    break
    print(fkl)
print('Done')
'''This is not an infinite-loop because at some point the break gets us out of the loop.'''

# A simple Definite Loop
x = [5, 4, 3, 2, 1]
for i in x:
  print(i)
print('Up')

# A Definite Loop with a strings
person = ['John, Micheal, Lowkey']
for i in person:
  print('Happy Birthday after rainy days:', i)
print('Right')
