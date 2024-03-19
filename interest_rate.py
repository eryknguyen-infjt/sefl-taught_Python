file = open('general.inp', 'r+')
findout = open('general.out', 'w')

lines = file.readline()
lines = lines.split()

c = int(file[0])
t = int(file[1])
a = int(file[2])
k = int(file[3])
h = int(file[4])

def calculate_amount(c, t, a, k, h, m):
    if c == 0:
        if t <= m:
            return round(a * (1 + k / 100) ** t, 1)
        else:
            return round(a * (1 + k / 100) ** m + (a * (1 + h / 100) ** (t - m)), 1)
    else:
        if t <= c:
            return round(a * (1 + k / 100) ** t, 1)
        else:
            return round(a * (1 + k / 100) ** c + (a * (1 + h / 100) ** (t - c)), 1)


findout.write(str(m))

file.close()
findout.close()
