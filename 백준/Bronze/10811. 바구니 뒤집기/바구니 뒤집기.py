a, b = map(int, input().split())
l = [i for i in range(1,a+1)]

for i in range(b):
    k = []
    c, d = map(int, input().split())
    for j in range(d-c+1):
        k.append(l[d-1-j])

    l[c-1:d]=k
print(*l)