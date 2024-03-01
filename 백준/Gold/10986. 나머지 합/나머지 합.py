n,m,*l = map(int, open(0).read().rsplit())

a = [0]*(n+1)
cnt = 0
r = [0]*m
r[0] = 1
for i in range(n):
    a[i + 1] = (a[i] + l[i]) % m
    if r[a[i+1]] > 0:
        cnt += r[a[i+1]]
    r[a[i+1]] += 1

print(cnt)