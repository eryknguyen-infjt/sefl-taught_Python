x = '123'
try:
    y = int(x)
except:
    x = -1

print('Second', x)

x = 'Hello Bob'
try:
    y = int(x)
except:
    x = -1

print('ho', x)

z = 'Hello Chimon'
try:
    print('Yeah')
    print('Yep')
    y = int(x)
except:
    x = -1

print('Done', x)


rew = input('Enter a number: ')
try:
    ivent = int(rew)
except:
    rew = 25

if ivent > 10:
    print('Good jobs')
else:
    print('There is a problem')