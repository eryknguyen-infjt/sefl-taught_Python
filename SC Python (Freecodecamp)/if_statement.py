# if statement
x = 5
if x < 10:
  print('Smaller')
if x < 20:
  print('Bigger')
print('Done')

x = input('Enter a number: ')
if float(x) > 2:
  print('Bigger than 2')
  print('Still bigger')
print('Done with 2')

x = 42
if x > 1:
  print('More than 1')
  if x < 100:
    print('Less than 100')
print('Done')

y = input('Enter a number: ')
if x == 0:
  if float(y) == 10:
    print('Yeah')

# else statement
x = 4
if x > 2:
  print('Bigger')
else:
  print('Smaller')
print('All done')

# elif statement
x = input('Enter a number: ')
if float(x) < 2:
  print('Small')
elif float(x) < 10:
  print('Medium')
else:
  print('LARGE')
print('All done')