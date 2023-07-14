hrs = input('Enter Hours: ')
r = input('Enter Rate: ')
try:
  z = float(hrs)
  y = float(r)
except:
  print('Error, please enter numberic input')
  quit()  #stop this code :particular stuation here: try&except, to prin z,y

print(z, y)
if z > 40:
  reg = y * z
  otp = (z - 40.0) * (y * 0.5)
  total = reg + otp
else:
  total = z * y
print('Pay:', total)