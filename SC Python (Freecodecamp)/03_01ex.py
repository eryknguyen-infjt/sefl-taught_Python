hrs = input('Enter Hours: ')
r = input('Enter Rate: ')
z = float(hrs)
y = float(r)
if z > 40:
  reg = y * z
  otp = (z - 40.0) * (y * 0.5)
  xp = reg + otp
else:
  xp = z * y
print('Pay:', xp)