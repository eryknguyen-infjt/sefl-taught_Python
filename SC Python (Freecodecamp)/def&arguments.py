# def statement
def thing():
  print('desk')
  print('laptop')

thing()
print('Zip')
thing()

# We also can say name of that code(def statement) is stored(and refuse) steps

# def statement with arguments
def lyrics(arguments):
  if arguments == 'London':
    print('Yeah. It is a good idea')
  elif arguments == 'Scotland':
    print('The sence here is so beautiful. You have a good eyes')
  else:
    print('So good')

lyrics('London')
lyrics('Scotland')
lyrics('France')


def gree_fst():
  return 'Hello. Nice to meet you'

print(gree_fst(), 'Eryk')


def ly(arguments):
  if arguments == 'London':
    return 'Yeah. It is a good idea'
  elif arguments == 'Scotland':
    return 'The sence here is so beautiful. You have a good eyes'
  else:
    return 'So good'

print(ly('London'), '. Welcome')
print(ly('Scotland'), '. Welcome')
print(ly('Swedish'), '. Welcome')


def addf(a, b):
  af = a + b
  return af

x = addf(4, 0)
print(x)
