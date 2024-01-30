l = []
for i in range(10):
    a = int(input())
    if a%42 not in l:
        l.append(a%42)

print(len(l))