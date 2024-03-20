file = open('general.inp', 'r')
findout = open('general.out', 'w')
for lines in file:
    c = int(lines[0])
    t = int(lines[1])
    a = int(lines[2])
    k = int(lines[3])
    h = int(lines[4])


def calculate_amount(c, t, a, k, h):
    m = a * (1 + k / 100) ** t
    if t == c:
        return round(m)
    elif t < c:
        return round(a * (1 + h / 100) ** t)
    else:
        return round(m + m * (1 + h / 100) ** (t - c))


outData = calculate_amount()
findout.write(str(outData))

file.close()
findout.close()
