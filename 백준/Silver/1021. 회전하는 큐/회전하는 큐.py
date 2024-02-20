def f2(n):
    global cnt
    for _ in range(n):
        a = l.pop(0)
        l.append(a)
        cnt += 1

def f3(n):
    global cnt
    for _ in range(n):
        a = l.pop()
        l.insert(0,a)
        cnt += 1

n,m = map(int,input().split())
d = list(map(int,input().split()))
l = [i for i in range(1,n+1)]

cnt = 0

for i in range(m):
    if d[i] != l[0]: 
        idx = l.index(d[i])
        if idx > len(l)/2:
            f3(len(l) - idx)
        else:
            f2(idx)
    l.pop(0)

print(cnt)