def computepay(hours, rate):
  #print('In computepay', hours, rate)
  if hours > 40:
    reg = rate * hours
    otp = (hours - 40.0) * (rate * 0.5)
    pay = reg + otp
  else:
    pay = hours * rate
  #print('Returing', pay)
  return pay


hrs = input('Enter Hours: ')
r = input('Enter Rate: ')
z = float(hrs)
y = float(r)

xp = computepay(z, y)

print('Pay:', xp)
