moon = 0
count = 0.0
while True:
  nval = input('Please, enter a number: ')
  if nval == 'done':
    break
  try:
    skval = float(nval)
  except:
    print('Invalid input')
    continue
  moon += 1
  count = count + skval

print(moon, count, count / moon)