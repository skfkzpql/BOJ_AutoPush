f = open(0)
t = int(f.readline())
for i in range(t):
    l = f.readline().rsplit()
    a = float(l.pop(0))
    for j in l:
        if j == '@':
            a *= 3
        elif j == '%':
            a += 5
        elif j == '#':
            a -= 7
    print(f"{a:.2f}")